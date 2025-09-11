import unittest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestAPI(unittest.TestCase):
    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIn("username", response.json()[0])

if __name__ == "__main__":
    unittest.main()