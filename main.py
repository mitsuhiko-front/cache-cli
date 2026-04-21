import sys
from client import fetch
from cache import get, set

url = sys.argv[1]

cached = get(url)

if cached:
    print("CACHE HIT")
    print(cached)
else:
    print("CACHE MISS")
    data = fetch(url)
    set(url, data)
    print(data)