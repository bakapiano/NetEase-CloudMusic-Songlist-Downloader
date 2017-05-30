#-*- coding: utf-8 -*-

import requests
import re
import os

ListID = raw_input('Input the NetEase-CloudMusic songlist id:')
url = 'http://music.163.com/playlist'
params = {'id': ListID}
context = requests.get(url, params=params).text
SongList = re.findall(ur'<li><a href="/song\?id=(.*?)">(.*?)</a></li>', context)
ListName = re.findall(ur'<title>(.*?) - 网易云音乐</title>', context)[0]
print ListName

if not os.path.exists(ListName):
	os.mkdir(ListName)
for i in SongList:
	SongID, SongName = i
	print 'Downloading', '"' + SongName + '"', '...'
	with open(ListName + '\\' + SongName + '.mp3', 'wb') as file:
		params = {'id': SongID + '.mp3'}
		res = requests.get('http://music.163.com/song/media/outer/url', params=params)
		file.write(res.content) 

print 'Done'