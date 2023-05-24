from flask import Blueprint, request, jsonify
from data_classes import User, Card, CSVManager, UserManager

your_blueprint = Blueprint("your_blueprint", __name__)

user_manager = UserManager(CSVManager("users.csv"))

@your_blueprint.route("/users/<int:user_id>/collection/remove", methods=["DELETE"])
def remove_card_from_collection(user_id):
    card_id = request.json["card_id"]

    # Get the user by ID
    user = user_manager.getUserById(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Get the card by ID
    card = Card(id=card_id, name="Test Card", image="test_image.png", description="A test card")

    # Remove the card from the user's collection
    if not user_manager.removeCard(user, card):
        return jsonify({"error": "Card not found in user's collection"}), 404

    # Update the user in the CSV file
    if not user_manager.csv_manager.updateUserInCSV(user):
        return jsonify({"error": "Failed to update user in CSV file"}), 500

    return jsonify({"message": "Updated card collection", "card_id": card_id}), 200