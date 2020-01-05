

import os
import re

all_label = []
result = {}
current_pos = []

def convert_Current_Dict(content):
	dict_content = {}
	all_content = content.split(' ')
	root_name = all_content.pop(0)
	dict_content[root_name] = {}
	for _text in all_content:
		if re.search(r'(=)',_text):
			_text = _text.split('=')
			dict_content[root_name][_text[0]] = _text[1]

	return dict_content

def next(re_dict, pos):
	return ''
def last(re_dict, pos):
	return ''


with open(os.path.join('.','dist','test.xml'),'r+',encoding='utf-8') as _f:
	text = _f.read().replace('\n','').replace('<','\n<')
	content = re.findall(r'(<.*>|.*)',text)
	# all_label = re.findall(r'(<.*>|.*)',_f.read())

	for count, _text in enumerate(content):
		_text = _text.strip()
		if not _text:
			continue
		lable_content =  re.sub(r'(\t+)',' ',_text)[1:-1]
		if re.search('(<.*>)',_text):
			if re.search('(>)',lable_content):
				# not label
				print('-'*99,'\n',_text,'\n','-'*99)
			else:
				# Make sure is the label
				# print(re.sub(r'(\t+)',' ',_text)[1:-1])
				print(convert_Current_Dict(re.sub(r'(\t+)',' ',_text)[1:-1]))

			_text = re.sub(r'(\t+)',' ',_text)[1:-1]
			continue
		# Other text
		print('>>>>>>>>>>>>>>>\n',_text,'\n<<<<<<<<<<<<<<<<<<<<<')
