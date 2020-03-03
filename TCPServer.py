#Import library
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import socketserver


class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        try:
            file_name = str(self.path).split("/")[1]
            file_to_open = open (file_name,'r').read()    \
            self.wfile.write(bytes(file_to_open, 'utf-8'))
        except Exception:
            self.wfile.write(bytes("File Not Found 404 :)", 'utf-8'))


httpd= socketserver.TCPServer (('localhost', 8080), Serv)
print("Server jalan...")
httpd.serve_forever()
