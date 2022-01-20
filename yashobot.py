import os 
import discord
from dotenv import load_dotenv
import random 
from discord.ext import commands
from dotenv import load_dotenv
import time
import wikipediaapi
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv(".env")
TOKEN=os.getenv('DISCORD_TOKEN')
#client = discord.Client()
bot = commands.Bot(command_prefix='`')

option = webdriver.FirefoxOptions()
option.headless=True
driver = webdriver.Firefox(firefox_options=option)
driver.set_window_size(1000,2000)
'''@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord\n')
'''
'''@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'Hello dumbass, welcome to the best server ever')
'''
@bot.command(name='99',help='Give a random brooklyn nine nine quote')
async def nine_nine(ctx):
	b99=['Bingpot!','Cool. Cool cool cool cool cool cool cool','no doubt no doubt no doubt no doubt.','BONEEEEEEEEE?','I\'m the human form of the 💯 emoji.','This B needs a C in her A']
	response = random.choice(b99)
	await ctx.send(response)

@bot.command(name='dice',help='Randomly generates dice rolls given the number of sides of a dice')
async def dice(ctx,sides: int):
	response = str(random.randrange(1,(sides+1)))
	await ctx.send(response)

@bot.command(name='search',help='Searches for all messages made by a user till a limit')
async def search(ctx,user,limit: int):
	file1=open("out.txt","w", encoding="utf-8")
	messages=await ctx.channel.history(limit=limit).flatten()
	for msg in messages:
		if str(msg.author).strip()==str(user).strip():
			print(str(msg.content)+"\t"+str(msg.created_at)+"\n")
			file1.write(str(msg.content)+"\t"+str(msg.created_at)+"\n")
	file1.close()
	await ctx.send("Your file is:", file=discord.File("out.txt"))
	
	os.remove("out.txt")
@bot.command(name='wikilink',help='Searches for shortest link between two wikipedia articles')
async def wikilink(ctx,*,input):
	s=time.time()
	await ctx.send("This may take some time")
	a=input.split(":")
	start=a[0]
	end=a[1]
	start=start.strip()
	end=end.strip()
	[w,pg1,pg2]=wikifast(start,end)
	embed=discord.Embed()
	if w==[]:
		pg1=wikipediaapi.Wikipedia('en').page(start)
		pg2=wikipediaapi.Wikipedia('en').page(end)
		if ((pg1.exists()==False) and (pg2.exists()==False)):
			embed.description="both pages doesn't exist\n"
		elif pg2.exists():
			embed.description="start page doesn't exist\n"
		elif pg1.exists():
			embed.description="end page doesn't exist\n"
		else:
			embed.description="Took too long-Terminated\n"
		await ctx.send(embed=embed)
	else:
		embed.description="Shortest path:\n"
		for i in range(len(w)):
			if i==0:
				url=w[i]
				embed.description += "[{}]({})\n".format(start,url)
			elif i==len(w)-1:
				url=w[i]
				embed.description += "[{}]({})\n".format(end,url)
			else:
				name=w[i].replace("https://en.wikipedia.org/wiki/","").replace("_"," ").replace("%E2%80%93","-")
				url=w[i]
				embed.description += "[{}]({})\n".format(name,url)
		e=time.time()
		embed.description += "Time taken: {} seconds".format("%.3f"%(e-s))
		await ctx.send(embed=embed)

def wikifast(start,end):
	pg1=wikipediaapi.Wikipedia('en').page(start)
	pg2=wikipediaapi.Wikipedia('en').page(end)
	if (pg1.exists() and pg2.exists()):
		driver.get("https://www.sixdegreesofwikipedia.com/?source={}&target={}".format(start,end))
		button=driver.find_elements_by_tag_name("button")
		button[0].click()
		time.sleep(2)
		try:
			driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element_by_class_name('lazyload-wrapper'))
		except:
			time.sleep(2)
			try:
				driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element_by_class_name('lazyload-wrapper'))
			except:
				time.sleep(3)
				try:
					driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element_by_class_name('lazyload-wrapper'))
				except:
					time.sleep(3)
					try:
						driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element_by_class_name('lazyload-wrapper'))
					except:
						time.sleep(3)
						try:
							driver.execute_script("arguments[0].scrollIntoView(true);",driver.find_element_by_class_name('lazyload-wrapper'))
						finally:
							return[[],p1,p2]
							
		time.sleep(0.3)
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
		return [out,pg1,pg2]
	else:
		return [[],pg1,pg2]
@bot.command(name='<>123<>',help='quits browser')
async def quit(ctx):
	driver.close()
@bot.command(name='<>456<>',help='opens browser')
async def opens(ctx):
	option = webdriver.FirefoxOptions()
	option.headless=True
	driver = webdriver.Firefox(firefox_options=option)
	driver.set_window_size(1000,2000)
'''@client.event
async def on_error(event, *args, **kwargs):
	with open('err.log', 'a') as f:
		if event == 'on_message':
			f.write(f'Unhandled message: {args[0]}\n')
		else:
			raise'''

bot.run(TOKEN)
#client.run(TOKEN)