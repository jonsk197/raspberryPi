from www import app
from flask import request
import sqlite3
import database_helper
import hashlib
import json
import uuid
import os, binascii
from gevent.wsgi import WSGIServer
from geventwebsocket import WebSocketServer, WebSocketApplication, Resource


@app.route('/')
def home():
   return app.send_static_file('index.html')

@app.route('/contact')
def contact():
   return app.send_static_file('contact.html')

@app.route('/today')
def today():
   return app.send_static_file('today.html')


@app.errorhandler(404)
def fallback(e):
	return app.send_static_file('index.html')
        
        
if __name__=='__main__':
	app.run()
	
