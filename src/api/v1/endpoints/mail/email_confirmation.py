from http import HTTPStatus

from flask_restx import Namespace, Resource, fields, reqparse

from src.db.db_factory import db
from src.repositories.auth_repository import AuthRepository
from src.services.auth_service import AuthService


api = Namespace(name="mail", path="/api/v1/users")
parser = reqparse.RequestParser()
parser.add_argument("code", type=str)


email_confirmayion_model_response = api.model(
    "EmailConfirmationResponse",
    {
        "result": fields.String(example="Ok"),
    },
)


@api.route("/<int:user_id>/mail")
class EmailConfirmation(Resource):
    @api.doc(
        responses={
            int(HTTPStatus.OK): (
                "Email confirmed.",
                email_confirmayion_model_response,
            ),
        },
        description="Подтверждение почты.",
    )
    @api.param("code", "Код подтверждения почты")
    def put(self, user_id):
        args = parser.parse_args()
        code = args.get("code")
        auth_repository = AuthRepository(db)
        auth_service = AuthService(repository=auth_repository)
        # нужен редис
        return "Ok"
