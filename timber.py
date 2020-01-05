"""
python version : 3.6
"""
import re
import configparser
import os
import xmltodict
config = configparser.ConfigParser()
print(config.read('default.ini'))
print(config.sections())
print(config['DEFAULT'])

separate = {',':'\\n'}
filter_text = []

with open(os.path.join('.','dist','test.log'),'rb') as _f:
	print(xmltodict.parse(_f.read()))
	print(_f.read().strip())
	
