# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Diseño.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import Resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1012, 607)
        MainWindow.setStyleSheet(u"color: black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Frame_superior = QFrame(self.centralwidget)
        self.Frame_superior.setObjectName(u"Frame_superior")
        self.Frame_superior.setMinimumSize(QSize(0, 70))
        self.Frame_superior.setMaximumSize(QSize(16777215, 70))
        self.Frame_superior.setStyleSheet(u"background-color: rgb(54, 48, 98);")
        self.Frame_superior.setFrameShape(QFrame.StyledPanel)
        self.Frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Frame_superior)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_menu = QPushButton(self.Frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 40))
        self.bt_menu.setMaximumSize(QSize(16777215, 70))
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"background-color: #363062;\n"
"font: 87 20pt \"Agency FB\";\n"
"border-radius: 0px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: white;\n"
"font: 87 20pt \"Agency FB\";\n"
"}")
        icon = QIcon()
        icon.addFile(u"Img/barra-de-menus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(592, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.Frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMaximumSize(QSize(16777215, 35))
        self.bt_minimizar.setStyleSheet(u"\n"
"QPushButton:hover {\n"
"  background-color: grey;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Img/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_minimizar)

        self.bt_restaurar = QPushButton(self.Frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMaximumSize(QSize(16777215, 35))
        self.bt_restaurar.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: cyan;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Img/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_restaurar)

        self.bt_maximizar = QPushButton(self.Frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMaximumSize(QSize(16777215, 35))
        self.bt_maximizar.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: GreenYellow;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"Img/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.Frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(16777215, 35))
        self.bt_cerrar.setStyleSheet(u"QPushButton:hover {\n"
"  background-color: red;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"Img/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_cerrar)


        self.verticalLayout.addWidget(self.Frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(0, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setStyleSheet(u"QFrame {\n"
"  background-color: rgb(67, 85, 133);\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: rgb(67, 85, 133);\n"
"  border-radius: 20px;\n"
"  border-radius: 20px;\n"
"  font: 75 25pt 'Agency FB';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: white;\n"
"  font: 75 27pt 'Agency FB';\n"
"}\n"
"\n"
"")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 50, -1, -1)
        self.btn_Inicio = QPushButton(self.frame_lateral)
        self.btn_Inicio.setObjectName(u"btn_Inicio")
        self.btn_Inicio.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_Inicio)

        self.btn_Asistente = QPushButton(self.frame_lateral)
        self.btn_Asistente.setObjectName(u"btn_Asistente")
        self.btn_Asistente.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btn_Asistente)

        self.btn_Configuracion = QPushButton(self.frame_lateral)
        self.btn_Configuracion.setObjectName(u"btn_Configuracion")
        self.btn_Configuracion.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"Img/configuracion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Configuracion.setIcon(icon5)
        self.btn_Configuracion.setIconSize(QSize(50, 35))

        self.verticalLayout_3.addWidget(self.btn_Configuracion)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font = QFont()
        font.setFamilies([u"Agency FB"])
        font.setPointSize(22)
        font.setBold(True)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"color: black;\n"
"background-color: rgb(245, 232, 199);\n"
"\n"
"\n"
"QPushButton {\n"
"  background-color: white;\n"
"  border-radius: 20px;\n"
"  font: 75 25pt 'Agency FB';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: grey;\n"
"  font: 75 27pt 'Agency FB';\n"
"}\n"
"\n"
"")
        self.pagina_uno = QWidget()
        self.pagina_uno.setObjectName(u"pagina_uno")
        self.label = QLabel(self.pagina_uno)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 811, 491))
        font1 = QFont()
        font1.setFamilies([u"Agency FB"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.label.setFont(font1)
        self.stackedWidget.addWidget(self.pagina_uno)
        self.pagina_dos = QWidget()
        self.pagina_dos.setObjectName(u"pagina_dos")
        self.label_ayudar = QLabel(self.pagina_dos)
        self.label_ayudar.setObjectName(u"label_ayudar")
        self.label_ayudar.setGeometry(QRect(100, -50, 831, 251))
        font2 = QFont()
        font2.setFamilies([u"Agency FB"])
        font2.setPointSize(30)
        font2.setBold(True)
        self.label_ayudar.setFont(font2)
        self.pushButton_9 = QPushButton(self.pagina_dos)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(100, 190, 231, 121))
        font3 = QFont()
        font3.setFamilies([u"Agency FB"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
"  background-color: white;\n"
"  border-radius: 20px;\n"
"  border-radius: 20px;\n"
"  font: 75 20pt 'Agency FB';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: Gainsboro;\n"
"  font: 75 22pt 'Agency FB';\n"
"}\n"
"")
        self.pushButton_10 = QPushButton(self.pagina_dos)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(400, 190, 261, 121))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"  background-color: white;\n"
"  border-radius: 20px;\n"
"  border-radius: 20px;\n"
"  font: 75 20pt 'Agency FB';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: Gainsboro;\n"
"  font: 75 22pt 'Agency FB';\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.pagina_dos)
        self.pagina_tres = QWidget()
        self.pagina_tres.setObjectName(u"pagina_tres")
        self.label_4 = QLabel(self.pagina_tres)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 50, 241, 101))
        font4 = QFont()
        font4.setFamilies([u"Agency FB"])
        font4.setPointSize(22)
        font4.setBold(False)
        self.label_4.setFont(font4)
        self.label_5 = QLabel(self.pagina_tres)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 140, 241, 101))
        self.label_5.setFont(font4)
        self.label_6 = QLabel(self.pagina_tres)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 230, 241, 101))
        self.label_6.setFont(font4)
        self.label_7 = QLabel(self.pagina_tres)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 320, 241, 101))
        self.label_7.setFont(font4)
        self.txtNombre = QLineEdit(self.pagina_tres)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(280, 80, 261, 51))
        self.txtNombre.setFont(font)
        self.txtNombre.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cbbIdioma = QComboBox(self.pagina_tres)
        self.cbbIdioma.addItem("")
        self.cbbIdioma.addItem("")
        self.cbbIdioma.setObjectName(u"cbbIdioma")
        self.cbbIdioma.setGeometry(QRect(280, 160, 261, 51))
        self.cbbIdioma.setFont(font)
        self.cbbIdioma.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cbbHora = QComboBox(self.pagina_tres)
        self.cbbHora.addItem("")
        self.cbbHora.addItem("")
        self.cbbHora.setObjectName(u"cbbHora")
        self.cbbHora.setGeometry(QRect(280, 250, 261, 51))
        self.cbbHora.setFont(font)
        self.cbbHora.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cbbHora_2 = QComboBox(self.pagina_tres)
        self.cbbHora_2.addItem("")
        self.cbbHora_2.addItem("")
        self.cbbHora_2.setObjectName(u"cbbHora_2")
        self.cbbHora_2.setGeometry(QRect(280, 350, 261, 51))
        self.cbbHora_2.setFont(font)
        self.cbbHora_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pushButton_12 = QPushButton(self.pagina_tres)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(290, 440, 161, 61))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"  background-color: white;\n"
