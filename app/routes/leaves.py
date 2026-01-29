from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import LeaveRequest, LeaveBalance

bp = Blueprint('leaves', __name__, url_prefix='/leaves')

@bp.route('/')
@login_required
def list_leaves():
    """List leave requests"""
    if current_user.role in ['admin', 'hr']:
        leave_requests = LeaveRequest.query.all()
    else:
        leave_requests = LeaveRequest.query.filter_by(
            employee_id=current_user.employee.id
        ).all()
    
    return render_template('leaves/list.html', leave_requests=leave_requests)

@bp.route('/request', methods=['GET', 'POST'])
@login_required
def request_leave():
    """Submit leave request"""
    if request.method == 'POST':
        # Implementation here
        pass
    
    return render_template('leaves/request.html')

@bp.route('/<int:id>')
@login_required
def view_leave(id):
    """View leave request details"""
    leave_request = LeaveRequest.query.get_or_404(id)
    return render_template('leaves/view.html', leave_request=leave_request)

@bp.route('/<int:id>/approve', methods=['POST'])
@login_required
def approve_leave(id):
    """Approve leave request"""
    # Implementation here
    pass

@bp.route('/<int:id>/reject', methods=['POST'])
@login_required
def reject_leave(id):
    """Reject leave request"""
    # Implementation here
    pass

@bp.route('/balance')
@login_required
def leave_balance():
    """View leave balance"""
    balances = LeaveBalance.query.filter_by(
        employee_id=current_user.employee.id
    ).all()
    
    return render_template('leaves/balance.html', balances=balances)
