import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, StudentAthlete, Business

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

        if athlete and athlete.password == password:
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

    # Get manually selected businesses from session storage
    selected_deals = session.get(f"selected_deals_{user_id}", [])

    return render_template('dashboard.html', athlete=athlete, selected_deals=selected_deals)

@app.route('/businesses', methods=['GET', 'POST'])
def businesses():
    if 'user_id' not in session:
        flash("Please log in to browse businesses.", "warning")
        return redirect(url_for('login'))

    user_id = session['user_id']
    athlete = StudentAthlete.query.get(user_id)

    if not athlete:
        flash("User not found. Please log in again.", "danger")
        return redirect(url_for('login'))

    businesses = Business.query.all()

    if request.method == 'POST':
        selected_business_id = request.form.get('business_id')
        business = Business.query.get(selected_business_id)

        if business:
            selected_deals = session.get(f"selected_deals_{user_id}", [])
            if business.name not in [deal["business"] for deal in selected_deals]:
                selected_deals.append({
                    "business": business.name,
                    "industry": business.industry,
                    "status": "Pending"
                })
                session[f"selected_deals_{user_id}"] = selected_deals
                flash("Business added to your NIL deals!", "success")
            else:
                flash("This business is already in your NIL deals.", "warning")

        return redirect(url_for('dashboard'))

    return render_template('businesses.html', athlete=athlete, businesses=businesses)

@app.route('/remove_business', methods=['POST'])
def remove_business():
    if 'user_id' not in session:
        flash("Please log in to modify your NIL deals.", "warning")
        return redirect(url_for('login'))

    user_id = session['user_id']
    business_name = request.form.get('business_name')

    if business_name:
        selected_deals = session.get(f"selected_deals_{user_id}", [])
        selected_deals = [deal for deal in selected_deals if deal["business"] != business_name]
        session[f"selected_deals_{user_id}"] = selected_deals
        flash(f"Removed {business_name} from your NIL deals.", "info")

    return redirect(url_for('dashboard'))

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
