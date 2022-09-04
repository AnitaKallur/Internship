from turtle import title
from urllib.request import urlopen
from cgitb import html
import requests
# from urllib.request import urlopen
from bs4 import BeautifulSoup
url = ("https://en.wikipedia.org/wiki/Main_Page")
request = requests.get(url)
htmlContent = request.content
soup = BeautifulSoup(htmlContent, "html.parser")
titles = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
print(*titles, sep='\n\n')

