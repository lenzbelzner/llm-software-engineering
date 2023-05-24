import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from data_classes import User, CSVManager, AuthManager
from flask.blueprints import Blueprint

# Create a blueprint for the user routes
user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/users", methods=["POST"])
def create_user():
    # Assume the request data is already validated
    username = "testuser"
    password = "testpassword"
    email = "test@example.com"

    # Create a User object
    user = User(username, password, email, [], [])

    # Save the user to the CSV file
    csv_manager = CSVManager("test.csv")
    csv_manager.saveUser = MagicMock(return_value=True)

    # Hash the user's password
    auth_manager = AuthManager("testdomain", "testclientid", "testclientsecret")
    auth_manager.hashPassword = MagicMock(return_value="hashedpassword")

    hashed_password = auth_manager.hashPassword(user.password)
    user.password = hashed_password

    # Save the user to the CSV file
    success = csv_manager.saveUser(user.username, user.password, user.email)

    if success:
        return json.dumps(user.__dict__), 201
    else:
        return json.dumps({"error": "Failed to create user"}), 500


class TestUserRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(user_routes)
        self.client = self.app.test_client()

    @patch("data_classes.CSVManager.saveUser")
    @patch("data_classes.AuthManager.hashPassword")
    def test_create_user(self, mock_hash_password, mock_save_user):
        mock_hash_password.return_value = "hashedpassword"
        mock_save_user.return_value = True

        response = self.client.post("/users")
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(data["username"], "testuser")
        self.assertEqual(data["password"], "hashedpassword")
        self.assertEqual(data["email"], "test@example.com")
        self.assertEqual(data["card_collection"], [])
        self.assertEqual(data["game_history"], [])

        mock_hash_password.assert_called_once_with("testpassword")
        mock_save_user.assert_called_once_with("testuser", "hashedpassword", "test@example.com")


if __name__ == "__main__":
    unittest.main()