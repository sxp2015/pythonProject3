import httpx
from bs4 import BeautifulSoup

# url1 = 'https://spa16.scrape.center/'
# url2 = 'https://ssr1.scrape.center/'
url = 'https://cn.bing.com/images/trending?form=Z9LH'

filename = 'result.html'

try:
    with httpx.Client(http2=True) as client:
        response = client.get(url)
        if response.status_code == 200:
            # 解析 HTML 并格式化
            soup = BeautifulSoup(response.text, 'html.parser')
            formatted = soup.prettify()

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(formatted)
                print(f'Successfully saved result to {filename}')
        else:
            print(f'Request failed with status code {response.status_code}')

except httpx.HTTPError as error:
    print(f'Request failed with error: {error}')
