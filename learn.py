
import random
from PyQt5 import QtCore

class Learn:
    track = 0 # counter to # of items

    def __init__(self, content, display, counter):
        self.content = content
        self.questions = [list(content)[index] for index in random.sample(range(0, len(list(content))), len(list(content)))]

        display.setText(self.questions[Learn.track])
        counter.setText(f'{Learn.track}/{len(self.questions) - 1}')

    def insert_range(self):
        return random.randint(0, 3)

    def answer(self):
        self.reveal = self.content.get(self.questions[Learn.track])
        return self.reveal

    def question_options(self): # self.content.get(word) for word in random.sample(self.questions, 4)
        self.options = [self.content.get(word) for word in random.sample(self.questions, 4)]
        answer = self.answer()

        if answer not in self.options:
            self.options.pop()
            self.options.insert(self.insert_range(), answer)
        else:
            self.options.remove(answer)
            self.options.insert(self.insert_range(), answer)

        return self.options

    def display_options(self, *args):
        self.buttons = args
        self.answer_options = self.question_options()
        for index, btn in enumerate(self.buttons):
            btn.setText(str(self.answer_options[index]))


    def answer_check(self, button_clicked, question_display,counter, home_screen, *args):
        if button_clicked.text() == self.answer():
            button_clicked.setStyleSheet("QPushButton {\n"
                                              "    background-color: rgb(72, 191, 83);\n"
                                              "    color: #FFFFFF;\n"
                                              "    padding: 2px;\n"
                                              "    font: 75 15pt \"Century Gothic\";\n"
                                              "    border-width: 6px;\n"
                                              "    border-radius: 5px;\n"
                                              "    border-color: rgb(72, 191, 83);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(72, 191, 83);\n"
                                              "}")

            loop = QtCore.QEventLoop()
            disable = [button.setEnabled(False) for button in args]
            QtCore.QTimer.singleShot(200, loop.quit)
            enable = [button.setDisabled(False) for button in args]
            loop.exec_()

            Learn.track += 1
            self.question_ranout(home_screen)
            counter.setText(f'{Learn.track}/{len(self.questions) - 1}')
            question_display.setText(self.questions[Learn.track])
            self.display_options(*args)
            self.button_color(*args)



        else:
            button_clicked.setStyleSheet("QPushButton {\n"
                                              "    background-color: rgb(225, 0, 0);\n"
                                              "    color: #FFFFFF;\n"
                                              "    padding: 2px;\n"
                                              "    font: 75 15pt \"Century Gothic\";\n"
                                              "    border-width: 6px;\n"
                                              "    border-radius: 5px;\n"
                                              "    border-color: rgb(225, 0, 0);\n"
                                              "}\n"
                                              "QPushButton:hover {\n"
                                              "    background-color: rgb(225, 0, 0);\n"
                                              "}")


    def button_color(self, *buttons):
        for btn in buttons:
            btn.setStyleSheet("QPushButton {\n"
                               "    background-color: rgb(90, 109, 168);\n"
                               "    color: #FFFFFF;\n"
                               "    padding: 2px;\n"
                               "    font: 75 15pt \"Century Gothic\";\n"
                               "    border-width: 6px;\n"
                               "    border-radius: 5px;\n"
                               "    border-color: rgb(46, 56, 86);\n"
                               "}\n"
                               "QPushButton:hover {\n"
                               "    background-color: rgb(70, 85, 131);\n"
                               "}")


    def question_ranout(self, switch):
        if Learn.track > len(self.questions) - 1:
            switch.setCurrentIndex(0)
            Learn.track = 0
            return


    def return_home(self, *args):
        Learn.track = 0
        return self.button_color(*args)


