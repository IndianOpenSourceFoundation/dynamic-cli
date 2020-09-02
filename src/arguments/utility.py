import requests
from termcolor import colored


class Utility:

    def make_request(self, que, tag: str):
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
        resp = requests.get("https://api.stackexchange.com/" +
                            "/2.2/search/advanced?order=desc&sort=relevance&tagged={}&title={}&site=stackoverflow".format(tag, que))
        return resp.json()

    def get_que(self, json_data):
        que_id = []
        for data in json_data['items']:
            if data["is_answered"]:
                que_id.append(data["question_id"])
        return que_id

    def get_ans(self, questions_list):
        # ans = []
        for questions in range(1):
            resp = requests.get("https://api.stackexchange.com/" +
                                "/2.2/questions/{}/answers?order=desc&sort=activity&site=stackoverflow&filter=!--1nZwsgqvRX".format(questions_list[questions]))
            json_ans_data = resp.json()
            print(
                colored("--------------------------------------------------------", 'red'))
            for data in json_ans_data['items']:
                print(data["body_markdown"])
                print("Link to answer : ", end=" ")
                print(data["link"])
                print(
                    colored("--------------------------------------------------------", 'red'))
