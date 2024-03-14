from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/get-endpoint':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"message": "This is a GET request"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        if self.path == '/post-endpoint':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"message": "POST request received", "data": post_data.decode('utf-8')}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, "Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

