from common.constant import *
from common.test_base import TestBase
from common.response_checker import *

class Organization_Test(TestBase):
    def test_geodata_success(self):
        organization = '123'

        #Preapare Data
        headers = {
            'Authorization': self.ACCESS_TOKEN,
            'X-Requested-By': 'abc',
            'Organization-Id': organization
        }
        payload = {'file': open('resources/addressfile.csv', 'rb')}

        #Send request
        response = self.post_method(self.apis.ORG_ADDRESS_API_ROUTE, headers=headers, files=payload)

        #Verify reponse
        self.assertTrue(isStatusCode(response, 200))

