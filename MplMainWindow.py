# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1105, 798)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mplCanvas = QtGui.QGraphicsView(self.centralwidget)
        self.mplCanvas.setGeometry(QtCore.QRect(20, 20, 651, 421))
        self.mplCanvas.setObjectName(_fromUtf8("mplCanvas"))
        self.textLeftBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textLeftBrowser.setGeometry(QtCore.QRect(20, 500, 321, 291))
        self.textLeftBrowser.setObjectName(_fromUtf8("textLeftBrowser"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(670, 20, 20, 771))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(920, 770, 161, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(700, 164, 72, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.IDEdit = QtGui.QLineEdit(self.centralwidget)
        self.IDEdit.setGeometry(QtCore.QRect(780, 170, 113, 21))
        self.IDEdit.setObjectName(_fromUtf8("IDEdit"))
        self.EAEdit = QtGui.QLineEdit(self.centralwidget)
        self.EAEdit.setGeometry(QtCore.QRect(780, 206, 113, 21))
        self.EAEdit.setObjectName(_fromUtf8("EAEdit"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 200, 72, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.EIEdit = QtGui.QLineEdit(self.centralwidget)
        self.EIEdit.setGeometry(QtCore.QRect(780, 246, 113, 21))
        self.EIEdit.setObjectName(_fromUtf8("EIEdit"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(700, 240, 72, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.StartEditX = QtGui.QLineEdit(self.centralwidget)
        self.StartEditX.setGeometry(QtCore.QRect(980, 170, 51, 21))
        self.StartEditX.setObjectName(_fromUtf8("StartEditX"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(900, 170, 72, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(900, 200, 72, 31))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(900, 240, 72, 31))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.AddBeamButton = QtGui.QPushButton(self.centralwidget)
        self.AddBeamButton.setGeometry(QtCore.QRect(870, 490, 81, 41))
        self.AddBeamButton.setObjectName(_fromUtf8("AddBeamButton"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 130, 72, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(690, 320, 401, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.WorldFreedomDegreeEdit = QtGui.QLineEdit(self.centralwidget)
        self.WorldFreedomDegreeEdit.setGeometry(QtCore.QRect(820, 63, 113, 21))
        self.WorldFreedomDegreeEdit.setObjectName(_fromUtf8("WorldFreedomDegreeEdit"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(700, 57, 111, 31))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(700, 23, 72, 31))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.GenerateButtom = QtGui.QPushButton(self.centralwidget)
        self.GenerateButtom.setGeometry(QtCore.QRect(960, 60, 111, 31))
        self.GenerateButtom.setObjectName(_fromUtf8("GenerateButtom"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(690, 100, 401, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(700, 380, 72, 31))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.ForceEdit = QtGui.QLineEdit(self.centralwidget)
        self.ForceEdit.setGeometry(QtCore.QRect(780, 386, 113, 21))
        self.ForceEdit.setObjectName(_fromUtf8("ForceEdit"))
        self.LocEdit = QtGui.QLineEdit(self.centralwidget)
        self.LocEdit.setGeometry(QtCore.QRect(980, 386, 113, 21))
        self.LocEdit.setObjectName(_fromUtf8("LocEdit"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(900, 380, 72, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(700, 420, 72, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.TypeEdit = QtGui.QLineEdit(self.centralwidget)
        self.TypeEdit.setGeometry(QtCore.QRect(780, 420, 113, 21))
        self.TypeEdit.setObjectName(_fromUtf8("TypeEdit"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(700, 290, 72, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.Solve = QtGui.QCommandLinkButton(self.centralwidget)
        self.Solve.setGeometry(QtCore.QRect(840, 570, 131, 41))
        self.Solve.setObjectName(_fromUtf8("Solve"))
        self.StartEditY = QtGui.QLineEdit(self.centralwidget)
        self.StartEditY.setGeometry(QtCore.QRect(1040, 170, 51, 21))
        self.StartEditY.setObjectName(_fromUtf8("StartEditY"))
        self.EndEditY = QtGui.QLineEdit(self.centralwidget)
        self.EndEditY.setGeometry(QtCore.QRect(1040, 210, 51, 21))
        self.EndEditY.setObjectName(_fromUtf8("EndEditY"))
        self.EndEditX = QtGui.QLineEdit(self.centralwidget)
        self.EndEditX.setGeometry(QtCore.QRect(980, 210, 51, 21))
        self.EndEditX.setObjectName(_fromUtf8("EndEditX"))
        self.L1 = QtGui.QSpinBox(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(760, 290, 31, 22))
        self.L1.setObjectName(_fromUtf8("L1"))
        self.L2 = QtGui.QSpinBox(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(800, 290, 31, 22))
        self.L2.setObjectName(_fromUtf8("L2"))
        self.L3 = QtGui.QSpinBox(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(840, 290, 31, 22))
        self.L3.setObjectName(_fromUtf8("L3"))
        self.L4 = QtGui.QSpinBox(self.centralwidget)
        self.L4.setGeometry(QtCore.QRect(880, 290, 31, 22))
        self.L4.setObjectName(_fromUtf8("L4"))
        self.L5 = QtGui.QSpinBox(self.centralwidget)
        self.L5.setGeometry(QtCore.QRect(920, 290, 31, 22))
        self.L5.setObjectName(_fromUtf8("L5"))
        self.L6 = QtGui.QSpinBox(self.centralwidget)
        self.L6.setGeometry(QtCore.QRect(960, 290, 31, 22))
        self.L6.setObjectName(_fromUtf8("L6"))
        self.mplCanvas2 = QtGui.QGraphicsView(self.centralwidget)
        self.mplCanvas2.setGeometry(QtCore.QRect(350, 500, 321, 291))
        self.mplCanvas2.setObjectName(_fromUtf8("mplCanvas2"))
        self.LocEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.LocEdit_2.setGeometry(QtCore.QRect(980, 250, 113, 21))
        self.LocEdit_2.setObjectName(_fromUtf8("LocEdit_2"))
        self.plusButton = QtGui.QPushButton(self.centralwidget)
        self.plusButton.setGeometry(QtCore.QRect(20, 450, 41, 28))
        self.plusButton.setObjectName(_fromUtf8("plusButton"))
        self.minusButton = QtGui.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(70, 450, 41, 28))
        self.minusButton.setObjectName(_fromUtf8("minusButton"))
        self.rightButton = QtGui.QPushButton(self.centralwidget)
        self.rightButton.setGeometry(QtCore.QRect(490, 450, 41, 28))
        self.rightButton.setObjectName(_fromUtf8("rightButton"))
        self.leftButton = QtGui.QPushButton(self.centralwidget)
        self.leftButton.setGeometry(QtCore.QRect(430, 450, 41, 28))
        self.leftButton.setObjectName(_fromUtf8("leftButton"))
        self.downButton = QtGui.QPushButton(self.centralwidget)
        self.downButton.setGeometry(QtCore.QRect(620, 450, 41, 28))
        self.downButton.setObjectName(_fromUtf8("downButton"))
        self.upButton = QtGui.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(560, 450, 41, 28))
        self.upButton.setObjectName(_fromUtf8("upButton"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(700, 470, 401, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.AddForce = QtGui.QPushButton(self.centralwidget)
        self.AddForce.setGeometry(QtCore.QRect(1010, 440, 81, 21))
        self.AddForce.setObjectName(_fromUtf8("AddForce"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(700, 340, 72, 31))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.BeamId = QtGui.QSpinBox(self.centralwidget)
        self.BeamId.setGeometry(QtCore.QRect(780, 340, 31, 31))
        self.BeamId.setObjectName(_fromUtf8("BeamId"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(700, 540, 401, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(700, 620, 401, 16))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.ShowButton = QtGui.QPushButton(self.centralwidget)
        self.ShowButton.setGeometry(QtCore.QRect(970, 670, 81, 31))
        self.ShowButton.setObjectName(_fromUtf8("ShowButton"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(740, 670, 72, 31))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.ShowEdit = QtGui.QLineEdit(self.centralwidget)
        self.ShowEdit.setGeometry(QtCore.QRect(820, 670, 113, 31))
        self.ShowEdit.setObjectName(_fromUtf8("ShowEdit"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LOL", None))
        self.textLeftBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Welcome to the my </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">structure mechanics calculator version 0.1!</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">All code is stored at github.com/n0lean.</span></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "DEMO1 Github:n0lean", None))
        self.label_2.setText(_translate("MainWindow", "ID", None))
        self.label_3.setText(_translate("MainWindow", "EA", None))
        self.label_4.setText(_translate("MainWindow", "EI", None))
        self.label_7.setText(_translate("MainWindow", "StartP", None))
        self.label_8.setText(_translate("MainWindow", "EndP", None))
        self.label_9.setText(_translate("MainWindow", "Mode", None))
        self.AddBeamButton.setText(_translate("MainWindow", "AddBeam", None))
        self.label_5.setText(_translate("MainWindow", "Beam", None))
        self.label_6.setText(_translate("MainWindow", "FreedomDegree", None))
        self.label_11.setText(_translate("MainWindow", "World", None))
        self.GenerateButtom.setText(_translate("MainWindow", "Generate", None))
        self.label_10.setText(_translate("MainWindow", "Force", None))
        self.label_12.setText(_translate("MainWindow", "Loc", None))
        self.label_13.setText(_translate("MainWindow", "Type", None))
        self.label_14.setText(_translate("MainWindow", "Lambda", None))
        self.Solve.setText(_translate("MainWindow", "Let\'s GO", None))
        self.plusButton.setText(_translate("MainWindow", "+", None))
        self.minusButton.setText(_translate("MainWindow", "-", None))
        self.rightButton.setText(_translate("MainWindow", "->", None))
        self.leftButton.setText(_translate("MainWindow", "<-", None))
        self.downButton.setText(_translate("MainWindow", "v", None))
        self.upButton.setText(_translate("MainWindow", "^", None))
        self.AddForce.setText(_translate("MainWindow", "AddForce", None))
        self.label_15.setText(_translate("MainWindow", "Beam", None))
        self.ShowButton.setText(_translate("MainWindow", "Show", None))
        self.label_16.setText(_translate("MainWindow", "ShowBeam", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
