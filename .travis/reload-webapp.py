"""Script to reload the web app via the PythonAnywhere API.

"""
import os
import requests

my_domain = os.environ['PYTHONANYWHERE_DOMAIN']
username = os.environ['PYTHONANYWHERE_USERNAME']
token = os.environ['PYTHONANYWHERE_API_TOKEN']

response = requests.post(
    'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain}/reload/'.format(
        username=username, domain=my_domain
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('All OK')
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))