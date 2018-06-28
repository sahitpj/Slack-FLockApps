"""
WSGI config for flock_testing_python project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os, json
from events.flock import application
from flockos import chat, EventHandlerClient
from events import config

def messageReply(event):
	userApp = config.App()
	userId = str(event.userId)
	botToken = userApp.botToken
	r = chat.send_message(token=botToken, to=userId, text="some random text")
	response = json.dumps(r)
	#print response
	return response

userApp = config.App()
event_handler_client = EventHandlerClient(userApp.appSecret, userApp.appId)
event_handler_client.on_chat_receive_message(messageReply)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flock_testing_python.settings")

application = application(event_handler_client, get_wsgi_application)
