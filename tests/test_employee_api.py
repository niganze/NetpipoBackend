import unittest
from app import app

class TestEmployeeAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_employee(self):
        response = self.app.post('/employees/', json={
            "name": "John Doe",
            "email": "john@example.com",
            "position": "Developer",
            "salary": 5000
        })
        self.assertEqual(response.status_code, 201)

if __name__ == "__main__":
    unittest.main()
