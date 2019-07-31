# Importing Flask and Redis
from flask import Flask
from redis import Redis

app = Flask(__name__)

# Attaching Redis
redis = Redis(host='redis', port=6379)


# Navigating to '/' in the webserver
@app.route('/')
def hello():
	# Increments the counter 'hits' in redis
    redis.incr('hits')

    # Displays some text with the counter value
    return 'Hello World! This page has been hit %s times. This is a continuous update reflection and works for all updates!' % redis.get('hits')


# Starting webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)