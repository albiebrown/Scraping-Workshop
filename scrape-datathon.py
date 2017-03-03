from bs4 import BeautifulSoup
from urllib2 import urlopen

import csv
import json


url = "http://bds.cs.brown.edu/datathon/"

soup = BeautifulSoup(urlopen(url).read(), 'lxml')

rows = soup.find_all("div", { "class" : "workshop-row" })	

for row in rows:
	print row
	print "#####"