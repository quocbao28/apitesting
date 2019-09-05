import json

def isStatusCode(response, code):
    return response.status_code == code

def isMessageDisplayed (response, message):
    return json.loads(response.content)['message']== message
        