import math
import pprint
import sys
from io import BytesIO

import pygame
import requests
from PIL import Image

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
map_api_server = "http://static-maps.yandex.ru/1.x/"
search_api_server = "https://search-maps.yandex.ru/v1/"


def get_pos(geocoder_params: dict):
    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    return json_response["response"]["GeoObjectCollection"]["featureMember"] \
        [0]["GeoObject"]["Point"]["pos"].split()


def get_district(kwargs: dict):
    response = requests.get(geocoder_api_server, params=kwargs)
    json_response = response.json()
    return json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['metaDataProperty'] \
        ['GeocoderMetaData']['Address']['Components'][5]['name']


def extract_size(geocoder_params: dict):
    response = requests.get(geocoder_api_server, params=geocoder_params)
    json_response = response.json()
    json_dict = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['boundedBy'][
        'Envelope']
    a, b = map(float, json_dict['lowerCorner'].split())
    a1, b1 = map(float, json_dict['upperCorner'].split())
    return abs(a - a1), abs(b - b1)


def get_map(kwargs: dict) -> Image:
    response = requests.get(map_api_server, params=kwargs)
    stream = BytesIO(response.content)
    image = Image.open(stream).convert("RGBA")
    return image


def get_organisation(kwargs):
    response = requests.get(search_api_server, params=kwargs)
    json_response = response.json()
    """do something"""


def lonlat_distance(a: float, b: float) -> str:
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = map(float, a)
    b_lon, b_lat = map(float, b)
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    distance = math.sqrt(dx * dx + dy * dy)

    return f'Растояние между адресом и аптекой составляет {round(distance, 3)} метров'


def pil_to_surface_converter(pil_image):
    return pygame.image.fromstring(
        pil_image.tobytes(), pil_image.size, pil_image.mode).convert()
