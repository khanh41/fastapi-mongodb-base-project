"""Custom base model."""

from __future__ import annotations

from pydantic import BaseModel


class CustomBaseModel(BaseModel):
    """Custom Base Model."""

    @classmethod
    def to_model(cls, datas: (tuple | list)):
        """Convert data to model.

        Args:
            datas: Data to convert.

        Returns:
            Converted model.
        """
        model_json = {}
        model_keys = list(cls.__fields__.keys())
        for index, data in enumerate(datas):
            model_json[model_keys[index]] = data
        return cls.parse_obj(model_json)
