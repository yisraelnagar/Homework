from http.server import HTTPServer, BaseHTTPRequestHandler


class HelloHandler(BaseHTTPRequestHandler):
    def do_Get(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello World!'.encode())


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), HelloHandler)
    print('Server Running On Port')
    server.serve_forever()


if __name__ == '__main__':
    main()
