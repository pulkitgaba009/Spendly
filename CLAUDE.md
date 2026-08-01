# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with the Spendly expense-tracker repository.

## Project Overview

Spendly is a Flask web application for tracking expenses. The application includes basic routes for landing, registration, login, terms, and privacy pages, with placeholder routes for future features (logout, profile, expense management).

## Project Structure

```
expense-tracker/
├── app.py                 # Main Flask application file
├── requirements.txt       # Python dependencies
├── README.md              # Project overview (minimal)
├── .gitignore             # Git ignore rules
├── database/              # Directory for database files (currently empty)
├── static/                # Static assets (CSS, JavaScript, images)
├── templates/             # HTML templates for Flask routes
│   ├── base.html          # Base template with common layout
│   ├── landing.html       # Landing page
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── privacy.html       # Privacy policy page
│   └── terms.html         # Terms of service page
├── venv/                  # Python virtual environment (created locally)
└── .claude/               # Claude Code settings (if any)
```

## Development Setup

1. **Clone the repository** (if not already done)
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment**:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask development server:

```bash
python app.py
```

The application will be available at `http://localhost:5001`.

Alternatively, you can use Flask CLI:
```bash
flask --app app.py run --port=5001
```

## Running Tests

The project includes `pytest` and `pytest-flask` in `requirements.txt` for testing. Although no tests are currently present, you can create a `tests/` directory and add test files.

To run tests:
```bash
pytest
```

## Code Style and Guidelines

- Follow the existing code style in `app.py` and template files.
- Keep templates organized in the `templates/` directory, extending `base.html` where appropriate.
- Static assets (CSS, JavaScript, images) belong in the `static/` directory.
- For database interactions, use the `database/` directory (though not implemented yet).

## Common Commands

| Command | Description |
|---------|-------------|
| `python app.py` | Run the Flask development server |
| `pip install -r requirements.txt` | Install dependencies |
| `pytest` | Run tests (if any exist) |
| `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (Unix) | Activate virtual environment |
| `deactivate` | Deactivate virtual environment |

## Notes

- The application runs on port 5001 by default (as set in `app.py`).
- Debug mode is enabled in `app.py` for development; disable in production.
- Templates use Bootstrap (check the base.html for CDN links) – you may need to add custom CSS in `static/css/`.
- When implementing new features, follow the pattern of existing routes in `app.py` and create corresponding templates in `templates/`.

This guide should help you quickly become productive when working on the Spendly project with Claude Code.