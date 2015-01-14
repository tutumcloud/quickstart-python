from flask import Flask
import redis
import os
import socket
app = Flask(__name__)

@app.route("/")
def hello():

	r = redis.StrictRedis(host=os.environ.get('REDIS_PORT_6379_TCP_ADDR'), 
						  port=os.environ.get('REDIS_PORT_6379_TCP_PORT'), 
						  db=0, password=os.environ.get('REDIS_ENV_REDIS_PASS'))
	try:
		counter = r.incr('counter')
	except:
		counter = "Redis Cache not found, counter disabled."		

	return "Hello" + os.environ.get('NAME') + '!</br>' + "Hostname: " + socket.gethostname() + '</br>' + "Counter: " + str(counter)

if __name__ == "__main__":
	app.run(host='0.0.0.0')