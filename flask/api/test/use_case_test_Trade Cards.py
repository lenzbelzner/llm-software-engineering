```python
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from data_classes import User, Card, HeroCard, ItemCard, Trade
from app import app, trade_blueprint

class TestTradeBlueprint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        app.register_blueprint(trade_blueprint)

    @patch('app.user_api.getUserById')
    @patch('app.card_api.getCardsByIds')
    @patch('app.trade.performTrade')
    @patch('app.user_api.updateUser')
    def test_trade_cards(self, mock_updateUser, mock_performTrade, mock_getCardsByIds, mock_getUserById):
        user1 = User(username='user1', password='password1', email='user1@example.com', card_collection=[], game_history=[])
        user2 = User(username='user2', password='password2', email='user2@example.com', card_collection=[], game_history=[])
        hero_card = HeroCard(id=1, name='hero1', image='hero1.png', description='hero card', health=100, attack=50, defense=30)
        item_card = ItemCard(id=2, name='item1', image='item1.png', description='item card', effect='heal')

        mock_getUserById.side_effect = [user1, user2]
        mock_getCardsByIds.side_effect = [[hero_card], [item_card]]
        mock_performTrade.return_value = {'user1': user1, 'user2': user2}
        mock_updateUser.return_value = 'success'

        response = self.app.post('/trade', data=json.dumps({
            'user1_id': 1,
            'user2_id': 2,
            'cards1': [1],
            'cards2': [2]
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Updated card collections for both users'})

        mock_getUserById.assert_any_call(1)
        mock_getUserById.assert_any_call(2)
        mock_getCardsByIds.assert_any_call([1])
        mock_getCardsByIds.assert_any_call([2])
        mock_performTrade.assert_called_once_with(user1, user2, [hero_card], [item_card])
        mock_updateUser.assert_any_call(user1)
        mock_updateUser.assert_any_call(user2)

if __name__ == '__main__':
    unittest.main()
```
This is a Python unit test for the specified use case using the Flask blueprint. It tests the trade cards functionality by mocking the required functions and asserting the expected behavior.