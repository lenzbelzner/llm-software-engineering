def create_user_controller_blueprint(user_service):
    from flask import Blueprint, json, request

    user_controller = Blueprint("user_controller", __name__)

    @user_controller.route("/users/<int:user_id>/collection", methods=["GET"])
    def get_user_collection(user_id):
        try:
            card_collection = user_service.get_user_collection(user_id)
            return json.dumps([card.__dict__ for card in card_collection]), 200
        except Exception as e:
            return str(e), 404

    return user_controller