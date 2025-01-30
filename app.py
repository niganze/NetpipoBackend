from flask import Flask
from flask_restx import Api
from config import Config
from models.db import db
from flask_migrate import Migrate
from routes.employee_routes import employee_ns
import os

app = Flask(__name__)

# Initialize Swagger
api = Api(app, version='1.0', title='Employee API', description='A simple Employee API', doc='/swagger')

# Load the configuration from the environment
app.config.from_object(Config)

# Initialize the database with Flask and configure it with Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Register Namespace for Employee Routes
api.add_namespace(employee_ns, path='/api/employees')

if __name__ == '__main__':
    # Bind to the port defined by the PORT environment variable, with a fallback to 5000
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
