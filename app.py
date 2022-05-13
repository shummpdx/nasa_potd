import flask
from flask.views import MethodView
from index import Index
from potd import Potd 
from history import History

app = flask.Flask(__name__)

app.add_url_rule('/',
        view_func=Index.as_view('index'),
        methods=["GET"])

app.add_url_rule('/potd',
        view_func=Potd.as_view('potd'),
        methods=["GET", "POST"])

app.add_url_rule('/history',
        view_func=History.as_view('history'),
        methods=["GET"])

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
