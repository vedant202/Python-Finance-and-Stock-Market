# https://www.moneycontrol.com/news/stocksinnews-142.html

import requests
from bs4 import BeautifulSoup
import json
import datetime

html = requests.get("https://www.moneycontrol.com/news/stocksinnews-142.html")

soup = BeautifulSoup(html.content, "html.parser")

# print(soup.prettify())

elements = soup.find(id="cagetory")
# print(elements)

all_li_elements = elements.find_all('li')
print(len(all_li_elements))

# all_li_elements = []
# for i in range(1,25):
#     all_li_elements.append(soup.find(id="newslist-"+str(i)))
# print(len(all_li_elements))

data = []

try:
    for i in range(1, len(all_li_elements)):
        element = all_li_elements[i]
        print(i)
        if(element['class'][0] != "hide-mobile"):
            title = element.h2.a.string
            a = element.h2.a
            p = element.p
            print(title)

            blog_url = element.h2.a['href']

            blog_html = requests.get(blog_url)
            soup1 = BeautifulSoup(blog_html.content, "html.parser")

            find_class = soup1.find("div", {"class": "arti-flow"})

            find_all_p = soup1.find_all("p")
            # print(find_all_p)
            para = ""
            for p in find_all_p[:-2]:
                if(len(str(p.string)) > 100):
                    para += str(p.string) + " \n"

            # json_data = soup1.find_all(type="application/ld+json")
            # print(json_data)
            news_json = {
                "title": str(title),
                "date": str(datetime.datetime.today()),
                "sub para": str(p),
                "article para": para
    }
            data.append(news_json)
        else:
            all_li_elements.remove(element)
except Exception as e:
    print(e)
finally:
    with open("stock_news_data.json", "w") as f:
        json.dump(data, f)



# print(datetime.datetime.today())
