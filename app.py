import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

class SPAServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Resolve requested file path
        requested_path = self.translate_path(self.path)
        # If file doesn't exist, route to index.html for Single-Page Application
        if not os.path.exists(requested_path) or os.path.isdir(requested_path) and not os.path.exists(os.path.join(requested_path, 'index.html')):
            self.path = "/index.html"
        return super().do_GET()

if __name__ == "__main__":
    # Allow port reuse immediately
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), SPAServer) as httpd:
        print(f"ALO Doctor Cockpit running on http://0.0.0.0:{PORT}")
        httpd.serve_forever()
