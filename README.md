# A script for searching classfields on insomnia.gr
With this script you can search for classfields on the website with criteria such as title and price range.

# Dependencies
To run the script you must have the following:
* beautifulsoup4
* requests

To install them run:
```bash
sudo pip install beautifulsoup4
sudo pip install requests
```
If you don't have pip run (ubuntu):
```bash
sudo apt-get install python-pip
```

# How to run the script:
```bash
python insomnia.py [-h] [-f] [-r] url query pages
```
Arguments in [] are optional.

Required arguments:

url: the url of the classfields page (e.g. the smartphone url)

query: the search criteria (e.g. "smartphone model" quotes included)

pages: number of pages to search (e.g. 5)

Optional arguments:

-h, --help: help

-f, --filter: removes classfields with no price tag

-r, --range: price range (e.g. 50-200)

# Examples

1) Search classfields with title "LG G6" in the LG page (shows 10 first pages):

Note: Search is case insensitive
```bash
python insomnia.py https://www.insomnia.gr/classifieds/category/52-lg/ "lg g6" 10
```
2) Search classfields with title "LG G6" in the LG page (showing only classfields with price tag):
```bash
python insomnia.py https://www.insomnia.gr/classifieds/category/52-lg/ "lg g6" 10 -f
```
3) Search classfields with title "LG G6" in the LG page (shows classfields in range of 200-400 in the first 5 pages):
```bash
python insomnia.py https://www.insomnia.gr/classifieds/category/52-lg/ "lg g6" 5 -r 200-400
```
