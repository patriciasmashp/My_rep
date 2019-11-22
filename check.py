import requests 
from bs4 import BeautifulSoup as bs 
import datetime
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_ym_uid=156587604930542632; _ym_d=1565876049; a05e2afef66f287301157ede30e3e523=8befirnn4jlmd1j30p4ahv0m99; _ym_isad=1',
'Host': 'ntgmk.ru',
'Referer': 'https://www.google.com/',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}




def find_repl_753(b):
	date = []
	d = None
	f = ''
	for i in b:
		if i is not None:
			d = i.findAll('td',attrs={'colspan':'7','height':'18','bgcolor':"#f6f6f6",'class':"tbl_c"})
			if len(d)>0:
				date.append(d)
	for tag in b: #b- all_soup
		a=(tag.find('td',attrs={'height':"12",'class':"tbl_c"}))
		if tag.text[6:8] == date[1][0].text[6:8]:	
			break

		if a is not None :
			if a.text[-2] == '3' and a.text[-3] == '5' and a.text[-4] == '7':
				f+=a.parent.text.replace('\n', '')+'\n'
	return f
def decor(func):
	def wrapper():
		print('Замены на {0}:'.format(date[0][0].text[6:8]))
		resoult= func()
		return resoult
	return wrapper




def resoult():
	b_url = 'http://ntgmk.ru/program/view_zamen.php'
	session = requests.Session()
	request = session.get(b_url, headers=headers)
	if request.status_code == 200:
		soup = bs(request.content, 'lxml')
		body_tag = soup.table	
		all_soup = body_tag.findAll()	
		a = find_repl_753(all_soup)
		return a
		

def check_rep(ba):
	global request
	Pnew_soup = bs(request.content, 'lxml')
	if ba.table == Pnew_soup.table:
		print('g')
		return False
	else:
		print(ba)
		return True



	
print(resoult())
