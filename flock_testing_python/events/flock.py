
from . import config
from flockos import chat, EventHandlerClient, TokenVerifierFilter
import jwt, json
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.core.wsgi import get_wsgi_application
from . import views


urlpatterns = [
	'/events/',
	'/admin/'
]

import cgi

form = b'''
<html>
    <head>
        <title>Hello User!</title>
    </head>
    <body>
        <form method="post">
            <label>Hello</label>
            <input type="text" name="name">
            <input type="submit" value="Go">
        </form>
    </body>
</html>
'''

def app(environ, start_response):
    if environ.get('PATH_INFO', None) == '/events/':
    	html = form

    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        html = b'Hello, ' + post['name'].value + '!'

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]

def messageReply(event):
	userApp = config.App()
	userId = str(event.userId)
	botToken = userApp.botToken
	chat.send_message(to=userId, token=botToken, text="some random text")
	return event
		

userApp = config.App()
event_handler_client = EventHandlerClient(userApp.appSecret, userApp.appId)
event_handler_client.on_chat_receive_message(messageReply)
def application(event_handler_client, get_wsgi_application):
	def inner(environ, start_response):
		try:
			return event_handler_client.handle(environ, start_response)
		except:
			return app(environ, start_response)
	return inner


