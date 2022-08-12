import requests
from concurrent.futures import ThreadPoolExecutor
BASE = "https://discretematt.herokuapp.com"
def get_url(url):
    return requests.get(url)
with ThreadPoolExecutor(max_workers=50) as pool:
    print(list(pool.map(get_url, [BASE + "/howold?dob=1989-07-07"] * 20)))