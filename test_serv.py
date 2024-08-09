from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "0.0.0.0"
serverPort = 9998

# Launch server commande: python -m http.server

def return_page1(given_self):
    return given_self.wfile.write(bytes("<p>Request: %s</p>" % given_self.path, "utf-8")), given_self.wfile.write(bytes("<h3> This is the first page of basic python web server</h3>", "utf-8")), given_self.wfile.write(bytes("<p> Lorem ipsus 1 and termus primus</p>", "utf-8"))

def return_page2(given_self):
    return given_self.wfile.write(bytes("<h3> This is the Second page of basic python web server</h3>", "utf-8")), given_self.wfile.write(bytes("<p> Lorem ipsus 2 arrivas secund y nihli!</p>", "utf-8"))


def return_page3(given_self):
    return given_self.wfile.write(bytes("<h3>This is the Third page of basic python web server</h3>", "utf-8")), given_self.wfile.write(bytes("<p> Lorem ipsus 3 triptic in greec</p>", "utf-8"))
    
    
class MyServer(BaseHTTPRequestHandler):
    # Sending the GET requests responses	
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Basic web server</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))        
        
        if self.path == "/glen":
            return_page1(self)
            

        elif self.path == "/filao":
            return_page2(self)  
            

        elif self.path == "/lastPage":
            return_page3(self)                        
           
        self.wfile.write(bytes("<html><head><title>Basic web server</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))            


if __name__ == "__main__":
    webServer = HTTPServer((hostName,serverPort),MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped")
