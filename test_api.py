import unittest
from app import app


class StudentCourseAPITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "success")

    def test_course_list_endpoint(self):
        response = self.client.get("/api/courses")
        self.assertEqual(response.status_code, 200)
        courses = response.get_json()
        self.assertIsInstance(courses, list)
        self.assertGreaterEqual(len(courses), 5)

    def test_single_course_endpoint(self):
        response = self.client.get("/api/courses/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["id"], 1)

    def test_invalid_course_endpoint(self):
        response = self.client.get("/api/courses/9999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.get_json()["status"], "error")


if __name__ == "__main__":
    unittest.main()
