from io import StringIO
from dynamic import api_test
import json


class TestApi():
    def test_post_request_json_input(self, monkeypatch):
        # Test to post response with data using json file

        self.test_object = api_test.ApiTesting()
        test_uri = "https://reqres.in/api/users"
        test_headers = ""

        test_store_data = "y"
        test_enter_payload_data = "2"

        test_data = "dynamic/tests/test_post/input.json"

        save_response = "n"
        inputs = StringIO(test_uri+"\n"+test_headers+"\n"+test_store_data +
                          "\n"+test_enter_payload_data+"\n"+test_data+"\n"+save_response)
        monkeypatch.setattr('sys.stdin', inputs)

        res = self.test_object.post_request()
        assert res.status_code == 201

    def test_post_request_terminal_input(self, monkeypatch):
        # Test to post response with data using terminal

        self.test_object = api_test.ApiTesting()
        test_uri = "https://reqres.in/api/users"
        test_headers = ""

        test_store_data = "y"
        test_enter_payload_data = "1"

        test_data = json.dumps({"name": "aditya", "job": "leader"})

        save_response = "n"
        inputs = StringIO(test_uri+"\n"+test_headers+"\n"+test_store_data +
                          "\n"+test_enter_payload_data+"\n"+test_data+"\n"+save_response)
        monkeypatch.setattr('sys.stdin', inputs)

        res = self.test_object.post_request()
        assert res.status_code == 201
