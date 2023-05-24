from flask import Blueprint, request, jsonify
from data_classes import User, Card, HeroCard, ItemCard, Trade
import app.user_api as user_api
import app.card_api as card_api
import app.trade as trade

trade_blueprint = Blueprint('trade_blueprint', __name__)

@trade_blueprint.route('/trade', methods=['POST'])
def trade_cards():
    data = request.get_json()

    user1_id = data['user1_id']
    user2_id = data['user2_id']
    cards1 = data['cards1']
    cards2 = data['cards2']

    user1 = user_api.getUserById(user1_id)
    user2 = user_api.getUserById(user2_id)

    cards1_data = card_api.getCardsByIds(cards1)
    cards2_data = card_api.getCardsByIds(cards2)

    updated_users = trade.performTrade(user1, user2, cards1_data, cards2_data)

    user_api.updateUser(updated_users['user1'])
    user_api.updateUser(updated_users['user2'])

    return jsonify(message='Updated card collections for both users')