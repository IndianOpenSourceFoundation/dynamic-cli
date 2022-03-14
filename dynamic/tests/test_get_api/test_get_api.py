from io import StringIO
import json
from dynamic import api_test


class TestApi():
    def test_get_request_no_headers(self, monkeypatch):
        # Test to check get api response without header

        self.test_object = api_test.ApiTesting()
        test_uri = "https://reqres.in/api/users/2"
        test_headers = ""
        save_response = "n"
        inputs = StringIO(test_uri+"\n"+test_headers+"\n"+save_response)
        monkeypatch.setattr('sys.stdin', inputs)
        res = self.test_object.get_request()

        file = open(
            'dynamic/tests/test_get_api/output.json')
        assert res == json.loads(file.read())
