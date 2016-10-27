#databaseHelper

import sqlite3
import os
from flask import g, Flask, request, jsonify

app = Flask(__name__)

db_filename = 'database.db'
schema_filename = 'database.sql'


def connect_db():
	
	db_is_new = not os.path.exists(db_filename)
	with sqlite3.connect(db_filename) as conn:
		if db_is_new:
			print 'Creating schema'
			with open(schema_filename, 'rt') as f:
				schema = f.read()
				conn.executescript(schema)
		else:
			print 'Database exists, assume schema does, too.'	
			return 'Database exists'

def postTemprature(date, temprature):
	with sqlite3.connect(db_filename) as conn:
		cursor = conn.cursor()
		try:
			query = """INSERT INTO temprature (temprature) VALUES(?);"""
 			cursor.execute(query, [temprature])
			conn.commit()
		except:
			conn.rollback()

def getTemprature(date):
	with sqlite3.connect(db_filename) as conn:
		cursor = conn.cursor()
		query = """SELECT * FROM temprature WHERE temprature = ?"""
		try:
			cursor.execute(query, temprature)
			temprature = cursor.fetchall()
			return temprature
		except:
			return 'No temprature'


#def query_db(query, args=(), one=False):
#    cur = g.db.execute(query, args)
#    rv = [dict((cur.description[idx][0], value)
#               for idx, value in enumerate(row)) for row in cur.fetchall()]
#    return (rv[0] if rv else None) if one else rv
   

#def get_db():
#	db = getattr(g, 'db', None)
#	if db is None:
#		db = g.db = sqlite3.connect(DATABASE)
#	return db
