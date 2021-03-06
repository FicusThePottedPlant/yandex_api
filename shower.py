from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setGeometry(QtCore.QRect(10, 100, 781, 431))
        self.map.setText("")
        self.map.setScaledContents(False)
        self.map.setObjectName("map")
        self.enter = QtWidgets.QLineEdit(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(10, 10, 641, 31))
        self.enter.setClearButtonEnabled(True)
        self.enter.setObjectName("enter")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(660, 10, 131, 31))
        self.search.setObjectName("search")
        self.scheme = QtWidgets.QRadioButton(self.centralwidget)
        self.scheme.setGeometry(QtCore.QRect(240, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scheme.setFont(font)
        self.scheme.setObjectName("scheme")
        self.sattelite = QtWidgets.QRadioButton(self.centralwidget)
        self.sattelite.setGeometry(QtCore.QRect(330, 50, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sattelite.setFont(font)
        self.sattelite.setObjectName("sattelite")
        self.hybrid = QtWidgets.QRadioButton(self.centralwidget)
        self.hybrid.setGeometry(QtCore.QRect(440, 50, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hybrid.setFont(font)
        self.hybrid.setObjectName("hybrid")
        self.full_address = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.full_address.setGeometry(QtCore.QRect(20, 110, 291, 31))
        self.full_address.setReadOnly(True)
        self.full_address.setObjectName("full_address")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(10, 550, 141, 31))
        self.reset.setObjectName("reset")
        self.show_index = QtWidgets.QCheckBox(self.centralwidget)
        self.show_index.setGeometry(QtCore.QRect(580, 560, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.show_index.setFont(font)
        self.show_index.setChecked(True)
        self.show_index.setObjectName("show_index")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Показыватель карт 3000"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.scheme.setText(_translate("MainWindow", "Схема"))
        self.sattelite.setText(_translate("MainWindow", "Спутник"))
        self.hybrid.setText(_translate("MainWindow", "Гибрид"))
        self.reset.setText(_translate("MainWindow", "Сброс"))
        self.show_index.setText(_translate("MainWindow", "Показать почтовый индекс"))
