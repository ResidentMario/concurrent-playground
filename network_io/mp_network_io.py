"""
Making network requests with multiprocessing. This would be faster if there was lots of data, but
with small amounts of data the fixed cost of spawning the process dominates.
"""

from multiprocessing import Pool
import requests

session = None

def initialize():
    global session
    if session is None:
        session = requests.Session()

urls = [
    'https://google.com',
    'https://www.curbed.com/',
    'https://www.nytimes.com/',
    'https://arstechnica.com',
    'https://amazon.com',
    'https://apple.com'
]

def download(url):
    with session as s:
        return (url, s.get(url).text)

if __name__ == "__main__":
    with Pool(2, initializer=initialize) as exec:
        results = exec.map(download, urls)
    print([(url, len(text)) for (url, text) in results])