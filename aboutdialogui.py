# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog.ui'
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

class Ui_AboutDialog(QtGui.QDialog):
    """AboutDialog UI definition"""
    def __init__(self, parent=None):
        super(Ui_AboutDialog, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName(_fromUtf8("AboutDialog"))
        AboutDialog.resize(406, 243)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 251, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(AboutDialog)
        self.frame.setGeometry(QtCore.QRect(20, 10, 361, 181))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 90, 251, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(130, 120, 111, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 150, 121, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButtonOK = QtGui.QPushButton(AboutDialog)
        self.pushButtonOK.setGeometry(QtCore.QRect(280, 200, 99, 27))
        self.pushButtonOK.setObjectName(_fromUtf8("pushButtonOK"))
        self.frame.raise_()
        self.label.raise_()
        self.pushButtonOK.raise_()

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About", None))
        self.label.setText(_translate("AboutDialog", "Visualization of Double Pendulums on a cart", None))
        self.label_3.setText(_translate("AboutDialog", "Zheng Huang", None))
        self.label_4.setText(_translate("AboutDialog", "Royal Institute of Technology (KTH)", None))
        self.label_5.setText(_translate("AboutDialog", "hzheng@kth.se", None))
        self.label_2.setText(_translate("AboutDialog", "Copyright@2015", None))
        self.pushButtonOK.setText(_translate("AboutDialog", "OK", None))

    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButtonOK_clicked(self):
        self.close()

