# HR Flask Application

A comprehensive Human Resources management system built with Flask.

## Features

- Employee Management
- Department Management
- Leave/Time Off Management
- Performance Reviews
- Recruitment & Onboarding
- Authentication & Authorization

## Project Structure

```
HrFlask-app/
├── app/
│   ├── __init__.py          # Application factory
│   ├── models/              # Database models
│   ├── routes/              # API endpoints & views
│   ├── services/            # Business logic
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, images
│   └── utils/               # Helper functions
├── migrations/              # Database migrations
├── tests/                   # Test suite
├── config.py                # Configuration
├── requirements.txt         # Dependencies
└── run.py                   # Application entry point
```

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
export DATABASE_URL=postgresql://user:password@localhost/hrapp
export SECRET_KEY=your-secret-key
```

4. Initialize database:
```bash
flask db init
flask db migrate
flask db upgrade
```

5. Run the application:
```bash
flask run
```

## Testing

```bash
pytest tests/
```

## License

MIT
//test
