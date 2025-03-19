from app import app, db
from models import StudentAthlete, Business, NILMatch

with app.app_context():
    # Check if data already exists
    if StudentAthlete.query.first() and Business.query.first() and NILMatch.query.first():
        print("✅ Mock data already exists. Skipping...")
        exit()

    # Add sample student-athletes
    athletes = [
        StudentAthlete(name="John Doe", email="john@example.com", sport="Basketball", school="State University", year="Junior", interests="Sneakers, Energy Drinks", location="Los Angeles, CA", password="john123"),
        StudentAthlete(name="Jane Smith", email="jane@example.com", sport="Soccer", school="City College", year="Sophomore", interests="Fitness, Healthy Eating", location="New York, NY", password="jane456"),
        StudentAthlete(name="Mike Johnson", email="mike@example.com", sport="Football", school="Southern Tech", year="Senior", interests="Supplements, Gym Equipment", location="Dallas, TX", password="mike789"),
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

    # Fetch added data
    athlete1 = StudentAthlete.query.filter_by(email="john@example.com").first()
    athlete2 = StudentAthlete.query.filter_by(email="jane@example.com").first()
    athlete3 = StudentAthlete.query.filter_by(email="mike@example.com").first()

    business1 = Business.query.filter_by(email="contact@sneakerco.com").first()
    business2 = Business.query.filter_by(email="info@healthybites.com").first()
    business3 = Business.query.filter_by(email="support@progymgear.com").first()

    # Add sample NIL Matches
    nil_deals = [
        NILMatch(athlete_id=athlete1.id, business_id=business1.id, status="Pending", deal_terms="Social media promotion"),
        NILMatch(athlete_id=athlete2.id, business_id=business2.id, status="Approved", deal_terms="Sponsored meal plan"),
        NILMatch(athlete_id=athlete3.id, business_id=business3.id, status="Rejected", deal_terms="Gym sponsorship"),
    ]

    db.session.add_all(nil_deals)
    db.session.commit()

    print("✅ Mock data added successfully! NIL Deals included!")
