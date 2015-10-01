# Rutgers IEEE Student Branch - Python Webscraping Workshop

## Workshop Leaders

Ravi Bhankharia

## Module 0 - Setup

We'll be using Requests (http://docs.python-requests.org/en/latest/) to load web pages as strings into python and Beautiful Soup (http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse the web page data.

## Module 1 - Retrieve the Data

Requests makes it easy to retrieve data from webpages, all you have to do is call the get function.

* `import requests`

* `response = requests.get("https://cbracco.github.io/html5-test-page/")`

This stores the entire html source of the html5 test page into the response variable. If you try to print the variable, you'll get an http header, in order to display access the actual string, you can use response.text.

## Module 2 - Parse the Data

Beautiful Soup is a library dedicated to parsing html very easily. In order to use it, you must import it:

* `from bs4 import BeautifulSoup`

To start off, let's get the process the page using beautiful soup:

* `soup = BeauitfulSoup(response.text, 'html.parser')`

Once a soup object is made, you can access tags by typing in

* `body = soup.body`

This will return the first 'body' tag in the html document. To get to a nested tag (for example 'b') type this:

* `boldInBody = soup.body.b`

To get the next occurrence of a tag in the document, you can use find_next(tag):

* `soup.a.find_next('a')`

You could also find the next p tag that appears:

* `soup.p.find_next('p')`

Note that a find_previous(tag) function also exists and works in the same manner but in reverse.

To get all of the 'a' tags, you use the function find_all:

* `list = soup.find_all('a')`

To get to an attribute of a tag (for example a class attribute inside a div tag):

* `soup.div.get('class')`

In fact, all attributes of a tag are stored in a python dictionary that can be accessed with `soup.div.attrs`. As a consequence of that `soup.div['class']` is equivalent to `soup.div.get('class')`. If there are more than one attribute in a tag, the value returned by getting that key is actually a list. Note that all of this is mutable, so if you wish to change an attribute you can.

The following chunk of code will print out all the links on a given page:

```
for link in soup.find_all('a'):
    print(link.get('href'))
```

The soup object's tags are organized into a tree, beautiful soup lets you navigate to a tag's enclosing tag (parent), any tag that shares the same parent (sibling) and any tag that is enclosed by it. Try out the following commands:

```
soup.title.parent
soup.li.next_sibling.next_sibling
soup.li.next_sibling.previous_sibling

for child in soup.ul.children:
    print(child)
```

If you want to print out the html tree/tag info in a readable fashion, use the `prettify()` funciton:

* `print(soup.a.prettify())`

To get the contents of what's in the tag use `.contents`:

* `print(soup.a.contents)`

## Module 3 - Mini Project

This link - http://www.cnn.com/services/rss/ has a list of all of CNN's RSS Feeds. Use the things you've learned in the workshop to scrape all the titles from the World category RSS all the way down to the Living category RSS and print them

Bonus points for printing the date/time as well!

If you're really stuck scroll below for some hints






















Hints:

*Check out the html source of those pages to figure out which tag holds the story titles.

*string addition ('hello' + ' ' + 'world' = 'hello world') is very helpful when iterating through all of the URL's.

* `base_url = 'http://rss.cnn.com/rss/'`

*Here's a helpful list of suffixes: `suffixes = ['cnn_world.rss', 'cnn_us.rss', 'money_latest.rss', 'cnn_allpolitics.rss', 'cnn_tech.rss', 'cnn_health.rss', 'cnn_showbiz.rss', 'cnn_travel.rss', 'cnn_living.rss']`

## Module - References
http://blog.miguelgrinberg.com/post/easy-web-scraping-with-python
