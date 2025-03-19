from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize db

class StudentAthlete(db.Model):
    __tablename__ = 'student_athlete'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Required for login
    sport = db.Column(db.String(50), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(20), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    interests = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(100), nullable=True)

class Business(db.Model):
    __tablename__ = 'business'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    target_sports = db.Column(db.String(200), nullable=True)
    budget = db.Column(db.Float, nullable=True)
