from flask import Blueprint, jsonify, request
from data_classes import User, Exploration, Battle
from your_service import UserService

your_blueprint = Blueprint("your_blueprint", __name__)
user_service = UserService()

@your_blueprint.route("/users/<int:user_id>/history", methods=["GET"])
def get_user_game_history(user_id):
    try:
        game_history = user_service.getUserGameHistory(user_id)
        return jsonify(game_history), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400