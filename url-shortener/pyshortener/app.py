from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect
)

from models import URI
from repositories import repo

URLS = {}

# Create the application instance
app = Flask(__name__, template_folder="templates")


# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.json.get('url')

    uri = URI(original_url)

    repo.create(uri)

    return jsonify({'short_url': uri.shrink()})


@app.route('/<path:path>')
def redir(path):
    uri = repo.find(path)

    return redirect(uri.url)


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)
