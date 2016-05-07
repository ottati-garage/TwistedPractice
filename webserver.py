from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor

import cgi
import sys
from pprint import pprint


class FormPage(Resource):
    def render_GET(self, request):
        return '<html><body><form method="POST"><input name="the-field" type="text" /></form></body></html>'.encode('utf-8')

    def render_POST(self, request):
        pprint(request.__dict__)
        sys.stdout.flush()
        return ('<html><body>You submitted: %s</body></html>' % (cgi.escape(request.args[b"the-field"][0].decode('utf-8')),)).encode('utf-8')


root = Resource()
root.putChild(b"form", FormPage())
factory = Site(root)
reactor.listenTCP(8882, factory)
reactor.run()
