# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt, QLine
from PyQt5.QtGui import QImage, QIcon
import cv2
import imutils


class Ui_Editor(QFileDialog):
    def setupUi(self, PhotoEditor):
        PhotoEditor.setObjectName("PhotoEditor")
        PhotoEditor.resize(990, 846)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/photo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PhotoEditor.setWindowIcon(icon)
        PhotoEditor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                  " stop:0 rgba(196, 242, 237, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label = QtWidgets.QLabel(PhotoEditor)
        self.label.setGeometry(QtCore.QRect(10, 5, 971, 21))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                 " stop:0 rgba(196, 242, 237, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                 "font: 75 italic 18pt \"Times New Roman\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton.setGeometry(QtCore.QRect(850, 590, 121, 71))
        self.pushButton.setStyleSheet("font: 75 italic 16pt \"Times New Roman\";\n"
                                      "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69),"
                                      " stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145),"
                                      " stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130),"
                                      " stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255),"
                                      " stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69),"
                                      " stop:1 rgba(255, 255, 0, 69));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 680, 121, 71))
        self.pushButton_2.setStyleSheet("font: 75 italic 16pt \"Times New Roman\";\n"
                                        "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69),"
                                        " stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145),"
                                        " stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130),"
                                        " stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255),"
                                        " stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69),"
                                        " stop:1 rgba(255, 255, 0, 69));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton_3.setGeometry(QtCore.QRect(650, 590, 121, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 255);\n"
                                        "background-color: rgb(0, 170, 255);\n"
                                        "font: 75 italic 16pt \"Times New Roman\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 590, 121, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 0);\n"
                                        "font: 75 italic 16pt \"Times New Roman\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 590, 121, 31))
        self.pushButton_5.setStyleSheet("font: 75 italic 16pt \"Times New Roman\";\n"
                                        "background-color: rgb(255, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton_6.setGeometry(QtCore.QRect(132, 640, 121, 51))
        self.pushButton_6.setStyleSheet("font: 75 italic 16pt \"Times New Roman\";\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                        " stop:0 rgba(242, 97, 72, 255),"
                                        " stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 640, 121, 51))
        self.pushButton_7.setStyleSheet("font: 75 italic 16pt \"Times New Roman\";\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                        " stop:0 rgba(38, 242, 75, 255),"
                                        " stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(PhotoEditor)
        self.pushButton_8.setGeometry(QtCore.QRect(650, 640, 121, 51))
        self.pushButton_8.setStyleSheet("font: 75 italic 16pt \"Times New Roman\";\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                        " stop:0 rgba(61, 167, 242, 255),"
                                        " stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_5 = QtWidgets.QLabel(PhotoEditor)
        self.label_5.setGeometry(QtCore.QRect(10, 710, 131, 20))
        self.label_5.setStyleSheet("font: 75 italic 8pt \"Times New Roman\";\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                   " stop:0 rgba(196, 242, 237, 255),"
                                   " stop:1 rgba(255, 255, 255, 255));")
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(PhotoEditor)
        self.label_2.setGeometry(QtCore.QRect(160, 710, 111, 16))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                   " stop:0 rgba(196, 242, 237, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "font: 75 italic 8pt \"Times New Roman\";\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(PhotoEditor)
        self.label_3.setGeometry(QtCore.QRect(290, 710, 101, 20))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                   " stop:0 rgba(196, 242, 237, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "font: 75 italic 8pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(PhotoEditor)
        self.label_4.setGeometry(QtCore.QRect(410, 710, 121, 16))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                   " stop:0 rgba(196, 242, 237, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "font: 75 italic 8pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(PhotoEditor)
        self.label_6.setGeometry(QtCore.QRect(650, 710, 121, 21))
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                   " stop:0 rgba(196, 242, 237, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                   "font: 75 italic 8pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(PhotoEditor)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 971, 541))
        self.label_7.setStyleSheet("border-color: rgb(0, 0, 0);\n"
                                   "border-color: rgb(0, 0, 0);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("C:/Users/79235/Programming tools/envs/env/Images/alps.jpg"))
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(PhotoEditor)
        self.lineEdit.setGeometry(QtCore.QRect(10, 731, 131, 31))
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                    " stop:0 rgba(145, 242, 113, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(PhotoEditor)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 730, 111, 31))
        self.lineEdit_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                      " stop:0 rgba(145, 242, 113, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(PhotoEditor)
        self.lineEdit_3.setGeometry(QtCore.QRect(292, 730, 101, 31))
        self.lineEdit_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                      " stop:0 rgba(145, 242, 113, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(PhotoEditor)
        self.lineEdit_4.setGeometry(QtCore.QRect(410, 730, 121, 31))
        self.lineEdit_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                      " stop:0 rgba(145, 242, 113, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(PhotoEditor)
        self.lineEdit_5.setGeometry(QtCore.QRect(650, 730, 113, 31))
        self.lineEdit_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
                                      " stop:0 rgba(145, 242, 113, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(PhotoEditor)
        self.pushButton.clicked.connect(self.loadImage)
        self.pushButton_2.clicked.connect(self.savePhoto)
        self.pushButton_3.clicked.connect(self.blue_cnl)
        self.pushButton_4.clicked.connect(self.grn_cnl)
        self.pushButton_5.clicked.connect(self.red_cnl)
        self.pushButton_6.clicked.connect(self.crop)
        self.pushButton_7.clicked.connect(self.rectangle)
        self.pushButton_8.clicked.connect(self.rotation)
        QtCore.QMetaObject.connectSlotsByName(PhotoEditor)

        self.filename = None  # Хранит в себе ссылку на фотографию
        self.tmp = None  # Хранить в себе временное изображение для отображения


    def rectangle(self):
        """
        Функция рисования синего прямоугольника по координатам
        :return:
        """
        while True:
            try:
                coord_1 = int(self.lineEdit.text())
                coord_2 = int(self.lineEdit_2.text())
                coord_3 = int(self.lineEdit_3.text())
                coord_4 = int(self.lineEdit_4.text())
            except:
                msg = QMessageBox()  # Вывод сообщений об ошибках
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Отсутствует изображение или введены неправильные данные!")
                msg.setInformativeText('Попробуйте снова')
                msg.setWindowTitle("Error")
                msg.exec_()
                break
            start = (coord_1, coord_2)
            end = (coord_3, coord_4)
            self.image = cv2.rectangle(self.image, start, end, (255, 255, 0), thickness=cv2.FILLED)
            self.setPhoto(self.image)
            break

    def rotation(self):
        while True:
            try:
                angle = int(self.lineEdit_5.text())
            except:
                msg = QMessageBox()  # Вывод сообщений об ошибках
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Отсутствует изображение или введены неправильные данные!")
                msg.setInformativeText('Попробуйте снова')
                msg.setWindowTitle("Error")
                msg.exec_()
                break

            (h, w) = self.image.shape[:2]
            center = (w/2, h/2)

            M = cv2.getRotationMatrix2D(center=center, angle=angle, scale=1.0)
            self.image = cv2.warpAffine(self.image, M, (w, h))
            self.setPhoto(self.image)
            break



    def loadImage(self):  # Функция загрузки изображения
        try:
            self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
            if self.filename:
                self.image = cv2.imread(self.filename)
                self.testim = self.image
                self.setPhoto(self.image)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Изображение неправильного формата или на на английском языке")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def setPhoto(self, image):  # Функция размещения изображения
        self.tmp = image
        image = imutils.resize(image, width=1280, height=1200)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label_7.setPixmap(QtGui.QPixmap.fromImage(image))


    def savePhoto(self):  # Функция сохранения изображения
        try:
            filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
            cv2.imwrite(filename, self.tmp)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Отсутствует изображение")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def red_cnl(self):  # Функция вывода красного канала изображения
        try:
            r = self.image.copy()
            r[:, :, 0] = 0
            r[:, :, 1] = 0
            width = 1000
            height = 550
            dimensions = (width, height)
            channel_img = cv2.resize(r, dimensions, interpolation=cv2.INTER_LINEAR)
            cv2.imshow('RED', channel_img)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Отсутствует изображение!")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def grn_cnl(self):
        try:
            g = self.image.copy()
            g[:, :, 0] = 0
            g[:, :, 2] = 0
            width = 1000
            height = 550
            dimensions = (width, height)
            channel_img = cv2.resize(g, dimensions, interpolation=cv2.INTER_LINEAR)
            cv2.imshow('GREEN', channel_img)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Отсутствует изображение!")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def blue_cnl(self):
        try:
            b = self.image.copy()
            b[:, :, 1] = 0
            b[:, :, 2] = 0
            width = 1000
            height = 550
            dimensions = (width, height)
            channel_img = cv2.resize(b, dimensions, interpolation=cv2.INTER_LINEAR)
            cv2.imshow('BLUE', channel_img)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Отсутствует изображение!")
            msg.setInformativeText('Попробуйте снова')
            msg.setWindowTitle("Error")
            msg.exec_()

    def crop(self):  # Функция изменения размера изображения
        while True:
            try:
                coord_1 = int(self.lineEdit.text())
                coord_2 = int(self.lineEdit_2.text())
                coord_3 = int(self.lineEdit_3.text())
                coord_4 = int(self.lineEdit_4.text())
                if (coord_1 < coord_2 and coord_3 < coord_4) and\
                        (coord_1 < 0 and coord_2 < 0 and coord_3 < 0 and coord_4 < 0):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Coordinate 1 и Coordinate 3 должны быть меньше"
                                " Coordinate 2 и Coordinate 4 соответственно!")
                    msg.setInformativeText('Попробуйте снова')
                    msg.setWindowTitle("Error")
                    msg.exec_()
                    break
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Отсутствует изображение или данные неверного типа!")
                msg.setInformativeText('Попробуйте снова')
                msg.setWindowTitle("Error")
                msg.exec_()
                break
            cropped_image = self.image[coord_1:coord_2, coord_3:coord_4]
            self.setPhoto(cropped_image)
            break



    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("PhotoEditor", "PhotoEditor"))

        self.label.setText(_translate("PhotoEditor", "Photo Editor"))
        self.label_2.setText(_translate("PhotoEditor", "Coordinate 2:"))
        self.label_3.setText(_translate("PhotoEditor", "Coordinate 3:"))
        self.label_4.setText(_translate("PhotoEditor", "Coordinate 4:"))
        self.label_5.setText(_translate("PhotoEditor", "Coordinate 1:"))
        self.label_6.setText(_translate("PhotoEditor", "Angle:"))

        self.pushButton.setText(_translate("PhotoEditor", "Open"))
        self.pushButton_2.setText(_translate("PhotoEditor", "Save"))
        self.pushButton_3.setText(_translate("PhotoEditor", "Blue"))
        self.pushButton_4.setText(_translate("PhotoEditor", "Green"))
        self.pushButton_5.setText(_translate("PhotoEditor", "Red"))
        self.pushButton_6.setText(_translate("PhotoEditor", "Crop"))
        self.pushButton_7.setText(_translate("PhotoEditor", "Rectangle"))
        self.pushButton_8.setText(_translate("PhotoEditor", "Rotation"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QDialog()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())
