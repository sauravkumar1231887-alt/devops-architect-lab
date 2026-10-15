
import unittest
from app.app import health_payload


class HealthTests(unittest.TestCase):
    def test_health_status_is_healthy(self):
        result = health_payload()
        self.assertEqual(result["status"], "healthy")

    def test_service_name_is_correct(self):
        result = health_payload()
        self.assertEqual(
            result["service"],
            "building-management-platform"
        )


if __name__ == "__main__":
    unittest.main()
