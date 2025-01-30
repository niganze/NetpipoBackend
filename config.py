import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://netpipo_db_user:CnMxWQmq7v2TVLaOW4c8SaBi8wubvCfD@dpg-cudio83tq21c738fes60-a.oregon-postgres.render.com/netpipo_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "supersecretkey"

