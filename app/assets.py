from flask import Blueprint, jsonify

assets_bp = Blueprint('assets', __name__)

# Assets route
@assets_bp.route('/assets')
def assets():
    asset_list = [
        {"id": 1, "name": "Asset 1"},
        {"id": 2, "name": "Asset 2"},
        {"id": 3, "name": "Asset 3"},
    ]
    return jsonify(asset_list)

# Single asset route
@assets_bp.route('/asset/<int:asset_id>')
def asset(asset_id):
    assets = [
        {"id": 1, "name": "Asset 1"},
        {"id": 2, "name": "Asset 2"},
        {"id": 3, "name": "Asset 3"},
    ]
    asset = next((a for a in assets if a["id"] == asset_id), None)
    if asset:
        return jsonify(asset)
    else:
        return "Asset not found", 404
