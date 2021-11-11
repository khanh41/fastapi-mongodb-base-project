import tensorflow as tf

from app.core.constant import TFRecordConstants


def load_image_from_directory(path_image_dataset, validation_split):

    train_ds = tensorflow_load(
        data_dir=path_image_dataset, validation_split=validation_split, subset="training"
    )
    class_names = train_ds.class_names
    train_ds = train_ds.prefetch(buffer_size=TFRecordConstants.AUTOTUNE)

    val_ds = tensorflow_load(
        data_dir=path_image_dataset, validation_split=validation_split, subset="validation"
    ).prefetch(buffer_size=TFRecordConstants.AUTOTUNE)

    return train_ds, val_ds, class_names


def tensorflow_load(data_dir, validation_split, subset):
    return tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset=subset,
        seed=123,
        image_size=TFRecordConstants.IMAGE_SIZE,
        batch_size=TFRecordConstants.BATCH_SIZE,
    )
