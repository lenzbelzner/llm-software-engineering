```python
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from data_classes import User, HeroCard, Location, Battle
from app import app, UserController, CardController, LocationController, BattleController, GPTManager

class TestBattleUseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.UserController')
    @patch('app.CardController')
    @patch('app.LocationController')
    @patch('app.BattleController')
    @patch('app.GPTManager')
    def test_battle_use_case(self, mock_gpt_manager, mock_battle_controller, mock_location_controller, mock_card_controller, mock_user_controller):
        # Set up mock data
        user = User(username='testuser', password='testpassword', email='test@example.com', card_collection=[], game_history=[])
        hero_card = HeroCard(id=1, name='Test Hero', image='test_hero.png', description='A test hero', health=10, attack=5, defense=3)
        location = Location(id=1, name='Test Location', image='test_location.png', description='A test location')
        battle = Battle(id=1, location=location, cards_used=[hero_card], players=[user], winner=user)

        # Set up mock return values
        mock_user_controller.getUser.return_value = user
        mock_card_controller.getCards.return_value = [hero_card]
        mock_location_controller.getLocation.return_value = location
        mock_battle_controller.initiateBattle.return_value = battle
        mock_gpt_manager.generateEventDescription.return_value = 'A test battle event description'

        # Send POST request to /battle
        response = self.app.post('/battle', data=json.dumps({'user_id': 1, 'cards': [1], 'location': 1}), content_type='application/json')

        # Check response status code and data
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['id'], 1)
        self.assertEqual(response_data['location']['name'], 'Test Location')
        self.assertEqual(response_data['cards_used'][0]['name'], 'Test Hero')
        self.assertEqual(response_data['players'][0]['username'], 'testuser')
        self.assertEqual(response_data['winner']['username'], 'testuser')

if __name__ == '__main__':
    unittest.main()
```
This is a Python unit test for the RESTful Flask blueprint that implements the specified use case for initiating a battle event with selected cards and location. The test uses the unittest module and mocks the necessary controllers and managers to isolate the test case.