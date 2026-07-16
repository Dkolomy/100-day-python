from bs4 import BeautifulSoup
import lxml

with open('website.html', 'r') as file:
  contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)

all_anchor_tags = soup.find_all(name='a') # find all anchor tags
print(all_anchor_tags)

for tag in all_anchor_tags:
  print(tag.getText())
  print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")

company_url = soup.select_one(selector="p a")