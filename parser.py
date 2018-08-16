__author__ = 'Nick Terskikh'
# -*- coding: utf-8 -*-
# 09.08.2018

import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data_items(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('a', {'class' : 'link link_outer_yes link_theme_outer path__item i-bem'})
    # return [a.get('href') for a in items]
    for a in items:
        href_soup = a.get('href')
        data = {'url': a,
                'href': href_soup}
        write_data_csv(data)


def write_data_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['url']))


def main():
    url = 'https://yandex.ru/search/?clid=9582&text=скачать&lr=118890&p=1'
    print(url)
    print(get_data_items(get_html(url)))


if __name__ == '__main__':
    main()
