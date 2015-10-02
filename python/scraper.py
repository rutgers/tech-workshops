import requests
from bs4 import BeautifulSoup

suffixes = ['cnn_world.rss', 'cnn_us.rss', 'money_latest.rss', 'cnn_allpolitics.rss', 'cnn_tech.rss', 'cnn_health.rss', 'cnn_showbiz.rss', 'cnn_travel.rss', 'cnn_living.rss']  ##Create a list to iterate through to generate all possible urls
base_url = 'http://rss.cnn.com/rss/'

for suffix in suffixes:   # Go through the entire list we just made

	response = requests.get(base_url+suffix)  # Concatenate the strings to access each URL in turn
	soup = BeautifulSoup(response.text, 'html.parser')  # Parse each webpage
	titleList = soup.find_all('title')    # All the titles were held in title tags
	titleList = titleList[2:]   # Cut off the first two title tags since they're both inconsequential

	for title in titleList:
		print(title.contents[0])  # Print out each title in the title list before looping through another RSS feed

"""
#For the pythonistas out there - if you're interested in how to do this as compactly as possible:
#(look up list comprehensions):
import requests, bs4
[[print(title.contents[0]) for title in bs4.BeautifulSoup(requests.get("http://rss.cnn.com/rss/"+suffix).text, 'html.parser').find_all('title')[2:]] for suffix in ['cnn_world.rss', 'cnn_us.rss', 'money_latest.rss', 'cnn_allpolitics.rss', 'cnn_tech.rss', 'cnn_health.rss', 'cnn_showbiz.rss', 'cnn_travel.rss', 'cnn_living.rss']]
"""
