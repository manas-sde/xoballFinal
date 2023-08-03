import datetime

from flask import Flask, render_template,request

app = Flask(__name__)



@app.route('/wc')
@app.route('/wc/')
def root():
    app_country = request.headers.get('X-Appengine-Country')
    app_region = request.headers.get('X-Appengine-Region')
    app_city = request.headers.get('X-Appengine-City')

    return f"This is a dummy flask service. <br> Country : {app_country} <br> City : {app_city} <br> Region : {app_region} <br> <center> <h3> <a href='/app'>Link to home page </a> </h3> </center>"


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)