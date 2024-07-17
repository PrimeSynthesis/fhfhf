import requests
from bs4 import BeautifulSoup




url_file = 'urls.txt'


def fetch_article(url):
  response = requests.get(url)
  if response.status_code != 200:
    print("Failed to retrieve the article")
    quit()
  return response

def clean_webpage(webpage):
  soup = BeautifulSoup(webpage.content,'html.parser')
  content = soup.find(id = "mw-content-text")
  title = soup.find(id="firstHeading").get_text()
  if content:
    paragraphs = content.find_all('p')
    text = "\n".join([para.get_text().strip() for para in paragraphs])
   
    return title, text

def read_urls(file):
  with open(file,"r") as file:
    lines = file.readlines()
    file.close()
  return lines


def save_article(article,title, url):
  with open("articles.txt","a")as file:
    file.write(f"Title:{title} URL:{url}\n")
    file.write(article)
    file.write("\n\n"+"="*80 + "\n\n")


def main():
  urls = read_urls(url_file)
  for url in urls:
    print(url)
    wiki_page = fetch_article(url.strip())
    title, text = clean_webpage(wiki_page)
    save_article(text,title,url)


main()







