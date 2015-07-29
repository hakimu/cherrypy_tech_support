# This is a CherryPy app being serverved by uWSGI and Gunicorn.

Here is the application object:

```
app = cherrypy.Application(HelloWorld(), '/', config=None)
```

The command I use to run the application with the agent server by gunicorn is:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn app:app
```

To run the app with uWSGI and the Python agent, I can run the following command:

```
NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program uwsgi --http :8080 -w app:app --single-interpreter --enable-threads
```
