from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        output_file = open('html_file', 'r')
        self.wfile.write(output_file.read().encode())

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), HelloHandler)
    print('Server Running On Port')
    server.serve_forever()


if __name__ == '__main__':
    main()
