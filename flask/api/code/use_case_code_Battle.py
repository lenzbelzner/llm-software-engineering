from flask import Blueprint, request, jsonify
from data_classes import User, HeroCard, Location, Battle
from app import UserController, CardController, LocationController, BattleController, GPTManager

battle_blueprint = Blueprint('battle_blueprint', __name__)

@battle_blueprint.route('/battle', methods=['POST'])
def battle():
    data = request.get_json()

    user_id = data.get('user_id')
    cards = data.get('cards')
    location_id = data.get('location')

    if not user_id or not cards or not location_id:
        return jsonify({'error': 'Missing required data'}), 400

    user = UserController.getUser(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    card_objects = CardController.getCards(cards)
    if not card_objects:
        return jsonify({'error': 'Cards not found'}), 404

    location = LocationController.getLocation(location_id)
    if not location:
        return jsonify({'error': 'Location not found'}), 404

    event_description = GPTManager.generateEventDescription(user, card_objects, location)
    battle = BattleController.initiateBattle(user, card_objects, location, event_description)

    return jsonify(battle.to_dict()), 200