Python Quickstart on Tutum
==========================


## Contents

Files included in this example:

* `app.py` - the sample "Hello World" application code
* `requirements.txt` - our app's pip dependencies
* `Dockerfile` - [set of instructions](https://docs.docker.com/reference/builder/) to build a Docker image with our app


## Building

In order to build an image with our "Hello World" application, execute the following command in the repository folder:

	docker build -t quickstart-python .
	
This will execute the instructions found in the `Dockerfile` in sequence, and finally it will create a repository called `quickstart-python` which contains our application code and the information needed to launch it.


## Launching locally

To launch our newly created image:

	docker run -p 5000:5000 quickstart-python

If you are running Docker locally, go to [http://localhost:5000/](http://localhost:5000/) to check that your container is running. If you are using [boot2docker](http://boot2docker.io), replace `localhost` with the IP returned by the `boot2docker ip` command.

You can also test it by using `curl`:

	$ curl http://localhost:5000/
	Hello World!


## Pushing

If you want to push it to the [Docker Hub](https://hub.docker.com), first create an account and then execute:

	docker tag quickstart-python yourusername/quickstart-python
	docker push yourusername/quickstart-python

If you want to push it to [Tutum](https://www.tutum.co)'s private registry, first create an account and then do:

	docker login tutum.co
	docker tag quickstart-python tutum.co/yourusername/quickstart-python
	docker push tutum.co/yourusername/quickstart-python

Alternatively, you can also push it using the [Tutum CLI](https://github.com/tutumcloud/tutum-cli):

	tutum image push quickstart-python


## Launching in Tutum

Using the [Tutum CLI](https://github.com/tutumcloud/tutum-cli), execute the following:

	tutum service run -p 5000:5000 tutum.co/yourusername/quickstart-python

Then, to retrieve the endpoint where the container is listening to, do:

	$ tutum container ps
	NAME               UUID      STATUS     IMAGE                                   RUN COMMAND       EXIT CODE  DEPLOYED       PORTS
	quickstart-python  8bdc89a2  ▶ Running  tutum.co/user/quickstart-python:latest  python app.py                5 minutes ago  quickstart-python.f3ff91a8-user.node.tutum.io:5000->5000/tcp

Navigate to the endpoint reported, or just use `curl` to test the deployment:

	$ curl http://quickstart-python.f3ff91a8-user.node.tutum.io:5000/
	Hello World!

