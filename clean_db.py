from flask import Flask
from models import db, Race, GpsPoint

app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def clean_database():
    with app.app_context():
        try:
            # Delete all GPS points first to maintain referential integrity
            GpsPoint.query.delete()
            # Then delete all races
            Race.query.delete()
            # Commit the changes
            db.session.commit()
            print("Database cleaned successfully! All races and GPS points have been removed.")
        except Exception as e:
            db.session.rollback()
            print(f"Error cleaning database: {str(e)}")

if __name__ == '__main__':
    clean_database()