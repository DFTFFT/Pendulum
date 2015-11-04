#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
import vtk
from PyQt4 import QtCore, QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from doublePendulum import doublePendulum
from aboutdialogui import Ui_AboutDialog
from helpdlgui import Ui_HelpDialog

import numpy as np
from scipy import sin, cos
from scipy.integrate import odeint

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
		QtGui.QMainWindow.__init__(self)
		# Setup UI widgets
		self.setupUi(self)
		# Setup input and output data structure
		self.input_data_pack = input_data()
		self.result_data_pack = result_data()
		# Setup timer
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.timerCallback)
		self.timer_count = 0
		self.current_time = 0.0
		self.len_convert_factor = 100.0   # 1m = 100 pixels
		# Setup camera control
		self.camCtl = cameraCtl()

    def setupUi(self, MainWindow):
        # mainwindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1600, 950)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        
        # centralWidget
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)

        MainWindow.setCentralWidget(self.centralWidget)

        # Left Ccontrol pannel
        # Frame
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        # Group_model
        self.groupBox_model = QtGui.QGroupBox(self.frame)
        self.groupBox_model.setGeometry(QtCore.QRect(15, 10, 361, 211))
        self.groupBox_model.setAutoFillBackground(False)
        self.groupBox_model.setObjectName(_fromUtf8("groupBox_model"))
        self.groupBox_model.setStyleSheet("QGroupBox{border: 1px solid rgb(192, 192, 192); border-radius:9px; font: bold}"
        	+"QGroupBox::title{subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px}")


        self.tableWidget = QtGui.QTableWidget(self.groupBox_model)
        self.tableWidget.setGeometry(QtCore.QRect(15, 30, 320, 120))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(2)
        header = ["M", "m", "L", "h"]
        self.tableWidget.setHorizontalHeaderLabels(header)
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.label_Cart = QtGui.QLabel(self.groupBox_model)
        self.label_Cart.setGeometry(QtCore.QRect(15, 170, 71, 17))
        self.label_Cart.setObjectName(_fromUtf8("label_Cart"))
        self.label_Cart_M = QtGui.QLabel(self.groupBox_model)
        self.label_Cart_M.setGeometry(QtCore.QRect(70, 170, 21, 17))
        self.label_Cart_M.setObjectName(_fromUtf8("label_Cart_M"))

        self.label_Cart_L = QtGui.QLabel(self.groupBox_model)
        self.label_Cart_L.setGeometry(QtCore.QRect(180, 170, 21, 17))
        self.label_Cart_L.setObjectName(_fromUtf8("label_Cart_L"))

        self.lineEdit_Cart_M = QtGui.QLineEdit(self.groupBox_model)
        self.lineEdit_Cart_M.setGeometry(QtCore.QRect(90, 160, 61, 27))
        self.lineEdit_Cart_M.setObjectName(_fromUtf8("lineEdit_Cart_M"))

        self.lineEdit_Cart_L = QtGui.QLineEdit(self.groupBox_model)
        self.lineEdit_Cart_L.setGeometry(QtCore.QRect(200, 160, 61, 27))
        self.lineEdit_Cart_L.setObjectName(_fromUtf8("lineEdit_Cart_L"))

        # Group_init
        self.groupBox_init = QtGui.QGroupBox(self.frame)
        self.groupBox_init.setGeometry(QtCore.QRect(20, 250, 361, 91))
        self.groupBox_init.setObjectName(_fromUtf8("groupBox_init"))
        self.groupBox_init.setStyleSheet("QGroupBox{border: 1px solid rgb(192, 192, 192); border-radius:9px; font: bold}"
        	+"QGroupBox::title{subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px}")

        self.label_init_x = QtGui.QLabel(self.groupBox_init)
        self.label_init_x.setGeometry(QtCore.QRect(10, 40, 21, 17))
        self.label_init_x.setObjectName(_fromUtf8("label_init_x"))
        self.label_init_vx = QtGui.QLabel(self.groupBox_init)
        self.label_init_vx.setGeometry(QtCore.QRect(10, 70, 21, 17))
        self.label_init_vx.setObjectName(_fromUtf8("label_init_vx"))
        self.label_init_th1 = QtGui.QLabel(self.groupBox_init)
        self.label_init_th1.setGeometry(QtCore.QRect(100, 40, 51, 17))
        self.label_init_th1.setObjectName(_fromUtf8("label_init_th1"))
        self.label_init_th2 = QtGui.QLabel(self.groupBox_init)
        self.label_init_th2.setGeometry(QtCore.QRect(230, 40, 51, 17))
        self.label_init_th2.setObjectName(_fromUtf8("label_init_th2"))
        self.label_init_w2 = QtGui.QLabel(self.groupBox_init)
        self.label_init_w2.setGeometry(QtCore.QRect(250, 70, 21, 17))
        self.label_init_w2.setObjectName(_fromUtf8("label_init_w2"))
        self.label_init_w1 = QtGui.QLabel(self.groupBox_init)
        self.label_init_w1.setGeometry(QtCore.QRect(120, 70, 21, 17))
        self.label_init_w1.setObjectName(_fromUtf8("label_init_w1"))

        self.lineEdit_init_x = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_init_x.setGeometry(QtCore.QRect(30, 30, 51, 27))
        self.lineEdit_init_x.setObjectName(_fromUtf8("lineEdit_init_x"))
        self.lineEdit_init_th1 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_init_th1.setGeometry(QtCore.QRect(160, 30, 51, 27))
        self.lineEdit_init_th1.setObjectName(_fromUtf8("lineEdit_init_th1"))
        self.lineEdit_init_th2 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_init_th2.setGeometry(QtCore.QRect(280, 30, 51, 27))
        self.lineEdit_init_th2.setObjectName(_fromUtf8("lineEdit_init_th2"))
        self.lineEdit_init_vx = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_init_vx.setGeometry(QtCore.QRect(30, 60, 51, 27))
        self.lineEdit_init_vx.setObjectName(_fromUtf8("lineEdit_init_vx"))
        self.lineEdit_init_w1 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_init_w1.setGeometry(QtCore.QRect(160, 60, 51, 27))
        self.lineEdit_init_w1.setObjectName(_fromUtf8("lineEdit_init_w1"))
        self.lineEdit_init_w2 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_init_w2.setGeometry(QtCore.QRect(280, 60, 51, 27))
        self.lineEdit_init_w2.setObjectName(_fromUtf8("lineEdit_init_w2"))

        # Group_time
        self.groupBox_time = QtGui.QGroupBox(self.frame)
        self.groupBox_time.setGeometry(QtCore.QRect(20, 370, 361, 61))
        self.groupBox_time.setObjectName(_fromUtf8("groupBox_time"))
        self.groupBox_time.setStyleSheet("QGroupBox{border: 1px solid rgb(192, 192, 192); border-radius:9px; font: bold}"
        	+"QGroupBox::title{subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px}")

        self.label_time_start = QtGui.QLabel(self.groupBox_time)
        self.label_time_start.setGeometry(QtCore.QRect(10, 40, 41, 17))
        self.label_time_start.setObjectName(_fromUtf8("label_time_start"))
        self.lineEdit_time_start = QtGui.QLineEdit(self.groupBox_time)
        self.lineEdit_time_start.setGeometry(QtCore.QRect(50, 30, 61, 27))
        self.lineEdit_time_start.setObjectName(_fromUtf8("lineEdit_time_start"))

        self.lable_time_end = QtGui.QLabel(self.groupBox_time)
        self.lable_time_end.setGeometry(QtCore.QRect(130, 40, 41, 17))
        self.lable_time_end.setObjectName(_fromUtf8("lable_time_end"))
        self.lineEdit_time_end = QtGui.QLineEdit(self.groupBox_time)
        self.lineEdit_time_end.setGeometry(QtCore.QRect(170, 30, 61, 27))
        self.lineEdit_time_end.setObjectName(_fromUtf8("lineEdit_time_end"))

        self.label_time_step = QtGui.QLabel(self.groupBox_time)
        self.label_time_step.setGeometry(QtCore.QRect(250, 40, 41, 17))
        self.label_time_step.setObjectName(_fromUtf8("label_time_step"))
        self.lineEdit_time_step = QtGui.QLineEdit(self.groupBox_time)
        self.lineEdit_time_step.setGeometry(QtCore.QRect(290, 30, 61, 27))
        self.lineEdit_time_step.setObjectName(_fromUtf8("lineEdit_time_step"))

        # Group_view
        self.groupBox_view = QtGui.QGroupBox(self.frame)
        self.groupBox_view.setGeometry(QtCore.QRect(20, 460, 361, 141))
        self.groupBox_view.setObjectName(_fromUtf8("groupBox_view"))
        self.groupBox_view.setStyleSheet("QGroupBox{border: 1px solid rgb(192, 192, 192); border-radius:9px; font: bold}"
        	+"QGroupBox::title{subcontrol-origin: margin; left: 10px; padding: 0 3px 0 3px}")

        #self.radioButton_default = QtGui.QRadioButton(self.groupBox_view)
        #self.radioButton_default.setGeometry(QtCore.QRect(20, 30, 131, 22))
        #self.radioButton_default.setObjectName(_fromUtf8("radioButton_default"))
        #self.radioButton_default.setChecked(True)

        #self.radioButton_sideview = QtGui.QRadioButton(self.groupBox_view)
        #self.radioButton_sideview.setGeometry(QtCore.QRect(20, 60, 131, 22))
        #self.radioButton_sideview.setObjectName(_fromUtf8("radioButton_sideview"))       

        self.pushButton_update_cam = QtGui.QPushButton(self.groupBox_view)
        self.pushButton_update_cam.setGeometry(QtCore.QRect(20, 30, 80, 30))
        self.pushButton_update_cam.setObjectName(_fromUtf8("pushButton_update_cam"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/camera.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_update_cam.setIcon(icon)
        self.pushButton_update_cam.setIconSize(QtCore.QSize(25, 25))

        self.checkBox_display_axes = QtGui.QCheckBox(self.groupBox_view)
        self.checkBox_display_axes.setGeometry(QtCore.QRect(180, 30, 110, 22))
        self.checkBox_display_axes.setObjectName(_fromUtf8("checkBox_display_axes"))

        self.checkBox_sideview = QtGui.QCheckBox(self.groupBox_view)
        self.checkBox_sideview.setGeometry(QtCore.QRect(180, 60, 110, 22))
        self.checkBox_sideview.setObjectName(_fromUtf8("checkBox_sideview"))

        self.horizontalSlider_elevation = QtGui.QSlider(self.groupBox_view)
        self.horizontalSlider_elevation.setGeometry(QtCore.QRect(100, 90, 241, 29))
        self.horizontalSlider_elevation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_elevation.setObjectName(_fromUtf8("horizontalSlider_elevation"))
        self.horizontalSlider_elevation.setMinimum(0)
        self.horizontalSlider_elevation.setMaximum(100)
        self.horizontalSlider_elevation.setTickInterval(10)

        self.label_pos = QtGui.QLabel(self.groupBox_view)
        self.label_pos.setGeometry(QtCore.QRect(20, 100, 67, 17))
        self.label_pos.setObjectName(_fromUtf8("label_pos"))

        # Functional Button
        self.pushButton_export_input = QtGui.QPushButton(self.frame)
        self.pushButton_export_input.setGeometry(QtCore.QRect(10, 630, 115, 35))
        self.pushButton_export_input.setObjectName(_fromUtf8("pushButton_export_input"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/export_database_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_export_input.setIcon(icon)
        self.pushButton_export_input.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_import_input = QtGui.QPushButton(self.frame)
        self.pushButton_import_input.setGeometry(QtCore.QRect(130, 630, 115, 35))
        self.pushButton_import_input.setObjectName(_fromUtf8("pushButton_import_input"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/download-database.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_import_input.setIcon(icon)
        self.pushButton_import_input.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_save_result = QtGui.QPushButton(self.frame)
        self.pushButton_save_result.setGeometry(QtCore.QRect(250, 630, 115, 35))
        self.pushButton_save_result.setObjectName(_fromUtf8("pushButton_save_result"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/save_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save_result.setIcon(icon)
        self.pushButton_save_result.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_reset = QtGui.QPushButton(self.frame)
        self.pushButton_reset.setGeometry(QtCore.QRect(10, 700, 115, 35))
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_reset.setIcon(icon)
        self.pushButton_reset.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_initialize = QtGui.QPushButton(self.frame)
        self.pushButton_initialize.setGeometry(QtCore.QRect(130, 700, 115, 35))
        self.pushButton_initialize.setObjectName(_fromUtf8("pushButton_initialize"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/iconvert.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_initialize.setIcon(icon)
        self.pushButton_initialize.setIconSize(QtCore.QSize(20, 20))       

        self.pushButton_simulate = QtGui.QPushButton(self.frame)
        self.pushButton_simulate.setGeometry(QtCore.QRect(250, 700, 115, 35))
        self.pushButton_simulate.setObjectName(_fromUtf8("pushButton_simulate"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/tick_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_simulate.setIcon(icon)
        self.pushButton_simulate.setIconSize(QtCore.QSize(20, 20))

        # vtkWidget
        self.widget_vtk = QVTKRenderWindowInteractor(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_vtk.sizePolicy().hasHeightForWidth())
        self.widget_vtk.setSizePolicy(sizePolicy)
        self.widget_vtk.setObjectName(_fromUtf8("widget_vtk"))
        self.setvtkWidget()

        # Matplotlib plot
        self.plot_trace = MyMplCanvas(self.centralWidget, width=1, height=1, dpi=50, Ndim=2)
        self.plot_trace.setObjectName(_fromUtf8("plot_trace"))
        self.plot_trace.axes.set_xlim(-1, 3)
        self.plot_trace.axes.set_ylim(-1, 3)
        #self.plot_trace.lines[0].set_color('red')     # it doesn't work?
        #self.plot_trace.lines[1].set_color('blue')
        self.plot_trace.fig.legend((self.plot_trace.lines[0],self.plot_trace.lines[1]),('Left sphere','Right sphere'),(0.15, 0.76))


        self.plot_angle = MyMplCanvas(self.centralWidget, width=1, height=1, dpi=50, Ndim=2)
        self.plot_angle.setObjectName(_fromUtf8("plot_angle"))
        self.plot_angle.axes.set_xlim(0, 10)
        self.plot_angle.axes.set_ylim(-1.6, 1.6)

        self.plot_cart_pos = MyMplCanvas(self.centralWidget, width=1, height=1, dpi=50, Ndim=1)
        self.plot_cart_pos.setObjectName(_fromUtf8("plot_cart_pos"))
        self.plot_cart_pos.axes.set_xlim(0, 10)
        self.plot_cart_pos.axes.set_ylim(-3, 3)      

        # MenuBar
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 912, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        # ToolBar
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBar.setIconSize(QtCore.QSize(50, 50))
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.actionStart = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart.setIcon(icon)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        
        self.actionStop = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/Stop-Normal-Blue-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStop.setIcon(icon)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))

        self.actionExportInput = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/export_database_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExportInput.setIcon(icon)
        self.actionExportInput.setObjectName(_fromUtf8("actionExportInput"))

        self.actionImportInput = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/download-database.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImportInput.setIcon(icon)
        self.actionImportInput.setObjectName(_fromUtf8("actionImportInput"))

        self.actionSaveResult = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/save_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveResult.setIcon(icon)
        self.actionSaveResult.setObjectName(_fromUtf8("actionSaveResult"))

        self.actionHelp = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/khelpcenter.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))

        self.actionAbout = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/Info_icon_002.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.actionExit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/Exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.actionInit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/iconvert.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInit.setIcon(icon)
        self.actionInit.setObjectName(_fromUtf8("actionInit"))

        self.actionSimulate = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/tick_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSimulate.setIcon(icon)
        self.actionSimulate.setObjectName(_fromUtf8("actionSimulate"))

        self.actionReset = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))

       
        self.mainToolBar.addAction(self.actionExportInput)
        self.mainToolBar.addAction(self.actionImportInput)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionInit)
        self.mainToolBar.addAction(self.actionSimulate)
        self.mainToolBar.addAction(self.actionReset)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionStart)
        self.mainToolBar.addAction(self.actionStop)  
        self.mainToolBar.addAction(self.actionSaveResult)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionHelp)
        self.mainToolBar.addAction(self.actionAbout)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)

		# current time display
        self.mainToolBar.addSeparator()
        self.label_currenttime = QtGui.QLabel(self.mainToolBar)
        self.label_currenttime.setGeometry(QtCore.QRect(1000, 25, 60, 30))
        self.label_currenttime.setObjectName(_fromUtf8("label_currenttime"))
        self.label_currenttime.setStyleSheet("QLabel{font-weight: bold; font-size: 22px}")

        self.lineEdit_timer = QtGui.QLineEdit(self.mainToolBar)
        self.lineEdit_timer.setGeometry(QtCore.QRect(1070, 20, 100, 40))
        self.lineEdit_timer.setObjectName(_fromUtf8("lineEdit_timer"))
        self.lineEdit_timer.setReadOnly(True)
        self.lineEdit_timer.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
        #self.mainToolBar.addWidget(self.lineEdit_timer)




        # statusBar
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)


        # Layout management
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.gridLayout.addWidget(self.frame, 0, 0, 3, 1)
        self.gridLayout.addWidget(self.widget_vtk, 0, 1, 2, 3)
        self.gridLayout.addWidget(self.plot_trace, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.plot_angle, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.plot_cart_pos, 2, 3, 1, 1)

        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """ """
        # Mainwindow
        MainWindow.setWindowTitle(_translate("MainWindow", "Pendulum Simulation", None))

        # Left control pannel
        self.groupBox_model.setTitle(_translate("MainWindow", "Model Parameters", None))
        self.label_Cart.setText(_translate("MainWindow", "Cart:", None))
        self.label_Cart_M.setText(_translate("MainWindow", "M", None))
        self.label_Cart_L.setText(_translate("MainWindow", "L", None))

        self.groupBox_init.setTitle(_translate("MainWindow", "Initial Condition", None))
        self.label_init_x.setText(_translate("MainWindow", "x", None))
        self.label_init_vx.setText(_translate("MainWindow", "vx", None))
        self.label_init_th1.setText(_translate("MainWindow", "theta1", None))
        self.label_init_th2.setText(_translate("MainWindow", "theta2", None))
        self.label_init_w2.setText(_translate("MainWindow", "w2", None))
        self.label_init_w1.setText(_translate("MainWindow", "w1", None))

        self.groupBox_time.setTitle(_translate("MainWindow", "Time Advancement", None))
        self.label_time_start.setText(_translate("MainWindow", "tstart", None))
        self.lable_time_end.setText(_translate("MainWindow", "tend", None))
        self.label_time_step.setText(_translate("MainWindow", "tstep", None))

        self.groupBox_view.setTitle(_translate("MainWindow", "Camera View", None))
        self.checkBox_display_axes.setText(_translate("MainWindow", "Display Axes", None))
        self.checkBox_sideview.setText(_translate("MainWindow", "Sideview", None))
        self.label_pos.setText(_translate("MainWindow", "position", None))
        #self.radioButton_default.setText(_translate("MainWindow", "Default view", None))
        #self.radioButton_sideview.setText(_translate("MainWindow", "Side view", None))
        self.pushButton_update_cam.setText(_translate("MainWindow", "Update", None))

        self.pushButton_export_input.setText(_translate("MainWindow", "Export Input", None))
        self.pushButton_import_input.setText(_translate("MainWindow", "Import Input", None))
        self.pushButton_save_result.setText(_translate("MainWindow", "Save Result", None))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_initialize.setText(_translate("MainWindow", "Initialize", None))
        self.pushButton_simulate.setText(_translate("MainWindow", "Simulate", None))

        # Toolbar action
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionStart.setToolTip(_translate("MainWindow", "Start", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionStop.setToolTip(_translate("MainWindow", "Stop", None))
        self.actionExportInput.setText(_translate("MainWindow", "Export Input", None))
        self.actionExportInput.setToolTip(_translate("MainWindow", "Export Input", None))
        self.actionImportInput.setText(_translate("MainWindow", "Import Input", None))
        self.actionImportInput.setToolTip(_translate("MainWindow", "Import Input", None))
        self.actionSaveResult.setText(_translate("MainWindow", "SaveResult", None))
        self.actionSaveResult.setToolTip(_translate("MainWindow", "SaveResult", None))                     
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp.setToolTip(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setToolTip(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit", None))
        self.actionInit.setText(_translate("MainWindow", "Initialize", None))
        self.actionInit.setToolTip(_translate("MainWindow", "Initialize", None))
        self.actionSimulate.setText(_translate("MainWindow", "Simulate", None))
        self.actionSimulate.setToolTip(_translate("MainWindow", "Simulate", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionReset.setToolTip(_translate("MainWindow", "Reset", None))

        self.label_currenttime.setText(_translate("MainWindow", "Time:", None))


    def setvtkWidget(self):
    	"""Set up the vtk widget"""
    	self.ren = vtk.vtkRenderer()
    	self.ren.SetBackground(0.1, 0.2, 0.3)
        self.widget_vtk.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.widget_vtk.GetRenderWindow().GetInteractor()
 
        # The cart model (includes a plate, two poles and four wheel)
        # Plate of the cart
        # Create source
        self.plate = vtk.vtkCubeSource()
        self.plate.SetXLength(100)
        self.plate.SetYLength(60)
        self.plate.SetZLength(6)
        self.plate.SetCenter(50, 0, -3)
 
        # Create a mapper
        plateMapper = vtk.vtkPolyDataMapper()
        plateMapper.SetInputConnection(self.plate.GetOutputPort())

        # Create a transform
        plateTransform = vtk.vtkTransform()
 
        # Create an actor
        self.plateActor = vtk.vtkActor()
        self.plateActor.SetMapper(plateMapper)
        self.plateActor.SetUserTransform(plateTransform)
        self.plateActor.GetProperty().SetColor(0.69, 0.77, 0.87)
 
        self.ren.AddActor(self.plateActor)

        # Two poles
        # Left pole
        # Create source
        self.poleL = vtk.vtkCylinderSource()
        self.poleL.SetRadius(1.0)
        self.poleL.SetHeight(50.0)
        self.poleL.SetCenter(10, 0, 0)
        self.poleL.SetResolution(100.0)

        # Create a mapper
        poleLMapper = vtk.vtkPolyDataMapper()
        poleLMapper.SetInputConnection(self.poleL.GetOutputPort())

        # Create a transform
        self.poleLTransform = vtk.vtkTransform()
        self.poleLTransform.SetInput(plateTransform)

        # Create an actor
        poleLActor = vtk.vtkActor()
        poleLActor.SetMapper(poleLMapper)
        poleLActor.SetUserTransform(self.poleLTransform)

        self.poleLTransform.RotateX(90.0)
        self.poleLTransform.Translate(0.0, 25.0, 0.0)

        self.ren.AddActor(poleLActor)

        # Right pole
        # Create source
        self.poleR = vtk.vtkCylinderSource()
        self.poleR.SetRadius(1.0)
        self.poleR.SetHeight(50.0)
        self.poleR.SetCenter(90, 0, 0)
        self.poleR.SetResolution(100.0)

        # Create a mapper
        poleRMapper = vtk.vtkPolyDataMapper()
        poleRMapper.SetInputConnection(self.poleR.GetOutputPort())

        # Create a transform
        self.poleRTransform = vtk.vtkTransform()
        self.poleRTransform.SetInput(plateTransform)

        # Create an actor
        poleRActor = vtk.vtkActor()
        poleRActor.SetMapper(poleRMapper)
        poleRActor.SetUserTransform(self.poleRTransform)

        self.poleRTransform.RotateX(90.0)
        self.poleRTransform.Translate(0.0, 25.0, 0.0)

        self.ren.AddActor(poleRActor)

        # 4 cart's wheels
        self.wheel = []
        wheelMapper = []
        wheelTransform = []
        wheelActor = []
        for i in range(4):
        	# Create source
            self.wheel.append(vtk.vtkCylinderSource())
            self.wheel[i].SetRadius(6.0)
            self.wheel[i].SetHeight(3.0)
            self.wheel[i].SetResolution(100.0)

        	# Create a mapper
            wheelMapper.append(vtk.vtkPolyDataMapper())
            wheelMapper[i].SetInputConnection(self.wheel[i].GetOutputPort())

            # Create a transform
            wheelTransform.append(vtk.vtkTransform())
            wheelTransform[i].SetInput(plateTransform)

        	# Create an actor
            wheelActor.append(vtk.vtkActor())
            wheelActor[i].SetMapper(wheelMapper[i])
            wheelActor[i].SetUserTransform(wheelTransform[i])
            wheelActor[i].GetProperty().SetColor(1.0, 1.0, 0.6)

            self.ren.AddActor(wheelActor[i])
        
        self.wheel[0].SetCenter(10, 25, -9.0)
        self.wheel[1].SetCenter(90, 25, -9.0)
        self.wheel[2].SetCenter(10, -25, -9.0)
        self.wheel[3].SetCenter(90, -25, -9.0)


        # Two spheres' model
        # Left sphere
        # Create source
        self.sphereL = vtk.vtkSphereSource()
        self.sphereL.SetRadius(5)
        self.sphereL.SetCenter(0, 0, 30)

        # Create a mapper
        sphereLMapper = vtk.vtkPolyDataMapper()
        sphereLMapper.SetInputConnection(self.sphereL.GetOutputPort())

        # Create an actor
        self.sphereLActor = vtk.vtkActor()
        self.sphereLActor.SetMapper(sphereLMapper)
        self.sphereLActor.GetProperty().SetColor(1.0, 0.2, 0.2)

        self.ren.AddActor(self.sphereLActor)

        # Right sphere
        # Create source
        self.sphereR = vtk.vtkSphereSource()
        self.sphereR.SetRadius(5)
        self.sphereR.SetCenter(100, 0, 30)

        # Create a mapper
        sphereRMapper = vtk.vtkPolyDataMapper()
        sphereRMapper.SetInputConnection(self.sphereR.GetOutputPort())

        # Create an actor
        self.sphereRActor = vtk.vtkActor()
        self.sphereRActor.SetMapper(sphereRMapper)
        self.sphereRActor.GetProperty().SetColor(0.0, 0.5, 1.0)

        self.ren.AddActor(self.sphereRActor)

        # Two poles (connected to the spheres, use lines stead)
        # Left
        self.LineL = vtk.vtkLineSource()
        self.LineL.SetPoint1(10, 0, 50)
        self.LineL.SetPoint2(0, 0, 30)

        LineLMapper = vtk.vtkPolyDataMapper()
        LineLMapper.SetInput(self.LineL.GetOutput())
        #LineLMapper.SetInputConnection(self.LineL.GetOutputPort())

        LineLActor = vtk.vtkActor()
        LineLActor.SetMapper(LineLMapper)
        #LineLActor.GetProperty().SetColor(1.0, 0.0, 0.0)
        LineLActor.GetProperty().SetLineWidth(5)

        self.ren.AddActor(LineLActor)

        # RighR
        self.LineR = vtk.vtkLineSource()
        self.LineR.SetPoint1(90, 0, 50)
        self.LineR.SetPoint2(100, 0, 30)

        LineRMapper = vtk.vtkPolyDataMapper()
        LineRMapper.SetInput(self.LineR.GetOutput())
        #LineRMapper.SetInputConnection(self.LineR.GetOutputPort())

        LineRActor = vtk.vtkActor()
        LineRActor.SetMapper(LineRMapper)
        #LineLActor.GetProperty().SetColor(1.0, 0.0, 0.0)
        LineLActor.GetProperty().SetLineWidth(5)

        self.ren.AddActor(LineRActor)

        # Coordinate axes and ticks
        self.axes = vtk.vtkAxesActor()
        self.axes.SetTotalLength(100, 100, 100)
        #self.axes.SetShaftTypeToLine()
        self.axes.SetConeRadius(0.1)
        axesTransform = vtk.vtkTransform()
        axesTransform.Translate(0.0, 0.0, -50.0)
        self.axes.SetUserTransform(axesTransform)
        self.axes.AxisLabelsOff()
        #self.ren.AddActor(self.axes) 

        # Create a camera
        #self.ren.ResetCamera()
        camera = vtk.vtkCamera()    
        self.ren.SetActiveCamera(camera)
        self.ren.GetActiveCamera().SetPosition(50, -300, 100)
        self.ren.GetActiveCamera().SetFocalPoint(50, 0, 0)
        self.ren.GetActiveCamera().SetViewUp(0, 0, 1)
        self.ren.GetActiveCamera().UpdateViewport(self.ren)
        #
        #camera.UseHorizontalViewAngleOn()
        #camera.SetViewAngle(40.0)
        #print("Distance=%f"%camera.GetDistance())
  

    def timerCallback(self):
		"""Timer callback function"""
		self.timer_count += 1
		#print(self.timer_count)
		# Display current time
		self.current_time = self.timer_count*self.input_data_pack.tstep
		self.lineEdit_timer.setText(str(self.current_time))

		# Terminate the simulation when reaching the preset stop time		
		if self.current_time > self.pendulum.te:
			self.timer.stop()
			return

		# Solve the system of the Lagrange mechanical equations at current time
		t = np.array([self.current_time-self.input_data_pack.tstep, self.current_time])
		result = self.pendulum.solve_ode(t)
		
		# Update the intial condition for next time step
		self.pendulum.init_status = result[6:12]   # Note the end index is 12 but not 11

		# Save the result to the result data package for export
		self.result_data_pack.addData(result)

		# Unpack the result data
		tim, X1, Y1, X2, Y2, X, x, th1, th2, dx, dth1, dth2 = result

		# Update the position of the pendulums and the cart in the vtk widget
		# Cart
		self.plateActor.GetUserTransform().Identity()
		self.plateActor.GetUserTransform().Translate((x-self.input_data_pack.x0)*self.len_convert_factor, 0.0, 0.0)
		# Two pendulums
		# It seems to have some problems by using the SetPosition function
		#self.sphereLActor.SetPosition(X1*self.len_convert_factor, 0.0, Y1*self.len_convert_factor)
		#self.sphereRActor.SetPosition(X2*self.len_convert_factor, 0.0, Y2*self.len_convert_factor)

		self.sphereL.SetCenter(X1*self.len_convert_factor, 0.0, Y1*self.len_convert_factor)
		self.sphereR.SetCenter(X2*self.len_convert_factor, 0.0, Y2*self.len_convert_factor)

		# Two ropes
		self.LineL.SetPoint1((X-self.input_data_pack.L/2)*self.len_convert_factor, 0, self.poleL.GetHeight())
		self.LineL.SetPoint2(X1*self.len_convert_factor, 0.0, Y1*self.len_convert_factor)

		self.LineR.SetPoint1((X+self.input_data_pack.L/2)*self.len_convert_factor, 0, self.poleR.GetHeight())
		self.LineR.SetPoint2(X2*self.len_convert_factor, 0.0, Y2*self.len_convert_factor)

		# Update the camera view
		#self.camCtl.updateCamera(self)
		
		# Update the vtk view
		self.iren.GetRenderWindow().Render()

		# Update the matplotlib plots
		# plot_trace
		self.plot_trace.updateFig([[X1, Y1], [X2, Y2]])
		# Setup the figure properties

		self.plot_trace.axes.set_title("Trace of the pendulums", fontsize = 25)
		self.plot_trace.axes.set_xlabel("x/m", fontsize = 15)
		self.plot_trace.axes.set_ylabel("y/m", fontsize = 15)

		# plot_angle
		self.plot_angle.updateFig([[tim, th1], [tim, th2]])

		self.plot_angle.axes.set_title("Angle of the pendulums", fontsize = 25)
		self.plot_angle.axes.set_xlabel("Time/sec", fontsize = 15)
		self.plot_angle.axes.set_ylabel("Angle/rad", fontsize = 15)

		# plot_cart_pos
		self.plot_cart_pos.updateFig([[tim, X]])

		self.plot_cart_pos.axes.set_title("Position of the cart", fontsize = 25)
		self.plot_cart_pos.axes.set_xlabel("Time/sec", fontsize = 15)
		self.plot_cart_pos.axes.set_ylabel("Position/m", fontsize = 15)


    # Toolbar button slot
    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionExportInput_triggered(self):
    	"""Toolbar export input button slot"""
    	self.on_pushButton_export_input_clicked()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionImportInput_triggered(self):
    	"""Toolbar import input button slot"""
    	self.on_pushButton_import_input_clicked()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionInit_triggered(self):
    	"""Toolbar init button slot"""
    	self.on_pushButton_initialize_clicked()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionSimulate_triggered(self):
    	"""Toolbar simulate button slot"""
    	self.on_pushButton_simulate_clicked()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionReset_triggered(self):
    	"""Toolbar reset button slot"""
    	self.on_pushButton_reset_clicked()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionStart_triggered(self):
    	"""Toolbar start button slot"""
    	self.timer.start(self.input_data_pack.tstep*1000)    # Convert unit from s to ms

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionStop_triggered(self):
    	"""Toolbar stop button slot"""
    	self.timer.stop()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionSaveResult_triggered(self):
    	"""Toolbar save-result button slot"""
    	self.on_pushButton_save_result_clicked()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionHelp_triggered(self):
    	"""Toolbar help button slot"""
    	helpDlg = Ui_HelpDialog()
    	helpDlg.setModal(True)
    	helpDlg.exec_()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionExit_triggered(self):
    	"""Toolbar exit button slot"""
    	self.close()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionAbout_triggered(self):
    	"""Toolbar about button slot"""
    	aboutDlg = Ui_AboutDialog()
    	aboutDlg.setModal(True)
    	aboutDlg.exec_()


    # CheckBox slot
    @QtCore.pyqtSlot() # signal with no arguments
    def on_checkBox_sideview_clicked(self):
    	"""Sideview checkBox slot"""
    	if self.checkBox_sideview.isChecked():
    		self.camCtl.bool_sideview = True
    	else:
    		self.camCtl.bool_sideview = False

    @QtCore.pyqtSlot() # signal with no arguments
    def on_checkBox_display_axes_clicked(self):
    	"""Display Axes"""
    	if self.checkBox_display_axes.isChecked():
    		self.ren.AddActor(self.axes)
    	else:	
    		self.ren.RemoveActor(self.axes)

    	self.iren.GetRenderWindow().Render()


    # horizontal slide slot
    #@QtCore.pyqtSlot() # signal with no arguments
    # Note that there is one argument passed to the slot
    def on_horizontalSlider_elevation_valueChanged(self, value):
    	"""Camara elevation"""
    	self.camCtl.elev(value, self)



    	
    # PushButton slot
    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_export_input_clicked(self):
    	"""Export input button function"""
    	self.input_data_pack.get_input_data(self)
    	filename = QtGui.QFileDialog.getSaveFileName(self, "Export Input file", "/home/hz")
    	if filename == "":
    		return
    	with open(filename, 'wb') as f:
    		# Model parameter
    		f.write("%f\n"%self.input_data_pack.M1)
    		f.write("%f\n"%self.input_data_pack.M2)
     		f.write("%f\n"%self.input_data_pack.m1)
    		f.write("%f\n"%self.input_data_pack.m2)   		
    		f.write("%f\n"%self.input_data_pack.L1)
    		f.write("%f\n"%self.input_data_pack.L2)
    		f.write("%f\n"%self.input_data_pack.h1)
    		f.write("%f\n"%self.input_data_pack.h2)
     		f.write("%f\n"%self.input_data_pack.M)
    		f.write("%f\n"%self.input_data_pack.L)

    		# Init condition
    		f.write("%f\n"%self.input_data_pack.x0)
    		f.write("%f\n"%self.input_data_pack.th10)
     		f.write("%f\n"%self.input_data_pack.th20)
    		f.write("%f\n"%self.input_data_pack.dx0)   		
    		f.write("%f\n"%self.input_data_pack.dth10)
    		f.write("%f\n"%self.input_data_pack.dth20)

    		# Time info
    		f.write("%f\n"%self.input_data_pack.ts)
    		f.write("%f\n"%self.input_data_pack.te)
     		f.write("%f\n"%self.input_data_pack.tstep)	

    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_import_input_clicked(self):
    	"""Import input button function"""
    	filename = QtGui.QFileDialog.getOpenFileName(self, "Open Input file", "/home/hz")
    	if filename == "":
    		return
    	read_data = []
    	with open(filename, 'r') as f:
    		for line in f.readlines():
    			read_data.append(float(line.strip()))
    	# Model parameter
    	self.input_data_pack.M1 = read_data[0]
    	self.input_data_pack.M2 = read_data[1]
     	self.input_data_pack.m1 = read_data[2]
    	self.input_data_pack.m2 = read_data[3]   		
    	self.input_data_pack.L1 = read_data[4]
    	self.input_data_pack.L2 = read_data[5]
    	self.input_data_pack.h1 = read_data[6]
    	self.input_data_pack.h2 = read_data[7]
     	self.input_data_pack.M = read_data[8]
    	self.input_data_pack.L = read_data[9]

    	# Init condition
    	self.input_data_pack.x0 = read_data[10]
    	self.input_data_pack.th10 = read_data[11]
     	self.input_data_pack.th20 = read_data[12]
    	self.input_data_pack.dx0 = read_data[13]   		
    	self.input_data_pack.dth10 = read_data[14]
    	self.input_data_pack.dth20 = read_data[15]

    	# Time info
    	self.input_data_pack.ts = read_data[16]
    	self.input_data_pack.te = read_data[17]
     	self.input_data_pack.tstep = read_data[18]

		#
    	self.input_data_pack.set_input_data(self)

    
    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_save_result_clicked(self):
    	"""Save result button function"""
    	filename = QtGui.QFileDialog.getSaveFileName(self, "Save result file", "/home/hz")
    	with open(filename, 'wb') as f:
    		f.write("Time  X1     Y1     X2     Y2     X     x     th1     th2     dx     dth1     dth2\n")
    		N = self.result_data_pack.getLen()
    		for i in range(N):
    			f.write("%f     %f     %f      %f      %f     %f     %f      %f     %f     %f     %f      %f\n"
    				%(self.result_data_pack.tim[i], self.result_data_pack.X1[i], self.result_data_pack.Y1[i],
    					self.result_data_pack.X2[i], self.result_data_pack.Y2[i], self.result_data_pack.X[i],
    					self.result_data_pack.x[i], self.result_data_pack.th1[i], self.result_data_pack.th2[i],
    					self.result_data_pack.dx[i], self.result_data_pack.dth1[i], self.result_data_pack.dth2[i]))


    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_initialize_clicked(self):
    	"""Initialize button function"""
    	# Get input data from GUI
    	self.input_data_pack.get_input_data(self)

    	# Update the cart dimension in the vtkwidget based on the input data
    	# plate
    	platelen = 0.1+self.input_data_pack.L+0.1
    	self.plate.SetXLength(platelen*self.len_convert_factor)
    	platepos = self.input_data_pack.x0+0.5*self.input_data_pack.L
    	self.plate.SetCenter(platepos*self.len_convert_factor, 0, -3)
    	self.plateActor.GetUserTransform().Identity()
    	self.plateActor.GetUserTransform().Translate(0.0, 0.0, 0.0)
    	# pole
    	# Left pole
    	poleLpos = self.input_data_pack.x0
    	self.poleL.SetCenter(poleLpos*self.len_convert_factor, 0.0, 0.0)
    	poleLlen = self.input_data_pack.h1
    	poleLlen_old = self.poleL.GetHeight()/self.len_convert_factor
    	self.poleL.SetHeight(poleLlen*self.len_convert_factor)
    	self.poleLTransform.Translate(0, (poleLlen-poleLlen_old)/2*self.len_convert_factor, 0)
    	# Right pole
    	poleRpos = self.input_data_pack.x0+self.input_data_pack.L
    	self.poleR.SetCenter(poleRpos*self.len_convert_factor, 0.0, 0.0)
    	poleRlen = self.input_data_pack.h2
    	poleRlen_old = self.poleR.GetHeight()/self.len_convert_factor
    	self.poleR.SetHeight(poleRlen*self.len_convert_factor)
    	self.poleRTransform.Translate(0, (poleRlen-poleRlen_old)/2*self.len_convert_factor, 0)
    	# 4 wheels
    	self.wheel[0].SetCenter((platepos-self.input_data_pack.L/2)*self.len_convert_factor, 25, -9.0)
    	self.wheel[1].SetCenter((platepos+self.input_data_pack.L/2)*self.len_convert_factor, 25, -9.0)
    	self.wheel[2].SetCenter((platepos-self.input_data_pack.L/2)*self.len_convert_factor, -25, -9.0)
    	self.wheel[3].SetCenter((platepos+self.input_data_pack.L/2)*self.len_convert_factor, -25, -9.0)
    	# Two shperes
    	#self.sphereLActor.SetPosition(0, 0, 0)
    	sphereLpos_x = self.input_data_pack.x0+self.input_data_pack.L1*sin(self.input_data_pack.th10)
    	sphereLpos_y = self.input_data_pack.h1-self.input_data_pack.L1*cos(self.input_data_pack.th10)
    	self.sphereL.SetCenter(sphereLpos_x*self.len_convert_factor, 0, sphereLpos_y*self.len_convert_factor)

    	sphereRpos_x = self.input_data_pack.x0+self.input_data_pack.L+self.input_data_pack.L2*sin(self.input_data_pack.th20)
    	sphereRpos_y = self.input_data_pack.h2-self.input_data_pack.L2*cos(self.input_data_pack.th20)
    	self.sphereR.SetCenter(sphereRpos_x*self.len_convert_factor, 0, sphereRpos_y*self.len_convert_factor)
    	# Two poles (use two lines stead)
    	self.LineL.SetPoint1((platepos-self.input_data_pack.L/2)*self.len_convert_factor, 0, poleLlen*self.len_convert_factor)
    	self.LineL.SetPoint2(sphereLpos_x*self.len_convert_factor, 0, sphereLpos_y*self.len_convert_factor)

    	self.LineR.SetPoint1((platepos+self.input_data_pack.L/2)*self.len_convert_factor, 0, poleRlen*self.len_convert_factor)
    	self.LineR.SetPoint2(sphereRpos_x*self.len_convert_factor, 0, sphereRpos_y*self.len_convert_factor)


    	#
    	# clean the plot view
    	self.plot_trace.clearAxia()
    	self.plot_trace.axes.set_xlim(-1, 3)
    	self.plot_trace.axes.set_ylim(-1, 3)

    	self.plot_angle.clearAxia()
    	self.plot_angle.axes.set_xlim(0, 10)
    	self.plot_angle.axes.set_ylim(-1.6, 1.6)

    	self.plot_cart_pos.clearAxia()
    	self.plot_cart_pos.axes.set_xlim(0, 10)
    	self.plot_cart_pos.axes.set_ylim(-3, 3)

    	# initialize the current time
    	self.current_time = 0.0
    	self.timer_count = 0
    	self.lineEdit_timer.setText(str(self.current_time))

    	# Update the vtkwidget view
    	self.iren.GetRenderWindow().Render()



    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_reset_clicked(self):
    	"""Reset button function"""
    	# reset the timer
    	self.current_time = 0.0
    	self.timer_count = 0
    	self.lineEdit_timer.setText(str(self.current_time))

    	# Get input data from GUI
    	self.input_data_pack.get_input_data(self)

    	# reset the vtkwidget (remove the transform effect on the cart and reset the pendulum)
    	self.plateActor.GetUserTransform().Identity()
    	self.plateActor.GetUserTransform().Translate(0.0, 0.0, 0.0)

    	# Two shperes
    	sphereLpos_x = self.input_data_pack.x0+self.input_data_pack.L1*sin(self.input_data_pack.th10)
    	sphereLpos_y = self.input_data_pack.h1-self.input_data_pack.L1*cos(self.input_data_pack.th10)
    	self.sphereL.SetCenter(sphereLpos_x*self.len_convert_factor, 0, sphereLpos_y*self.len_convert_factor)

    	sphereRpos_x = self.input_data_pack.x0+self.input_data_pack.L+self.input_data_pack.L2*sin(self.input_data_pack.th20)
    	sphereRpos_y = self.input_data_pack.h2-self.input_data_pack.L2*cos(self.input_data_pack.th20)
    	self.sphereR.SetCenter(sphereRpos_x*self.len_convert_factor, 0, sphereRpos_y*self.len_convert_factor)
    	# Two poles (use two lines stead)
    	platepos = self.input_data_pack.x0+0.5*self.input_data_pack.L
    	poleLlen = self.input_data_pack.h1
    	poleRlen = self.input_data_pack.h2
    	self.LineL.SetPoint1((platepos-self.input_data_pack.L/2)*self.len_convert_factor, 0, poleLlen*self.len_convert_factor)
    	self.LineL.SetPoint2(sphereLpos_x*self.len_convert_factor, 0, sphereLpos_y*self.len_convert_factor)

    	self.LineR.SetPoint1((platepos+self.input_data_pack.L/2)*self.len_convert_factor, 0, poleRlen*self.len_convert_factor)
    	self.LineR.SetPoint2(sphereRpos_x*self.len_convert_factor, 0, sphereRpos_y*self.len_convert_factor)


    	# clean the plot view
    	self.plot_trace.clearAxia()
    	self.plot_trace.axes.set_xlim(-1, 3)
    	self.plot_trace.axes.set_ylim(-1, 3)

    	self.plot_angle.clearAxia()
    	self.plot_angle.axes.set_xlim(0, 10)
    	self.plot_angle.axes.set_ylim(-1.6, 1.6)

    	self.plot_cart_pos.clearAxia()
    	self.plot_cart_pos.axes.set_xlim(0, 10)
    	self.plot_cart_pos.axes.set_ylim(-3, 3)


    	# update the view
    	self.iren.GetRenderWindow().Render()


    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_simulate_clicked(self):
    	"""Simulate button function"""
    	# Get input data from GUI
    	self.input_data_pack.get_input_data(self)

    	# Create pendulum instance
    	self.pendulum = doublePendulum(self.input_data_pack.input_para, \
    		self.input_data_pack.time_info, self.input_data_pack.init_cond)
    	
    	# Start time advancement process
    	self.timer.start(self.input_data_pack.tstep*1000)    # Convert unit from s to ms

    	# Updata the UI widgets to display the instantenous results


    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_update_cam_clicked(self):
    	"""Update camera button function"""
    	self.camCtl.updateCamera(self)








class input_data():
    def __init__(self):
		# Model parameters
    	self.M1 = 1000.0
    	self.M2 = 1000.0
    	self.L1 = 1.0
    	self.L2 = 10.0
    	self.m1 = 1.0
    	self.m2 = 1.0
    	self.h1 = 1.0
    	self.h2 = 10.0
    	self.M = 1.0
    	self.L = 2.0
    	self.input_para = np.array([self.M1, self.M2, self.L1, self.L2, self.m1, self.m2, self.h1, self.h2, self.M, self.L])

		# Initial condition
    	self.x0 = 0.0
    	self.th10 = 1.0
    	self.th20 = -1.0
    	self.dx0 = 0.0
    	self.dth10 = 0.0
    	self.dth20 = 0.0
    	self.init_cond = np.array([self.x0, self.th10, self.th20, self.dx0, self.dth10, self.dth20])

    	# Time information
    	self.ts = 0.0									# start time
    	self.te = 100.0									# end time
    	self.tstep = 0.1								# time step
    	self.time_info = np.array([self.ts, self.te, self.tstep])

    def get_input_data(self, MainWindow):
    	# Model parameters (from table widget)
    	self.M1 = MainWindow.tableWidget.item(0, 0).text().toDouble()[0]
    	self.M2 = MainWindow.tableWidget.item(1, 0).text().toDouble()[0]
    	self.m1 = MainWindow.tableWidget.item(0, 1).text().toDouble()[0]
    	self.m2 = MainWindow.tableWidget.item(1, 1).text().toDouble()[0]
    	self.L1 = MainWindow.tableWidget.item(0, 2).text().toDouble()[0]
    	self.L2 = MainWindow.tableWidget.item(1, 2).text().toDouble()[0]    	
    	self.h1 = MainWindow.tableWidget.item(0, 3).text().toDouble()[0]
    	self.h2 = MainWindow.tableWidget.item(1, 3).text().toDouble()[0]
    	self.M = MainWindow.lineEdit_Cart_M.text().toDouble()[0]
    	self.L = MainWindow.lineEdit_Cart_L.text().toDouble()[0]
    	self.input_para = np.array([self.M1, self.M2, self.L1, self.L2, self.m1, self.m2, self.h1, self.h2, self.M, self.L])

		# Initial condition
    	self.x0 = MainWindow.lineEdit_init_x.text().toDouble()[0]
    	self.th10 = MainWindow.lineEdit_init_th1.text().toDouble()[0]
    	self.th20 = MainWindow.lineEdit_init_th2.text().toDouble()[0]
    	self.dx0 = MainWindow.lineEdit_init_vx.text().toDouble()[0]
    	self.dth10 = MainWindow.lineEdit_init_w1.text().toDouble()[0]
    	self.dth20 = MainWindow.lineEdit_init_w2.text().toDouble()[0]
    	self.init_cond = np.array([self.x0, self.th10, self.th20, self.dx0, self.dth10, self.dth20])

    	# Time information
    	self.ts = MainWindow.lineEdit_time_start.text().toDouble()[0]
    	self.te = MainWindow.lineEdit_time_end.text().toDouble()[0]
    	self.tstep = MainWindow.lineEdit_time_step.text().toDouble()[0]
    	self.time_info = np.array([self.ts, self.te, self.tstep])

    def set_input_data(self, MainWindow):
    	# Model parameters (from table widget)
    	MainWindow.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(str(self.M1)))
    	MainWindow.tableWidget.setItem(1, 0, QtGui.QTableWidgetItem(str(self.M2)))
    	MainWindow.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(str(self.m1)))
    	MainWindow.tableWidget.setItem(1, 1, QtGui.QTableWidgetItem(str(self.m2)))
    	MainWindow.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem(str(self.L1)))
    	MainWindow.tableWidget.setItem(1, 2, QtGui.QTableWidgetItem(str(self.L2)))  	
    	MainWindow.tableWidget.setItem(0, 3, QtGui.QTableWidgetItem(str(self.h1)))
    	MainWindow.tableWidget.setItem(1, 3, QtGui.QTableWidgetItem(str(self.h2)))
    	MainWindow.lineEdit_Cart_M.setText(str(self.M))
    	MainWindow.lineEdit_Cart_L.setText(str(self.L))

		# Initial condition
    	MainWindow.lineEdit_init_x.setText(str(self.x0))
    	MainWindow.lineEdit_init_th1.setText(str(self.th10))
    	MainWindow.lineEdit_init_th2.setText(str(self.th20))
    	MainWindow.lineEdit_init_vx.setText(str(self.dx0))
    	MainWindow.lineEdit_init_w1.setText(str(self.dth10))
    	MainWindow.lineEdit_init_w2.setText(str(self.dth20))

    	# Time information
    	MainWindow.lineEdit_time_start.setText(str(self.ts))
    	MainWindow.lineEdit_time_end.setText(str(self.te))
    	MainWindow.lineEdit_time_step.setText(str(self.tstep))


class result_data():
	"""result_data package"""
	def __init__(self):
		self.tim = []
		self.X1 = []
		self.Y1 = []
		self.X2 = []
		self.Y2 = []
		self.X = []

		self.x = []
		self.th1 = []
		self.th2 = []
		self.dx = []
		self.dth1 = []
		self.dth2 = []

	def getLen(self):
		return len(self.tim)

	def addData(self, result):
		self.tim.append(result[0])
		self.X1.append(result[1])
		self.Y1.append(result[2])
		self.X2.append(result[3])
		self.Y2.append(result[4])
		self.X.append(result[5])

		self.x.append(result[6])
		self.th1.append(result[7])
		self.th2.append(result[8])
		self.dx.append(result[9])
		self.dth1.append(result[10])
		self.dth2.append(result[11])



class MyMplCanvas(FigureCanvas):
	"""Embed the matplotlib into the Qt"""
	def __init__(self, parent=None, width=5, height=4, dpi=100, Ndim=1):
		self.fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = self.fig.add_subplot(111)
		#self.axes.hold(False)

		self.NLine = Ndim			# Number of lines in this plot
		self.lines = []
		self.xdata = []
		self.ydata = []
		for i in range(self.NLine):
			self.xdata.append([])
			self.ydata.append([])
			line, = self.axes.plot([], [])
			self.lines.append(line)

		self.axes.set_xlim(-1, 3)
		self.axes.set_ylim(-1, 3)

		#
		FigureCanvas.__init__(self, self.fig)
		self.setParent(parent)

		#FigureCanvas.setSizePolicy(self,
		#	QtGui.QSizePolicy.Expanding,
		#	QtGui.QSizePolicy.Expanding)

		#FigureCanvas.updateGeometry(self)

	def updateFig(self, data):
		# add the new data points and update the plot
		for i in range(self.NLine):
			self.xdata[i].append(data[i][0])
			self.ydata[i].append(data[i][1])
			self.lines[i].set_data(self.xdata[i], self.ydata[i])
		
		# Update the figure canvas
		self.updateAxisRange()
		self.draw()

	def updateAxisRange(self):
		xlim_min, xlim_max = self.axes.get_xlim()
		ylim_min, ylim_max = self.axes.get_ylim()
		Xmax = np.amax(self.xdata, axis=0)[-1]
		Xmin = np.amin(self.xdata, axis=0)[-1]
		Ymax = np.amax(self.ydata, axis=0)[-1]
		Ymin = np.amin(self.ydata, axis=0)[-1]

		# X limit
		if Xmin < xlim_min:
			if Xmin > 0:
				xlim_min = Xmin/2.0
			else:
				xlim_min = Xmin*2.0

		if Xmax > xlim_max:
			if Xmax > 0:
				xlim_max = Xmax*2.0
			else:
				xlim_max = Xmax/2.0

		# Y limit
		if Ymin < ylim_min:
			if Ymin > 0:
				ylim_min = Ymin/2.0
			else:
				ylim_min = Ymin*2.0

		if Ymax > ylim_max:
			if Ymax > 0:
				ylim_max = Ymax*2.0
			else:
				ylim_max = Ymax/2.0


		self.axes.set_xlim(xlim_min, xlim_max)
		self.axes.set_ylim(ylim_min, ylim_max)	

	def clearAxia(self):
		self.axes.cla()

		self.lines = []
		self.xdata = []
		self.ydata = []
		for i in range(self.NLine):
			self.xdata.append([])
			self.ydata.append([])
			line, = self.axes.plot([], [])
			self.lines.append(line)

		self.axes.set_xlim(-1, 3)
		self.axes.set_ylim(-1, 3)

		self.draw()

class cameraCtl():
	"""Control the camera view"""
	def __init__(self):
		self.bool_sideview = False
		self.bool_track = False

		self.cx = 0.0
		self.cy = -300.0
		self.cz = 0.0

	def updateCamera(self, MainWindow):
		
		if self.bool_sideview:
			camera = MainWindow.ren.GetActiveCamera()
			self.cz = 0.0
			self.cy = -300.0

			if len(MainWindow.result_data_pack.X) == 0:
				self.cx = (MainWindow.input_data_pack.x0+0.5*MainWindow.input_data_pack.L)*MainWindow.len_convert_factor
			else:
				self.cx = MainWindow.result_data_pack.X[-1]

			# update the camera view
			camera.SetPosition(self.cx, self.cy, self.cz)
			camera.SetFocalPoint(self.cx, 0, 0)
			camera.SetViewUp(0, 0, 1)

			MainWindow.ren.GetActiveCamera().UpdateViewport(MainWindow.ren)

		# key line: to adjust the actor within the camera view range
		MainWindow.ren.ResetCamera()
		# Updatet the mainwindow
		MainWindow.iren.GetRenderWindow().Render()
			

	def elev(self, value, MainWindow):
		# for elevation the rotated angle is accumulated
		#angle = (float(value)/MainWindow.horizontalSlider_elevation.maximum()-0.5)*2.0*np.pi
		#angle = np.pi/4.0
		#print("angle=%f"%angle)
		#MainWindow.ren.GetActiveCamera().Elevation(angle)
		#MainWindow.ren.GetActiveCamera().UpdateViewport(MainWindow.ren)
		#MainWindow.iren.GetRenderWindow().Render()

		ele = float(value)/MainWindow.horizontalSlider_elevation.maximum()*300.0
		cx, cy, cz = MainWindow.ren.GetActiveCamera().GetPosition()
		cz = ele

		MainWindow.ren.GetActiveCamera().SetPosition(cx, cy, cz)
		MainWindow.ren.GetActiveCamera().UpdateViewport(MainWindow.ren)
		MainWindow.iren.GetRenderWindow().Render()	
		


if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
 
    window = Ui_MainWindow()

    window.show()

    window.iren.Initialize()

    sys.exit(app.exec_())
