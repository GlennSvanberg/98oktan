import requests

headers = {
    'authority': 'frends.st1.fi',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json',
    'x-apikey': 'c286ac79-2684-4c6b-a873-ac1307ebaff6',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'origin': 'https://www.st1.se',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.st1.se/',
    'accept-language': 'sv-SE,sv;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
}

data = '{"northWestPosition":{"latitude":75.49484595036753,"longitude":-30.69288593749999},"southEastPosition":{"latitude":42.80273595057877,"longitude":60.273910937500006},"searchQuery":"","filters":{"fuels":["sweden/vpower"],"stationTypes":["!sweden/marinestation"],"services":["!sweden/ploq"]},"countryCode":"se"}'

response = requests.post('https://frends.st1.fi/api/place-locator/v1/find-places/area', headers=headers, data=data)

print(response.text)