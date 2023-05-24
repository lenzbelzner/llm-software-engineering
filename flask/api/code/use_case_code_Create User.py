from flask import Blueprint, request, jsonify
from data_classes import User, CSVManager, AuthManager

user_routes = Blueprint("user_routes", __name__)
csv_manager = CSVManager("test.csv")
auth_manager = AuthManager("testdomain", "testclientid", "testclientsecret")

@user_routes.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data or not all(key in data for key in ("username", "password", "email")):
        return jsonify({"error": "Invalid request data"}), 400

    username = data["username"]
    password = data["password"]
    email = data["email"]

    hashed_password = auth_manager.hashPassword(password)

    user = User(username, hashed_password, email, [], [])

    success = csv_manager.saveUser(user.username, user.password, user.email)

    if success:
        return jsonify(user.__dict__), 201
    else:
        return jsonify({"error": "Failed to create user"}), 500