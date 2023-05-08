from parsel import Selector

html_content = """<div class="container">
		<div class="d-lg-flex justify-content-lg-between align-items-center top-nav-links">
			<ul class="nav align-items-center justify-content-center">
				<li class="nav-item" data-bs-toggle="tooltip" data-bs-animation="false"  data-bs-original-title="Home Page">
					<a class="nav-link1" href="https://www.546464546.com/index.htm"><i class="fal fa-home-alt me-1"></i> Home</a>
				</li>
				<li class="nav-item2" data-bs-toggle="tooltip"  data-bs-placement="bottom" data-bs-original-title="Online Coding System">
					<a class="nav-link2" href="https://www.tutorialspoint.com/codingground.htm"><i class="fal fa-code me-1"></i> Coding Ground</a>
				</li>
				<li class="nav-item3" data-bs-toggle="tooltip" data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Job Openings">
					<span><a class="nav-link3" href="https://www.tutorialspoint.com/about/about_careers.htm"><i class="fal fa-suitcase me-1"></i> Jobs</a></span>
				</li>
				<li class="nav-item4"  data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Tutorials Library">
					<span><a class="nav-link4" href="https://www.baidu.com"><i class="fal fa-books me-1"></i> Library</a></span>
				</li>
				<li class="nav-item"  data-bs-original-title="test">
					<span><a class="nav-link5" href="https://www.qq.com">访问</a></span>
				</li>
			</ul>
			<!-- Navbar top Right-->
			<div class="d-flex align-items-center justify-content-center">
				<div class="navbar-nav ms-2">
				  <div class="modeswitch-wrap" id="darkModeSwitch">
					 <div class="modeswitch-item">
						<div class="modeswitch-icon">
							<i class="fal fa-sun toggle-sun"></i>
							<i class="fal fa-moon toggle-moon"></i>
						</div>
					 </div>
				  </div>
				</div>
				<div class="me-3c top-nav-social">
				  <a class="nav-link" href="https://www.123123123.com/market/teach_with_us.jsp" target="_self" data-bs-toggle="tooltip" data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Teach with us"><i class="fal fa-users-class me-2"></i> <span>Teach with us</span></a>
				</div>
				<ul class="list-unstyled mb-0 top-nav-social">
					<li><a class="px-2 nav-link" rel="nofollow"  href="https://www.facebook.com/tutorialspointindia" data-bs-toggle="tooltip" data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Tutorialspoint Facebook"><i class="fab fa-facebook"></i></a> </li>
					<li><a class="px-2 nav-link" rel="nofollow" href="https://www.instagram.com/tutorialspoint_/"  data-bs-toggle="tooltip" data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Tutorialspoint Instagram"><i class="fab fa-instagram"></i></a> </li>
					<li><a class="px-2 nav-link active" rel="nofollow"  href="https://twitter.com/tutorialspoint" target="_blank" data-bs-toggle="tooltip" data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Tutorialspoint Twitter"><i class="fab fa-twitter"></i></a> </li>
					<li><a class="px-2 nav-link" rel="nofollow" href="https://www.youtube.com/channel/UCVLbzhxVTiTLiVKeGV7WEBg" target="_blank" data-bs-toggle="tooltip" data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Tutorialspoint Youtube"><i class="fab fa-youtube"></i></a> </li>
					<li><a class="px-2 nav-link" rel="nofollow"  href="https://www.linkedin.com/authwall?trk=bf&amp;trkInfo=AQEkqX2eckF__gAAAX-wMwEYvrsjBVbEtWQd4pgEdVSzkL22Nik1KEpY_ECWLKDGc41z8IOZWr2Bb0fvJplT60NPBtSw87J6QCpc7wD4qQ3iU13n6xJtBxME5o05Wmpg5JPm5YY=&amp;originalReferer=&amp;sessionRedirect=https%3A%2F%2Fwww.linkedin.com%2Fcompany%2Ftutorialspoint"  data-bs-toggle="tooltip" data-bs-animation="false" data-bs-placement="bottom" data-bs-original-title="Tutorialspoint LinkedIn"><i class="fab fa-linkedin-in"></i></a> </li>
				</ul>
			</div>
		</div>
	</div>"""

selector = Selector(text=html_content)

items1 = selector.css('.nav-item')
# contains()是XPath的一个函数，用于检查一个字符串是否包含另一个字符串，是模糊匹配模式
items2 = selector.xpath('//li[contains(@class, "nav-item" )]')
items3 = selector.xpath('//a[contains(@class, "nav-link" )]')
# 提取单个文本
items4 = selector.xpath('//a[contains(@class, "nav-link" )]').get()
# 提取所有文本
items5 = selector.xpath('//a[contains(@class, "nav-link" )]').getall()
# 提取属性
items6 = selector.css('.nav-item a::attr(href)').getall()
# xpath多条件组合，提取属性
items7 = selector.xpath('//a[contains(@class, "active") and contains(@rel, "nofollow") ]').get()

# 正则提取
items8 = selector.css('.nav-link').re('target?.*')

# 遍历取值
for item in items1:
    text = item.xpath('.//a/text()').get()
    print('item text ==', text)

print('len1 ==', len(items1), '\ntype 1==', type(items1), '\nvalue ==', items1)
print('len2 ==', len(items2), '\ntype2 ==', type(items2), '\nvalue 2==', items2)

print('获取单个==', items4)
print('获取所有==', items5)

print('提取属性==', items6)
print('多条件 xpath提取属性 ==', items7)
print('正则提取 提取属性 ==', len(items8), items8)

