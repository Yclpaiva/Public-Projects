import json
import requests
import sys


if len(sys.argv) != 4:
    sys.exit()

response = requests.get(f"https://itunes.apple.com/search?entity={sys.argv[3]}&limit={sys.argv[2]}&term={sys.argv[1]}")
print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o['results']:
    print(result['trackName'])