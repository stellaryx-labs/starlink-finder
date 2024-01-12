import requests
from modules.indicators import *


def get_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print_error("Unable to fetch data")
        return None
