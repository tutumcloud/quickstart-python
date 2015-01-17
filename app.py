from flask import Flask
from redis import Redis
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, password=os.environ.get('REDIS_ENV_REDIS_PASS'))

app = Flask(__name__)

@app.route("/")
def hello():

	try:
		counter = redis.incr('counter')
	except:
		counter = "Redis Cache not found, counter disabled."		

	return "Hello " + os.environ.get('NAME') + '!</br>' + "Hostname: " + socket.gethostname() + '</br>' + "Counter: " + str(counter)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
