from flask import Flask, render_template
from database.db import get_db, init_db, seed_db

app = Flask(__name__)

# Initialize database on startup
with app.app_context():
    init_db()
    seed_db()

# Existing routes (unchanged)
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)