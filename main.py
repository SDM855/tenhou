from http.server import HTTPServer,BaseHTTPRequestHandler
import json
import re

data = {'result':'this is a test'}
host = ('localhost', 12121)

def my_function(inputData):
    print(inputData["hai"])
    return 'success'

def selfDiscard(data):
    fixedData = data[1:]
    my_list = []
    my_list.append(fixedData)
    print(my_list)

class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        #print(data)
        if(data["tag"] == 'INIT'):
            # print(data["hai"])
            my_str = my_function(data)
        elif (re.search('T[0-9]{1,3}', data["tag"])):
            print(data["tag"])

        elif (re.search('[D][0-9]{1,3}', data["tag"])):
            #自家
            print(data["tag"])
            selfDiscard(data)


        elif (re.search('[e][0-9]{1,3}', data["tag"])):
            #下家
            print(data["tag"])
        elif (re.search('[f][0-9]{1,3}', data["tag"])):
            #对家
            print(data["tag"])
        elif (re.search('[g][0-9]{1,3}', data["tag"])):
            #上家
            print(data["tag"])



if __name__ == '__main__':
    server = HTTPServer(host, Request)
    print('Starting server, listen at: %s:%s' % host)
    server.serve_forever()