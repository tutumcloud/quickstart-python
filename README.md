## quickstart-python

[![Deploy to Tutum](https://s.tutum.co/deploy-to-tutum.svg)](https://dashboard.tutum.co/stack/deploy/)

A simple Python app (using Flask) which can easily be deployed to Tutum.

This application support the [Getting Started with Python](https://support.tutum.co/support/solutions/folders/5000171774) on Tutum article - check it out.

### Running locally

```
$ git clone https://github.com/tutumcloud/quickstart-python.git
$ cd quickstart-python
$ docker build --tag quickstart-python .
$ docker run -d -p 80 quickstart-python
```

Alternatively, you can run the dockerized version:

```
$ docker run -d -p 80 tutum/quickstart-python
```

Your app should now be running:

```
curl 192.168.59.103:49153
Hello World!</br>Hostname: ebf2b5258db0</br>Counter: Redis Cache not found, counter disabled.
```

### Deploying to Tutum

[Install the Tutum CLI.](https://support.tutum.co/support/solutions/articles/5000049209-installing-the-command-line-interface-tool)

```
$ tutum login
$ tutum service run tutum/quickstart-python 
```

**Continue with this tutorial [here](https://support.tutum.co/support/solutions/folders/5000171774).**
