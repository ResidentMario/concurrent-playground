"""
Making network requests asynchronously. This should be the fastest option.
"""

import aiohttp
import asyncio

urls = [
    'https://google.com',
    'https://www.curbed.com/',
    'https://www.nytimes.com/',
    'https://arstechnica.com',
    'https://amazon.com',
    'https://apple.com'
]
results = []
session = aiohttp.ClientSession()

async def download(url):
    response = await session.get(url)
    result = await response.text()
    results.append((url, result))

# The main method is necessary here because the session can only be closed asynchronously,
# which means it has to be inside of an async function, e.g. we could not place it in the
# __main__ directly.
async def main():
    await asyncio.gather(*[download(url) for url in urls])
    await session.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print([(url, len(text)) for (url, text) in results])