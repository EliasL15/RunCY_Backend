from flask import Flask
from models import db, Race
from datetime import datetime

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_race():
    with app.app_context():
        new_race = Race(start_time=datetime.utcnow(), is_active=True)
        db.session.add(new_race)
        db.session.commit()
        print("New race created successfully!")

if __name__ == '__main__':
    create_race()
