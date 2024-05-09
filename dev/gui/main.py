import sys
sys.path.append("C:/Users/ramir/OneDrive/Escritorio/proyecto/dev")
from config import check_config, create_config_file, initial_config
import subprocess
from PySide6 import QtWidgets
from Diseño_ui import Ui_MainWindow
from Diseño_ui import *
from PySide6 import QtCore
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtWidgets import QMessageBox  # Aquí está la modificación


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        # Cargar la configuración actual al iniciar la aplicación
        self.load_config()
        # Conectar el botón a la función de guardar la configuración
        self.ui.pushButton_12.clicked.connect(self.save_config)
        #eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)
        self.setWindowOpacity(1)
        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        # mover ventana
        self.ui.Frame_superior.mouseMoveEvent = self.mover_ventana
        #acceder a las paginas
        self.ui.btn_Inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_uno))			
        self.ui.btn_Asistente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_dos))
        self.ui.btn_Configuracion.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pagina_tres))

        self.ui.pushButton_9.clicked.connect(self.ejecutar_script) 


		#control barra de titulos
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())

        self.ui.bt_restaurar.hide()

        #menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)

    def load_config(self):
        # Leer la configuración actual de config.txt
        config = check_config("dev/config.txt")  # Aquí está la modificación
        # Cargar la configuración en los widgets correspondientes
        self.ui.txtNombre.setText(config["name"])
        self.ui.cbbIdioma.setCurrentText(config["language"])
        self.ui.cbbHora.setCurrentText(config["hour_format"])
        self.ui.cbbHora_2.setCurrentText(config["voice_number"])

    def save_config(self):
        # Obtener los valores actuales de los widgets
        config = {
            "name": self.ui.txtNombre.text(),
            "language": self.ui.cbbIdioma.currentText(),
            "hour_format": self.ui.cbbHora.currentText(),
            "voice_number": self.ui.cbbHora_2.currentText(),
        }
        # Guardar la configuración en config.txt
        if create_config_file("dev/config.txt", config):  # Aquí está la modificación
            QMessageBox.information(self, "Información", "Configuración actualizada")

    def ejecutar_script(self): 
        subprocess.run(["python", "dev/va.py"])
        
    def control_bt_minimizar(self):
        self.showMinimized()		

    def  control_bt_normal(self): 
        self.showNormal()		
        self.ui.bt_restaurar.hide()
        self.ui.bt_maximizar.show()

    def  control_bt_maximizar(self): 
        self.showMaximized()
        self.ui.bt_maximizar.hide()
        self.ui.bt_restaurar.show()

    def mover_menu(self):
        if True:			
            width = self.ui.frame_lateral.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
	## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
    ## mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