"  border-radius: 20px;\n"
"  border-radius: 20px;\n"
"  font: 75 20pt 'Agency FB';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: Gainsboro;\n"
"  font: 75 22pt 'Agency FB';\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.pagina_tres)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.btn_Inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btn_Asistente.setText(QCoreApplication.translate("MainWindow", u"Inteligencia\n"
"artificial", None))
        self.btn_Configuracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">\u00a1Bienvenido a VAI, el asistente virtual! Puedo </p><p align=\"justify\">responder cualquier duda que tengas y </p><p align=\"justify\">ayudarte con algunas de mis </p><p align=\"justify\">funciones especiales. </p><p align=\"justify\"><br/></p><p align=\"justify\">\u00bfQuieres intentarlo? \u00a1Dale a </p><p align=\"justify\">\u00abInteligencia artificial\u00bb para probar!</p></body></html>", None))
        self.label_ayudar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\">Soy tu asistente, \u00bfC\u00f3mo te puedo ayudar hoy?</p></body></html>", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n por voz", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Funci\u00f3n por texto", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Nombre del asistente:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Idioma preferido:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Formato de hora:</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Voz del asistente:</p></body></html>", None))
        self.txtNombre.setText("")
        self.cbbIdioma.setItemText(0, QCoreApplication.translate("MainWindow", u"es-ES", None))
        self.cbbIdioma.setItemText(1, QCoreApplication.translate("MainWindow", u"en-US", None))

        self.cbbHora.setItemText(0, QCoreApplication.translate("MainWindow", u"12", None))
        self.cbbHora.setItemText(1, QCoreApplication.translate("MainWindow", u"24", None))

        self.cbbHora_2.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.cbbHora_2.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))

        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
    # retranslateUi

