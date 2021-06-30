import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        number1_1 = ''
        number1_2 = ''
        result_1 = ''
        number2_1 = ''
        number2_2 = ''
        result_2 = ''
        number3_1 = ''
        number3_2 = ''
        result_3 = ''
        self.render('index.html', number1_1 = '', number1_2 = '', result_1 = '', number2_1 = '', 
                     number2_2 = '', result_2 = '', number3_1 = '', number3_2 = '', result_3 = '')

class CalcPageHandler(tornado.web.RequestHandler):
    def post(self):
           
        number1_1 = self.get_argument('number1_1')
        number1_2 = self.get_argument('number1_2')
        #if number1_1.isdigit() and number1_2.isdigit():
        try:
            number1_1 = float(number1_1)
            number1_2 = float(number1_2)
            result_1 = str(float(number1_1 * number1_2 / 100))
        except ValueError:
            number1_1 = ''
            number1_2 = ''
            result_1 = ''
        
        number2_1 = self.get_argument('number2_1')
        number2_2 = self.get_argument('number2_2')
        #if number2_1.isdigit() and number2_2.isdigit():
        try:
            number2_1 = float(number2_1)
            number2_2 = float(number2_2)
            result_2 = str(float(number2_1 / number2_2 * 100))
        except ValueError:
            number2_1 = ''
            number2_2 = ''
            result_2 = ''
        
        number3_1 = self.get_argument('number3_1')
        number3_2 = self.get_argument('number3_2')        
        #if number3_1.isdigit() and number3_2.isdigit():
        try:
            number3_1 = float(number3_1)
            number3_2 = float(number3_2)
            result_3 = str(float((number3_2 - number3_1) / number3_1 * 100))
        except ValueError:
            number3_1 = ''
            number3_2 = ''
            result_3 = ''
        
        self.render('index.html', number1_1 = number1_1, number1_2 = number1_2, result_1 = result_1, number2_1 = number2_1, 
                     number2_2 = number2_2, result_2 = result_2, number3_1 = number3_1, number3_2 = number3_2, result_3 = result_3)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/index', CalcPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
    debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
else:
    # wrap as WSGI
    import tornado.wsgi
    app = tornado.wsgi.WSGIAdapter(app)
