import http
import unittest
from http.server import HTTPServer
from server import SimpleHTTPRequestHandler
import http.client
import json
import threading

class TestServerGET(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_address = ('localhost', 8000)
        cls.server = HTTPServer(cls.server_address, SimpleHTTPRequestHandler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()
    

    def test_get_method(self):
        # Connect to the server and send a GET request
        connection = http.client.HTTPConnection(*self.server_address)
        connection.request('GET', '/')
        respone = connection.getresponse()

        # Read and Decode the response
        data = respone.read().decode()
        connection.close()

        #check That the resopnse as expected
        self.assertEqual(respone.status, 200)
        self.assertEqual(respone.reason, 'OK')
        self.assertEqual(respone.getheader('Content-Type'), 'application/json')

        # Parse the JSON data and verify the content
        respone_data = json.loads(data)
        self.assertEqual(respone_data, {'message': 'This is a GET request response'})
        
if __name__ == '__main__':
    unittest.main()