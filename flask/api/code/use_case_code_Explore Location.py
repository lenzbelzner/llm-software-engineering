from flask import Blueprint, request, jsonify
from data_classes import User, HeroCard, ItemCard, Location, Exploration
from controllers.user_controller import ExplorationService

explore_bp = Blueprint('explore', __name__)

exploration_service = ExplorationService()

@explore_bp.route('/explore', methods=['POST'])
def explore_location():
    user_id = request.json.get('user_id')
    cards = request.json.get('cards')
    location = request.json.get('location')

    try:
        exploration = exploration_service.initiateExploration(user_id, cards, location)
        return jsonify(exploration.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400