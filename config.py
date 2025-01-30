import os

class Config:
    # Ensure SSL is required for Render's PostgreSQL
    db_url = 'postgresql://netpipo_db_user:CnMxWQmq7v2TVLaOW4c8SaBi8wubvCfD@dpg-cudio83tq21c738fes60-a.oregon-postgres.render.com/netpipo_db'
    # Add SSL mode to the URL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', db_url + '?sslmode=require')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecretkey"