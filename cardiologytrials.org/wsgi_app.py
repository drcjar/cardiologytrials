#-*- coding: utf-8 -*-
import pprint

def wsgi_app(environ, start_response):
    """ Display the contents of the environ dictionary."""
    # produce some content
    output = pprint.pformat(environ)
    
    # send first header and status
    status = '200 OK'
    headers = [('Content-type', 'text/plain'),
		('Content-Length', str(len(output)))]
    start_response(status, headers)

    # wsgi apps should return and iterable, the following is acceptable 
    # too : return [output]
    yield output
# mod_wsgi need the *application* variable to serve our small app
application = wsgi_app
