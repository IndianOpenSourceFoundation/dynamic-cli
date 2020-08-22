#!/usr/bin/env python
import argparse
import requests

PARSER = argparse.ArgumentParser()
PARSER.add_argument("-s", "--search", help="enable debug mode",action="store_true")

ARGV = PARSER.parse_args()

def make_request(que, tag):
	
	"""
	This function uses the requests library to make the rest api call to the stackexchange server.

	:param que: The user questions that servers as a question in the api.
	:type que: String 
	:param tag: The tags that user wants for searching the relevant answers. For e.g. TypeError might be for multiple languages so is tag is used as "Python" then the api will return answers based on the tags and question.
	:type tag: String
	:return: Json response from the api call.
	:rtype: Json format data
	"""

	print("Searching for the answer")
	resp = requests.get("https://api.stackexchange.com/"+"/2.2/search/advanced?order=desc&sort=relevance&tagged={}&title={}&site=stackoverflow".format(tag,que))
	return resp.json()

def get_que(json_data):
	que_id = []
	for i in json_data['items']:
		if i["is_answered"]:
			que_id.append(i["question_id"])
	return que_id
	
def get_ans(questions_list):
	ans = [] 
	for i in range(1):
		resp = requests.get("https://api.stackexchange.com/"+"/2.2/questions/{}/answers?order=desc&sort=activity&site=stackoverflow&filter=!--1nZwsgqvRX".format(questions_list[i]))
		json_ans_data = resp.json()
		print("--------------------------------------------------------")
		for j in json_ans_data['items']:
			print(j["body_markdown"]) 
			print("Link to answer : ", end=" ")
			print(j["link"])
			print("------------------------------------------------------------------")

def search_args():
    if ARGV.search:
        print("What do you want to search - ", end=" ")
        question = input()
        print("Tags : ", end=" ")
        tags = input()
        json_output = make_request(question,tags)
        questions = get_que(json_output)
        get_ans(questions)