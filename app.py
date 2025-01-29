from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
