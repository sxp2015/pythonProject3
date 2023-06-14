# 发送异步请求
import httpx
import asyncio

from httpx_socks import AsyncProxyTransport
# 107.181.168.145	4145
# 180.183.230.16	8080
# 159.69.153.169	5566
# 199.102.105.242	4145
# 74.119.144.60	4145
transport = AsyncProxyTransport.from_url('socks5://104.200.135.46:4145')


async def main():
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.get('https://httpbin.org/get')
        print(response.text)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
