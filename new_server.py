from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl, os.path
server_address="0.0.0.0"
ssl_on = True
port = 8087
routes = [
     {'name': '/accueil', 'methode': None},
     {'name': '/contact', 'methode': None},
     {'name': '/article', 'methode': None}
     ]
public = os.getcwd() + '/www'#/.well-know/acme-challenge'

if ssl_on == True:
    port = 9998

def find_routes(given_path):
    rout_finded = None
    # print(f"path = {given_path}")
    for item in routes:
        if item['name'] == given_path:
            rout_finded = item
            break  
    # print(f"rout_finded = {rout_finded}")
    return rout_finded


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        result = find_routes(self.path)
        print("result = ", result)
        # It will serve files
        if result == None:
            # Check if the file exist in the public directory
            file_exist =  os.path.isfile(public + self.path)
            print("file exist", file_exist)
            print("path = ", public +self.path)

            print("Self path  = ", self.path)
            
            if file_exist:
                print("coucou je suis dans file exist:")
                print("Self path  = ", self.path)    
                # Detecte its extention
                # text/html
                # read file
                f = open(public + self.path, "r")
                
                content = f.read()
                # send file
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes(content, "utf-8"))

            else:
                # send 404    
                pass

        # if not ssl_on:
        #     self.send_header("Content-type", "text/html")
        #     self.end_headers()
        #     self.send_response(200)
            
        #     self.wfile.write(b'4on9Hox0a9yL5v26ElLnJOBHwXIdFejQDi4LUMMIoX0.wZYHjiTR-Y9Y_uqTexuDlunn9HVMRLBD-Fs6YkdKUXM')

        #     print(f"url = {self.path}")
        # else:
        #     self.send_response(200)
        #     self.end_headers()
        #     self.wfile.write(b'Hello, world!')



print(f"Port = {port}")
if __name__ == "__main__":
    httpd = HTTPServer((server_address, port), SimpleHTTPRequestHandler)
    if ssl_on:
      httpd.socket = ssl.wrap_socket (httpd.socket,keyfile="./keys_pem/privkey.pem", 
        certfile='./keys_pem/cert.pem', server_side=True)

    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      pass

    httpd.server_close()
