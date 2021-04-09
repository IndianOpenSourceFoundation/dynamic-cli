import requests, json

class Api_Testing():
    default_url = "127.0.0.1:8000"

    @classmethod
    def get_request(self):
        request_url = Api_Testing.default_url
        input_url = input('Enter URL: ')
        if input_url != '':
            request_url = input_url

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