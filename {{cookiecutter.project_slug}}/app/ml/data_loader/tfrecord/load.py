import json
import os
from functools import partial

import matplotlib.pyplot as plt
import tensorflow as tf
import wget

from app.core.constants import DownloadUrlConstants, TFRecordConstants


def show_batch(image_batch, label_batch):
    plt.figure(figsize=(10, 10))
    for n in range(10):
        plt.subplot(5, 5, n + 1)
        plt.imshow(image_batch[n] / 255.0)
        if label_batch[n]:
            plt.title("MALIGNANT")
        else:
            plt.title("BENIGN")
        plt.axis("off")


class LoadTFRecordsDataset:
    def __init__(self, path_tfrecord=None, path_infor_file=None, language=None):
        if path_tfrecord and path_infor_file:
            self.path_tfrecord = path_tfrecord
        else:
            (
                _,
                self.path_tfrecord,
                self.path_infor_file,
            ) = TFRecordConstants.get_record_path(language)

        if not os.path.isfile(self.path_infor_file) and not os.path.isfile(
                self.path_tfrecord
        ):
            print("Not found dataset, downloading...")
            os.makedirs(os.path.dirname(self.path_infor_file), exist_ok=True)
            os.makedirs(os.path.dirname(self.path_tfrecord), exist_ok=True)
            wget.download(
                DownloadUrlConstants.GDOWN_TFRECORD_INFOR, self.path_infor_file)
            wget.download(DownloadUrlConstants.GDOWN_TFRECORD_DATASET, self.path_tfrecord)

        self.ds_infor = self.load_infor(self.path_infor_file)

    def get(self, train_size=1):
        train_size = int(train_size * self.ds_infor["length_dataset"])
        test_size = self.ds_infor["length_dataset"] - train_size
        return self._get_dataset(train_size, test_size)

    @staticmethod
    def load_infor(path_infor_file):
        with open(path_infor_file, "r") as f:
            return json.load(f)

    @staticmethod
    def decode_image(image):
        image = tf.image.decode_jpeg(image, channels=3)
        image = tf.cast(image, tf.float32)
        image = tf.image.resize(image, TFRecordConstants.IMAGE_SIZE)
        return image

    def _read_tfrecord(self, example, labeled):
        tfrecord_format = (
            {
                "image_raw": tf.io.FixedLenFeature([], tf.string),
                "label": tf.io.FixedLenFeature([], tf.int64),
            }
            if labeled
            else {
                "image_raw": tf.io.FixedLenFeature([], tf.string),
            }
        )
        example = tf.io.parse_single_example(example, tfrecord_format)
        image = self.decode_image(example["image_raw"])
        if labeled:
            label = tf.cast(example["label"], tf.int32)
            return image, label
        return image

    def _load_dataset(self, labeled=True):
        ignore_order = tf.data.Options()
        ignore_order.experimental_deterministic = False  # disable order, increase speed
        dataset = tf.data.TFRecordDataset(
            self.path_tfrecord
        )  # automatically interleaves reads from multiple files
        dataset = dataset.with_options(
            ignore_order
        )  # uses data as soon as it streams in, rather than in its original order
        dataset = dataset.map(
            partial(self._read_tfrecord, labeled=labeled),
            num_parallel_calls=TFRecordConstants.AUTOTUNE,
        )
        # returns a dataset of (image, label) pairs if labeled=True or just images if labeled=False
        return dataset

    def _get_dataset(self, train_size, test_size, labeled=True):
        tf.random.set_seed(123)
        dataset = self._load_dataset(labeled=labeled)
        dataset = dataset.shuffle(8192)

        train_dataset = (
            dataset.take(train_size)
                .prefetch(buffer_size=TFRecordConstants.AUTOTUNE)
                .batch(TFRecordConstants.BATCH_SIZE)
        )

        test_dataset = (
            dataset.skip(train_size)
                .take(test_size)
                .prefetch(buffer_size=TFRecordConstants.AUTOTUNE)
                .batch(TFRecordConstants.BATCH_SIZE)
        )
        return train_dataset, test_dataset


if __name__ == "__main__":
    _, path_ds, path_infor = TFRecordConstants.get_record_path("en")
    train_ds = LoadTFRecordsDataset(path_infor).get(train_size=1)
    image_batch, label_batch = next(iter(train_ds))
