from app import app, db
from models import StudentAthlete, Business

with app.app_context():
    # Add sample student-athletes
    athletes = [
        StudentAthlete(name="John Doe", email="john@example.com", sport="Basketball", school="State University", year="Junior", interests="Sneakers, Energy Drinks", location="Los Angeles, CA"),
        StudentAthlete(name="Jane Smith", email="jane@example.com", sport="Soccer", school="City College", year="Sophomore", interests="Fitness, Healthy Eating", location="New York, NY"),
        StudentAthlete(name="Mike Johnson", email="mike@example.com", sport="Football", school="Southern Tech", year="Senior", interests="Supplements, Gym Equipment", location="Dallas, TX")
    ]

    # Add sample businesses
    businesses = [
        Business(name="SneakerCo", email="contact@sneakerco.com", industry="Apparel", target_sports="Basketball, Football", budget=50000, location="Los Angeles, CA"),
        Business(name="Healthy Bites", email="info@healthybites.com", industry="Food & Beverage", target_sports="Soccer, Track", budget=20000, location="New York, NY"),
        Business(name="Pro Gym Gear", email="support@progymgear.com", industry="Fitness Equipment", target_sports="Football, Basketball", budget=75000, location="Dallas, TX")
    ]

    # Add data to the database
    db.session.add_all(athletes + businesses)
    db.session.commit()

    print("✅ Mock data added successfully!")