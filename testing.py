import unittest
import sqlite3
from login import login_user

class TestLoginFunction(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Setup the test database
        cls.conn = sqlite3.connect('test_databaseexam.db')
        cls.cursor = cls.conn.cursor()
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT,
                email TEXT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        cls.conn.commit()
    
    @classmethod
    def tearDownClass(cls):
        # Close the database connection and remove the test database
        cls.conn.close()
        import os
        os.remove('test_databaseexam.db')

    def setUp(self):
        # Clear the users table before each test
        self.cursor.execute('DELETE FROM users')
        self.conn.commit()
        # Insert a test user
        self.cursor.execute('''
            INSERT INTO users (fullname, email, username, password)
            VALUES ('Test User', 'testuser@example.com', 'testuser', 'password123')
        ''')
        self.conn.commit()

    def test_login_success(self):
        user = login_user('testuser', 'password123')
        self.assertIsNotNone(user)
        self.assertEqual(user[3], 'testuser')  # Check the username field
        self.assertEqual(user[2], 'testuser@example.com')
    
    def test_login_failure_wrong_password(self):
        user = login_user('testuser', 'wrongpassword')
        self.assertIsNone(user)
    
    def test_login_failure_nonexistent_user(self):
        user = login_user('nonexistentuser', 'password123')
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
