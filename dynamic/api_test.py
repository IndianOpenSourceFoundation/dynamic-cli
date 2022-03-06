import json
import requests
from pygments import highlight, lexers, formatters


class ApiTesting:
    default_url = "https://127.0.0.1:8000"
    default_headers = {}
    invalid_schema_message = (
        "Check whether the URL is valid or check if"
        + "the localhost server is active or not"
    )
    # fetches the input data for making a request

    @classmethod
    def fetch_input_url(cls):
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
                endpoint = input("Input endpoint " +
                                 "(Without the starting slash): ")
            else:
                endpoint = input("Input endpoint (With the starting slash): ")
            request_url += endpoint

        print("Trying ...\u26A1")
        return {
            "request_url": request_url,
            "request_headers": request_headers,
        }

    @classmethod
    def read_data_from_file(cls):
        filename = input("Enter a filename (response_data.json)")
        data = {}
        if filename.strip() == "":
            filename = "response_data.json"
            print(f"filename empty, so default file {filename} is used ")
        with open(filename, "r") as reader:
            file_content = reader.read()
            try:
                json_data = json.loads(file_content)
                data = json_data.get("data")
                # Make sure the data is not None and send
            except json.JSONDecodeError:
                print("Unable to parse the file, Please try again")
                cls.read_data_from_file()
        return data

    @classmethod
    def enter_data_payload(cls):
        print("Option 1: For sending data payload from terminal\n")
        print("Option 2: For sending data payload by reading from json file\n")
        store = int(input("Please choose the above options? (1/2)"))

        data = {}
        if store == 1:
            data = input("Enter data as key value pairs")
            try:
                data = json.loads(data)
            except Exception as exception_obj:
                print(
                    f"Unable to load the data due to {exception_obj}, please try again \n"
                )
                cls.enter_data_payload()
        elif store == 2:
            data = cls.read_data_from_file()
        else:
            print(
                f"you have entered {store}, please choose from above options")
            cls.enter_data_payload()
        return data

    @classmethod
    def fetch_payload_data(cls):
        store = input("Do you want to send data payload? (Y/N)")
        data = None
        if store.lower() == "y":
            data = cls.enter_data_payload()

        elif store.lower() == "n":
            data = {}
        else:
            print(
                f"You have entered {store}, please enter from the above options")
            cls.fetch_payload_data()
        return data

    # saves the json response into a file
    @classmethod
    def save_response_data(cls, response_data):
        store_data = input("Store response data? (Y/N): ")
        if store_data.lower() == "y":
            filename = input("Enter a filename (response_data.json)")
            if filename == "":
                filename = "response_data.json"
            with open(filename, "w") as jsonFile:
                json.dump(response_data, jsonFile, indent=4)
            print(f"Response data stored in {filename}")
        elif (store_data.lower()) == "n":
            print(
                f"You have entered {store_data}, So the response is not saved")
        else:
            print(f"You have entered {store_data}, please enter either Y or N")
            cls.save_response_data(response_data)

    # formats the response data and prints it in json on console
    @classmethod
    def print_response_json(cls, response):
        print(f"Reponse Status Code: {response.status_code}")
        response_data = json.loads(response.content)
        parsed_json = json.dumps(response_data, indent=4)
        output_json = highlight(
            parsed_json, lexers.JsonLexer(), formatters.TerminalFormatter()
        )
        print(output_json)

    # Make GET request
    @classmethod
    def get_request(cls):
        request_data = cls.fetch_input_url()
        # Make GET request and store the response in response_data.json
        try:
            response = requests.get(
                request_data["request_url"], headers=request_data["request_headers"]
            )
            cls.print_response_json(response)
            response_data = json.loads(response.content)
            cls.save_response_data(response_data)
            return response.json()
        except requests.exceptions.InvalidSchema:
            print(cls.invalid_schema_message)
        except Exception as exception_obj:
            print(exception_obj)

    # Make a POST request
    @classmethod
    def post_request(cls):
        request_data = cls.fetch_input_url()
        data = cls.fetch_payload_data()
        try:
            response = requests.post(
                url=request_data["request_url"],
                headers=request_data["request_headers"],
                data=data,
            )
            cls.print_response_json(response)
            response_data = json.loads(response.content)
            cls.save_response_data(response_data)
        except requests.exceptions.InvalidSchema:
            print(cls.invalid_schema_message)
        except Exception as exception_obj:
            print(exception_obj)

    # Make a delete request
    @classmethod
    def delete_request(cls):
        # request_data contains dictionary of inputs entered by user
        request_data = cls.fetch_input_url()
        try:
            response = requests.delete(
                request_data["request_url"], headers=request_data["request_headers"]
            )
            cls.print_response_json(response)
            response_data = json.loads(response.content)
            cls.save_response_data(response_data)

        except requests.exceptions.InvalidSchema:
            print(cls.invalid_schema_message)
        except Exception as exception_obj:
            print(exception_obj)

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
