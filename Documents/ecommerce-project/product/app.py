from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products')
def get_products():
    return jsonify({"products": ["product1", "product2", "product3"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
