import urllib.request
from bs4 import BeautifulSoup
url = 'http://awallpapersimages.com/2016/07/top-60-best-hd-virat-kohli-wallpapers-new-images-free-download/'
#put your web page url above
import requests
headers={}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req=urllib.request.Request(url,headers=headers)
i=1
sam=str(i)
page=urllib.request.urlopen(req)
soup=BeautifulSoup(page,"html.parser")
for img in soup.find_all('img'):
	try:
		src=img.get('src')
		if src is not None:
			if src[:1]=="/":
				src=url+src
			response = requests.get(src)
			if response.status_code == 200:
				file=open(sam+".jpg","wb")
				file.write(response.content)
				i=i+1
				sam=str(i)
	except Exception as e:
		print(e)
