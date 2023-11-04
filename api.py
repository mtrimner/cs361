import requests

def foodSearch(food):
    payload = food
    url = f'https://trackapi.nutritionix.com/v2/search/instant?query={payload}&detailed=true'
    headers= {'x-app-id': '288d43cd', 'x-app-key': '49d1906256314a9e8c56bd3e7aea54ed', 'x-remote-user-id': '0'}
    r = requests.get(url, headers=headers).json()
    return r

