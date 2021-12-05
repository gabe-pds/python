# Python Projects
This folder contains some projects I have completed using Python. These projects are currently pretty simple, but I hope to develop my understanding and progress into more intense projects eventually. My goal with Python would be to eventually begin developing my understanding and mastery of big data. 

## Project 1 - Tic-Tac-Toe
This is an entry level Tic-Tac-Toe gane after following the Pierian Data Complete Python BootCamp. This project includes the usage of for loops, while loops, if then statements, simple boolean logic, and functions. 

## Project 2 - Black Jack 
This is an entry level Black Jack game following the Pierian Data Complete Python BootCamp.This project takes everything we learned before but adds object oriented programing to the mix. First Crack at OOP and I enjoyed it a bunch. I hope to use OOP whenever I get a chance in newer projects!  

## Project 3 - Website Sentiment Analysis
This is a medium level project that uses the webscraping module beautifulsoup and the NLP module textblob to perform sentitment analysis on certain online news sources. My goal for this project was to create a visual representation which indicated the subjectivity and polartity of all the current news sites on the main page of a news company. This project required basic understanging of HTML to find the text which would be analyzed. 

The main limitation of this code is the fact that not all websites are formatted the same way. This code works by going to the main site page, collecting all the links from that page, then looping through those links and going to the 'p' <div> which had the text for analysis. Some of the websites had the main text in different HTML locations like classes, but the majority could be found in the 'p' div so that what I focused on accessing. I also encountered an issue with paywalls, which blocked me off completely from obtaining the information for analysis. 
  
I eventually plan on analyzing multiple news sources at once, but that will require better filteration methods and a way to circumvent paywalls. For now, this code works on the list of news sources seen below.
  
So far I've described the how, but not the why. The USA is divided currently and I wanted to get a better understanding of the news sources which are a primary factor towards casuing this divide. I hoped that my analysis could shed some insight on whether or not these news sources are putting out positive or negative messages for their readers. The media is mosts only source of information which makes me think they should be completely objective and neurtal on what information they are presenting. I hope this code helps me get a better understanding of the state of mind that the media comapnies are currently in. 
  
main_websites = ['https://www.huffpost.com/', 'https://www.foxnews.com/','https://www.nbcnews.com/','https://www.dailymail.co.uk/ushome/index.html','https://www.theguardian.com/us','https://abcnews.go.com/','https://www.bbc.com/news']

## Most recent update 12/5/2021 10:41
First Project upload and completition
Updated folder format and directory
Uploaded final black jack code
Uploaded website sentiment analysis code 

