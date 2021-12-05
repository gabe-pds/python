from textblob import TextBlob
import requests
import bs4
import matplotlib.pyplot as plt
import re

web_page = 'https://www.huffpost.com/'
##################################CONSISTENT FOR ALL MAIN PAGES###########################################
main_page = requests.get(web_page)

#print(main_page.text)


main_page_soup = bs4.BeautifulSoup(main_page.text, 'lxml')

main_page_links = []
for link in main_page_soup.find_all('a', attrs={'href': re.compile("^https://")}):
    main_page_links.append(link.get('href'))
# print(main_page_links)
# print(main_page_links[0])
# print(len(main_page_links))
##################################CONSISTENT FOR ALL MAIN PAGES###########################################


#Initiate empty polarity and sentiment lists
web_pages_subjectivity = []
web_pages_polarity = []

################################VARIES ON A SITE TO SITE BASIS###########################################

#Begin implementing loops from tests.py to analyze current news with text blob

for loc in range(0, len(main_page_links)):
    current_article = requests.get(main_page_links[loc])
    current_soup = bs4.BeautifulSoup(current_article.text, 'lxml')
    current_paragraph_list=current_soup.find_all('p')
    current_paragraph_string=''

    for p in range(0,len(current_soup.select('p'))):
        current_paragraph_string=current_paragraph_string+current_soup.find_all('p')[p].getText()
#################################VARIES ON A SITE TO SITE BASIS###########################################

    current_texblob=TextBlob(current_paragraph_string)
    current_polarity=current_texblob.polarity #positive or negative (-1,1)
    current_subjectivity=current_texblob.subjectivity #Personal Opinion (0,1)
    web_pages_subjectivity.append(current_subjectivity)
    web_pages_polarity.append(current_polarity)


plt.scatter(web_pages_polarity, web_pages_subjectivity)
plt.axis([-1,1,0,1])
plt.grid()
#And lets name the x label and y label
plt.xlabel('Article Polarity/Bias')
plt.ylabel('Article Subjectivity')
plt.title(web_page)
plt.show()
