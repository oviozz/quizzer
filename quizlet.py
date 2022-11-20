
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from control_function import Functions
from PyQt5.QtWidgets import QFileDialog
import lxml

class Quizlet:
    def __init__(self, url):
        self._url = url


    def valid_url(self):
        if 'https://quizlet.com/' not in self._url or len(self._url) < 30:
            return False
        return True

    def scrape_content(self):

        headers = {
            "Sec-Ch-Ua": "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"99\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "close"
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


    def question_table(self, table, widget, placeholder):
        try:
            self.item_content = self.store_content()
            if self.valid_url():
                for row, (ques, ans) in enumerate(self.item_content.items()):
                    table.setRowCount(len(self.item_content))
                    table.setItem(row, 0, widget(ques))
                    table.setItem(row, 1, widget(ans))
            else:
                Functions().error_prompt(placeholder)
        except:
            Functions().error_prompt(placeholder)


    def download_data(self, file_url):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        pdf.cell(200, 10, txt="Quizzer Quizlet", ln=1, align='C')
        pdf.cell(200, 10, txt="Made by oviozz", ln=2, align='C')

        for row, (ques, ans) in enumerate(self.item_content.items()):
            pdf.cell(100, 10, txt=f'{ques}:  {ans}', ln=row + 1, align='A')

        pdf.output(f'{file_url[0]}.pdf', 'F')



