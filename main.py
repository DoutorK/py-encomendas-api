import http.server
import socketserver
class PingPongHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"message": "pong"}')
        else:
            self.send_response(404)
            self.end_headers()


PORT = 8080
with socketserver.TCPServer(("",PORT), PingPongHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()               