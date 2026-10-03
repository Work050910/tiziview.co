# -*- coding: utf-8 -*-
import http.server
import socketserver
import os

PORT = 1313
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
DIRECTORY = os.path.abspath(DIRECTORY)

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Prevent browser from caching old content
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), NoCacheHTTPRequestHandler) as httpd:
        print(f"Serving {DIRECTORY} on http://localhost:{PORT} and http://127.0.0.1:{PORT} (No-Cache enabled)...")
        httpd.serve_forever()
