from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (for demonstration purposes only)
orders = []
users = []  # Assuming we have a user list to validate user existence

# Route for placing an order
@app.route('/', methods=['POST'])
def place_order():
    data = request.get_json()
    username = data.get('username')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    # Basic validation
    if not username or not product_id or not quantity:
        return jsonify({"error": "Username, product ID, and quantity are required!"}), 400

    # Check if user exists
    if not any(user['username'] == username for user in users):
        return jsonify({"error": "User does not exist!"}), 404

    # Create a new order
    order_id = len(orders) + 1
    orders.append({
        'order_id': order_id,
        'username': username,
        'product_id': product_id,
        'quantity': quantity
    })
    return jsonify({"message": "Order placed successfully!", "order_id": order_id}), 201

# Route to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)  # Changed port for order service
