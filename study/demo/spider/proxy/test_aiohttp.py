import asyncio
import aiohttp
import certifi
from aiohttp_socks import ProxyConnector

# connector = ProxyConnector.from_url('socks5://98.162.96.52:4145')
# connector = ProxyConnector.from_url('socks5://107.152.98.5:4145')
# connector = ProxyConnector.from_url('socks5://192.252.208.70:14282')
connector = ProxyConnector.from_url('socks5://142.54.239.1:4145', verify_ssl=False)


async def main():
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get('https://httpbin.org/get') as response:
            print(response.text)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
