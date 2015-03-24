## Stream Twitter clone

This is a simple twitter clone app built with [Stream](http://getstream.io)'s API. It shows you how you can use [GetStream.io](https://getstream.io/ "GetStream.io") to built a site similar to Twitter.

### Tutorial

This application is based on the [Build a scalable Twitter clone with Django and GetStream.io](https://gist.github.com/tbarbugli/97bf26f400ecf1443ef6) tutorial.

### Live Demo

You can see a live demo of this application [here](http://tw.getstream.io/).

### Heroku

The best way to try this application is via Heroku; you can deploy this example (for free) on Heroku
by pressing the Deploy button below.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

If you prefer to run this locally then make sure to signup for GetStream's service and follow this steps:


**Install the requirements**

```
pip install -r requirements.txt
```

**Add your API keys to settings.py**

```python
STREAM_API_KEY = 'my_api_key'
STREAM_API_SECRET = 'my_api_secret'
```

**Setup your database and the demo data:**

```
python manage.py after_deploy
```
