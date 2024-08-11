from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 9998

# Launch server commande: python -m http.server

def return_pages(given_self):
    if given_self.path == '/glen':
        return given_self.wfile.write(bytes("<h3> This is the first page of basic python web server</h3>", "utf-8")), given_self.wfile.write(bytes("<p> Lorem ipsus 1 and termus primus</p>", "utf-8"))
        
    elif given_self.path == '/filao':
        return given_self.wfile.write(bytes("<h3> This is the Second page of basic python web server</h3>", "utf-8")), given_self.wfile.write(bytes("<p> Lorem ipsus 2 arrivas secund y nihli!</p>", "utf-8"))
   
    elif given_self.path == '/lastPage':
        return given_self.wfile.write(bytes("<h3>This is the Third page of basic python web server</h3>", "utf-8")), given_self.wfile.write(bytes("<p> Lorem ipsus 3 triptic in greec</p>", "utf-8"))

    
class MyServer(BaseHTTPRequestHandler):

    # Sending the GET requests responses
    def do_GET(self):

        if self.path in ['/glen', '/filao','/lastPage']:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Basic web server</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            # calling a method for specific 3 pages
            return_pages(self)

            self.wfile.write(bytes("<p>The link of this turorial is <a href='https://pythonbasics.org/webserver/'>This</a></p>", "utf-8"))
            self.wfile.write(bytes("<html><head><title>Basic web server</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName,serverPort),MyServer)
    print(" Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print(" Server stopped")
