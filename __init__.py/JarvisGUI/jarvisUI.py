# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JARVIS(object):
    def setupUi(self, JARVIS):
        JARVIS.setObjectName("JARVIS")
        JARVIS.resize(1297, 869)
        self.centralwidget = QtWidgets.QWidget(JARVIS)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1301, 841))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("JarvisGUI\\7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1030, 760, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1140, 760, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -50, 481, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("JarvisGUI\\Jarvis_Loading_Screen.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(760, 20, 256, 51))
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1030, 20, 256, 51))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"color:white;\n"
"font-size:20px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        JARVIS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JARVIS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1297, 26))
        self.menubar.setObjectName("menubar")
        JARVIS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JARVIS)
        self.statusbar.setObjectName("statusbar")
        JARVIS.setStatusBar(self.statusbar)

        self.retranslateUi(JARVIS)
        QtCore.QMetaObject.connectSlotsByName(JARVIS)

    def retranslateUi(self, JARVIS):
        _translate = QtCore.QCoreApplication.translate
        JARVIS.setWindowTitle(_translate("JARVIS", "MainWindow"))
        self.pushButton.setText(_translate("JARVIS", "RUN"))
        self.pushButton_2.setText(_translate("JARVIS", "TERMINATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JARVIS = QtWidgets.QMainWindow()
    ui = Ui_JARVIS()
    ui.setupUi(JARVIS)
    JARVIS.show()
    sys.exit(app.exec_())
