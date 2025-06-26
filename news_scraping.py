import requests
from bs4 import BeautifulSoup

html_title=[]
html_h2_header=[]
html_h3_header=[]

URL="https://www.thehindu.com/"
response=requests.get(URL)

try:
  if response.status_code==200:
    soup=BeautifulSoup(response.content,"html.parser")

    title_tag=soup.find("title")
    if title_tag:
      html_title.append(title_tag.get_text(strip=True))

    h2_header_tags=soup.find_all("h2")
    for h2_headers in h2_header_tags:
      html_h2_header.append(h2_headers.get_text(strip=True))

    h3_header_tags=soup.find_all("h3")
    for h3_headers in h3_header_tags:
      html_h3_header.append(h3_headers.get_text(strip=True))

    with open("news_scraping.txt","w") as file:
      file.write("<Title>Tag:\n")
      for title in html_title:
        file.write("\n"+title+"\n")

      file.write("\n<H2>Tags:\n")
      for h2 in html_h2_header:
        file.write("\n"+h2+"\n")

      file.write("\n<H3>Tags:\n")
      for h3 in html_h3_header:
        file.write("\n"+h3+"\n")

      print("Scraping completed. Headlines saved to news_scraping.txt.")

  else:
    print("Failed to fetch page. Status code:", response.status_code)

except Exception as e:
  print("Error while fetching data:", e)


