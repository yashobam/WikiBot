import requests
from bs4 import BeautifulSoup
from collections import deque
class wikifinder:
	def __init__(self,start,end):
		self.start="https://en.wikipedia.org/wiki/"+start.strip().replace(" ","_")
		self.end="https://en.wikipedia.org/wiki/"+end.strip().replace(" ","_")
		self.path={}
	def shortest_path(self):
		self.path[self.start]=[self.start]
		Q=deque([self.start])
		while len(Q) != 0:
			page=Q.popleft()
			links = self.get_links(page)
			for link in links:
				if link in self.end:
					return self.path[page] + [link]
				if (link not in self.path) and (link != page):
					self.path[link] = self.path[page] + [link]
					Q.append(link)
		return None
	def get_links(self,page):
		r=requests.get(page)
		soup=BeautifulSoup(r.content,'html.parser')
		base_url=page[:page.find('/wiki/')]
		links=list({base_url+a['href'] for a in soup.select('p a[href]') if a['href'].startswith('/wiki/')})
		print("still doing something!\n")
		return links
	def page_check(self):
		languages=[]
		for page in [self.start,self.end]:
			try:
				ind=page.find('.wikipedia.org/wiki/')
				languages.append(page[(ind-2):ind])
				request.get(page)
			except:
				print('{} does not appear to be a valid wikipedia page'.format(page))
				return False
		if len(self.get_links(self.start))==0:
			print('Start page has no links')
		end_soup=BeautifulSoup(requests.get(self.end).content,'html_parser')
		if end_soup.find('table',{'class':'metadata plainlinks ambox ambox-style ambox-Orphan'}):
			print('End page has no page linking to it')
			return False
		return True
	def redirected(self):
		end_soup=BeautifulSoup(requests.get(self.end).content,'html.parser')
		title=end_soup.find('h1').text
		title=title.replace(" ","_",len(title))
		base_url=self.end[:self.end.find('/wiki/') + len('/wiki/')] 
		return set([self.end,base_url+title])
	def results(self):
		if self.path:
			result=self.path
		else:
			result="no path!"
		d="start: "+str(self.start).replace("https://en.wikipedia.org/wiki/","")+"\nend: "+str(self.end).replace("https://en.wikipedia.org/wiki/","")+"\npath: "+str(result).replace("https://en.wikipedia.org/wiki/","").replace("[","").replace("]","").replace("_"," ").replace(",","-->")
		return d
	def run(self):
		if True:
			e=self.end
			self.end=self.redirected()
			self.path=self.shortest_path()
			self.end=e
			result=self.results()
			print(result)
			return (result)