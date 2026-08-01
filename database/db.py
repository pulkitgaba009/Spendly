import sqlite3
from werkzeug.security import generate_password_hash
import os
from datetime import datetime, timedelta

def get_db():
    """Returns a SQLite connection with row_factory and foreign keys enabled."""
    # Use expense_tracker.db in project root
    db_path = os.path.join(os.path.dirname(__file__), '..', 'expense_tracker.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Enable dictionary-like access
    conn.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
    return conn

def init_db():
    """Creates tables using CREATE TABLE IF NOT EXISTS."""
    conn = get_db()
    try:
        # Create users table
        conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")

        # Create expenses table
        conn.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, amount REAL NOT NULL, category TEXT NOT NULL, date TEXT NOT NULL, description TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (user_id) REFERENCES users (id))")
        conn.commit()
    finally:
        conn.close()

def seed_db():
    """Inserts demo user and sample expenses if no users exist."""
    conn = get_db()
    try:
        # Check if users already exist
        cursor = conn.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] > 0:
            return  # Already seeded

        # Create demo user
        password_hash = generate_password_hash('demo123')
        cursor = conn.execute(
            '''INSERT INTO users (name, email, password_hash)
               VALUES (?, ?, ?)''',
            ('Demo User', 'demo@spendly.com', password_hash)
        )
        user_id = cursor.lastrowid

        # Sample expenses data (8 expenses across required categories)
        today = datetime.now()
        expenses_data = [
            # Food
            (user_id, 15.50, 'Food', (today - timedelta(days=2)).strftime('%Y-%m-%d'), 'Lunch at cafe'),
            (user_id, 32.00, 'Food', (today - timedelta(days=5)).strftime('%Y-%m-%d'), 'Groceries'),

            # Transport
            (user_id, 5.00, 'Transport', (today - timedelta(days=3)).strftime('%Y-%m-%d'), 'Bus fare'),

            # Bills
            (user_id, 75.00, 'Bills', (today - timedelta(days=1)).strftime('%Y-%m-%d'), 'Electricity bill'),

            # Health
            (user_id, 20.00, 'Health', (today - timedelta(days=4)).strftime('%Y-%m-%d'), 'Pharmacy'),

            # Entertainment
            (user_id, 12.00, 'Entertainment', (today - timedelta(days=6)).strftime('%Y-%m-%d'), 'Movie ticket'),

            # Shopping
            (user_id, 25.99, 'Shopping', (today - timedelta(days=0)).strftime('%Y-%m-%d'), 'New shirt'),

            # Other
            (user_id, 10.00, 'Other', (today - timedelta(days=8)).strftime('%Y-%m-%d'), 'Gift for friend')
        ]

        # Insert expenses
        conn.executemany(
            '''INSERT INTO expenses (user_id, amount, category, date, description)
               VALUES (?, ?, ?, ?, ?)''',
            expenses_data
        )

        conn.commit()
    finally:
        conn.close()