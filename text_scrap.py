# import necessary libraries
from bs4 import BeautifulSoup
import requests
import re

#response in in jason format 
response=requests.get("https://www.bajajfinservhealth.in/articles-sitemap-0.xml")
main_doc=response.text
web_details= BeautifulSoup(main_doc,'html.parser')

count=0
website_list=[]
#to get all the websites to website_list
for link in web_details.find_all('loc'):
    website_list.append(link.text)

# print(website_list)

print(len(website_list)," no. of articles found \n #########################")

# for i in website_list:
check=requests.get(website_list[3])
doc=check.text
web= BeautifulSoup(doc,'html.parser')

c=(web.find("div",class_="e-css-7h4c0a"))

avoid=["strong","img","a"]

previous_align=0
current_align=0
space="     "

tags=["h2","h3","p","ul","li"]
for k in c:
    if (k.name not in avoid):
        if (k.name=="h2"):
            print("------------------------")
        if (k.name=="h3"):
            print("\n")
        if (k.string!=None):    
            print(k.string)
        else:
            for j in k:
                print(j.text)