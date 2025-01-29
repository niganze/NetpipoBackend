from flask import Blueprint, request, jsonify
from models.employee import Employee
from app import db  # Import db from app

employee_bp = Blueprint('employees', __name__)

# Create Employee
@employee_bp.route('/employees/', methods=['POST'])
def create_employee():
    data = request.json
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee created successfully!"}), 201

# List All Employees
@employee_bp.route('/employees/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([e.__dict__ for e in employees]), 200

# Get Employee by ID
@employee_bp.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.__dict__), 200

# Update Employee
@employee_bp.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    employee = Employee.query.get_or_404(id)
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify({"message": "Employee updated successfully!"}), 200

# Delete Employee
@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully!"}), 200
