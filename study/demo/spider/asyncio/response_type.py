#!/usr/bin/python3
# coding:utf-8            
#
# Copyright (C) 2023 - 2023 Sunny， Inc. All Rights Reserved 
#
# @Time    : 2023-05-15 20:35
# @Author  : Code_By_Sunny_Sun
# @Email   : 240746804@qq.com
# @File    : response_type.py
# @IDE     : PyCharm
import asyncio
import aiohttp


async def main():
    # 定义Post请求的数据
    data = {'name': 'germ', 'age': 25}
    # 定义请求超时时间为5秒
    timeout = aiohttp.ClientTimeout(total=5)
    async with aiohttp.ClientSession(timeout=timeout) as session_temp:
        async with session_temp.post('https://www.httpbin.org/post', data=data) as response:
            # 输出响应的状态码、头部信息、文本内容、二进制内容和JSON内容等信息
            print('status:', response.status)
            print('headers:', response.headers)
            print('body:', response.text)
            print('bytes:', response.read)
            print('json:', response.json)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
