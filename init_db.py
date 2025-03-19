from app import app, db
import models  # Ensure models are imported
from sqlalchemy import text

print("🔄 Starting database initialization...")

with app.app_context():
    print("✅ Inside Flask application context!")

    # Drop all tables first (Optional: Only if you want a full reset)
    db.drop_all()

    # Create all tables
    db.create_all()

    # Verify tables
    inspector = db.session.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    tables = [row[0] for row in inspector.fetchall()]

    print(f"📋 Tables created: {tables}")

    if not tables:
        print("❌ ERROR: No tables were created! Check model registration.")

    print("🎉 Database initialized successfully!")
