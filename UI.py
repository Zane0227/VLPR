import sys

import cv2
import qtawesome
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QCursor, QImage, QPixmap

import my_pic_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        qss1 = '''
        QPushButton{border:none;color:#1F2F3D;font-size:22px;font-weight:700;}
        '''
        # 圆角窗口
        qss2 = '''#MainWindow{background:white;border-radius:30px}
        '''
        # 下拉列表样式
        qss3 = '''QComboBox{
            border: 1px solid cyan;
            border-radius:2px;
            color: white;
            select-background-color:cyan;
            background-color:black;
            selection-color:black;
        }
        '''
        # button 6,7
        qss6 = '''
        QPushButton
        {  
            font-size:16px;
            font-weight:900;
            font-family: "Helvetica Neue", Helvetica, Arial;
            color: #409eff;  
            background-color: #ecf5ff;  
            border-style:outset;  
            border-width:2px;
            border-radius:10px;  
            min-width:50px;  
            min-height:20px;  
            padding:4px;  
        } 
         
        /*鼠标悬浮时的效果*/
        QPushButton:hover
        {
            color: white;
            background-color: #409eff; /*改变背景色*/
            border-style:inset;/*改变边框风格*/
            padding-left:3px;
            padding-top:3px;
        }

        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 600)
        MainWindow.setStyleSheet(qss2)
        MainWindow.setFixedSize(
            MainWindow.width(), MainWindow.height())  # 不可调整宽高
        # 左侧图像
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.centralWidget.setStyleSheet(qss3)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 611, 501))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        # 车牌图像
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 90, 191, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(qss1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(700, 140, 181, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        # 识别结果
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 230, 191, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(qss1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(705, 280, 171, 41))
        self.label_3.setAlignment(
            QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.label_3.setStyleSheet(
            "color: black;font-size: 24px;font-weight:1000;border-radius:10px;background-color: #f5f5f5")

        # 车牌颜色
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 360, 181, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(qss1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(700, 400, 181, 41))
        self.label_4.setText("")
        self.label_4.setStyleSheet("background-color: blue")
        self.label_4.setObjectName("label_4")

        # 底部按钮
        self.pushButton_6 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 492, 75, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(qss6)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(810, 490, 71, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet(qss6)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "交通门禁车牌检测和识别系统"))
        self.pushButton_3.setText(_translate("MainWindow", "车牌图像"))
        self.pushButton_4.setText(_translate("MainWindow", "识别结果"))
        self.pushButton_5.setText(_translate("MainWindow", "车牌颜色"))
        self.pushButton_6.setText(_translate("MainWindow", "图像"))
        self.pushButton_7.setText(_translate("MainWindow", "视频"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
