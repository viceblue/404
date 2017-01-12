

import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/viceblue/404/master/sc.py")

print response.text
print response.status_code