#coding: utf-8

from flask import Flask, render_template, request
from buskita import client
import datetime



app = Flask(__name__)


icon_numbers = [
    '/static/images/number-1.png',
    '/static/images/number-2.png',
    '/static/images/number-3.png',
    '/static/images/number-4.png',
    '/static/images/number-5.png',
]


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/'), 'favicon.ico', )


@app.route("/")
@app.route("/index")
def _index():
    routes = {
        '工大発 工大線': [],
        '工大発 ろう学校線': [],
        '東通り発 工大線': [],
        '中島三丁目発 ろう学校線': []
    }

    incomings = client.get_incomings(departure_busstop=681, arrival_busstop=391)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['工大発 工大線'] = incomings

    incomings = client.get_incomings(departure_busstop=661, arrival_busstop=391)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['工大発 ろう学校線'] = incomings

    incomings = client.get_incomings(departure_busstop=391, arrival_busstop=681)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['東通り発 工大線'] = incomings

    incomings = client.get_incomings(departure_busstop=391, arrival_busstop=661)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['中島三丁目発 ろう学校線'] = incomings


    return render_template(
        'index.html',
        routes=routes
    )



if __name__ == "__main__":
    app.run(debug=True)