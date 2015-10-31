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
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from doublePendulum import doublePendulum

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
		self.setupUi(self)
		self.input_data_pack = input_data()
		self.timer_count = 0

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

        self.checkBox_camera_track = QtGui.QCheckBox(self.groupBox_view)
        self.checkBox_camera_track.setGeometry(QtCore.QRect(20, 30, 98, 22))
        self.checkBox_camera_track.setObjectName(_fromUtf8("checkBox_camera_track"))
        self.checkBox_camera_sideview = QtGui.QCheckBox(self.groupBox_view)
        self.checkBox_camera_sideview.setGeometry(QtCore.QRect(20, 60, 98, 22))
        self.checkBox_camera_sideview.setObjectName(_fromUtf8("checkBox_camera_sideview"))

        self.horizontalSlider_pos = QtGui.QSlider(self.groupBox_view)
        self.horizontalSlider_pos.setGeometry(QtCore.QRect(100, 90, 241, 29))
        self.horizontalSlider_pos.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pos.setObjectName(_fromUtf8("horizontalSlider_pos"))

        self.label_pos = QtGui.QLabel(self.groupBox_view)
        self.label_pos.setGeometry(QtCore.QRect(20, 100, 67, 17))
        self.label_pos.setObjectName(_fromUtf8("label_pos"))

        # Functional Button
        self.pushButton_save_input = QtGui.QPushButton(self.frame)
        self.pushButton_save_input.setGeometry(QtCore.QRect(10, 630, 115, 35))
        self.pushButton_save_input.setObjectName(_fromUtf8("pushButton_save_input"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/export_database_icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save_input.setIcon(icon)
        self.pushButton_save_input.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_import_input = QtGui.QPushButton(self.frame)
        self.pushButton_import_input.setGeometry(QtCore.QRect(140, 630, 115, 35))
        self.pushButton_import_input.setObjectName(_fromUtf8("pushButton_import_input"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/Import_Data.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_import_input.setIcon(icon)
        self.pushButton_import_input.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_save_result = QtGui.QPushButton(self.frame)
        self.pushButton_save_result.setGeometry(QtCore.QRect(270, 630, 115, 35))
        self.pushButton_save_result.setObjectName(_fromUtf8("pushButton_save_result"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/save_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save_result.setIcon(icon)
        self.pushButton_save_result.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_reset = QtGui.QPushButton(self.frame)
        self.pushButton_reset.setGeometry(QtCore.QRect(140, 700, 115, 35))
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_reset.setIcon(icon)
        self.pushButton_reset.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_start = QtGui.QPushButton(self.frame)
        self.pushButton_start.setGeometry(QtCore.QRect(270, 700, 115, 35))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/tick_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start.setIcon(icon)
        self.pushButton_start.setIconSize(QtCore.QSize(20, 20))

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
        self.plot_trace = MyStaticMplCanvas(self.centralWidget, width=1, height=1, dpi=50)
        self.plot_trace.setObjectName(_fromUtf8("plot_trace"))

        self.plot_angle = MyStaticMplCanvas(self.centralWidget, width=1, height=1, dpi=50)
        self.plot_angle.setObjectName(_fromUtf8("plot_angle"))

        self.plot_cart_pos = MyStaticMplCanvas(self.centralWidget, width=1, height=1, dpi=50)
        self.plot_cart_pos.setObjectName(_fromUtf8("plot_cart_pos"))        

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

        self.mainToolBar.addAction(self.actionStart)
        self.mainToolBar.addAction(self.actionStop)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionHelp)
        self.mainToolBar.addAction(self.actionAbout)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)


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
        self.checkBox_camera_track.setText(_translate("MainWindow", "tracking", None))
        self.checkBox_camera_sideview.setText(_translate("MainWindow", "side view", None))
        self.label_pos.setText(_translate("MainWindow", "position", None))

        self.pushButton_save_input.setText(_translate("MainWindow", "Save Input", None))
        self.pushButton_import_input.setText(_translate("MainWindow", "Import Input", None))
        self.pushButton_save_result.setText(_translate("MainWindow", "Save Result", None))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset", None))
        self.pushButton_start.setText(_translate("MainWindow", "Start", None))

        # Toolbar action
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionStart.setToolTip(_translate("MainWindow", "Start", None))
        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionStop.setToolTip(_translate("MainWindow", "Stop", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp.setToolTip(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout.setToolTip(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit", None))

    def setvtkWidget(self):
    	"""Set up the vtk widget"""
    	self.ren = vtk.vtkRenderer()
        self.widget_vtk.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.widget_vtk.GetRenderWindow().GetInteractor()
 
        # The cart model (includes a plate, two poles and four wheel)
        # Plate of the cart
        # Create source
        plate = vtk.vtkCubeSource()
        plate.SetXLength(100)
        plate.SetYLength(60)
        plate.SetZLength(6)
        plate.SetCenter(50, 0, -3)
 
        # Create a mapper
        plateMapper = vtk.vtkPolyDataMapper()
        plateMapper.SetInputConnection(plate.GetOutputPort())

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
        poleL = vtk.vtkCylinderSource()
        poleL.SetRadius(1.0)
        poleL.SetHeight(50.0)
        poleL.SetCenter(10, 0, 0)
        poleL.SetResolution(100.0)

        # Create a mapper
        poleLMapper = vtk.vtkPolyDataMapper()
        poleLMapper.SetInputConnection(poleL.GetOutputPort())

        # Create a transform
        poleLTransform = vtk.vtkTransform()
        poleLTransform.SetInput(plateTransform)

        # Create an actor
        poleLActor = vtk.vtkActor()
        poleLActor.SetMapper(poleLMapper)
        poleLActor.SetUserTransform(poleLTransform)

        poleLTransform.RotateX(90.0)
        poleLTransform.Translate(0.0, 25.0, 0.0)

        self.ren.AddActor(poleLActor)

        # Right pole
        # Create source
        poleR = vtk.vtkCylinderSource()
        poleR.SetRadius(1.0)
        poleR.SetHeight(50.0)
        poleR.SetCenter(90, 0, 0)
        poleR.SetResolution(100.0)

        # Create a mapper
        poleRMapper = vtk.vtkPolyDataMapper()
        poleRMapper.SetInputConnection(poleR.GetOutputPort())

        # Create a transform
        poleRTransform = vtk.vtkTransform()
        poleRTransform.SetInput(plateTransform)

        # Create an actor
        poleRActor = vtk.vtkActor()
        poleRActor.SetMapper(poleRMapper)
        poleRActor.SetUserTransform(poleRTransform)

        poleRTransform.RotateX(90.0)
        poleRTransform.Translate(0.0, 25.0, 0.0)

        self.ren.AddActor(poleRActor)

        # 4 cart's wheels
        wheel = []
        wheelMapper = []
        wheelTransform = []
        wheelActor = []
        for i in range(4):
        	# Create source
            wheel.append(vtk.vtkCylinderSource())
            wheel[i].SetRadius(6.0)
            wheel[i].SetHeight(3.0)
            wheel[i].SetResolution(100.0)

        	# Create a mapper
            wheelMapper.append(vtk.vtkPolyDataMapper())
            wheelMapper[i].SetInputConnection(wheel[i].GetOutputPort())

            # Create a transform
            wheelTransform.append(vtk.vtkTransform())
            wheelTransform[i].SetInput(plateTransform)

        	# Create an actor
            wheelActor.append(vtk.vtkActor())
            wheelActor[i].SetMapper(wheelMapper[i])
            wheelActor[i].SetUserTransform(wheelTransform[i])
            wheelActor[i].GetProperty().SetColor(1.0, 1.0, 0.6)

            self.ren.AddActor(wheelActor[i])
        
        wheel[0].SetCenter(10, 25, -9.0)
        wheel[1].SetCenter(90, 25, -9.0)
        wheel[2].SetCenter(10, -25, -9.0)
        wheel[3].SetCenter(90, -25, -9.0)


        # Two spheres' model
        # Left sphere
        # Create source
        sphereL = vtk.vtkSphereSource()
        sphereL.SetRadius(5)
        sphereL.SetCenter(0, 0, 30)

        # Create a mapper
        sphereLMapper = vtk.vtkPolyDataMapper()
        sphereLMapper.SetInputConnection(sphereL.GetOutputPort())

        # Create an actor
        sphereLActor = vtk.vtkActor()
        sphereLActor.SetMapper(sphereLMapper)
        sphereLActor.GetProperty().SetColor(1.0, 0.2, 0.2)

        self.ren.AddActor(sphereLActor)

        # Right sphere
        # Create source
        sphereR = vtk.vtkSphereSource()
        sphereR.SetRadius(5)
        sphereR.SetCenter(100, 0, 30)

        # Create a mapper
        sphereRMapper = vtk.vtkPolyDataMapper()
        sphereRMapper.SetInputConnection(sphereR.GetOutputPort())

        # Create an actor
        sphereRActor = vtk.vtkActor()
        sphereRActor.SetMapper(sphereRMapper)
        sphereRActor.GetProperty().SetColor(0.0, 0.5, 1.0)

        self.ren.AddActor(sphereRActor)

        # Create a camera
        #self.ren.ResetCamera()
        camera = vtk.vtkCamera()
        self.ren.SetActiveCamera(camera)
        self.ren.GetActiveCamera().SetPosition(50, -300, 100)
        self.ren.GetActiveCamera().SetFocalPoint(50, 0, 0)
        self.ren.GetActiveCamera().SetViewUp(0, 0, 1)
        self.ren.GetActiveCamera().UpdateViewport(self.ren)

    

    def timerCallback(self):
		"""Timer callback function"""
		print(self.timer_count)
		self.plateActor.GetUserTransform().Identity()
		self.plateActor.GetUserTransform().Translate(self.timer_count, 0.0, 0.0)
		
		self.iren.GetRenderWindow().Render()
		self.timer_count += 1

    # Toolbar button slot
    def on_actionStart_triggered(self):
    	"""Start button slot"""
    	timer.start(100)

    def on_actionStop_triggered(self):
    	"""Stop button slot"""
    	timer.stop()

    def on_actionExit_triggered(self):
    	"""Toolbar start button slot"""
    	self.close()

    	
    # PushButton slot
    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_start_clicked(self):
    	"""Start button function"""
    	self.input_data_pack.get_input_data(self)
    	value = self.input_data_pack.M1
    	print("hello world%f"%value)

    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_save_input_clicked(self):
    	"""Save input button function"""
    	self.input_data_pack.get_input_data(self)
    	filename = QtGui.QFileDialog.getSaveFileName(self, "Save Input file", "/home/hz")
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
    	"""Save input button function"""
    	filename = QtGui.QFileDialog.getOpenFileName(self, "Open Input file", "/home/hz")
    	data = []
    	with open(filename, 'r') as f:
    		for line in f.readlines():
    			data.append(float(line.strip()))
    	print data
    	# Model parameter
    	self.input_data_pack.M1 = data[0]
    	self.input_data_pack.M2 = data[1]
     	self.input_data_pack.m1 = data[2]
    	self.input_data_pack.m2 = data[3]   		
    	self.input_data_pack.L1 = data[4]
    	self.input_data_pack.L2 = data[5]
    	self.input_data_pack.h1 = data[6]
    	self.input_data_pack.h2 = data[7]
     	self.input_data_pack.M = data[8]
    	self.input_data_pack.L = data[9]

    	# Init condition
    	self.input_data_pack.x0 = data[10]
    	self.input_data_pack.th10 = data[11]
     	self.input_data_pack.th20 = data[12]
    	self.input_data_pack.dx0 = data[13]   		
    	self.input_data_pack.dth10 = data[14]
    	self.input_data_pack.dth20 = data[15]

    	# Time info
    	self.input_data_pack.ts = data[16]
    	self.input_data_pack.te = data[17]
     	self.input_data_pack.tstep = data[18]

		#
    	self.input_data_pack.set_input_data(self)


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
    	self.tstep = 0.01								# time step
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


class MyMplCanvas(FigureCanvas):
	"""Embed the matplotlib into the Qt"""
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		self.axes.hold(False)
		self.compute_initial_figure()

		#
		FigureCanvas.__init__(self, fig)
		self.setParent(parent)

		#FigureCanvas.setSizePolicy(self,
		#	QtGui.QSizePolicy.Expanding,
		#	QtGui.QSizePolicy.Expanding)

		#FigureCanvas.updateGeometry(self)

	def compute_initial_figure(self):
		pass

class MyStaticMplCanvas(MyMplCanvas):
	def compute_initial_figure(self):
		t = np.arange(0.0, 3.0, 0.01)
		s = sin(2*3.14*t)
		self.axes.plot(t, s)



if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
 
    window = Ui_MainWindow()

    window.show()

    window.iren.Initialize()

    # Setup timer
    timer = QtCore.QTimer(window)
    timer.timeout.connect(window.timerCallback)

	# Create pendulum instance
    #pendulum = doublePendulum(input_para, time_info, init_cond)

    sys.exit(app.exec_())
