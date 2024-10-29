from flask import Flask
from .routes.cat_routes import cats_bp
from .db import migrate, db
from .models import cat

def create_app():

    app = Flask(__name__)
    # __name__ stores the name of the module we're in
    app.config['SQLALCHEMY_TRACK_NOTIFICATION'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        'postgresql+psycopg2://elzara:postgres@localhost:5432/flasky_development'
    )

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cats_bp)

    return app
