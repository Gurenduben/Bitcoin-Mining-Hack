import http.server
import socketserver

PORT = 8000  # You can change this port
DIRECTORY = "."  # Serve files from the current directory

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # To stop the server gracefully, press Ctrl+C
    httpd.serve_forever()