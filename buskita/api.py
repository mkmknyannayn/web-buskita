import requests
import json



class BuskitaApi:

    def __init__(self):
        self.HOST_URL = "https://api.buskita.com"
        self.Headers = {
            "content-type"      : "application/json",
            "Accept"            : "application/json, text/plain, */*",
            "user-agent"        : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "Origin"            : "https://db.buskita.com",
            "Referer"           : "https://db.buskita.com",
            "sec-ch-ua-mobile"  : "?0",
            "sec-ch-ua-platform": "Windows"
        }
        self.token =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJtZWRpYW1hZ2ljLmNvLmx0ZCIsInN1YiI6IkF1dGhvcml6ZWRUb2tlbiIsImV4cCI6IjE2NTgwODIxMTEiLCJuYmYiOiIxNjU1NDkwMTExIiwidXNlcklkIjoxMDM0ODUsInNpdGVJZCI6OH0.OzU3T8LMWNlTvGpyarp0gFEglSdLonY5PbixqskGDC6qsN7LejrumPrf5Nvv-cNMBBwzxx3X5K_CDNUnAYeL3yJ_XA9HpO1JJ-Q4IJ_FzFgnLBBIl7GF_HB38_Tp9kt0i0Btu97qrM21DDKzjeWTmmnCOSnCR4idX0U0ePHZG3Q"


        """ BUSSTOPS """
        # self.busstops = {
        #     busstop["id"]: busstop
        #     for busstop in self.get_busstops()["busstops"]
        # }



    def find_busstops(self, name):
        pass

    def get_busstops(self):
        _payload = {
            "language": 1,
            "siteId"  : 8,
            "version" : 1
        }

        r = requests.post(
            self.HOST_URL + '/get-busstops',
            json=_payload,
            headers=self.Headers
        )
        
        return r.json()

    def get_timetable(self, departure_busstop: str, arrival_busstop: str):
        _payload = {
                "company"         : "don",
                "departureBusstop": departure_busstop,
                "arrivalBusstop"  : arrival_busstop,
                "language"        : 1,
                "siteId"          : 8
        }

        r = requests.post(
            self.HOST_URL + '/get-timetable',
            json=_payload,
            headers=self.Headers
        )

        return r.json()


    def search_routes(
        self, 
        target_time: str="2022/06/17 11:33", 
        arrival_busstop: int=731, 
        departure_busstop: int=391
    ):
        departure_busstop
        _payload = {
            "arrivalBusstop"  : arrival_busstop,
            "arrivalCompany"  : "don",
            "arrivalOption"   : [],
            "departureBusstop": departure_busstop,
            "departureCompany": "don",
            "departureOption" : [],
            "kind"            : 1,
            "language"        : 1,
            "siteId"          : 8,
            "targetTime"      : target_time,
            "transfer"        : False,
        }

        r = requests.post(
            self.HOST_URL + '/search-routes',
            json=_payload,
            headers=self.Headers
        )

        return r.json()

    def get_mybuses(self, target_time: str="2022/06/17 11:33"):
        _payload = {
                "jwt"       : self.token,
                "userId"    : 103485,
                "siteId"    : 8,
                "targetTime": target_time
        }

        r = requests.post(
            self.HOST_URL + '/get-mybuses',
            json=_payload,
            headers=self.Headers
        )

        return r.json()