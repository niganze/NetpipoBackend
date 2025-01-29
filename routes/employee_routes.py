from flask import Blueprint, request, jsonify
from flask_restplus import Api, Resource, fields
from models.employee import Employee
from app import db

employee_bp = Blueprint('employees', __name__)
api = Api(employee_bp)

# Define the Employee Model for Swagger UI
employee_model = api.model('Employee', {
    'id': fields.Integer(readOnly=True, description='The employee unique identifier'),
    'name': fields.String(required=True, description='The employee name'),
    'email': fields.String(required=True, description='The employee email'),
})

# Create Employee
@employee_bp.route('/employees/', methods=['POST'])
@api.doc(description='Create a new employee')
@api.expect(employee_model)
def create_employee():
    data = request.json
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({"message": "Employee created successfully!"}), 201

# List All Employees
@employee_bp.route('/employees/', methods=['GET'])
@api.doc(description='Get all employees')
def get_employees():
    employees = Employee.query.all()
    employees_data = [employee.to_dict() for employee in employees]
    return jsonify(employees_data), 200

# Get Employee by ID
@employee_bp.route('/employees/<int:id>', methods=['GET'])
@api.doc(description='Get an employee by ID')
@api.response(404, 'Employee not found')
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.to_dict()), 200

# Update Employee
@employee_bp.route('/employees/<int:id>', methods=['PUT'])
@api.doc(description='Update an existing employee')
@api.expect(employee_model)
@api.response(404, 'Employee not found')
def update_employee(id):
    data = request.json
    employee = Employee.query.get_or_404(id)
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify({"message": "Employee updated successfully!"}), 200

# Delete Employee
@employee_bp.route('/employees/<int:id>', methods=['DELETE'])
@api.doc(description='Delete an employee by ID')
@api.response(404, 'Employee not found')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Employee deleted successfully!"}), 200
