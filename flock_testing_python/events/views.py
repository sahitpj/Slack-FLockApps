# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import config
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from flockos import EventHandlerClient,  chat
import json


# Create your views here.

def index(request):
	return HttpResponse('Heyy bitches')


