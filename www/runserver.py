from gevent.wsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from www import app
http_server = WSGIServer(("", 5000), app, handler_class=WebSocketHandler)
http_server.serve_forever()
app.run(debug=True)
