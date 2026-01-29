from datetime import datetime
from app import db

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    employee_id = db.Column(db.String(20), unique=True, nullable=False, index=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    
    # Employment details
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    position = db.Column(db.String(100))
    hire_date = db.Column(db.Date, nullable=False)
    employment_type = db.Column(db.String(20))  # full-time, part-time, contract
    salary = db.Column(db.Numeric(10, 2))
    manager_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    
    # Status
    status = db.Column(db.String(20), default='active')  # active, on_leave, terminated
    termination_date = db.Column(db.Date)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    department = db.relationship('Department', backref='employees', lazy=True)
    manager = db.relationship('Employee', remote_side=[id], backref='subordinates')
    leave_requests = db.relationship('LeaveRequest', backref='employee', lazy=True)
    performance_reviews = db.relationship('PerformanceReview', backref='employee', lazy=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self):
        return f'<Employee {self.employee_id}: {self.full_name}>'
