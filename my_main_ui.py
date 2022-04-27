# -*- coding: utf-8 -*-

"""
__author__ = xujing
__date__  = 2019-07-05
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_my_main_ui import Ui_MainWindow
import sys
import cv2
from car_id_detect import *
from svm_train import *
from card_seg import *
import time

DEFAULT_PATH = "./test_img/wAUB816.jpg"
class MainWindow(QMainWindow, Ui_MainWindow):
    """
    槽函数
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        最小化
        """
        print('最小化')
        QMainWindow.showMinimized(self)

    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        退出
        """
        print("退出")
        sys.exit(0)

    @pyqtSlot()
    def on_pushButton_6_clicked(self,path):
        """
        加载图像
        """
        print("加载图像")
        try:
            if path != "":
                self.file_dir = path
            else:
                self.file_dir_temp, _ = QFileDialog.getOpenFileName(self, "选择被检测的车辆")
                self.file_dir = self.file_dir_temp.replace("\\", "/")
            if self.file_dir == '':
                print('未选择图片')
                return
            print(self.file_dir)
            # 计时
            time_start = time.time()
            # roi为图片
            roi, label, color = CaridDetect(self.file_dir)
            seg_dict, _, pre = Cardseg([roi], [color], None)
            print(pre)

            # ui相关操作
            cv2.imwrite(os.path.join("./temp/seg_card.jpg"), roi)
            seg_img = cv2.imread("./temp/seg_card.jpg")
            seg_rows, seg_cols, seg_channels = seg_img.shape
            bytesPerLine = seg_channels * seg_cols
            cv2.cvtColor(seg_img, cv2.COLOR_BGR2RGB, seg_img)
            QImg = QImage(seg_img.data, seg_cols, seg_rows,
                          bytesPerLine, QImage.Format_RGB888)
            self.label_2.setPixmap(QPixmap.fromImage(QImg).scaled(self.label_2.size(),
                                                                  Qt.KeepAspectRatio, Qt.SmoothTransformation))

            # reg result
            pre.insert(2, "·")
            self.label_3.setText(" "+"".join(pre))

            # clor view
            if color == "yello":
                self.label_4.setStyleSheet(
                    "background-color: rgb(255, 255, 0);")
            elif color == "green":
                self.label_4.setStyleSheet("background-color: rgb(0, 255,0);")
            elif color == "blue":
                self.label_4.setStyleSheet("background-color: rgb(0, 0, 255);")
            else:
                self.label_4.setText("未识别出车牌颜色")

            frame = cv2.imread(self.file_dir)
            # cv2.rectangle(frame, (label[0],label[2]), (label[1],label[3]), (0,0,255), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            img_rows, img_cols, channels = frame.shape
            bytesPerLine = channels * img_cols
            cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
            QImg = QImage(frame.data, img_cols, img_rows,
                          bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(QImg).scaled(self.label.size(),
                                                                Qt.KeepAspectRatio, Qt.SmoothTransformation))
            QtWidgets.QApplication.processEvents()
            time_end = time.time()
            print('time cost', time_end-time_start, 's')
        except Exception as e:
            QMessageBox.warning(self, "错误提示", str(e))

    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        加载视频
        """
        print("加载视频")
        QMessageBox.information(self, "加载实时视频", "未检测到实时视频源或暂未开通快该服务！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()
    ui = MainWindow()
    ui.on_pushButton_6_clicked(DEFAULT_PATH) # 默认图像
    ui.show()
    # splash.finish(ui)

    sys.exit(app.exec_())
