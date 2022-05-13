from flask import render_template
from flask.views import MethodView
import spaceModel

class Index(MethodView):
    def get(self):
        return render_template('index.html')

