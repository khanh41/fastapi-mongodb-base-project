import json

from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.api.database.excute.predict import (
    add_predict,
    delete_predict,
    retrieve_predicts,
    retrieves_predict_by_race_id,
    update_predict,
)
from app.api.database.models.predict import PredictSchema
from app.api.responses.base import BaseResponse
from app.api.services.predict_service import Predict

router = APIRouter()
response = BaseResponse()
predict_service = Predict()


@router.get("/", response_description="predicts retrieved")
async def get_predicts():
    predicts = retrieve_predicts()
    if predicts:
        response.base_response["data"] = predicts
        return response.base_response
    return BaseResponse.error_response("Empty list returned")


@router.get("/{id}", response_description="predict data retrieved")
async def get_predict_data(id):
    # predict = retrieve_predict(id)
    predict = retrieves_predict_by_race_id(id)
    if predict:
        response.base_response["data"] = predict
        return response.base_response
    return BaseResponse.error_response("predict doesn't exist.", 404)


@router.put("/{id}")
async def update_predict_data(id: str, req: PredictSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_predict = update_predict(id, req)
    if updated_predict:
        return BaseResponse.success_response(
            "predict with ID: {} name update is successful".format(id),
        )
    return BaseResponse.error_response(
        "There was an error updating the predict data.",
        404,
    )


@router.delete("/{id}", response_description="predict data deleted from the database")
async def delete_predict_data(id: str):
    deleted_predict = delete_predict(id)
    if deleted_predict:
        return BaseResponse.success_response(
            "predict with ID: {} removed".format(id), "predict deleted successfully"
        )
    return BaseResponse.error_response(
        "predict with id {0} doesn't exist".format(id), 404
    )