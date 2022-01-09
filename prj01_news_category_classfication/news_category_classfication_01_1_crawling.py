# -*- coding: utf-8 -*-
"""prj01_news_category_classfication_01_1_crawling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HW-j_v0eKn1FgyhwQyMSDS7n5xsBBUSr
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime

print(datetime.datetime.today().strftime('%Y%m%d'))
category = ['Politics', 'Economic', 'Social', 'Culture',
            'World', 'IT']

# url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
# resp = requests.get(url, headers=headers)

# print(list(resp))

# print(type(resp))

# soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)
#
# title_tags = soup.select('.cluster_text_headline')
# print(title_tags)
# print(type(title_tags[0]))
#
# titles = []
# for title_tag in title_tags:
#     titles.append(re.compile('[^가-힣|a-z|A-Z ]').sub(' ', title_tag.text))
# print(titles)
# print(len(titles))
#
# pd.set_option('display.unicode.east_asian_width', True)

df_titles = pd.DataFrame()
re_title = re.compile('[^가-힣|a-z|A-Z ]')

for i in range(6):
    resp = requests.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{}'.format(i), headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    title_tags = soup.select('.cluster_text_headline')
    titles = []
    for title_tag in title_tags:
        titles.append(re_title.sub(' ', title_tag.text))
    df_section_titles = pd.DataFrame(titles, columns=['title'])
    df_section_titles['category'] = category[i]
    df_titles = pd.concat([df_titles, df_section_titles],
                axis='rows', ignore_index=True)
    print('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10%d'%(i))
print(df_titles.head())
print(df_titles.info())
print(df_titles['category'].value_counts())

print(df_titles.head())

df_titles.to_csv('./crawling/naver_headline_news{}.csv'.format(
    datetime.datetime.today().strftime('%Y%m%d')))