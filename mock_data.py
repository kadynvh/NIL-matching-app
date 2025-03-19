from app import app, db
from models import StudentAthlete, Business

with app.app_context():
    # Check if data already exists
    if StudentAthlete.query.first() and Business.query.first():
        print("✅ Mock data already exists. Skipping...")
        exit()

    # Add sample student-athletes
    athletes = [
        StudentAthlete(name="John Doe", email="john@example.com", sport="Basketball", school="State University", year="Junior", interests="Sneakers, Energy Drinks", location="Los Angeles, CA", password="john123"),
        StudentAthlete(name="Jane Smith", email="jane@example.com", sport="Soccer", school="City College", year="Sophomore", interests="Fitness, Healthy Eating", location="New York, NY", password="jane456"),
        StudentAthlete(name="Mike Johnson", email="mike@example.com", sport="Football", school="Southern Tech", year="Senior", interests="Supplements, Gym Equipment", location="Dallas, TX", password="mike789"),
    ]

    # Add sample businesses (Now with 10+ businesses)
    businesses = [
        Business(name="SneakerCo", email="contact@sneakerco.com", industry="Apparel", target_sports="Basketball, Football", budget=50000, location="Los Angeles, CA"),
        Business(name="Healthy Bites", email="info@healthybites.com", industry="Food & Beverage", target_sports="Soccer, Track", budget=20000, location="New York, NY"),
        Business(name="Pro Gym Gear", email="support@progymgear.com", industry="Fitness Equipment", target_sports="Football, Basketball", budget=75000, location="Dallas, TX"),
        Business(name="Elite Supplements", email="elite@suppl.com", industry="Health & Wellness", target_sports="All Sports", budget=30000, location="Chicago, IL"),
        Business(name="GameBoost", email="info@gameboost.com", industry="Esports & Gaming", target_sports="Esports", budget=45000, location="Seattle, WA"),
        Business(name="HydraWater", email="contact@hydrawater.com", industry="Beverages", target_sports="Swimming, Track", budget=35000, location="Miami, FL"),
        Business(name="Peak Performance", email="peak@perf.com", industry="Fitness Coaching", target_sports="All Sports", budget=40000, location="Denver, CO"),
        Business(name="Urban Wear", email="sales@urbanwear.com", industry="Fashion", target_sports="Basketball, Soccer", budget=25000, location="Atlanta, GA"),
        Business(name="SpeedPro Energy", email="info@speedpro.com", industry="Energy Drinks", target_sports="Football, Racing", budget=60000, location="Las Vegas, NV"),
        Business(name="Champion Physio", email="contact@championphysio.com", industry="Physical Therapy", target_sports="Injury Recovery", budget=15000, location="Houston, TX"),
        Business(name="NextGen Tech", email="hello@nextgentech.com", industry="Wearable Tech", target_sports="All Sports", budget=80000, location="San Francisco, CA"),
        Business(name="Nutriblend", email="team@nutriblend.com", industry="Supplements", target_sports="Weightlifting, Wrestling", budget=50000, location="Phoenix, AZ"),
    ]

    # Add data to the database
    db.session.add_all(athletes + businesses)
    db.session.commit()

    print("✅ Mock data added successfully!")
