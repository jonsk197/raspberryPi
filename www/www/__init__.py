#ServerCode

import sqlite3
import database_helper
import hashlib
import json
import uuid
import os, binascii


from flask import Flask, request, jsonify
app = Flask('www')
app = Flask(__name__.split('.')[0])


import www.views


