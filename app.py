from flask import Flask, render_template, redirect, url_for, jsonify

app = Flask(__name__)

# Define your routes/views
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/error')
def error():
    return render_template('error.html')  # Assuming you have an 'error.html' file in your templates folder

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('error'))



# Items route
@app.route('/items')
def items():
    item_list = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]
    return jsonify(item_list)

# Single item route
@app.route('/item/<int:item_id>')
def item(item_id):
    items = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
        {"id": 3, "name": "Item 3"},
    ]
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return "Item not found", 404

# Assets route
@app.route('/assets')
def assets():
    asset_list = [
        {"id": 1, "name": "Asset 1"},
        {"id": 2, "name": "Asset 2"},
        {"id": 3, "name": "Asset 3"},
    ]
    return jsonify(asset_list)

# Single asset route
@app.route('/asset/<int:asset_id>')
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



if __name__ == '__main__':
    app.run(debug=True)
