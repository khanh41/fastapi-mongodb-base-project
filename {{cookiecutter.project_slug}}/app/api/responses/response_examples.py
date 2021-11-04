responses = {
    "text_detection": {
        200: {
            "model": "TextDetectionModel",
            "description": "Data predicted",
            "content": {
                "application/json": {
                    "example": {
                        "status": "success",
                        "status_code": 200,
                        "message": "",
                        "data": {
                            "coordinates": [
                                [
                                    21,
                                    229,
                                    186,
                                    248
                                ],
                                [
                                    22,
                                    212,
                                    156,
                                    229
                                ],
                                [
                                    258,
                                    206,
                                    394,
                                    224
                                ]
                            ],
                            "name_card_img": "base64"
                        }
                    }
                }
            },
        },
    },
}
