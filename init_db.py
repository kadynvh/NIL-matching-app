from app import app
from models import db

print("Starting database initialization...")

with app.app_context():
    print("Inside application context...")
    db.create_all()
    print("Database tables created successfully!")


