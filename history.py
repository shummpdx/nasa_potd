from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import spaceModel
import requests

class History(MethodView):
    def get(self):
        model = spaceModel.get_model()
        entries = [dict(title=row[0], date=row[1], url=row[2], explanation=row[3], copyright=row[4]) for row in model.select()]

        return render_template('history.html',entries=entries)
