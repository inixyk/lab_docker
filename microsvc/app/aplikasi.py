from flask import Flask, Response, request
import requests
import hashlib
import redis
import html
app = Flask(__name__)
cache = redis.StrictRedis(host='redis', port=6379, db=0)
default_name = 'admin'

@app.route('/', methods=['GET', 'POST'])
def utama():
    name = default_name
    if request.method == 'POST':
        name = html.escape(request.form['nama'], quote=True) 

    header = '<html><head><title>Aplikasi</title></head><body>'
    body = '''<form method="POST">
                  Hallo <input type="text" name="nama" value="{0}">
              <input type="submit" value="submit">
              </form>
              <p>Avatar kamu:
              <img src="/monster/{1}"/>
              '''.format(name, name)
    footer = '</body></html>'
    return header + body + footer

@app.route('/monster/<name>')
def avatar(name):
    name = html.escape(name, quote=True) 
    image = cache.get(name)
    if image is None:
        print ("Cache miss", flush=True)
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
        image = r.content
        cache.set(name, image)
    return Response(image, mimetype='image/png')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')