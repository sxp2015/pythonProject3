from urllib.robotparser import RobotFileParser

rp = RobotFileParser()

rp.set_url('https://www.baidu.com/robots.txt')

rp.read()

# can_fetch() 判断网页是否可以被抓取
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))
