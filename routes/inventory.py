# routes/inventory.py
from flask import Blueprint, jsonify
from models import db, Item
import requests

inventory_bp = Blueprint('inventory', __name__)

# External API + add to database
@inventory_bp.route('/fetch/<barcode>', methods=['GET'])
def fetch_and_add(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("status") == 1:
            product_name = data["product"].get("product_name", "Unknown Product")

            # Check if item already exists
            existing_item = Item.query.filter_by(barcode=barcode).first()
            if existing_item:
                return jsonify({"message": "Product already exists in inventory"}), 200

            # Add new product
            item = Item(name=product_name, quantity=1, price=0.0, barcode=barcode)
            db.session.add(item)
            db.session.commit()
            return jsonify({"message": f"Product '{product_name}' added to inventory"})

    return jsonify({"error": "Product not found"}), 404