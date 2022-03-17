# python3
# -*- coding: utf-8 -*-

import random


class Codec:
    
    def __init__(self):
        self.url_dict = {}
        self.string_length = 6
        self.letters = ('abcdefghijklmnopqrstuvwxyzABCDEF'
                        'GHIJKLMNOPQRSTUVWXYZ0123456789')


    def generate_short_url(self):
        short_url = ''
        for i in range(self.string_length):
            short_url += random.choice(self.letters)
    
        # if short_url already exists as a key in url_dict
        while short_url in self.url_dict: 
            short_url = self.generate_short_url()

        return short_url


    def encode(self, long_url: str) -> str:
        # added self. to generate_short_url() 
        short_url = self.generate_short_url() 

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
            # return None if short_url does not exist
            return None 


