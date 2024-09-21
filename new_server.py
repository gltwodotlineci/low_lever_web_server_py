from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
localhost="0.0.0.0"


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

httpd = HTTPServer((localhost, 4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="./key.pem", 
        certfile='./cert.pem', server_side=True)

httpd.serve_forever()
