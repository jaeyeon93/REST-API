from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
# when the app runs, db.create.all() execute and sqlite:///data.db file created