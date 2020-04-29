import requests

link="http://www.fishc.com/ooxx.html"

#
# try:
#     r = requests.get(link,timeout=10)
#     print(r.status_code)
# except (requests.exceptions.HTTPError,requests.exceptions.ConnectionError) as e:
#     print(e)

r = requests.get(link,timeout=10)
print(r.status_code)
r.raise_for_status()
