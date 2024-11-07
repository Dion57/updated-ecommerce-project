from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    return jsonify({"products": ["product1", "product2", "product3"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# Sample data for demonstration purposes
PRODUCTS = [
    {"id": 1, "name": "Product 1", "price": 19.99},
    {"id": 2, "name": "Product 2", "price": 29.99},
    {"id": 3, "name": "Product 3", "price": 39.99}
]

@app.route('/products', methods=['GET'])
def get_products():
    """
    Endpoint to get the list of products.
    Returns:
        JSON: A JSON response containing a list of products.
    """
    return jsonify({
        "status": "success",
        "data": PRODUCTS
    }), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    """
    Endpoint to get a product by its ID.
    
    Args:
        product_id (int): The ID of the product to retrieve.
    
    Returns:
        JSON: A JSON response containing the product details or an error message.
    """
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product:
        return jsonify({
            "status": "success",
            "data": product
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(host='0.0.0.0', port=5001, debug=True)

