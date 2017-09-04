from wsgiref.simple_server import make_server

from Web.MyServer import  application

httpd = make_server('', 3332, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()