import os  # For file path handling
import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy

app = Flask(__name__)

# Ensure the 'instance' directory exists
INSTANCE_DIR = os.path.join(os.getcwd(), "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

# Configure the database (store it in 'instance/')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(INSTANCE_DIR, 'nil.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize the database
db = SQLAlchemy(app)

@app.route('/')
def home():
    # Render the index.html template with a welcome message
    return render_template('index.html', message="Welcome to NIL Deal Matcher!")

if __name__ == '__main__':
    app.run(debug=True)
