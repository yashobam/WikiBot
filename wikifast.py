import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def wikifast(start,end):
	driver.find_element_by_class_name('mbox-text')
	startpage=driver.get("https://en.wikipedia.org/wiki/"+start)
	print(startpage)
	if ()
	option = webdriver.ChromeOptions()
	option.add_argument('headless')
	driver = webdriver.Chrome("C:\\Users\\Yashobam\\Downloads\\chromedriver.exe",options=option)
	driver.get("https://www.sixdegreesofwikipedia.com/?source={}&target={}".format(start,end))
	button=driver.find_elements_by_tag_name("button")
	button[0].click()
	time.sleep(6)
	driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element_by_class_name('lazyload-wrapper'))
	time.sleep(3)
	x=driver.find_elements_by_xpath("//a[@href]")
	c=1
	out=[]
	for b in x:
		if ("https://en.wikipedia.org/wiki/" in b.get_attribute("href")):
			if c==1:
				st=b.get_attribute("href")
			elif c==2:
				en=b.get_attribute("href")
			elif b.get_attribute("href")!=en:
				out.append(b.get_attribute("href"))
			elif b.get_attribute("href")==en:
				out.append(b.get_attribute("href"))
				break
			c=c+1
	driver.quit()
	return out
	