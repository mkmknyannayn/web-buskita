#coding: utf-8

from flask import Flask, render_template, send_from_directory, request
import os
from buskita import client
import datetime
import asyncio
import time



app = Flask(__name__)

routes = {
    '工大発 工大線': {
        'route_image': '/static/images/college.png',
        'route_color': "background-color:#2874A6;color:#EAECEE;justify-content:center;",
        'incomings': [],
        'departure_busstop': 681, 
        'arrival_busstop': 391
    },
    '工大発 ろう学校線': {
        'route_image': '/static/images/bus.png',
        'route_color': "background-color:#4A235A;color:#EAECEE;justify-content:center;",
        'incomings': [],
        'departure_busstop': 661, 
        'arrival_busstop': 391
    },
    '東通り発 工大線': {
        'route_image': '/static/images/college.png',
        'route_color': "background-color:#2874A6;color:#EAECEE;justify-content:center;",
        'incomings': [],
        'departure_busstop': 391, 
        'arrival_busstop': 681
    },
    '中島三丁目発 ろう学校線': {
        'route_image': '/static/images/bus.png',
        'route_color': "background-color:#4A235A;color:#EAECEE;justify-content:center;",
        'incomings': [],
        'departure_busstop': 391, 
        'arrival_busstop': 661
    }
}


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, '/static/'), 'favicon.ico', )


@app.route("/")
@app.route("/index")
async def _index():
    st = time.time()

    for route in routes:
        routes[route]['incomings'] = await client.get_incomings(
            departure_busstop=routes[route]['departure_busstop'], 
            arrival_busstop=routes[route]['arrival_busstop']
        )

    print(time.time()-st)
    return render_template(
        'index.html',
        title="Muroran Bus Now!",
        routes=routes
    )




if __name__ == "__main__":
    app.run(debug=True)