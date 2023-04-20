from flask_restx import Model, fields

from src.api.v1.dto.base import BaseModelResponse


InputEmailConfirmationModel = Model(
    "InputEmailConfirmationModel",
    {
        "code": fields.String(
            required=True, description="Код подтверждения почты"
        ),
    },
)


EmailConfirmationResponse = Model.inherit(
    "EmailConfirmationResponse",
    BaseModelResponse,
    {
        "result": fields.String(example="Ok"),
    },
)
