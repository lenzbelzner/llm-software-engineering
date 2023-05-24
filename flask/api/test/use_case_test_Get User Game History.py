```python
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from data_classes import User, Exploration, Battle
from your_blueprint import your_blueprint

class GetUserGameHistoryTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(your_blueprint)
        self.client = self.app.test_client()

        self.user_id = 1
        self.user = User(username="testuser", password="testpassword", email="test@example.com", card_collection=[], game_history=[])

        self.exploration1 = Exploration(id=1, location=None, cards_used=[], players=[self.user])
        self.exploration2 = Exploration(id=2, location=None, cards_used=[], players=[self.user])

        self.battle1 = Battle(id=1, location=None, cards_used=[], players=[self.user], winner=self.user)
        self.battle2 = Battle(id=2, location=None, cards_used=[], players=[self.user], winner=self.user)

    @patch("your_blueprint.UserService")
    def test_get_user_game_history(self, mock_user_service):
        mock_user_service.getUserGameHistory.return_value = [self.exploration1, self.exploration2, self.battle1, self.battle2]

        response = self.client.get(f"/users/{self.user_id}/history")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 4)
        self.assertEqual(data[0]["id"], self.exploration1.id)
        self.assertEqual(data[1]["id"], self.exploration2.id)
        self.assertEqual(data[2]["id"], self.battle1.id)
        self.assertEqual(data[3]["id"], self.battle2.id)

        mock_user_service.getUserGameHistory.assert_called_once_with(self.user_id)

if __name__ == "__main__":
    unittest.main()
```
This is a Python unit test for a RESTful Flask blueprint that implements the "Get User Game History" use case. The test checks if the UserService's `getUserGameHistory` method is called with the correct user_id and if the response contains the correct data.