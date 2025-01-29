from flask_restx import Namespace, Resource, fields  # Corrected import
from flask import request, jsonify
from models.employee import Employee
from app import db

employee_ns = Namespace('employees', description='Employee operations')  # Corrected namespace variable

employee_model = employee_ns.model('Employee', {
    'name': fields.String(required=True, description='Employee name'),
    'email': fields.String(required=True, description='Employee email'),
    'position': fields.String(required=True, description='Employee position'),
    'salary': fields.Float(required=True, description='Employee salary')
})

# Create Employee
@employee_ns.route('/')
class EmployeeList(Resource):
    @employee_ns.expect(employee_model)
    def post(self):
        data = request.json
        new_employee = Employee(**data)
        db.session.add(new_employee)
        db.session.commit()
        return {"message": "Employee created successfully!"}, 201

    def get(self):
        employees = Employee.query.all()
        return [e.to_dict() for e in employees], 200


@employee_ns.route('/<int:id>')
class EmployeeResource(Resource):
    def get(self, id):
        employee = Employee.query.get_or_404(id)
        return employee.to_dict(), 200

    def put(self, id):
        data = request.json
        employee = Employee.query.get_or_404(id)
        for key, value in data.items():
            setattr(employee, key, value)
        db.session.commit()
        return {"message": "Employee updated successfully!"}, 200

    def delete(self, id):
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        return {"message": "Employee deleted successfully!"}, 200
