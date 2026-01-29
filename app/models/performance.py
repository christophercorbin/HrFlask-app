from datetime import datetime
from app import db

class PerformanceReview(db.Model):
    __tablename__ = 'performance_reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    review_period_start = db.Column(db.Date, nullable=False)
    review_period_end = db.Column(db.Date, nullable=False)
    review_date = db.Column(db.Date, nullable=False)
    
    # Ratings (1-5 scale)
    overall_rating = db.Column(db.Integer)
    technical_skills = db.Column(db.Integer)
    communication = db.Column(db.Integer)
    teamwork = db.Column(db.Integer)
    leadership = db.Column(db.Integer)
    problem_solving = db.Column(db.Integer)
    
    # Comments
    strengths = db.Column(db.Text)
    areas_for_improvement = db.Column(db.Text)
    goals = db.Column(db.Text)
    comments = db.Column(db.Text)
    
    # Status
    status = db.Column(db.String(20), default='draft')  # draft, submitted, acknowledged
    acknowledged_date = db.Column(db.DateTime)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    reviewer = db.relationship('Employee', foreign_keys=[reviewer_id], backref='conducted_reviews')
    
    def __repr__(self):
        return f'<PerformanceReview {self.id}: Employee {self.employee_id}>'
