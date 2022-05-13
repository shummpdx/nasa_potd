from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from google.cloud import vision
import io
import spaceModel
import requests

class Potd(MethodView):
    def get(self):
        model = spaceModel.get_model()
        entries = [dict(title=row[0], date=row[1], url=row[2], explanation=row[3], copyright=row[4]) for row in model.select()]

        return render_template('potd.html',entries=entries)

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to potd when completed.
        """
        model = spaceModel.get_model()

        entries = [dict(title=row[0], date=row[1], url=row[2], explanation=row[3], copyright=row[4]) for row in model.select()]

        searchDate = request.form['date']
        url = f'https://api.nasa.gov/planetary/apod?api_key=jRVxIP7hbqYDRh067E11YUURM3OVtahMKz6t7UPp&date={searchDate}'
        s = requests.Session()
        resp = s.get(url)
        jsonResponse = resp.json()

        client = vision.ImageAnnotatorClient()

        image = vision.Image()
        image.source.image_uri = jsonResponse['url']

        response = client.label_detection(image=image)
        labels = response.label_annotations
        try:
            model.insert(jsonResponse['title'], request.form['date'], jsonResponse['url'], jsonResponse['explanation'], jsonResponse["copyright"])
        except:
            model.insert(jsonResponse['title'], request.form['date'], jsonResponse['url'], jsonResponse['explanation'], '')
        return render_template('potd.html',jsonResponse=jsonResponse, entries=entries, labels=labels)
