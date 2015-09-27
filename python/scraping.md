# Rutgers IEEE Student Branch - Python Webscraping Workshop

## Workshop Leaders

Ravi Bhankharia, Niral Shah

## Module 0 - Setup

We'll be using Requests (http://docs.python-requests.org/en/latest/) to load web pages as strings into python and Beautiful Soup (http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the web page data.

## Module 1 - Retrieve the Data

Requests makes it easy to retrieve data from webpages, all you have to do is call the get function.

** `import requests`

** `response = requests.get("http://")`

This stores the entire html source of the page into a file called "response.text".

## Module 2 - Parse the Data

Beautiful Soup is a library dedicated to parsing html very easily. In order to use it, you must import it:

** `from bs4 import BeautifulSoup`

```
for link in soup.find_all('a'):
    print(link.get('href'))
```

## Module - References
http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python
