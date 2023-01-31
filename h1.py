!pip install selenium
!pip install BeautifulSoup
!pip install pandas
!pip install numpy

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import sys
import matplotlib.pyplot as plt
#For inserting the LeaderBoard Names in the List
def printName(name):
    i = 0
    for a in soup.findAll("div", attrs={'class': 'span-flex-4'}):
        if i>0:
            name.append(str(a.text).strip())
        i = i + 1
    print(name)

#For inserting the LeaderBoard Scores in the List    
def printScore(score):
    i = 0
    for a in soup.findAll("div", attrs={'class': 'span-flex-3'}):
        if(i>=2 and i%2==0):
            score.append(str(a.text).strip())
        i = i + 1
    print(score)

driver1 = webdriver.Chrome()
name1 = []
score1 = []
driver1.get('https://www.hackerrank.com/contests/scanit-weekly-contest-23-aug-2020/leaderboard')  #Link of the Particular Site (LeaderBoard 1)
content1 =driver1.page_source
soup = BeautifulSoup(content1,features="html.parser")
printName(name1)
printScore(score1)
df1 = pd.DataFrame({'Name':name1,'Score':score1})


driver2 = webdriver.Chrome()
name2 = []
score2 = []
driver2.get('https://www.hackerrank.com/contests/scanit-weekly-contest-23-aug-2020/leaderboard/2')  #Link of the Particular Site (LeaderBoard 2)
content2 = driver2.page_source
soup = BeautifulSoup(content2,features="html.parser")
printName(name2)
printScore(score2)
df2 = pd.DataFrame({'Name':name2,'Score':score2})
df1 = df1.append(df2, ignore_index=True)

driver3 = webdriver.Chrome()
name3 = []
score3 = []
driver3.get('https://www.hackerrank.com/contests/scanit-weekly-contest-23-aug-2020/leaderboard/3') #Link of the Particular Site (LeaderBoard 3) which is in the Link
content3 =driver3.page_source
soup = BeautifulSoup(content3,features="html.parser")
printName(name3)
printScore(score3)
df3 = pd.DataFrame({'Name':name3,'Score':score3})

df1 = df1.append(df3, ignore_index=True)

df1.to_csv('Excel_Sheet.csv',index=False,encoding="utf-8") 
