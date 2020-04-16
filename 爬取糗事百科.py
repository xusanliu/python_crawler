import requests
from bs4 import BeautifulSoup
headers={
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

for i in range(2):
	r=requests.get('http://xiaohua.zol.com.cn/lengxiaohua/{}.html'.format(i),
	headers=headers)
	html=r.text
	soup=BeautifulSoup(html,'lxml')
	jokes=soup.select('.article-summary')
	for joke in jokes:
		text=joke.select('.summary-text').text
		print(text)
