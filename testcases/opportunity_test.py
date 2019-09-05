from common.test_base import TestBase
from common.response_checker import *
from common.constant import *
from common.json_helper import *
from common.apis import APIS
import json
import pytest

class opportunity_Test(TestBase):

    def test_createOpportunity(self):

        # Preapare Data
        headers = {
            'Content-Type': 'application/json',
            'X-Requested-By': 'Bao automation script',
            'Organization-Id': ORGANIZATION_ID
        }
        body = json.dumps({
            'title': OPPORTUNITY_TITLE,
            'customer_id': CUSTOMER_ID,
            'product_id': PRODUCT_ID,
            'product_package_id': PRODUCT_PACKAGE_ID,
            'assignee_id': ASSIGNEE_ID,
            'description': DESCRIPTION_TEXT
        })

        # Send request
        response = self.post_method( self.apis.CREATE_OPPORTUNITY_API, headers=headers, data=body)
        pytest.opportunityID = getValueRespone(response,'data', 'opportunity_id')

        # Verify reponse
        self.assertTrue(isStatusCode(response, 201))
        self.assertTrue(isMessageDisplayed(response, "Create an opportunity sucessfully!"))


    def test_getOpportunity(self):
        # Preapare Data
        headers = {
            'Organization-Id': ORGANIZATION_ID
        }

        # Send request
        response = self.get_method(self.apis.GET_OPPORTUNITY_API(pytest.opportunityID), headers=headers)      

        # Verify reponse
        self.assertTrue(isStatusCode(response, 200))
