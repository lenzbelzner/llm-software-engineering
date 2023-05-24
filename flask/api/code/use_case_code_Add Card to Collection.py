from flask import Blueprint, request, jsonify
from data_classes import User, Card, HeroCard, ItemCard
from app.services.user_service import UserService

user_blueprint = Blueprint('user_blueprint', __name__)
user_service = UserService()

@user_blueprint.route('/users/<int:user_id>/collection/add', methods=['POST'])
def add_card_to_collection(user_id):
    card_data = request.get_json()
    card = HeroCard(**card_data) if 'health' in card_data else ItemCard(**card_data)
    updated_collection = user_service.addUserCardToCollection(user_id, card)
    if updated_collection is not None:
        return jsonify({'collection': [card.__dict__ for card in updated_collection]}), 200
    else:
        return jsonify({'error': 'Failed to add card to collection'}), 400