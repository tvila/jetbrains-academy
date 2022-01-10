import requests

from bs4 import BeautifulSoup

import string

import os

num_pages, type_article = int(input()), str(input())
url_master = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page='

def web_scrapper(url, type, num_pages):
    # CREATE DIRS
    for i in range(num_pages):
        dirs = 'Page_' + str(i + 1)
        owd = os.getcwd()
        os.mkdir(dirs)
        os.chdir(dirs)
        url_page = url + str(i + 1)
        print(url_page)

        # GET URLS
        response = requests.get(url_page, headers={'Accept-Language': 'en-US,en;q=0.5'})
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')

        # BROWSING ARTICLES
        for article in articles:
            if article.find('span', {'class': 'c-meta__type'}).text == type:
                title = article.find('h3')
                ref = title.find('a')

                # Article Content
                article_url = 'https://www.nature.com' + ref.get('href')
                r = requests.get(article_url)
                art_soup = BeautifulSoup(r.content, 'html.parser')

                try:
                    content = art_soup.find('div', {'class': 'article__body cleared'}).text.strip()

                except:
                    content = art_soup.find('div', {'class': 'article-item__body'}).text.strip()

                ## Rename & create files
                file_name = title.text

                ### Avoid punctuation symbols
                symbols = list(string.punctuation)
                for i in symbols:
                    file_name = file_name.replace(i, "")
                file_name = file_name.strip().replace(" ", "_") + '.txt'

                ### Saving articles
                art_file = open(file_name, 'w', encoding='UTF-8')
                print(f'File "{file_name}" saved!')

                art_file.write(content)
                art_file.close()

        # RESET DIR
        os.chdir(owd)

    print('Saved all articles.')

