from http.server import BaseHTTPRequestHandler, HTTPServer
import time, json
from urllib.parse import parse_qs

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
            self.wfile.write(bytes("<html><head><title>Post of basic web server</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            # calling a method for specific 3 pages
            return_pages(self)

            self.wfile.write(bytes("<p>The link of this turorial is <a href='https://pythonbasics.org/webserver/'>This</a></p>", "utf-8"))
            self.wfile.write(bytes("<h4>Please enter your name and your age in the form.</h4>", "utf-8"))            

            # Creating A Form
            #Form with it's atributes
            self.wfile.write(bytes("<form action='/inputFor%s' method='post' id='nameAge%s' >"%(self.path,self.path), "utf-8"))

            self.wfile.write(bytes("<label>Name: </label>", "utf-8"))
            self.wfile.write(bytes("<input type='text' name='name' required />", "utf-8"))
            self.wfile.write(bytes("<label>Age: </label>", "utf-8"))
            self.wfile.write(bytes("<input type='text' name='age' required />", "utf-8"))
            self.wfile.write(bytes("<input type='submit' value='Enter' required />", "utf-8"))
            self.wfile.write(bytes("</form >", "utf-8"))

            self.wfile.write(bytes("</body></html>", "utf-8"))


    # collect post data with do_GET method
    def do_POST(self):

        if self.path in ['/inputFor/glen', '/inputFor/filao','/inputFor/lastPage']:
            
	    # Creating the page
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Post of basic web server</title></head>", "utf-8"))
            
            # Geting and parsing Data            
            content_length = int(self.headers['Content-Length'])
            print("self.hdaders ---->>>   ",self.headers)
            print("____________")
            post_data = self.rfile.read(content_length)
            print("Post Data (post_data) ----->   ", post_data)
            decoded_post_data = post_data.decode('utf-8')   
            print('dedoded_post_data --->>>   ', decoded_post_data)
            print("_____________")         
            parsed_post_data = parse_qs(decoded_post_data)
            print("parsed_post_data, --->>   ", parsed_post_data)
            print("_____________")         

            # If the data is sended as the prevews string 'name=John&age=30'
            name = parsed_post_data.get('name')[0]
            age = parsed_post_data.get('age')[0]
            
            # Returning datas from post
            self.wfile.write(bytes("<h3> Hellow Mr/Mrs %s you are %s years old and you are using a Post request with a low level python web server</h3>"%(name,age), "utf-8"))
                
            self.wfile.write(bytes("</body></html>", "utf-8"))
            

if __name__ == "__main__":
    webServer = HTTPServer((hostName,serverPort),MyServer)
    print(" Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print(" Server stopped")
