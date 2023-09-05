print('Start api uitlees applicatie')

import requests

paginaresults = request.get('https://catfact.ninja/facts')
print(paginaresults)

feitjes = paginaresults.json()
print(feitjes["data"][0]])