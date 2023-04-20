from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource

from src.api.v1.dto.base import ErrorModel, ErrorModelResponse
from src.api.v1.dto.email_confirmation import EmailConfirmationResponse
from src.api.v1.dto.user import InputUserRegisterModel
from src.db import db_models
from src.repositories.auth_repository import AuthRepository
from src.repositories.role_repository import RolesRepository
from src.services.auth_service import AuthService


api = Namespace(name="auth", path="/api/v1/users")
api.models[InputUserRegisterModel.name] = InputUserRegisterModel
api.models[EmailConfirmationResponse.name] = EmailConfirmationResponse
api.models[ErrorModel.name] = ErrorModel
api.models[ErrorModelResponse.name] = ErrorModelResponse


@api.route("/<string:user_id>/mail")
class EmailConfirmation(Resource):
    @api.doc(
        responses={
            int(HTTPStatus.OK): (
                "Email confirmed.",
                EmailConfirmationResponse,
            ),
            int(HTTPStatus.NOT_FOUND): (
                "Email not found.",
                ErrorModelResponse,
            ),
        },
        description="Подтверждение почты.",
    )
    @api.expect(InputUserRegisterModel)
    def post(self, user_id):
        secret_code = request.json.get("code")

        auth_repository = AuthRepository(db_models.db)
        roles_repository = RolesRepository(db_models.db)
        auth_service = AuthService(
            auth_repository=auth_repository, roles_repository=roles_repository
        )
        return auth_service.email_confirmation(
            secret_code=secret_code, user_id=user_id
        )
