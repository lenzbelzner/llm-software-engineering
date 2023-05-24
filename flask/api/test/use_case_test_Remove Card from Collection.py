```python
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from data_classes import User, Card, CSVManager
from your_blueprint import your_blueprint

class TestRemoveCardFromCollection(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(your_blueprint)
        self.client = self.app.test_client()

        self.user_id = 1
        self.card_id = 100
        self.user = User(username="testuser", password="testpassword", email="test@example.com", card_collection=[], game_history=[])
        self.card = Card(id=self.card_id, name="Test Card", image="test_image.png", description="A test card")

    @patch("your_blueprint.CSVManager")
    @patch("your_blueprint.UserManager")
    def test_remove_card_from_collection(self, mock_user_manager, mock_csv_manager):
        # Mock the UserManager and CSVManager methods
        mock_user_manager.getUserById.return_value = self.user
        mock_user_manager.removeCard.return_value = True
        mock_csv_manager.readUserFromCSV.return_value = self.user
        mock_csv_manager.updateUserInCSV.return_value = True

        # Make the DELETE request
        response = self.client.delete(f"/users/{self.user_id}/collection/remove", json={"card_id": self.card_id})

        # Check the response status and JSON data
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["message"], "Updated card collection")
        self.assertEqual(response_data["card_id"], self.card_id)

        # Check if the mocked methods were called with the correct arguments
        mock_user_manager.getUserById.assert_called_once_with(self.user_id)
        mock_user_manager.removeCard.assert_called_once_with(self.user, self.card)
        mock_csv_manager.readUserFromCSV.assert_called_once_with(self.user_id)
        mock_csv_manager.updateUserInCSV.assert_called_once_with(self.user)

if __name__ == "__main__":
    unittest.main()
```
This is a Python unit test for the "Remove Card from Collection" use case. It uses the unittest library and mocks the UserManager and CSVManager classes to test the RESTful Flask blueprint.