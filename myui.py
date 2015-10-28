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
import doublePendulum

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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(912, 640)
        #centralWidget
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))

        self.m_label = QtGui.QLabel(self.centralWidget)
        self.m_label.setGeometry(QtCore.QRect(750, 70, 91, 17))
        self.m_label.setObjectName(_fromUtf8("m_label"))
        self.m_pushButton = QtGui.QPushButton(self.centralWidget)
        self.m_pushButton.setGeometry(QtCore.QRect(740, 110, 99, 27))
        self.m_pushButton.setObjectName(_fromUtf8("m_pushButton"))

        #vtkWidget
        self.m_widget = QVTKRenderWindowInteractor(self.centralWidget)
        self.m_widget.setGeometry(QtCore.QRect(60, 60, 591, 501))
        self.m_widget.setObjectName(_fromUtf8("m_widget"))
        self.setvtkWidget()

        MainWindow.setCentralWidget(self.centralWidget)

        #menuBar
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 912, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        #toolBar
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        #statusBar
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.m_label.setText(_translate("MainWindow", "Hello world", None))
        self.m_pushButton.setText(_translate("MainWindow", "Say Hi!", None))

    def setvtkWidget(self):
    	self.ren = vtk.vtkRenderer()
        self.m_widget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.m_widget.GetRenderWindow().GetInteractor()
 
        # The car model (includes a plate, two poles and four wheel)
        # Plate of the car
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

        # 4 car's wheels
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


class car():
	def __init__(self):
		self.X = 0.0
		self.Y = 0.0

	def SetCenterPosition(self, cx, cy):
	    self.X = cx
	    self.Y = cy

class vtkTimerCallback():
	def __init__(self):
		m_car.SetCenterPosition(0.0, 0.0)
		self.timer_count = 0

	def execute(self, obj, event):
		print(self.timer_count)
		#self.actor.SetPosition(self.timer_count, 0.0, 0.0)
		self.actor.GetUserTransform().Identity()
		self.actor.GetUserTransform().Translate(float(self.timer_count)/5, 0.0, 0.0)
		iren = obj
		iren.GetRenderWindow().Render()
		self.timer_count += 1

	def restart(self, obj, event):
		# The mouse interaction (zoom)stops the timer
		# Restart the timer after the mouse interaction event
		iren = obj
		iren.ResetTimer(timerId)


if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
 
    window = Ui_MainWindow()

    window.show()

    window.iren.Initialize()

    m_car = car()

    # Sign up to receive TimerEvent
    cb = vtkTimerCallback()
    cb.actor = window.plateActor
    window.iren.AddObserver('TimerEvent', cb.execute)
    window.iren.AddObserver('EndInteractionEvent', cb.restart)
    timerId = window.iren.CreateRepeatingTimer(1000)

    window.iren.Start()
 
    sys.exit(app.exec_())
