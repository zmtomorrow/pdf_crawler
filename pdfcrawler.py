import re
import sys
import urllib
import os

#target="http://cs224d.stanford.edu/lectures/"

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return  html

def getImg(html,location):
	#reg = r'src="(.+?\.jpg)" pic_ext'
	reg = r'href="(.+?\.pdf)"'
	imgre = re.compile(reg)
	imglist = imgre.findall(html)
	for name in imglist:
		down=target + name
		print down
		urllib.urlretrieve(down,'./'+ location+'/'+name)

if __name__=='__main__':
	target = sys.argv[1]
	location = sys.argv[2]
	os.mkdir(location)
	html = getHtml(target)
	getImg(html,location)
