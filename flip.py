#!/usr/bin/env python

from socketserver import *
from http.server import *
import random

f = open('tables.txt', 'r')
tables = f.readlines()

class HTTPReq(SimpleHTTPRequestHandler):

    def do_GET(self):

        data = random.choice(tables)
        print(data)
        data = "<!DOCTYPE html><html lang='de'><head><meta http-equiv='Content-Type' content='text/html; charset=utf-8'/></head><body>%s</body>"%data
        index = open('index.html', 'w')
        index.write(data)
        index.close()
        SimpleHTTPRequestHandler.do_GET(self)

def run():

    server = TCPServer(('', 10001), HTTPReq)
    server.serve_forever()

if __name__ == '__main__':

    run()
