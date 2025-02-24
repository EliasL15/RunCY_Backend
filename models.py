from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class GpsPoint(db.Model):
    __tablename__ = 'gps_points'
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    race_id = db.Column(db.Integer, db.ForeignKey('races.id'), nullable=False)

class Race(db.Model):
    __tablename__ = 'races'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean, default=True)
    points = db.relationship('GpsPoint', backref='race', lazy=True)

    @property
    def last_point(self):
        return GpsPoint.query.filter_by(race_id=self.id).order_by(GpsPoint.timestamp.desc()).first()
