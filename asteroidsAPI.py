import requests
import asyncio
import aiohttp
import json
import re

URL = "https://nasaapidimasv1.p.rapidapi.com/getClosestAsteroids"
PAYLOAD = ""
HEADERS = {
    'x-rapidapi-host': "NasaAPIdimasV1.p.rapidapi.com",
    'x-rapidapi-key': "e646847615mshdfaec820f4577f2p16f0a6jsne2e64569f3f1",
    'content-type': "application/x-www-form-urlencoded"
    }


def get_closest_asteroids_first():
    response = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)
    print(response.text)


async def get_closest_asteroids_second():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.post(URL, data=PAYLOAD) as response:
            print(response.status)
            print(await response.text())


def verify_count():
    response = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)
    result = json.loads(response.text)
    api_count = result["contextWrites"]["to"]["element_count"]
    res = len(re.findall(r"\"is_potentially_hazardous_asteroid\"", response.text))
    print("Built-in count: "+ str(api_count) + "\n" + "Additional check count: " + str(res))


def find_hazardous():
    response = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS)
    res = len(re.findall(r"\"is_potentially_hazardous_asteroid\":true", response.text))
    print("Hazardous asteroids: " + str(res))


def big_hazardous():
    pass

if __name__ == '__main__':
    get_closest_asteroids_first()
    verify_count()
    find_hazardous()