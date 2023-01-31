"""
#sudo apt install chromium-chromedriver
#sudo apt install python-pip
#!pip3 install selenium
#!pip3 install BeautifulSoup
#!pip3 install pandas
#!pip3 install numpy
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import sys

#For inserting the LeaderBoard Names in the List
def printName(name):
    i = 0
    for a in soup.findAll("div", attrs={'class': 'span-flex-4'}):
        if i>0:
            name.append(str(a.text).strip())
        i = i + 1
    #print(name)

#For inserting the LeaderBoard Scores in the List    
def printScore(score):
    i = 0
    for a in soup.findAll("div", attrs={'class': 'span-flex-3'}):
        if(i>=2 and i%2==0):
            score.append(str(a.text).strip())
        i = i + 1
    #print(score)

name1 = []
score1 = []
df1 = pd.DataFrame({'Name':name1,'Score':score1})

i =0
while(True):
    driver1 = webdriver.Chrome()
    
    driver1.get('https://www.hackerrank.com/contests/hexprac108/leaderboard/'+str(i))  
    content1 =driver1.page_source
    soup = BeautifulSoup(content1,features="html.parser")
    printName(name1)
    printScore(score1)
    i=i+1
    if(i==10):
        break

df1.to_csv('Excel_Sheet.csv',index=False,encoding="utf-8")
