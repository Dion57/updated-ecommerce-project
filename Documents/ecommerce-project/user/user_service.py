from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (for demonstration purposes only)
users = []

# Route for user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    # Basic validation
    if not username or not email:
        return jsonify({"error": "Username and email are required!"}), 400

    # Check if user already exists
    for user in users:
        if user['username'] == username:
            return jsonify({"error": "User already exists!"}), 400

    # Add user to the list
    users.append({'username': username, 'email': email})
    return jsonify({"message": "User registered successfully!"}), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
