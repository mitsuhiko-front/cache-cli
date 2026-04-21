cache = {}

def get(url: str):
    return cache.get(url)

def set(url: str, data: str):
    cache[url] = data