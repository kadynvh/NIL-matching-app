from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize db without binding it yet

def init_db(app):  # Ensure db is properly linked
    db.init_app(app)
    with app.app_context():
        db.create_all()
        print("✅ Tables have been created!")

class StudentAthlete(db.Model):
    __tablename__ = 'student_athlete'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
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

class NILMatch(db.Model):
    __tablename__ = 'nil_match'
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('student_athlete.id'), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default="Pending")
    deal_terms = db.Column(db.Text, nullable=True)

    athlete = db.relationship('StudentAthlete', backref='matches')
    business = db.relationship('Business', backref='matches')
