# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v0_2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from time import strftime, gmtime
import sys,os
import RPi.GPIO as GPIO
global LED_state
LED_state=False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 429)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.NIR = QtWidgets.QWidget()
        self.NIR.setObjectName("NIR")
        self.AcquireImage = QtWidgets.QPushButton(self.NIR)
        self.AcquireImage.setGeometry(QtCore.QRect(20, 10, 281, 61))
        self.AcquireImage.setObjectName("AcquireImage")
        self.AcquireImage.clicked.connect(acquire_image_wrapper)
        self.ToggleLED = QtWidgets.QRadioButton(self.NIR)
        self.ToggleLED.setGeometry(QtCore.QRect(310, 30, 111, 21))
        self.ToggleLED.setObjectName("ToggleLED")
        self.ToggleLED.clicked.connect(toggle_LED_wrapper)
        self.imagePreview = QtWidgets.QGraphicsView(self.NIR)
        self.imagePreview.setGeometry(QtCore.QRect(20, 80, 561, 241))
        self.imagePreview.setObjectName("imagePreview")
        self.patientNumber = QtWidgets.QTextEdit(self.NIR)
        self.patientNumber.setGeometry(QtCore.QRect(420, 30, 161, 21))
        self.patientNumber.setObjectName("patientNumber")
        self.tabWidget.addTab(self.NIR, "")
        self.SPO2 = QtWidgets.QWidget()
        self.SPO2.setObjectName("SPO2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.SPO2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spo2Output = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.spo2Output.setObjectName("spo2Output")
        self.gridLayout_3.addWidget(self.spo2Output, 0, 0, 1, 1)
        self.initSPO2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.initSPO2.setObjectName("initSPO2")
        self.gridLayout_3.addWidget(self.initSPO2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.SPO2, "")
        self.ECG = QtWidgets.QWidget()
        self.ECG.setObjectName("ECG")
        self.tabWidget.addTab(self.ECG, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPreferences = QtWidgets.QMenu(self.menubar)
        self.menuPreferences.setObjectName("menuPreferences")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPulse_Oximeter = QtWidgets.QAction(MainWindow)
        self.actionPulse_Oximeter.setObjectName("actionPulse_Oximeter")
        self.actionIR_Camera = QtWidgets.QAction(MainWindow)
        self.actionIR_Camera.setObjectName("actionIR_Camera")
        self.actionECG = QtWidgets.QAction(MainWindow)
        self.actionECG.setObjectName("actionECG")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuPreferences.addAction(self.actionPulse_Oximeter)
        self.menuPreferences.addAction(self.actionIR_Camera)
        self.menuPreferences.addAction(self.actionECG)
        self.menuPreferences.addSeparator()
        self.menuView.addAction(self.actionTest)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Raspberry Pi Monitor v-0.2"))
        self.AcquireImage.setText(_translate("MainWindow", "Acquire Image"))
        self.ToggleLED.setText(_translate("MainWindow", "Toggle LED"))
        self.patientNumber.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Patient #:</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.NIR), _translate("MainWindow", "NIR Imaging"))
        self.initSPO2.setText(_translate("MainWindow", "Initialize SPO2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SPO2), _translate("MainWindow", "Pulse Oximetry"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ECG), _translate("MainWindow", "ECG"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPreferences.setTitle(_translate("MainWindow", "Preferences"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionPulse_Oximeter.setText(_translate("MainWindow", "Pulse Oximeter"))
        self.actionIR_Camera.setText(_translate("MainWindow", "IR Camera"))
        self.actionECG.setText(_translate("MainWindow", "ECG"))
        self.actionTest.setText(_translate("MainWindow", "Test"))

def acquire_image_wrapper():
    # wrapper for AcquireImage.connect() slot
    # Calls acquire_image()
    acquire_image(strftime("%a,%d%Y%H:%M:%S", gmtime()))

def acquire_image(current_time):
    # Should create image using Pi NoIR using time stamp as file name
    # File will end up on default path /home/pi
    os.system('raspistill -o %s.png'%current_time)
    #print("It is %s"%current_time)

def toggle_LED_wrapper():
    # wrapper for ToggleLED radio button
    # Calls toggle_LED
    toggle_LED()

def toggle_LED():
    LED_state = not LED_state
    GPIO.output(12, LED_state)

def init_GPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    init_GPIO()
    #os.system('matchbox-keyboard')
    sys.exit(app.exec_())

