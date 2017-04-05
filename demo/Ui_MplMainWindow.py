# -*- coding: utf-8 -*-



# Form implementation generated from reading ui file 'MplMainWindow.ui'

#

# Created: Mon Aug 11 14:18:31 2014

#      by: PyQt4 UI code generator 4.10.3

#

# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui

from mplCanvasWrapper import MplCanvasWrapper

try:

    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    def _fromUtf8(s):

        return s

try:

    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig)


# inheritent from QtGui.QMainWindow

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))

        MainWindow.resize(690, 427)

        self.centralWidget = QtGui.QWidget(MainWindow)

        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        self.gridLayout = QtGui.QGridLayout(self.centralWidget)

        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.horizontalLayout = QtGui.QHBoxLayout()

        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.btnStart = QtGui.QPushButton(self.centralWidget)

        self.btnStart.setObjectName(_fromUtf8("btnStart"))

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnPause = QtGui.QPushButton(self.centralWidget)

        self.btnPause.setObjectName(_fromUtf8("btnPause"))

        self.horizontalLayout.addWidget(self.btnPause)

        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.mplCanvas = MplCanvasWrapper(self.centralWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        sizePolicy.setHorizontalStretch(0)

        sizePolicy.setVerticalStretch(0)

        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())

        self.mplCanvas.setSizePolicy(sizePolicy)

        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))

        self.gridLayout.addWidget(self.mplCanvas, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

        self.btnStart.setText(_translate("MainWindow", "开始", None))

        self.btnPause.setText(_translate("MainWindow", "暂停", None))