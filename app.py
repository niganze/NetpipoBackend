import sys
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

# Use a test configuration for testing
app.config.from_object(Config)

# Initialize the database with Flask and configure it with Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Register Namespace for Employee Routes
api.add_namespace(employee_ns, path='/api/employees')

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False)
    except Exception as e:
        print(f"Error starting the server: {e}", file=sys.stderr)
