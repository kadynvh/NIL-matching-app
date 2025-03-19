from app import db  # Import the existing db instance from app.py

# User model
class StudentAthlete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    sport = db.Column(db.String(50), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(20), nullable=False)  # Freshman, Sophomore, etc.
    bio = db.Column(db.Text, nullable=True)
    interests = db.Column(db.String(200), nullable=True)  # Keywords for matching
    location = db.Column(db.String(100), nullable=True)  # New field for matching by city/state

# Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=True)  # Business location for geo-matching
    target_sports = db.Column(db.String(200), nullable=True)  # Sports they want to sponsor
    budget = db.Column(db.Float, nullable=True)

# NIL Matching Model (Tracks which businesses are matched with which athletes)
class NILMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('student_athlete.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pending")  # Pending, Approved, Rejected
    deal_terms = db.Column(db.Text, nullable=True)  # Description of deal

    athlete = db.relationship('StudentAthlete', backref='matches')
    business = db.relationship('Business', backref='matches')
