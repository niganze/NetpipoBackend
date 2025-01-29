
# Employee Management API

![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white) ![JWT](https://img.shields.io/badge/JWT-000000?style=flat&logo=json-web-tokens&logoColor=white)

## Overview

This project implements a **RESTful API** for managing employees in a company. The API allows the creation, retrieval, updating, and deletion (CRUD) of employee data. The application is built with **Flask** and uses **PostgreSQL** for database management and **JWT authentication** to secure the endpoints. The API is structured following **Object-Oriented Programming (OOP)** principles.

## Features

- **CRUD Operations**:
  - **POST /employees/**: Create a new employee.
  - **GET /employees/**: List all employees.
  - **GET /employees/{id}**: Retrieve a specific employee by ID.
  - **PUT /employees/{id}**: Update an employee's details.
  - **DELETE /employees/{id}**: Delete an employee.
- **Authentication**:
  - Secured routes using **JWT Authentication** to allow only authorized users to perform modification operations.
- **Database**:
  - Database used: **PostgreSQL**.
  - Designed the database schema with proper relationships for the employee data.
- **Error Handling**:
  - Proper error handling with meaningful HTTP status codes and error messages.

## Technologies Used

- **Backend Framework**: 
  - ![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
- **Database**: 
  - ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
- **Authentication**: 
  - ![JWT](https://img.shields.io/badge/JWT-000000?style=flat&logo=json-web-tokens&logoColor=white)
- **Programming Language**: 
  - ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
- **Database Management**: 
  - **SQLAlchemy** ORM for PostgreSQL

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/NetpipoBackend.git
cd NetpipoBackend
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL Database

- Create a PostgreSQL database:

```bash
psql -U postgres
CREATE DATABASE employee_management;
```

### 5. Configure environment variables

Create a `.env` file in the root directory and add your PostgreSQL credentials and other configurations:

```bash
DATABASE_URL=postgresql://user:password@localhost/employee_management
SECRET_KEY=yoursecretkey
```

### 6. Run database migrations

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 7. Run the application

Start the Flask application:

```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. **Create an Employee**

- **Endpoint**: `POST /api/employees/`
- **Request Body** (JSON):
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "position": "Developer",
    "salary": 50000
  }
  ```
- **Response**:
  ```json
  {
    "message": "Employee created successfully!"
  }
  ```

### 2. **List All Employees**

- **Endpoint**: `GET /api/employees/`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "position": "Developer",
      "salary": 50000
    }
  ]
  ```

### 3. **Get Employee by ID**

- **Endpoint**: `GET /api/employees/{id}`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "position": "Developer",
    "salary": 50000
  }
  ```

### 4. **Update Employee**

- **Endpoint**: `PUT /api/employees/{id}`
- **Request Body** (JSON):
  ```json
  {
    "salary": 55000
  }
  ```
- **Response**:
  ```json
  {
    "message": "Employee updated successfully!"
  }
  ```

### 5. **Delete Employee**

- **Endpoint**: `DELETE /api/employees/{id}`
- **Response**:
  ```json
  {
    "message": "Employee deleted successfully!"
  }
  ```

## Authentication

For sensitive routes like `POST`, `PUT`, and `DELETE`, a **JWT token** is required for authentication. To generate the token, use the login endpoint (if implemented) and pass the token in the `Authorization` header.

Example:
```bash
Authorization: Bearer <your-jwt-token>
```

## Project Structure

```
/NetpipoBackend
│
├── /app.py                   # Flask application entry point
├── /config.py                # Application configuration
├── /models/                  # Database models
│   └── /employee.py          # Employee model
│   └── /db.py                # Database initialization
├── /routes/                  # API routes (Blueprints)
│   └── /employee_routes.py   # Employee CRUD routes
├── /migrations/              # Database migrations
├── /requirements.txt         # Project dependencies
└── /README.md                # Project README
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

