# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarim.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1031, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(460, 20, 201, 81))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 30, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 170, 401, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(190, 30, 181, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(110, 20, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(110, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 81, 23))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 72, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 120, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(780, 170, 181, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 60, 141, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 137, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.spinBox_2 = QtWidgets.QSpinBox(self.layoutWidget1)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(50)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(500, 190, 181, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.label_23.setObjectName("label_23")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox.setEnabled(False)
        self.comboBox.setGeometry(QtCore.QRect(50, 30, 111, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_16.setGeometry(QtCore.QRect(160, 430, 681, 51))
        self.groupBox_16.setObjectName("groupBox_16")
        self.label_39 = QtWidgets.QLabel(self.groupBox_16)
        self.label_39.setGeometry(QtCore.QRect(460, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: ")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_16)
        self.label_40.setGeometry(QtCore.QRect(590, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: bl")
        self.label_40.setObjectName("label_40")
        self.label_26 = QtWidgets.QLabel(self.groupBox_16)
        self.label_26.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label_26.setStyleSheet("color: green;")
        self.label_26.setObjectName("label_26")
        self.label_41 = QtWidgets.QLabel(self.groupBox_16)
        self.label_41.setGeometry(QtCore.QRect(200, 20, 251, 16))
        self.label_41.setStyleSheet("color: blue")
        self.label_41.setObjectName("label_41")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(890, 20, 111, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("asset/statistics.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setEnabled(True)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 100, 301, 171))
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setEnabled(False)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 80, 131, 80))
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_11.setObjectName("label_11")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_9)
        self.spinBox_4.setGeometry(QtCore.QRect(80, 20, 42, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(300)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_9)
        self.spinBox_5.setGeometry(QtCore.QRect(80, 50, 42, 22))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(300)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox_9)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_12.setObjectName("label_12")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_4.setGeometry(QtCore.QRect(170, 50, 101, 17))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_10.setGeometry(QtCore.QRect(170, 80, 111, 80))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox_10)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_10)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_14.setObjectName("label_14")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_8)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 20, 104, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_8)
        self.layoutWidget3.setGeometry(QtCore.QRect(150, 20, 126, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_34 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_4.addWidget(self.label_34)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_11.setGeometry(QtCore.QRect(20, 10, 981, 51))
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_16 = QtWidgets.QLabel(self.groupBox_11)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 111, 16))
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.groupBox_11)
        self.label_19.setGeometry(QtCore.QRect(270, 20, 71, 16))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.groupBox_11)
        self.label_21.setGeometry(QtCore.QRect(350, 20, 81, 16))
        self.label_21.setObjectName("label_21")
        self.label_32 = QtWidgets.QLabel(self.groupBox_11)
        self.label_32.setGeometry(QtCore.QRect(130, 20, 111, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_11)
        self.label_33.setGeometry(QtCore.QRect(460, 20, 501, 16))
        self.label_33.setObjectName("label_33")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(740, 240, 201, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_20.setGeometry(QtCore.QRect(690, 110, 311, 101))
        self.groupBox_20.setObjectName("groupBox_20")
        self.label_25 = QtWidgets.QLabel(self.groupBox_20)
        self.label_25.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_25.setObjectName("label_25")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_17 = QtWidgets.QLabel(self.groupBox_20)
        self.label_17.setGeometry(QtCore.QRect(20, 70, 241, 16))
        self.label_17.setObjectName("label_17")
        self.label_46 = QtWidgets.QLabel(self.tab)
        self.label_46.setGeometry(QtCore.QRect(40, 370, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.tab)
        self.label_47.setGeometry(QtCore.QRect(140, 370, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color:\"green\"")
        self.label_47.setObjectName("label_47")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(340, 100, 321, 171))
        self.groupBox_7.setObjectName("groupBox_7")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 20, 281, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 50, 246, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.spinBox_3 = QtWidgets.QSpinBox(self.layoutWidget4)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(10)
        self.spinBox_3.setProperty("value", 3)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_5.addWidget(self.spinBox_3)
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_7)
        self.groupBox_15.setGeometry(QtCore.QRect(20, 110, 111, 51))
        self.groupBox_15.setObjectName("groupBox_15")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_15)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_13.setGeometry(QtCore.QRect(160, 430, 681, 51))
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_28 = QtWidgets.QLabel(self.groupBox_13)
        self.label_28.setGeometry(QtCore.QRect(460, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_13)
        self.label_29.setGeometry(QtCore.QRect(590, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_5 = QtWidgets.QLabel(self.groupBox_13)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label_5.setStyleSheet("color: green")
        self.label_5.setObjectName("label_5")
        self.label_35 = QtWidgets.QLabel(self.groupBox_13)
        self.label_35.setGeometry(QtCore.QRect(200, 20, 251, 16))
        self.label_35.setStyleSheet("color: blue")
        self.label_35.setObjectName("label_35")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(50, 30, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 30, 171, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setGeometry(QtCore.QRect(140, 80, 141, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(460, 280, 91, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(570, 280, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(470, 30, 261, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(890, 20, 111, 101))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("asset/test.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(20, 80, 111, 41))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap("asset/tensorboard-logo-social.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_12.setGeometry(QtCore.QRect(30, 150, 391, 241))
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_27 = QtWidgets.QLabel(self.groupBox_12)
        self.label_27.setGeometry(QtCore.QRect(10, 20, 371, 211))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_14.setGeometry(QtCore.QRect(540, 350, 331, 141))
        self.groupBox_14.setObjectName("groupBox_14")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_14)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 311, 111))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(880, 430, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cinsiyet algılayıcı"))
        self.pushButton.setText(_translate("MainWindow", "Yükle"))
        self.groupBox.setTitle(_translate("MainWindow", "Veri seti içeriği"))
        self.pushButton_2.setText(_translate("MainWindow", "Bilgi"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Veri seti böl"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Bilgiler"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Test resim adeti:"))
        self.label_4.setText(_translate("MainWindow", "Eğitim resim adeti:"))
        self.pushButton_3.setText(_translate("MainWindow", "Böl"))
        self.label.setText(_translate("MainWindow", "Test seti (%):"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Veri arttır"))
        self.pushButton_4.setText(_translate("MainWindow", "Veri arttır"))
        self.label_20.setText(_translate("MainWindow", "Arttırma oranı (%):"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Veri seti seç"))
        self.label_23.setText(_translate("MainWindow", "Seç:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Normal veri seti"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Veri seti bilgileri"))
        self.label_39.setText(_translate("MainWindow", "Resim sayısı: 0"))
        self.label_40.setText(_translate("MainWindow", "Sınıf sayısı: 0"))
        self.label_26.setText(_translate("MainWindow", "Veri seti: -"))
        self.label_41.setText(_translate("MainWindow", "Test oranı: 0%, Eğitim oranı: 0%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Veri Seti"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Eğitim"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Özel ayarlar"))
        self.label_11.setText(_translate("MainWindow", "Epochs:"))
        self.label_12.setText(_translate("MainWindow", "Batch size:"))
        self.radioButton_3.setText(_translate("MainWindow", "Özel ayar"))
        self.radioButton_4.setText(_translate("MainWindow", "Varsayılan ayar"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Özel ayarlar"))
        self.label_13.setText(_translate("MainWindow", "Epochs: 60"))
        self.label_14.setText(_translate("MainWindow", "Batch size: 64"))
        self.label_15.setText(_translate("MainWindow", "Model:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "AlexNet"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "VGG16"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "VGG19"))
        self.label_34.setText(_translate("MainWindow", "Optimizer:"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Adam"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "SGD"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Adadelta"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "Adagrad"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "RMSprop"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Eğtim bilgileri"))
        self.label_16.setText(_translate("MainWindow", "Model: AlexNet"))
        self.label_19.setText(_translate("MainWindow", "Epochs: 60"))
        self.label_21.setText(_translate("MainWindow", "Batch size: 64"))
        self.label_32.setText(_translate("MainWindow", "Optimizer: Adam"))
        self.label_33.setText(_translate("MainWindow", "Ek özellikler: TensorBoard"))
        self.pushButton_5.setText(_translate("MainWindow", "Eğit"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Model adı"))
        self.label_25.setText(_translate("MainWindow", "Adı:"))
        self.pushButton_9.setText(_translate("MainWindow", "Onayal"))
        self.label_17.setText(_translate("MainWindow", "Tam ad:  -"))
        self.label_46.setText(_translate("MainWindow", "İşlem durumu:"))
        self.label_47.setText(_translate("MainWindow", "-"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Ek özellikler"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Early stopping"))
        self.checkBox.setText(_translate("MainWindow", "Uygula"))
        self.label_9.setText(_translate("MainWindow", "İyileşme olmayan maksimum epoch sayısı: "))
        self.groupBox_15.setTitle(_translate("MainWindow", "Model check point"))
        self.checkBox_2.setText(_translate("MainWindow", "Uygula"))
        self.groupBox_13.setTitle(_translate("MainWindow", "Veri seti bilgileri"))
        self.label_28.setText(_translate("MainWindow", "Resim sayısı: 0"))
        self.label_29.setText(_translate("MainWindow", "Sınıf sayısı: 0"))
        self.label_5.setText(_translate("MainWindow", "Veri seti: -"))
        self.label_35.setText(_translate("MainWindow", "Test oranı: 0%, Eğitim oranı: 0%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Eğitim"))
        self.label_22.setText(_translate("MainWindow", "Model Seç:"))
        self.pushButton_7.setText(_translate("MainWindow", "TensorBoard Bilgi Göster"))
        self.pushButton_6.setText(_translate("MainWindow", "Test"))
        self.label_10.setText(_translate("MainWindow", "-"))
        self.label_18.setText(_translate("MainWindow", "Test resmi"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Confusion matrix"))
        self.label_27.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Diğer başarı bilgileri"))
        self.pushButton_8.setText(_translate("MainWindow", "Bilgi getir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Test Ve Bilgi"))
