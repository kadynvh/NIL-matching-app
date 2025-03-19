import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, StudentAthlete, Business, NILMatch

app = Flask(__name__)
app.secret_key = "your_secret_key"

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
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if user exists and password matches
        athlete = StudentAthlete.query.filter_by(email=email).first()

        if athlete and athlete.password == password:  # Simple password check
            session['user_id'] = athlete.id
            flash("Login successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid email or password. Try again.", "danger")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please log in to access the dashboard.", "warning")
        return redirect(url_for('login'))

    user_id = session['user_id']
    athlete = StudentAthlete.query.get(user_id)

    if not athlete:
        flash("User not found. Please log in again.", "danger")
        return redirect(url_for('login'))

    # Fetch only the NIL deals relevant to the logged-in student-athlete
    matches = NILMatch.query.filter_by(athlete_id=athlete.id).all()

    nil_deals = []
    for match in matches:
        business = Business.query.get(match.business_id)
        nil_deals.append({
            "business": business.name if business else "Unknown",
            "industry": business.industry if business else "Unknown",
            "status": match.status
        })

    return render_template('dashboard.html', athlete=athlete, nil_deals=nil_deals)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("✅ Tables have been created at runtime.")
    app.run(debug=True)
