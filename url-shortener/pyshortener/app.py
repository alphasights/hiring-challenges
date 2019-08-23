from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect,
    abort
)

from models import URL
from repositories import repo


# Create the application instance
app = Flask(__name__, template_folder="templates")


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.json.get('url')

    url = URL(original_url)

    repo.create(url)

    return jsonify({'short_url': url.shrink()})


@app.route('/list')
def shortened_urls():
    urls_as_dicts = [url.to_dict() for url in repo.all()]

    return jsonify(urls_as_dicts)


# noinspection SpellCheckingInspection
@app.route('/<path:path>', methods=['GET'])
def redir(path):
    urls = repo.find(path)

    if urls:
        return redirect(urls[0].original)

    return abort(404)


@app.route('/<path:path>', methods=['DELETE'])
def delete(path):
    url = repo.find(path)[0]
    repo.delete(url)
    return ''


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
