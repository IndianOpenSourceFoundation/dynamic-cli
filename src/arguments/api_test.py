import requests, json
from pygments import highlight, lexers, formatters


class ApiTesting:
    default_url = "https://127.0.0.1:8000"
    default_headers = {}
    # Make GET request
    @classmethod
    def get_request(cls):
        request_url = cls.default_url
        request_headers = cls.default_headers
        input_url = input("Enter URL: ")
        input_headers = input("Enter Headers: ")
        if input_url != "":
            request_url = input_url
        if input_headers != "":
            try:
                request_headers = json.loads(input_headers)
            except Exception:
                print("Failed to parse Input Headers")
        # Check whether the request_url has an endpoint or not
        has_endpoint = cls.__check_endpoint(request_url)

        # Check if http:// or https:// is present in request_url
        has_protocol = cls.__check_protocol(request_url)

        if not (has_protocol):
            request_url = "https://" + request_url

        # Ask the user for endpoint if not present in request_url
        if not (has_endpoint):
            if request_url[-1] == "/":
                endpoint = input("Input endpoint " + "(Without the starting slash): ")
            else:
                endpoint = input("Input endpoint (With the starting slash): ")
            request_url += endpoint

        print("Trying ...\u26A1")

        # Make GET request and store the response in response_data.json
        try:
            response = requests.get(request_url, headers=request_headers)
            print(f"Reponse Status Code: {response.status_code}")
            response_data = json.loads(response.content)
            parsed_json = json.dumps(response_data, indent=4)
            output_json = highlight(
                parsed_json, lexers.JsonLexer(), formatters.TerminalFormatter()
            )
            print(output_json)

            store_data = input("Store response data? (Y/N): ")
            if store_data == "Y" or store_data == "y":
                with open("response_data.json", "w") as jsonFile:
                    json.dump(response_data, jsonFile, indent=4)
                print("Response data stored in response_data.json")

        except requests.exceptions.InvalidSchema:
            print(
                "Check whether the URL is valid or check if "
                + "the localhost server is active or not"
            )
        except Exception as e:
            print(e)

    @classmethod
    def __check_endpoint(cls, request_url):
        if request_url == cls.default_url:
            return False
        else:
            return True

    @classmethod
    def __check_protocol(cls, request_url):
        if request_url[:4] == "http":
            return True
        else:
            return False
