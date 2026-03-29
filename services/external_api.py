# routes/inventory.py
from flask import Blueprint, jsonify
from models import db, Item
import requests

inventory_bp = Blueprint('inventory', __name__)

def fetch_product(barcode):
    """
    Fetch product details from OpenFoodFacts API using a barcode.
    Returns a dictionary with product info or None if not found.
    """
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == 1:  # product found
            product = data["product"]
            return {
                "name": product.get("product_name", "Unknown Product"),
                "barcode": barcode
            }
    return None

@inventory_bp.route('/fetch/<barcode>', methods=['GET'])
def fetch_and_add(barcode):
    """
    Fetch product from OpenFoodFacts API and add it to database.
    """
    product = fetch_product(barcode)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Check if product already exists to avoid duplicates
    existing_item = Item.query.filter_by(barcode=barcode).first()
    if existing_item:
        return jsonify({"message": "Product already exists in inventory"}), 200

    # Add new product to database
    item = Item(name=product["name"], quantity=1, price=0.0, barcode=barcode)
    db.session.add(item)
    db.session.commit()

    return jsonify({"message": f"Product '{product['name']}' added to inventory"})