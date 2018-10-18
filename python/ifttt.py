#-*-coding:utf-8-*-
# https://chasuke.com/python_ifttt/
import requests

class Ifttt(object):

    def __init__(self, config):
        self.api_key = config.get("api_key")
    
    def tweet(self, message):
        print("tweet:{}".format(message))

        payload = {
            "value1": message
        }
        url = "https://maker.ifttt.com/trigger/{}/with/key/{}".format("noren_speaked", self.api_key)
        response = requests.post(url, data=payload)
        print(response.status_code, response.text)
        return response
