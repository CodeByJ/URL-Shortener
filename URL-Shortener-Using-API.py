# python3
# -*- coding: utf-8 -*-
# Uses gotiny api https://github.com/robvanbakel/gotiny-api due to ease-of-use for developers and simple response which includes the full url and code

import random
import requests

class Codec:
    
    def __init__(self):
        self.url_dict = {}
        self.string_length = 6
        self.letters = ('abcdefghijklmnopqrstuvwxyzABCDEF'
                        'GHIJKLMNOPQRSTUVWXYZ0123456789')


    def generate_short_url(self, long_url: str) -> str:
        api_url = "https://gotiny.cc/api"
        todo = {"input": long_url}
        response = requests.post(api_url, json=todo)
        #response returns long_url and code which is the shortened url
        short_url = response.json()[0]['code']
        
        while short_url in self.url_dict:
            short_url = self.generate_short_url(long_url)
        return short_url


    def encode(self, long_url: str) -> str:
        short_url = self.generate_short_url(long_url) 

        if long_url not in self.url_dict.keys():
            self.url_dict[short_url] = long_url
        else:
            self.url_dict = {k: v for k, v in self.url_dict.items() if v == long_url}
            self.url_dict[short_url] = long_url

        return short_url


    def decode(self, short_url: str) -> str:
        if short_url in self.url_dict: 
            return self.url_dict[short_url]
        else:
            return None #return 