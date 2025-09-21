import unittest
from src.api_client import get_location
from unittest.mock import patch


class ApiClientTest(unittest.TestCase):
    @patch("src.api_client.requests.get")
    def test_get_location_returns_expeted(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "United States",
            "regionName": "America",
            "cityName": "California",
        }

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "United States")
        self.assertEqual(result.get("region"), "America")
        self.assertEqual(result.get("city"), "California")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
