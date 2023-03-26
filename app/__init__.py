from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import main
    from .assets import assets_bp
    from .items import items_bp

    app.register_blueprint(main)
    app.register_blueprint(assets_bp)
    app.register_blueprint(items_bp)

    return app
