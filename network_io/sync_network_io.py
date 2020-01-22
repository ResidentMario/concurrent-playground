"""
Making network requests synchronously. This is the basic way.
"""

import requests

session = requests.session()
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
    for url in urls:
        download(url)
    print([(url, len(text)) for (url, text) in results])