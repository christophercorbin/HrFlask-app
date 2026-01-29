import pytest
from app import create_app, db
from app.models import User, Employee, Department

@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create test CLI runner"""
    return app.test_cli_runner()

@pytest.fixture
def auth_headers(client):
    """Get authentication headers for testing"""
    # Create test user
    user = User(username='testuser', email='test@example.com', role='admin')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    
    # Login
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    return {'Authorization': f'Bearer {response.get_json().get("token")}'}
