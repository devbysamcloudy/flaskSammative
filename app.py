from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests

# Initialize app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float)
    barcode = db.Column(db.String(50), unique=True)

@app.route('/fetch/<product_name>', methods=['GET'])
def fetch_and_add(product_name):
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product_name}&search_simple=1&json=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        products = data.get("products", [])
        if not products:
            return jsonify({"error": "Product not found"}), 404

        product = products[0]  # first match
        product_name = product.get("product_name", "Unknown Product")
        barcode = product.get("code", "UnknownBarcode")

        existing_item = Item.query.filter_by(barcode=barcode).first()
        if existing_item:
            return jsonify({"message": "Product already exists in inventory"}), 200

        item = Item(name=product_name, quantity=1, price=0.0, barcode=barcode)
        db.session.add(item)
        db.session.commit()
        return jsonify({"message": f"Product '{product_name}' added to inventory"})

    return jsonify({"error": "Product not found"}), 404

@app.route('/items', methods=['GET', 'POST'])
def items():
    if request.method == 'GET':
        items = Item.query.all()
        result = [
            {"id": i.id, "name": i.name, "quantity": i.quantity, "price": i.price, "barcode": i.barcode}
            for i in items
        ]
        return jsonify(result)

    elif request.method == 'POST':
        data = request.get_json()
        name = data.get("name")
        quantity = data.get("quantity", 1)
        price = data.get("price", 0.0)
        barcode = data.get("barcode")

        existing_item = Item.query.filter_by(barcode=barcode).first()
        if existing_item:
            return jsonify({"message": "Itm already exists"}), 200

        item = Item(name=name, quantity=quantity, price=price, barcode=barcode)
        db.session.add(item)
        db.session.commit()
        return jsonify({"message": f"Item '{name}' added"})

@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": f"Item '{item.name}' deleted"})

@app.route('/items/<int:id>', methods=['PATCH'])
def update_item(id):
    item = Item.query.get_or_404(id)
    data = request.get_json()
    item.name = data.get("name", item.name)
    item.quantity = data.get("quantity", item.quantity)
    item.price = data.get("price", item.price)
    db.session.commit()
    return jsonify({"message": f"Item '{item.name}' updated"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)