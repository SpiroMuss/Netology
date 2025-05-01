from task_1 import logger
from datetime import datetime, timedelta

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import TimeoutException
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

keywords = ['дизайн', 'фото', 'web', 'python']

@logger
def start_browser():
    chrome_path = ChromeDriverManager().install()
    service = Service(executable_path=chrome_path)
    options = ChromeOptions()
    options.add_argument('--headless')
    return Chrome(service=service, options=options)

@logger
def article_dict(a, b, c):
    return {
        'datetime': a,
        'title': b,
        'link': c
    }


if __name__ == '__main__':

    browser = start_browser()
    browser.get('https://habr.com/ru/articles/')
    articles = browser.find_elements(by=By.CLASS_NAME, value='tm-articles-list__item')
    article_info = []

    for article in articles:
        flag = 0

        date_element = article.find_element(By.TAG_NAME, 'time')
        date = datetime.fromisoformat(date_element.get_attribute('datetime').replace('Z', '')) + timedelta(hours=3)

        header = article.find_element(By.CLASS_NAME, 'tm-title__link')
        title = header.text
        link = header.get_attribute('href')

        tags = article.find_elements(By.CLASS_NAME, 'tm-publication-hub__link')

        for tag in tags:
            if any(tag.text.lower().find(x) != -1 for x in keywords):
                article_info.append(article_dict(str(date), title, link))
                flag = 1
                break

        if flag == 0:
            if any(title.lower().find(x) != -1 for x in keywords):
                article_info.append(article_dict(str(date), title, link))
                flag = 1

        if flag == 0:
            content = article.find_elements(By.CLASS_NAME, 'article-formatted-body')
            for block in content:
                if any(block.text.lower().find(x) != -1 for x in keywords):
                    article_info.append(article_dict(str(date), title, link))
                    break

    for article in article_info:
        print(f'{article['datetime']} - {article['title']} - {article['link']}')
