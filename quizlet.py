
import requests
from bs4 import BeautifulSoup

class Quizlet:
    def __init__(self, url):
        self._url = url

    def valid_url(self):
        if 'quizlet' not in self._url:
            return False
        return True

    def scrape_content(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip',
            'DNT': '1',  # Do Not Track Request Header
            'Connection': 'close'
        }

        grab_url = requests.get(self._url, headers=headers)
        soup = BeautifulSoup(grab_url.content, 'lxml')

        terms_table = soup.find_all('div', {'class': 'SetPageTerm-contentWrapper'})  # includes both question and answer
        question_table = soup.find_all('a', {'class': 'SetPageTerm-wordText'})

        self.question = [ques.text for ques in question_table]
        self.answer = [val.text.replace(repl, '').strip() for val, repl in zip(terms_table, self.question)]


    def store_content(self):

        self.scrape_content()
        self.terms_final = {}

        for ques, ans in zip(self.question, self.answer):
            self.terms_final[ques] = ans

        return self.terms_final
