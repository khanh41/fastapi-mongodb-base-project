from typing import List

from pydantic import BaseModel, Field


class PredictSchema(BaseModel):
    raceID: str = Field(...)
    timePredict: str = Field(...)
    typePredict: str = Field(...)
    status: int = Field(...)
    horseRank: List = Field(...)
    lastFinalRank: List = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "raceID": "1233",
                "timePredict": "5H 22/05/2021",
                "typePredict": "T1",
                "status": 1,
                "horseRank": [1, 2, 3, 4, 5, 6],
                "horseRank": [1, 2, 3],
            }
        }
