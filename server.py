import flask

app = flask.Flask(__name__)

MANIFEST_LOCATION = '/my_app_name.webmanifest'
ICON_NAME = 'app.png'
ICON_LOCATION = '/' + ICON_NAME

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World! PWA</title>
        <link rel="manifest" href=""" + MANIFEST_LOCATION + """>
        <script>
            if ('serviceWorker' in navigator) {
                navigator.serviceWorker.register('/sw.js');
            }
        </script>
    </head>
    <body>
        <h1>Hello World!</h1>
    </body>
    </html>
"""

@app.route('/apple-touch-icon.png') 
def apple_touch_icon():
  return flask.send_file(ICON_NAME)

@app.route(ICON_LOCATION)
def icon():
    return flask.send_file(ICON_NAME)

@app.get(MANIFEST_LOCATION)
def manifest():
    return {
        "name": "my_app_name for user ",
        "short_name": "shot app name",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#000",
        "theme_color": "#000",
        "icons": [
            {
                #"src": "http://localhost:5000" + ICON_LOCATION,
                "src": ICON_LOCATION,
                "sizes": "512x512",
                "type": "image/png"
            }
        ]
    }

@app.get("/sw.js")
def sw():
    return """
    self.addEventListener('install', function(event) {});
    self.addEventListener('fetch', function(event) {});
    self.addEventListener('activate', function(event) {});
    """

if __name__ == '__main__':
    # run on http://localhost:5000
    #app.run() 

    # run on http://<your_ip>:5000
    app.run(host='0.0.0.0', port=5000, debug=True) 
    
    # run on https://<your_ip>:5000
    # for local dev : genrate with this command :
    #   openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
    # for prod use : certbot https://certbot.eff.org/ for example

    #ssl_context = ('server.crt', 'server.key') 
    #app.run(ssl_context=ssl_context, host='0.0.0.0', port=5000, debug=True) 
