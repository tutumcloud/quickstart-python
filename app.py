from flask import Flask
from redis import Redis, ConnectionError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, password=os.environ.get('REDIS_ENV_REDIS_PASS'))

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        visits = redis.incr('counter')
    except ConnectionError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv('NAME', "world"), hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
