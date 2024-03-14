from webServer import SimpleHTTPRequestHandler
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


if __name__ == 'main':
    unittest.main()
