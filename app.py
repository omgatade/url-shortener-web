from flask import Flask, request, jsonify, render_template, redirect
from hashlib import md5

app = Flask(__name__)

url_map = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    original_url = data['url']
    short_url = md5(original_url.encode()).hexdigest()[:6]
    url_map[short_url] = original_url
    return jsonify({'short_url': short_url})

@app.route('/<short_url>')
def redirect_url(short_url):
    original_url = url_map.get(short_url)
    if original_url:
        return redirect(original_url)
    return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
