import pytest
from app import create_app, db
from app.models import Employee
from datetime import datetime

@pytest.fixture(scope='module')
def client():
    # Create a new Flask application and test client
    app = create_app('testing')
    with app.test_client() as client:
        # Set up the app context
        with app.app_context():
            # Create all tables for the testing database
            db.create_all()
        yield client
        # Clean up after the test
        with app.app_context():
            db.drop_all()

def test_create_employee(client):
    # Test creating a new employee via POST
    new_employee = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "position": "Developer",
        "salary": 50000
    }

    response = client.post('/api/employees/', json=new_employee)

    assert response.status_code == 201  # Ensure the employee was created
    assert 'id' in response.json  # Ensure the response contains the employee ID

def test_create_employee_duplicate_email(client):
    # Test creating an employee with a duplicate email
    new_employee = {
        "name": "John Doe",
        "email": "john.doe@example.com",  # Same email as above
        "position": "Developer",
        "salary": 50000
    }

    # Create the first employee
    client.post('/api/employees/', json=new_employee)

    # Try creating another employee with the same email
    response = client.post('/api/employees/', json=new_employee)

    assert response.status_code == 400  # Bad request due to duplicate email
    assert 'error' in response.json  # Error message should be present

def test_get_employees(client):
    # Test retrieving all employees via GET
    employee_1 = Employee(name="Alice", email="alice@example.com", position="Manager", salary=60000)
    employee_2 = Employee(name="Bob", email="bob@example.com", position="Designer", salary=40000)

    with client.application.app_context():
        db.session.add(employee_1)
        db.session.add(employee_2)
        db.session.commit()

    response = client.get('/api/employees/')
    assert response.status_code == 200  # Ensure the GET request is successful
    assert len(response.json) == 2  # Ensure the response contains the two employees

def test_update_employee(client):
    # Test updating an employee via PUT
    employee = Employee(name="Charlie", email="charlie@example.com", position="Developer", salary=50000)

    with client.application.app_context():
        db.session.add(employee)
        db.session.commit()

    updated_employee = {
        "name": "Charlie Updated",
        "email": "charlie@example.com",  # Email stays the same
        "position": "Senior Developer",
        "salary": 70000
    }

    response = client.put(f'/api/employees/{employee.id}', json=updated_employee)
    
    assert response.status_code == 200  # Ensure the employee was updated
    assert response.json['name'] == 'Charlie Updated'  # Ensure the name was updated
    assert response.json['position'] == 'Senior Developer'  # Ensure the position was updated
    assert response.json['salary'] == 70000  # Ensure the salary was updated

def test_delete_employee(client):
    # Test deleting an employee via DELETE
    employee = Employee(name="David", email="david@example.com", position="Intern", salary=20000)

    with client.application.app_context():
        db.session.add(employee)
        db.session.commit()

    response = client.delete(f'/api/employees/{employee.id}')
    
    assert response.status_code == 200  # Ensure the employee was deleted
    assert response.json['message'] == 'Employee deleted successfully'  # Ensure the success message

def test_get_employee_by_id(client):
    # Test retrieving a single employee by ID
    employee = Employee(name="Eve", email="eve@example.com", position="HR", salary=55000)

    with client.application.app_context():
        db.session.add(employee)
        db.session.commit()

    response = client.get(f'/api/employees/{employee.id}')
    
    assert response.status_code == 200  # Ensure the GET request is successful
    assert response.json['id'] == employee.id  # Ensure the correct employee is returned
    assert response.json['name'] == 'Eve'  # Ensure the name matches
    assert response.json['email'] == 'eve@example.com'  # Ensure the email matches
