import re
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_movies(link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.116 Safari/537.36 '

    }
    movie_names = []
    movie_types = []
    movie_dis = []
    movie_grade = []
    movie_addr = []
    movie_actor = []
    movie_director = []
    movie_year = []
    r = requests.get(link, headers=headers, timeout=10)
    soup = BeautifulSoup(r.text, "lxml")

    for each in soup.find_all('div', class_='abstract'):
        a = each.text

        tp = re.search(r'类型: (.*)', a)
        if tp == None:
            movie_types.append(" ")
        else:
            movie_types.append(tp.group(1))
        actor = re.search(r'主演: (.*)', a)
        if actor == None:
            movie_actor.append(" ")
        else:
            movie_actor.append(actor.group(1))
        director = re.search(r'导演: (.*)', a)
        if director == None:
            movie_director.append(" ")
        else:
            movie_director.append(director.group(1))
        addr = re.search(r'制片国家/地区: (.*)', a)
        if addr == None:
            movie_addr.append(" ")
        else:
            movie_addr.append(addr.group(1))
        year = re.search(r'年份: (.*)', a)
        if year == None:
            movie_year.append(" ")
        else:
            year_str = year.group(1)
            sj = int(year_str[:2]) + 1
            nd = year_str[2] + '0'
            movie_year.append(str(sj) + '世纪' + nd + '年代')
    # 查询所有class=title的div
    div_list = soup.find_all('div', class_='title')
    for each in div_list:
        movie_name = each.a.text.strip()
        movie_names.append(movie_name)
    for each in soup.find_all('div', class_='rating'):
        a = each.text.split('\n')
        # 获取字符串中的数字
        x = re.sub("\D", "", a[3])
        movie_dis.append(int(x))
        movie_grade.append(float(a[2]))
    return movie_names, movie_types, movie_dis, movie_grade, movie_addr, movie_actor, movie_director, movie_year

movies=get_movies("https://www.douban.com/doulist/240962/")
movies_1=pd.DataFrame({'电影名称':movies[0],'电影类型':movies[1],'导演':movies[6],'主演':movies[5],'评价人数':movies[2],'评分':movies[3],'国家/地区':movies[4],'年代':movies[7]})
for i in range(1,30):

    link="https://www.douban.com/doulist/240962/?start="+str(i*25)
    movies=get_movies(link)
    movies_1=movies_1.append(pd.DataFrame({'电影名称':movies[0],'电影类型':movies[1],'导演':movies[6],'主演':movies[5],'评价人数':movies[2],'评分':movies[3],'国家/地区':movies[4],'年代':movies[7]}),ignore_index=True)
all_movies=movies_1


all_movies.to_excel(r'C:\Users\Administrator\Desktop\豆瓣数据.xlsx')
