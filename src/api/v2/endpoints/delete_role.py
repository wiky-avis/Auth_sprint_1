from flask_restx import Namespace, Resource


api = Namespace(name="v2", path="/api/v2/roles")


@api.route("/delete_role")
class DeleteRole(Resource):
    def delete(self):
        pass
