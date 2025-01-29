from flask import Flask
from flask_restplus import Api  # Add this import for Swagger
from config import Config
from models.db import db
from flask_migrate import Migrate
from routes.employee_routes import employee_bp

app = Flask(__name__)

# Initialize Swagger
api = Api(app, version='1.0', title='Employee API', description='A simple Employee API', doc='/swagger')

# Use a test configuration for testing
app.config.from_object(Config)

# Initialize the database with Flask and configure it with Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprint for Employee Routes
app.register_blueprint(employee_bp, url_prefix='/api')

# Function to create and set up the app for testing
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    return app

if __name__ == '__main__':
    app.run(debug=True)
