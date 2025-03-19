import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, StudentAthlete, Business, NILMatch

app = Flask(__name__)

# Ensure the 'instance' directory exists
INSTANCE_DIR = os.path.join(os.getcwd(), "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(INSTANCE_DIR, 'nil.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html', message="Welcome to NIL Deal Matcher!")

@app.route('/dashboard')
def dashboard():
    with app.app_context():
        athletes = StudentAthlete.query.all()
        matches = NILMatch.query.all()

        # Fetch NIL deals along with business information
        nil_deals = []
        for match in matches:
            business = Business.query.get(match.business_id)
            nil_deals.append({
                "athlete": match.athlete.name,
                "business": business.name if business else "Unknown",
                "industry": business.industry if business else "Unknown",
                "status": match.status
            })

    return render_template('dashboard.html', athletes=athletes, nil_deals=nil_deals)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Tables have been created at runtime.")
    app.run(debug=True)
