#coding: utf-8

from flask import Flask, render_template, send_from_directory, request
import os
from buskita import client
import datetime
import asyncio



app = Flask(__name__)

routes = {
    '工大発 工大線': {
        'route_image': '/static/images/college.png',
        'route_color': "background-color:#2874A6;color:#EAECEE;justify-content:center;",
        'incomings': []
    },
    '工大発 ろう学校線': {
        'route_image': '/static/images/bus.png',
        'route_color': "background-color:#4A235A;color:#EAECEE;justify-content:center;",
        'incomings': []
    },
    '東通り発 工大線': {
        'route_image': '/static/images/college.png',
        'route_color': "background-color:#2874A6;color:#EAECEE;justify-content:center;",
        'incomings': []
    },
    '中島三丁目発 ろう学校線': {
        'route_image': '/static/images/bus.png',
        'route_color': "background-color:#4A235A;color:#EAECEE;justify-content:center;",
        'incomings': []
    }
}

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
async def _index():
    incomings = await client.get_incomings(departure_busstop=681, arrival_busstop=391)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['工大発 工大線']['incomings'] = incomings

    incomings = await client.get_incomings(departure_busstop=661, arrival_busstop=391)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['工大発 ろう学校線']['incomings'] = incomings

    incomings = await client.get_incomings(departure_busstop=391, arrival_busstop=681)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['東通り発 工大線']['incomings'] = incomings

    incomings = await client.get_incomings(departure_busstop=391, arrival_busstop=661)
    for icon_number, incoming in zip(icon_numbers, incomings):
        incoming['icon_number'] = icon_number
            
    routes['中島三丁目発 ろう学校線']['incomings'] = incomings


    return render_template(
        'index.html',
        title="Muroran Bus Now!",
        routes=routes
    )



if __name__ == "__main__":
    app.run(debug=True)