import unittest
import requests
import sys
import os
from common.constant import *
import json
from common.apis import APIS

class TestBase(unittest.TestCase):
    _timeout = 30

    def setUp(self):   
        self.passed = True

    def assertTrue(self, expr, msg="False"):
        try:
            unittest.TestCase.assertTrue(self, expr)
        except:
            self.passed = False
            self.fail(msg)

    def assertFalse(self, expr, msg="False"):
        try:
            unittest.TestCase.assertFalse(self, expr)
        except:
            self.passed = False
            self.fail(msg)

    def assertEqual(self, first, second, msg="False"):
        try:
            unittest.TestCase.assertEqual(self, first, second)
        except:
            self.passed = False
            self.fail(msg)

    def assertNotEqual(self, first, second, msg="False"):
        try:
            unittest.TestCase.assertNotEqual(self, first, second)
        except:
            self.passed = False
            self.fail(msg)

    def assertIn(self, member, container, msg="False"):
        try:
            unittest.TestCase.assertIn(self, member, container)
        except:
            self.passed = False
            self.fail(msg)

    def assertNotIn(self, member, container, msg="False"):
        try:
            unittest.TestCase.assertNotIn(self, member, container, msg)
        except:
            self.sauce_client.jobs.update_job(
                self._driver._driver.session_id, passed=False)
            self.fail(msg)

    def get_method(self, url="", headers=None, params=None):
        """
        @summary: send a GET http request and get the response data
        @param url: Url REST address
        @param header: header values with format dictionary
        @param params: parameter values with format dictionary
        @return: response data of http request
        """
        try:
            response = requests.get(
                url, headers=headers, params=params, timeout=self._timeout)
            return response
        except Exception as ex:
            raise ex

    def post_method(self, url="", headers=None, data=None, **kwargs):
        """
        @summary: send a POST http request and get the response data
        @param url: Url REST address
        @param header: header values with format dictionary
        @param data: data value with format json object
        @return: response data of http request
        """
        try:
            response = requests.post(
                url, headers=headers, data=data, timeout=self._timeout, **kwargs)
            return response
        except Exception as ex:
            raise ex

    def delete_method(self, url=None, headers=None, data=None):
        """
        @summary: send a DELETE http request and get the response data
        @param: url: Url REST address
        @param header: header values with format dictionary
        @param data: data value with format json object
        @return:   response data of http request
        """
        try:
            response = requests.delete(
                url, headers=headers, data=data, timeout=self._timeout)
            return response
        except Exception as ex:
            raise ex

    def patch_method(self, url=None, headers=None, data=None):
        """
        @summary: send a PATCH http request and get the response data
        @param: url: Url REST address
        @param header: header values with format dictionary
        @param data: data value with format json object
        @return: response data of http request
        """

        try:
            response = requests.patch(
                url, headers=headers, data=data, timeout=self._timeout)
            return response
        except Exception as ex:
            raise ex

    def put_method(self, url=None, headers=None, data=None):
        """
        @summary: send a PUT http request and get the response data
        @param: url: Url REST address
        @param header: header values with format dictionary
        @param data: data value with format json object
        @return:   response data of http request
        """
        try:
            response = requests.put(
                url, headers=headers, data=data, timeout=self._timeout)
            return response
        except Exception as ex:
            raise ex

    @property
    def ACCESS_TOKEN(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "password": "aIJAryLEmErFlUSePtio",
            "grant_type": "password",
            "client_id": "aws-lambda-oidc-authorizer",
            "username": "wwn_1267"
        }
        response = self.post_method(
            self.apis.GET_ACCESS_TOKEN_ROUTE, headers=header, data=body)
        return json.loads(response.content)['access_token']

    @property
    def apis(self):
        return  APIS(os.environ["DEBUSSY"])
    
if __name__ == "__main__":
    unittest.main()
