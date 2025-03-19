from app import db  # Import the existing db instance from app.py

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)  # 'athlete' or 'business'

# Profile model
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Link to the User table
    location = db.Column(db.String(100))
    interests = db.Column(db.String(200))  # Comma-separated interests
    followers = db.Column(db.Integer)      # For athletes
    budget = db.Column(db.Integer)         # For businesses
