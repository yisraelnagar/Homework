from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        output_file = open('html_file', 'r')
        self.wfile.write(output_file.read().encode())


def run_server():
    server = HTTPServer(('localhost', PORT), HelloWorldHandler)
    print('Server Running On Port ' + str(PORT))
    server.serve_forever()


if __name__ == '__main__':
    run_server()
