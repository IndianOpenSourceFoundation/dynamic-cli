from pprint import pprint
import requests
from termcolor import colored
import re




class reddit:

	def getjson(self,question):
		headers = {'User-Agent': 'user1'}
		api_url = 'https://www.reddit.com/subreddits/search.json?q={}&sort=relavance&limit=5'.format(question,)
		response = requests.get(api_url, headers=headers)
		if (response.status_code==200):
			value=response.json()
			return value
		else:
			print(colored("nothing found on reddit","red"))


	def getdata(self,value1):
		value=value1
		print(
                colored("------------------------------------------------------------------------------------------------", 'red'))
		for i in range(len(value["data"]["children"])):
			print("Title: ", re.sub(' +', ' ',value["data"]["children"][i]["data"]["title"]))
			#print("\nPublic Description: ", value["data"]["children"][i]["data"]["public_description"])
			print("\nDescription: ", re.sub(' +', ' ',value["data"]["children"][i]["data"]["description"]))
			print("\nURL: ",re.sub(' +', ' ',"www.reddit.com"+value["data"]["children"][i]["data"]["url"]))
			print(
                colored("------------------------------------------------------------------------------------------------", 'red'))
