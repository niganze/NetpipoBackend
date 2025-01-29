from flask import Flask
from config import Config
from models.db import db
from flask_migrate import Migrate
from routes.employee_routes import employee_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database with Flask and configure it with Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Register Blueprint for Employee Routes
app.register_blueprint(employee_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
