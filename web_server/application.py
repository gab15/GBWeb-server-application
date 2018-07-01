import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

from web_server.handlers import user_registration, user_login

from mongoengine import connect


class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
            tornado.web.url(
                pattern=r'/registration',
                handler=user_registration.UserRegistrationHandler,
                name='registration',
                kwargs={}
            ),
            tornado.web.url(
                pattern=r'/login',
                handler=user_login.UserLoginHandler,
                name='login',
                kwargs={}
            ),
        ]

        super(Application, self).__init__(handlers)


if __name__ == "__main__":
    connect('users', host='127.0.0.1', port=27099, alias="users")  # Temporary use of local db

    define("port", default=8080, help="Run on the given port.", type=int)

    tornado.options.parse_command_line()

    app = Application()

    http_server = tornado.httpserver.HTTPServer(app)

    http_server.listen(options.port)

    tornado.ioloop.IOLoop.instance().start()
