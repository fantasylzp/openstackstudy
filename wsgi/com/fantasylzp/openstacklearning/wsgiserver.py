#coding=utf-8
'''

copy code form  http://blog.yongli1992.com/2015/01/23/python-wsgi-5/


'''
from wsgiref.simple_server import make_server
import time


aaa = 1 ;
ISOTIMEFORMAT='%Y-%m-%d %X'
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="get" action="parsing_get.wsgi">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
   </body>
</html>
"""

def application(environ, start_response):


    d = parse_qs(environ['QUERY_STRING'])


    age = d.get('age', [''])[0] 
    hobbies = d.get('hobbies', []) 


    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % (age or 'Empty',
               ', '.join(hobbies or ['No Hobbies']))

    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

httpd = make_server(
    'localhost', 
    8051, 
    application 
    )


while True:
    httpd.handle_request()
    aaa = aaa +1
    print aaa ,time.strftime( ISOTIMEFORMAT, time.localtime() )
