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

data = [] # To store stock json data

for link in bs.find_all('a'): #finds all a anchor tag containing links

    if(str(type(link.string))== "<class 'bs4.element.NavigableString'>" and len(link.string.strip())>35):
        title = link.string # Extracting title from link
        date = link.parent.next_sibling.next_sibling.string # Extracting date from link
        p = date.next_element.next_element.string # Extracting sub para from link
        
        print(str(m)+" Title" + ". " + link.string)
        print("Date "+date)
        print("P :-"+p)
        print()
        # print(link['href'])
        
        html2 = rs.get(link['href']) # Extracting whole news paragraph with request using the url inside of link
        bs1 = BeautifulSoup(html2.content,"html.parser")
        div = bs1.find_all("div", {"class": "story-with-main-sec"})
        div_children = div[0]  #Extracting first element inside div object 
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
            "para":para
            }
        print(d)
        data.append(d)
        m += 1
        

with open("finance_news_data.json","w") as f:
    json.dump(data,f)        