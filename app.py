import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"
    index.exposed = True

app = cherrypy.Application(HelloWorld(), '/', config=None)

