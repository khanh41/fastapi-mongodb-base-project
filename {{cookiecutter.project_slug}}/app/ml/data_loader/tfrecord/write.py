import json
import os

import tensorflow as tf

from app.core.constants import TFRecordConstants


class WriteTFRecordsDataset:
    def __init__(self, input_dir, language="en"):
        self.image_labels = {}
        (
            self.output_dir,
            self.path_infor,
            self.path_ds,
        ) = TFRecordConstants.get_record_path(language_font=language)
        self.labels = os.listdir(input_dir)
        self.store_information_dataset()

    def save_tfrecord_dataset(self):
        # Write the raw image files to `images.tfrecords`.
        # First, process the two images into `tf.train.Example` messages.
        # Then, write to a `.tfrecords` file.
        length_dataset = 0
        with tf.io.TFRecordWriter(self.path_ds) as writer:
            for filename, label in self.image_labels.items():
                image_string = open(filename, "rb").read()
                tf_example = self.image_example(image_string, label)
                writer.write(tf_example.SerializeToString())

                length_dataset += 1

        self.save_information_dataset(length_dataset)

    def save_information_dataset(self, length_dataset):
        with open(self.path_infor, "w") as f:
            json.dump(
                {
                    "labels": self.labels,
                    "length_dataset": length_dataset,
                },
                f,
            )

    def store_information_dataset(self):
        for i, label in enumerate(self.labels):
            path_dir = os.path.join(self.output_dir, label)
            for path_img in os.listdir(path_dir):
                self.image_labels[os.path.join(path_dir, path_img)] = i

    def image_example(self, image_string, label):
        """Create a dictionary with features that may be relevant."""
        image_shape = tf.io.decode_jpeg(image_string).shape

        feature = {
            "height": self._int64_feature(image_shape[0]),
            "width": self._int64_feature(image_shape[1]),
            "depth": self._int64_feature(image_shape[2]),
            "label": self._int64_feature(label),
            "image_raw": self._bytes_feature(image_string),
        }
        return tf.train.Example(features=tf.train.Features(feature=feature))

    def _bytes_feature(self, value):
        """Returns a bytes_list from a string / byte."""
        if isinstance(value, type(tf.constant(0))):
            value = (
                value.numpy()
            )  # BytesList won't unpack a string from an EagerTensor.
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

    def _float_feature(self, value):
        """Returns a float_list from a float / double."""
        return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

    def _int64_feature(self, value):
        """Returns an int64_list from a bool / enum / int / uint."""
        return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))
