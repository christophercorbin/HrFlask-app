from datetime import datetime
from app import db

class LeaveRequest(db.Model):
    __tablename__ = 'leave_requests'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    leave_type = db.Column(db.String(50), nullable=False)  # vacation, sick, personal, etc.
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    days_requested = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected, cancelled
    
    # Approval details
    approver_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    approval_date = db.Column(db.DateTime)
    approval_notes = db.Column(db.Text)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    approver = db.relationship('Employee', foreign_keys=[approver_id], backref='approved_leaves')
    
    def __repr__(self):
        return f'<LeaveRequest {self.id}: {self.employee_id} ({self.status})>'

class LeaveBalance(db.Model):
    __tablename__ = 'leave_balances'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    leave_type = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    total_days = db.Column(db.Integer, nullable=False)
    used_days = db.Column(db.Integer, default=0)
    remaining_days = db.Column(db.Integer)
    
    employee = db.relationship('Employee', backref='leave_balances', lazy=True)
    
    def __repr__(self):
        return f'<LeaveBalance {self.employee_id}: {self.leave_type} ({self.year})>'
