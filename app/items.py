from flask import Blueprint, jsonify

items_bp = Blueprint('items', __name__)

# Items route
@items_bp.route('/items')
def items():
    asset_list = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]
    return jsonify(asset_list)

# Single asset route
@items_bp.route('/item/<int:item_id>')
def item(item_id):
    items = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]
    item = next((a for a in items if a["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return "Item not found", 404
