import tornado.web
import json


class BaseHandler(tornado.web.RequestHandler):

    def initialize(self, *args, **kwargs):
        super(BaseHandler, self).initialize()

    def data_received(self, chunk):
        pass

    def error_message(self, message, **body):
        self.write(json.dumps({"message": message, "info": body}))
