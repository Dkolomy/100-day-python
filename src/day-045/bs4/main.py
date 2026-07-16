from bs4 import BeautifulSoup
import lxml

# with open('website.html', 'r') as file:
#   contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)

# all_anchor_tags = soup.find_all(name='a') # find all anchor tags
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#   print(tag.getText())
#   print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")

# company_url = soup.select_one(selector="p a")

# https://news.ycombinator.com/news

import requests

TARGET_URL = "https://news.ycombinator.com/news"

response = requests.get(TARGET_URL)

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all(name="a")
article_texts = []
article_links = []
for article in articles:
  text = article.getText()
  article_texts.append(text)
  link = article.get("href")
  article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_number)

# print(article_texts)
# print(article_links)
# print(article_upvotes)




# print(soup.title.string)

# all_anchor_tags = soup.find_all(name='a')

# for tag in all_anchor_tags:
#   print(tag.getText())
#   print(tag.get("href"))