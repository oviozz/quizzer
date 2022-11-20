
from PyQt5 import QtCore, QtGui, QtWidgets
from control_function import Functions
from functools import partial
from quizlet import Quizlet
from flashcard import Flashcards
from learn import Learn
from PyQt5.QtWidgets import QFileDialog
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 756)#(778, 756)
        MainWindow.setStyleSheet("background-color: rgb(31, 29, 43);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SwitchScreen = QtWidgets.QTabWidget(self.centralwidget)
        self.SwitchScreen.setGeometry(QtCore.QRect(-10, -30, 1081, 831))
        self.SwitchScreen.setStyleSheet("background-color: rgb(31, 29, 43);")
        self.SwitchScreen.setObjectName("SwitchScreen")
        self.search_screen = QtWidgets.QWidget()
        self.search_screen.setObjectName("search_screen")
        self.url_search = QtWidgets.QLineEdit(self.search_screen)
        self.url_search.setEnabled(True)
        self.url_search.setGeometry(QtCore.QRect(50, 30, 721, 41))
        self.url_search.setAutoFillBackground(False)
        self.url_search.setStyleSheet("background-color: rgb(45, 48, 62);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Century Gothic\";\n"
"border: 2px rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"")
        self.url_search.setText("")
        self.url_search.setCursorPosition(0)
        self.url_search.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.url_search.setObjectName("url_search")
        self.search_icon = QtWidgets.QLabel(self.search_screen)
        self.search_icon.setGeometry(QtCore.QRect(20, 30, 41, 41))
        self.search_icon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_icon.setStyleSheet("background-color: rgb(45, 48, 62);\n"
"border: 2px rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.search_icon.setText("")
        self.search_icon.setPixmap(QtGui.QPixmap("icons/search_bar_icon.png"))
        self.search_icon.setObjectName("search_icon")
        self.search_button = QtWidgets.QPushButton(self.search_screen)
        self.search_button.setGeometry(QtCore.QRect(730, 30, 41, 41))
        self.search_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.search_button.setStyleSheet("    background-color: rgb(45, 48, 62);\n"
"    color: White;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(96, 166, 235);\n"
"")
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/submit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setObjectName("search_button")
        self.question_answer_table = QtWidgets.QTableWidget(self.search_screen)
        self.question_answer_table.setGeometry(QtCore.QRect(20, 90, 751, 601))
        self.question_answer_table.setStyleSheet("""QHeaderView::section {background-color: rgb(31, 29, 43);

color: rgb(255, 255, 255);
	font: 12pt "Century Gothic";
    border: none;

}

QHeaderView{
	color: rgb(255, 255, 255);
    background-color:  rgb(45, 48, 62);
	font: 12pt "Century Gothic";
    border: none;
}
QTableView { 
	color: rgb(255, 255, 255);
	background: rgb(45, 48, 62);
	font: 12pt "Century Gothic";
	border: none;
 }

QTableCornerButton::section {
	color: rgb(255, 255, 255);
 	background-color: rgb(31, 29, 43); 
	font: 12pt "Century Gothic";

}

 QScrollBar:vertical {
	border: none;
    background: rgb(45, 45, 68);
    width: 14px;
    margin: 15px 0 15px 0;
	border-radius: 0px;
 }

/*  HANDLE BAR VERTICAL */
QScrollBar::handle:vertical {	
	background-color: rgb(80, 80, 122);
	min-height: 30px;
	border-radius: 7px;
}
QScrollBar::handle:vertical:hover{	
	background-color: rgb(80, 80, 122);
}
QScrollBar::handle:vertical:pressed {	
	background-color: rgb(80, 80, 122);
}

/* BTN TOP - SCROLLBAR */
QScrollBar::sub-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-top-left-radius: 7px;
	border-top-right-radius: 7px;
	subcontrol-position: top;
	subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical:hover {	
	background-color: rgb(80, 80, 122);
}
QScrollBar::sub-line:vertical:pressed {	
	background-color:rgb(80, 80, 122);
}

/* BTN BOTTOM - SCROLLBAR */
QScrollBar::add-line:vertical {
	border: none;
	background-color: rgb(59, 59, 90);
	height: 15px;
	border-bottom-left-radius: 7px;
	border-bottom-right-radius: 7px;
	subcontrol-position: bottom;
	subcontrol-origin: margin;
}
QScrollBar::add-line:vertical:hover {	
	background-color: rgb(80, 80, 122);
}
QScrollBar::add-line:vertical:pressed {	
	background-color: rgb(80, 80, 122);
}

/* RESET ARROW */
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
}
""")
        self.question_answer_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded) #QtCore.Qt.ScrollBarAsNeeded
        self.question_answer_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff) #QtCore.Qt.ScrollBarAlwaysOff

        self.question_answer_table.setGridStyle(QtCore.Qt.SolidLine)
        self.question_answer_table.setObjectName("question_answer_table")
        self.question_answer_table.setColumnCount(2)
        self.question_answer_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.question_answer_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.question_answer_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.question_answer_table.setHorizontalHeaderItem(1, item)

        self.question_answer_table.setColumnWidth(0, 368)
        self.question_answer_table.setColumnWidth(1, 366)

        self.question_answer_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection) # disable selecting
        self.question_answer_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.question_answer_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) # disable editing
        self.question_answer_table.setFocusPolicy(QtCore.Qt.NoFocus) # disable selection

        self.learn_button = QtWidgets.QPushButton(self.search_screen)
        self.learn_button.setGeometry(QtCore.QRect(40, 700, 131, 41))
        self.learn_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 48, 62);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: 75 15pt \"Century Gothic\";\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(46, 56, 86);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(68, 73, 94);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/learn icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.learn_button.setIcon(icon1)
        self.learn_button.setIconSize(QtCore.QSize(50, 50))
        self.learn_button.setObjectName("learn_button")
        self.flashcard_button = QtWidgets.QPushButton(self.search_screen)
        self.flashcard_button.setGeometry(QtCore.QRect(200, 700, 161, 41))
        self.flashcard_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 48, 62);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: 75 15pt \"Century Gothic\";\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(46, 56, 86);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(68, 73, 94);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/flashcard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flashcard_button.setIcon(icon2)
        self.flashcard_button.setIconSize(QtCore.QSize(50, 50))
        self.flashcard_button.setObjectName("flashcard_button")
        self.download_button = QtWidgets.QPushButton(self.search_screen)
        self.download_button.setGeometry(QtCore.QRect(390, 700, 171, 41))
        self.download_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 48, 62);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: 75 15pt \"Century Gothic\";\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(46, 56, 86);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(68, 73, 94);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/download_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.download_button.setIcon(icon3)
        self.download_button.setIconSize(QtCore.QSize(50, 50))
        self.download_button.setObjectName("download_button")
        self.exit_button = QtWidgets.QPushButton(self.search_screen)
        self.exit_button.setGeometry(QtCore.QRect(590, 700, 131, 41))
        self.exit_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(45, 48, 62);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: 75 15pt \"Century Gothic\";\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(46, 56, 86);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(68, 73, 94);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/exit_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon4)
        self.exit_button.setIconSize(QtCore.QSize(40, 40))
        self.exit_button.setObjectName("exit_button")
        self.search_icon.raise_()
        self.url_search.raise_()
        self.search_button.raise_()
        self.question_answer_table.raise_()
        self.learn_button.raise_()
        self.flashcard_button.raise_()
        self.download_button.raise_()
        self.exit_button.raise_()
        self.SwitchScreen.addTab(self.search_screen, "")
        self.learn_screen = QtWidgets.QWidget()
        self.learn_screen.setObjectName("learn_screen")
        self.learn_question_display = QtWidgets.QLabel(self.learn_screen)
        self.learn_question_display.setGeometry(QtCore.QRect(50, 40, 701, 371))
        self.learn_question_display.setAutoFillBackground(False)
        self.learn_question_display.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Century Gothic\";")
        self.learn_question_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.learn_question_display.setScaledContents(False)
        self.learn_question_display.setWordWrap(True)
        self.learn_question_display.setObjectName("learn_question_display")
        self.learn_question_display.setAlignment(QtCore.Qt.AlignCenter)
        self.option1 = QtWidgets.QPushButton(self.learn_screen)
        self.option1.setGeometry(QtCore.QRect(90, 440, 631, 61))
        self.option1.setStyleSheet("QPushButton {\n"
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
        self.option1.setObjectName("option1")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.option1)
        self.option2 = QtWidgets.QPushButton(self.learn_screen)
        self.option2.setGeometry(QtCore.QRect(90, 520, 631, 61))
        self.option2.setStyleSheet("QPushButton {\n"
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
        self.option2.setObjectName("option2")
        self.buttonGroup.addButton(self.option2)
        self.option3 = QtWidgets.QPushButton(self.learn_screen)
        self.option3.setGeometry(QtCore.QRect(90, 600, 631, 61))
        self.option3.setStyleSheet("QPushButton {\n"
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
        self.option3.setObjectName("option3")
        self.buttonGroup.addButton(self.option3)
        self.option4 = QtWidgets.QPushButton(self.learn_screen)
        self.option4.setGeometry(QtCore.QRect(90, 680, 631, 61))
        self.option4.setStyleSheet("QPushButton {\n"
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
        self.option4.setObjectName("option4")
        self.buttonGroup.addButton(self.option4)
        self.learn_counter = QtWidgets.QLabel(self.learn_screen)
        self.learn_counter.setGeometry(QtCore.QRect(40, 10, 721, 31))
        self.learn_counter.setStyleSheet("font: 12pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")
        self.learn_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.learn_counter.setObjectName("learn_counter")
        self.learn_home_button = QtWidgets.QPushButton(self.learn_screen)
        self.learn_home_button.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.learn_home_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.learn_home_button.setStyleSheet("    background-color: rgb(31, 29, 43);\n"
                                       "    color: White;\n"
                                       "    padding: 2px;\n"
                                       "    font: bold 20px;\n"
                                       "    border-width: 6px;\n"
                                       "    border-radius: 5px;\n"
                                       "    border-color: rgb(96, 166, 235);\n"
                                       "")
        self.learn_home_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/home_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.learn_home_button.setIcon(icon5)
        self.learn_home_button.setIconSize(QtCore.QSize(40, 40))
        self.learn_home_button.setObjectName("learn_home_button")


        self.SwitchScreen.addTab(self.learn_screen, "")
        self.flashcard_screen = QtWidgets.QWidget()
        self.flashcard_screen.setObjectName("flashcard_screen")
        self.flash_card_back = QtWidgets.QPushButton(self.flashcard_screen)
        self.flash_card_back.setGeometry(QtCore.QRect(80, 600, 251, 61))
        self.flash_card_back.setStyleSheet("QPushButton {\n"
"    background-color: rgb(46, 56, 86);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(46, 56, 86);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(70, 85, 131);\n"
"}")
        self.flash_card_back.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/arrow_left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flash_card_back.setIcon(icon6)
        self.flash_card_back.setIconSize(QtCore.QSize(100, 100))
        self.flash_card_back.setAutoDefault(False)
        self.flash_card_back.setDefault(False)
        self.flash_card_back.setFlat(False)
        self.flash_card_back.setObjectName("flash_card_back")
        self.flash_card_foward = QtWidgets.QPushButton(self.flashcard_screen)
        self.flash_card_foward.setGeometry(QtCore.QRect(450, 600, 251, 61))
        self.flash_card_foward.setStyleSheet("QPushButton {\n"
"    background-color: rgb(46, 56, 86);\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(46, 56, 86);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(70, 85, 131);\n"
"}")
        self.flash_card_foward.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/arrow_right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flash_card_foward.setIcon(icon7)
        self.flash_card_foward.setIconSize(QtCore.QSize(100, 100))
        self.flash_card_foward.setObjectName("flash_card_foward")
        self.flashcard_questions = QtWidgets.QLabel(self.flashcard_screen)
        self.flashcard_questions.setGeometry(QtCore.QRect(50, 60, 701, 421))
        self.flashcard_questions.setAutoFillBackground(False)
        self.flashcard_questions.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Century Gothic\";")
        self.flashcard_questions.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.flashcard_questions.setScaledContents(False)
        self.flashcard_questions.setWordWrap(True)
        self.flashcard_questions.setAlignment(QtCore.Qt.AlignCenter)
        self.flashcard_questions.setObjectName("flashcard_questions")
        self.flashcard_answer_button = QtWidgets.QPushButton(self.flashcard_screen)
        self.flashcard_answer_button.setGeometry(QtCore.QRect(40, 490, 721, 31))
        self.flashcard_answer_button.setStyleSheet("QPushButton {\n"
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
        self.flashcard_answer_button.setObjectName("flashcard_answer_button")
        self.flashcard_counter = QtWidgets.QLabel(self.flashcard_screen)
        self.flashcard_counter.setGeometry(QtCore.QRect(40, 20, 721, 31))
        self.flashcard_counter.setStyleSheet("font: 12pt \"Century Gothic\";\n"
"color: rgb(255, 255, 255);")
        self.flashcard_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.flashcard_counter.setObjectName("flashcard_counter")

        self.flashcard_home_button = QtWidgets.QPushButton(self.flashcard_screen)
        self.flashcard_home_button.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.flashcard_home_button.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.flashcard_home_button.setStyleSheet("    background-color: rgb(31, 29, 43);\n"
                                         "    color: White;\n"
                                         "    padding: 2px;\n"
                                         "    font: bold 20px;\n"
                                         "    border-width: 6px;\n"
                                         "    border-radius: 5px;\n"
                                         "    border-color: rgb(96, 166, 235);\n"
                                         "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/home_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flashcard_home_button.setText("")
        self.flashcard_home_button.setIcon(icon8)
        self.flashcard_home_button.setIconSize(QtCore.QSize(40, 40))
        self.flashcard_home_button.setObjectName("flashcard_home_button")


        self.SwitchScreen.addTab(self.flashcard_screen, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.SwitchScreen.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.search_button.clicked.connect(lambda x: self.insert_table_content())

        # navigates through learn and flashcard screen
        self.learn_button.clicked.connect(partial(self.navigate_screen, 'learn'))
        self.flashcard_button.clicked.connect(partial(self.navigate_screen, 'flashcard'))
        self.download_button.clicked.connect(lambda x: self.download())

        self.learn_home_button.clicked.connect(partial(self.home, 'learn'))
        self.flashcard_home_button.clicked.connect(partial(self.home, 'flashcard'))

        self.flash_card_back.clicked.connect(partial(self.flash_card, 'back'))
        self.flash_card_foward.clicked.connect(partial(self.flash_card, 'forward'))
        self.flashcard_answer_button.clicked.connect(lambda x: self.flash_card_reveal())


        self.option1.clicked.connect(partial(self.learn_buttons, 0))
        self.option2.clicked.connect(partial(self.learn_buttons, 1))
        self.option3.clicked.connect(partial(self.learn_buttons, 2))
        self.option4.clicked.connect(partial(self.learn_buttons, 3))


        self.exit_button.clicked.connect(lambda x: sys.exit())


        self.is_valid = False
        self.data_collected = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quizzer"))
        self.url_search.setPlaceholderText(_translate("MainWindow", " Paste your link here"))
        item = self.question_answer_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.question_answer_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Question"))
        item = self.question_answer_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Answer"))
        self.learn_button.setText(_translate("MainWindow", "Learn"))
        self.flashcard_button.setText(_translate("MainWindow", "Flashcards"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.exit_button.setText(_translate("MainWindow", "EXIT"))
        self.SwitchScreen.setTabText(self.SwitchScreen.indexOf(self.search_screen), _translate("MainWindow", "Tab 1"))
        self.learn_question_display.setText(_translate("MainWindow", "Hello Word"))
        self.option1.setText(_translate("MainWindow", "Option 1"))
        self.option2.setText(_translate("MainWindow", "Option 2"))
        self.option3.setText(_translate("MainWindow", "Option 3"))
        self.option4.setText(_translate("MainWindow", "Option 4"))
        self.learn_counter.setText(_translate("MainWindow", "0/100"))
        self.SwitchScreen.setTabText(self.SwitchScreen.indexOf(self.learn_screen), _translate("MainWindow", "Tab 2"))
        self.flashcard_questions.setText(_translate("MainWindow", "Hello World"))
        self.flashcard_answer_button.setText(_translate("MainWindow", "Answer"))
        self.flashcard_counter.setText(_translate("MainWindow", "0/100"))
        self.SwitchScreen.setTabText(self.SwitchScreen.indexOf(self.flashcard_screen), _translate("MainWindow", "Page"))


    def insert_table_content(self):
        self.content = Quizlet(self.url_search.text())
        self.is_valid = self.content.valid_url()
        self.content.question_table(self.question_answer_table, QtWidgets.QTableWidgetItem, self.url_search)
        self.data_collected = True

    def navigate_screen(self, location):
        if self.data_collected:
            if location == 'flashcard':
                self.flash_cards = Flashcards(self.content.terms_final, self.flashcard_questions, self.flashcard_counter)# pre-loads the content
            elif location == 'learn':
                self.learn = Learn(self.content.terms_final, self.learn_question_display, self.learn_counter)
                self.learn.display_options(self.option1, self.option2, self.option3, self.option4)
        Functions().switch_to_learn(self.SwitchScreen, location, self.url_search, self.is_valid, self.flash_card)


    def home(self, tab_home):
        if tab_home == 'learn':
            self.learn.return_home(self.option1, self.option2, self.option3, self.option4)
        elif tab_home == 'flashcard':
            self.flash_cards.return_home(self.flashcard_counter)
        Functions().return_home(self.SwitchScreen)


    def flash_card(self, previous_next):
        self.flash_cards.back_next(self.flashcard_questions, previous_next, self.flashcard_counter)

    def flash_card_reveal(self):
        self.flash_cards.reveal_answer(self.flashcard_questions)


    def learn_buttons(self, options):
        btn_clicked = [self.option1, self.option2, self.option3, self.option4]
        self.learn.answer_check(btn_clicked[options], self.learn_question_display, self.learn_counter, self.SwitchScreen, self.option1, self.option2, self.option3, self.option4)


    def download(self):
        if self.data_collected:
            filename = QFileDialog.getSaveFileName(None, 'Save Quizlet File', os.getenv('HOME'))
            self.content.download_data(filename)
        else:
            return Functions().error_prompt(self.url_search)


# BUG FIX: When we search "a"(any text that doesn't go through) and try to switch screen it crashes
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


