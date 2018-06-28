#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:10:20 2018

@author: Sahit
"""
from flockos import chat

userId = 'u:i8xsffx8x2gixvic'

class App(object):
	def __init__(self):
		self.appId = 'dca3f797-c4a2-4d6c-aff3-db76f33f6d89'
		self.appSecret = 'a620fa90-5536-4c39-afe6-7b5b1651ed13'
		self.botUserId = 'u:Bj8aocwi78eyyjei'
		self.botToken = '917b2caf-c88b-4626-8d8f-38538e42630e'

		
userApp = App()

if 2 < 4:
    r = chat.send_message(to=userId,token=userApp.botToken,text="Hello, world")
    print r