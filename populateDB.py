import requests
import json

from .private import apiKey

origin_api_url = "https://api.nasa.gov/planetary/apod?api_key=" + apiKey
dest_api_url = "http://127.0.0.1:8000/astronomypictures/"

startDate = "2022-01-01"
endDate = "2022-05-31"

def anadirImagenes():
    response_origin = requests.get(origin_api_url + "&start_date=" + startDate + "&end_date=" + endDate)
    imagenes = json.loads(response_origin.text)

    for imagen in imagenes:
        try:
            imagen.pop("copyright")
        except:
            pass
        try:
            imagen.pop("date")
        except:
            pass
        try:
            imagen.pop("media_type")
        except:
            pass
        try:
            imagen.pop("service_version")
        except:
            pass
        response_dest = requests.post(dest_api_url, data=imagen)


anadirImagenes()


