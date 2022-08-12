import requests
from concurrent.futures import ThreadPoolExecutor
BASE = "http://127.0.0.1:5000"
def get_url(url):
    return requests.get(url)
with ThreadPoolExecutor(max_workers=50) as pool:
    print(list(pool.map(get_url, [BASE + "/howold?dob=1989-07-07"] * 20)))