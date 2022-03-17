# python3 
from URL-Shortener-Using-API import *


def test_question_2(urls:str) -> str:
    full_urls = []
    codec = Codec()
    for url in urls:
        encoded = codec.encode(url)
        full_urls.append("gotiny.cc/" + encoded)
    
    return full_urls


urls = ['https://www.google.com/','https://www.youtube.com/','https://www.wikipedia.org/']
print(urls)
print(test_question_2(urls))
