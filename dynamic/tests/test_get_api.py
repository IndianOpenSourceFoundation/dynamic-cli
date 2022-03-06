from io import StringIO
import json
from ..api_test import ApiTesting

class TestApi():
    def test_get_request_no_headers(self, monkeypatch):
        """Test to check get api response without header."""
        self.test_object = ApiTesting()
        
        test_uri = "https://reqres.in/api/users/2"
        test_headers = ""
        save_response = "n"
        
        inputs = StringIO(test_uri+"\n"+test_headers+"\n"+save_response)
        
        monkeypatch.setattr('sys.stdin', inputs)
        
        res = self.test_object.get_request()
        
        assert res==json.loads("""{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}""")