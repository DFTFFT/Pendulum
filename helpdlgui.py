# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpdialog.ui'
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

class Ui_HelpDialog(QtGui.QDialog):
    """HelpDialog UI definition"""
    def __init__(self, parent=None):
        super(Ui_HelpDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, HelpDialog):
        HelpDialog.setObjectName(_fromUtf8("HelpDialog"))
        HelpDialog.resize(614, 756)
        self.frame = QtGui.QFrame(HelpDialog)
        self.frame.setGeometry(QtCore.QRect(20, 30, 571, 671))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 0, 131, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 40, 521, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(20, 60, 521, 591))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 431, 231))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 131, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 431, 121))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 440, 151, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(20, 460, 431, 81))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(40, 60, 431, 121))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(40, 30, 431, 441))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(HelpDialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 720, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(HelpDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(HelpDialog)

    def retranslateUi(self, HelpDialog):
        HelpDialog.setWindowTitle(_translate("HelpDialog", "Help", None))
        self.label.setText(_translate("HelpDialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Instructions</span></p></body></html>", None))
        self.label_2.setText(_translate("HelpDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Model</span></p></body></html>", None))
        self.label_3.setText(_translate("HelpDialog", "<html><head/><body><p>Pendulum (i=1,2)</p><p>Mi: mass of the sphere (kg)</p><p>mi: mass of the pole connected to the sphere (kg)</p><p>Li: length of the pole connected to the sphere (m)</p><p>hi: height of the vertical pole connected to the cart (m)</p><p>Cart</p><p>M: mass of the cart (kg)</p><p>L: horizontal distance between two vertical poles</p><p><br/></p></body></html>", None))
        self.label_4.setText(_translate("HelpDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initial condition</span></p></body></html>", None))
        self.label_5.setText(_translate("HelpDialog", "<html><head/><body><p>x: initial position of the cart (m)</p><p>thi: initial angle of the sphere (rad) (i=1,2)</p><p>vx: initial velocity of the cart (m/s)</p><p>wi: initial angular velocity of the sphere (rad/s) (i=1,2) </p></body></html>", None))
        self.label_6.setText(_translate("HelpDialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Time advancement</span></p></body></html>", None))
        self.label_7.setText(_translate("HelpDialog", "<html><head/><body><p>ts: start time (s)</p><p>te: end time (s)</p><p>tstep: time step (s)</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("HelpDialog", "Input Parameters", None))
        self.label_8.setText(_translate("HelpDialog", "<html><head/><body><p>x: initial position of the cart (m)</p><p>thi: initial angle of the sphere (rad) (i=1,2)</p><p>vx: initial velocity of the cart (m/s)</p><p>wi: initial angular velocity of the sphere (rad/s) (i=1,2) </p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("HelpDialog", "Output result", None))
        self.label_9.setText(_translate("HelpDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Export input</span>: save the current input parameters into an external file</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Import input</span>: read the input from the selected external file</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Initialize</span>: initialize the simulation after reading the input information</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Simulate</span>: start the solver engine and time advancement</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Reset</span>: reset the system back to the initial status</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Save result</span>: save the calculation results into the file</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Help</span>: prompt the help information</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">About</span>: prompt the author information</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Exit</span>: exit</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("HelpDialog", "Toolbar Button", None))
        self.pushButton.setText(_translate("HelpDialog", "OK", None))

    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_clicked(self):
        self.close()