import requests, json
import re

class Api_Testing():
    default_url = "127.0.0.1:8000"

    @classmethod
    def get_request(self):
        request_url = Api_Testing.default_url
        input_url = input('Enter URL: ')
        if input_url != '':
            request_url = input_url

        has_endpoint = self.check_endpoint(request_url)

        if not(has_endpoint):
            if(request_url[-1] == '/'):
                endpoint = input("Input endpoint (Without the starting slash): ")
            else:
                endpoint = input("Input endpoint (With the starting slash): ")
            request_url += endpoint

        print("Trying ...\u26A1")

        try:
            response = requests.get(request_url)
            print(f"Reponse Status Code: {response.status_code}")
            print("Response data stored in response_data.json")
            parsed = json.loads(response.content)
            with open('response_data.json', 'w') as jsonFile:
                json.dump(parsed, jsonFile, indent=4)
        except requests.exceptions.InvalidSchema:
            print("Check whether the URL is valid or check if the localhost server is active or not")
        except Exception as e:
            print(e)

    def check_endpoint(url):
        check_string = url
        is_localhost_url = False

        if(len(check_string.split(":")[-1]) <= 5):
            is_localhost_url = True

        if(is_localhost_url):
            check_string = check_string.split(':')[-1]
        else:
            check_string = check_string.split('.')[-1]

        if(len(check_string) <= 5):
            return False
        else:
            return True