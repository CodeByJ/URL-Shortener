# python3
import unittest
from URL-Shortener-Without-API import *

class Test(unittest.TestCase):
	
	codec = Codec()
	url_file = open("test_urls.txt")
	data = url_file.read()
	urls = data.split("\n")
	url_file.close()	
	
	def test_length(self):
		for url in self.urls:
			length = len(self.codec.encode(url))		
			self.assertEqual(length, 6)
			
	def test_existing(self):
		for url in self.urls:
			encoded = self.codec.encode(url) 
			encoded_2 = self.codec.encode(url)
			self.assertNotEqual(encoded,encoded_2)
			self.assertEqual(self.codec.decode(encoded),self.codec.decode(encoded_2)) 

	def test_encode_decode(self):
		for url in self.urls:
			encoded = self.codec.encode(url)
			decoded = self.codec.decode(encoded)
			self.assertEqual(decoded, url)

	def test_not_existing(self):
		encoded = self.codec.generate_short_url()
		decoded = self.codec.decode(encoded)
		self.assertEqual(decoded, None)
	
if __name__ == '__main__':
	unittest.main()
