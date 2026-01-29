import pytest
from app.models import User
from app import db

def test_user_password_hashing():
    """Test password hashing"""
    user = User(username='testuser', email='test@example.com')
    user.set_password('password123')
    
    assert user.password_hash is not None
    assert user.check_password('password123')
    assert not user.check_password('wrongpassword')

def test_login_page(client):
    """Test login page loads"""
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_logout(client):
    """Test logout functionality"""
    # Create and login user
    user = User(username='testuser', email='test@example.com', role='admin')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    
    client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    })
    
    # Logout
    response = client.get('/auth/logout', follow_redirects=True)
    assert response.status_code == 200
