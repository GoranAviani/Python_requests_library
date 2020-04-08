import requests

#Simple get request
response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
