"""
Making network requests in a thread. Since requests is implicitly synchronous, this isn't actually
faster.
"""

from concurrent.futures import ThreadPoolExecutor
import requests

session = requests.Session()

urls = [
    'https://google.com',
    'https://www.curbed.com/',
    'https://www.nytimes.com/',
    'https://arstechnica.com',
    'https://python.com',
    'https://apple.com'
]
results = []

def download(url):
    with session as s:
        results.append((url, s.get(url).text))

if __name__ == "__main__":
    with ThreadPoolExecutor(2) as exec:
        exec.map(download, urls)

    print([(url, len(text)) for (url, text) in results])