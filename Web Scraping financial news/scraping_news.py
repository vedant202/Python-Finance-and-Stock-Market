# https://www.businesstoday.in/latest/economy

from bs4 import BeautifulSoup
import requests as rs
import json
html = rs.get('https://www.businesstoday.in/latest/economy')

# print(html.content)

bs = BeautifulSoup(html.content,"html.parser")

# print(bs.prettify())

# for link in bs.find_all('a'):
#     print(type(link.string), " ", link.string)
m = 1

data = []

for link in bs.find_all('a'):

    if(str(type(link.string))== "<class 'bs4.element.NavigableString'>" and len(link.string.strip())>35):
        date = link.parent.next_sibling.next_sibling.string
        p = date.next_element.next_element.string
        title = link.string
        
        print(str(m)+" Title" + ". " + link.string)
        print("Date "+date)
        print("P :-"+p)
        print()
        # print(link['href'])
        
        html2 = rs.get(link['href'])
        bs1 = BeautifulSoup(html2.content,"html.parser")
        div = bs1.find_all("div", {"class": "story-with-main-sec"})
        div_children = div[0]
        div_children_p = div_children.find_all('p')
        # print(div_children_p)
        para = ""
        for p in div_children_p:
            para += str(p.string) + " \n"
        print(para)
        
        d = {"title":str(title),
                "date":str(date),
                "sub para":str(p),
                "link":str(link['href']),
                "para":para}
        data.append(d)
        m += 1
        

with open("finance_news_data.json","w") as f:
    json.dump(data,f)        