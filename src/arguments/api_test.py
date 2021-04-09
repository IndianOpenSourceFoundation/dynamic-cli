import requests, json
import re

class Api_Testing():
    default_url = "127.0.0.1:8000"

    # Make GET request
    @classmethod
    def get_request(self):
        request_url = Api_Testing.default_url
        input_url = input('Enter URL: ')
        if input_url != '':
            request_url = input_url

        # Check whether the request_url has an endpoint or not
        has_endpoint = self.check_endpoint(request_url)

        # Ask the user for endpoint if not present in request_url
        if not(has_endpoint):
            if(request_url[-1] == '/'):
                endpoint = input("Input endpoint (Without the starting slash): ")
            else:
                endpoint = input("Input endpoint (With the starting slash): ")
            request_url += endpoint

        print("Trying ...\u26A1")

        # Make GET request and store the response in response_data.json
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

    # This method works by first checking whether the url is a localhost url
    # If it is, the length of the substring after ':' (Example, 127.0.0.1:8000) is checked
    # The length should be less than 6 as either 8000 or 8000/ can be possible (No endpoint)
    # If the url is not a localhost url
    # The length of the substring after '.' is checked
    # The length should be less than 5 (Example: com/, com, io/, io) (For no endpoint)
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