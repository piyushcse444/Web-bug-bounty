from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(f"[+] Hit from {self.client_address}")  # 👈 IMPORTANT

        self.send_response(200)
        self.send_header("Content-type", "application/javascript")
        self.end_headers()

        self.wfile.write(b"console.log('XSS triggered');")

if __name__ == "__main__":
    server = HTTPServer(("192.168.166.246", 8000), MyHandler)
    print("Server running on port 8000...")
    server.serve_forever()

