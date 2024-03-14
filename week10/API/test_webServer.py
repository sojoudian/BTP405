import unittest
from unittest.mock import patch
from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import urlencode
import json

class TestWebServer(unittest.TestCase):
    @patch('urllib.request.urllib')
    def test_get_endpoint(self, mock_urlopen):
        mock_response = json.dumps({"message": "This is a GET request"}).encode('utf-8')
        mock_urlopen.return_value.read.return_value = mock_response
        mock_urlopen.return_value.__enter__.return_value = mock_urlopen.return_value

        response = urlopen('http://localhost:8000/get-endpoint').read()

        self.assertEqual(json.loads(response), {"message": "This is a GET request"})

    @patch('urllib.request.urlopen')
    def test_post_endpoint(self, mock_urlopen):
        # Mock the response for the POST request
        mock_response = json.dumps({"message": "POST request received", "data": "test data"}).encode('utf-8')
        mock_urlopen.return_value.read.return_value = mock_response
        mock_urlopen.return_value.__enter__.return_value = mock_urlopen.return_value

        data = urlencode({'some': 'data'}).encode()
        response = urlopen('http://localhost:8000/post-endpoint', data=data ).read()
        self.assertEqual(json.loads(response), {"message": "POST request received", "some": "data")
if __name__ == 'main':
    unittest.main()
