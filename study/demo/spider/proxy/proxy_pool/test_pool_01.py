import httpx
import httpx_socks
import asyncio
# 代理地址和端口
proxy_host = '180.183.230.16'
proxy_port = 8080

# 目标 URL
url = 'https://httpbin.org/get'


async def main():
    # 创建一个 httpx 的异步客户端，并设置 socks5 代理
    async with httpx.AsyncClient(http2=True, transport=httpx_socks.AsyncProxyTransport.from_url(
            f"socks5://{proxy_host}:{proxy_port}")) as client:
        try:
            # 发起请求
            response = await client.get(url)

            # 查看响应结果
            print(response.status_code)
            print(response.text)
        except httpx.RequestError as e:
            print(f'请求发生异常: {e}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
