import os
import sys

from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIntValidator, QTextCursor
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QTextEdit, QMessageBox, QApplication

from libs import connect
from libs.test_with_association import spodes, debug


class EmittingStream(QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass  # Необходимо для совместимости с sys.stdout


class FileUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        current_dir = os.path.dirname(__file__)
        ui_path = os.path.join(current_dir, 'maket.ui')

        uic.loadUi(ui_path, self)

        self.number_com = self.findChild(QLineEdit, 'com')
        self.number_com.setValidator(QIntValidator())

        self.serial = self.findChild(QLineEdit, 'serial')
        self.serial.setValidator(QIntValidator())

        self.speed = self.findChild(QLineEdit, 'speed')
        self.speed.setValidator(QIntValidator())

        self.start = self.findChild(QPushButton, 'start_button')
        self.start.clicked.connect(self.start_command)

        self.text_edit = self.findChild(QTextEdit, 'textEdit')
        self.text_edit.setReadOnly(True)  # Запрещаем редактирование
        self.redirect_stdout()
        self.stream.textWritten.connect(self.on_text_written)

        self.applyDarkTheme()

    def check_fields(self):
        if not self.number_com.text().strip():
            # Показываем предупреждение
            QMessageBox.warning(
                self,
                "Предупреждение",
                "Введите COM соединения!",
                QMessageBox.Ok
            )
            return False
        if not self.serial.text().strip():
            # Показываем предупреждение
            QMessageBox.warning(
                self,
                "Предупреждение",
                "Введите серийник!",
                QMessageBox.Ok
            )
            return False
        if not self.speed.text().strip():
            # Показываем предупреждение
            QMessageBox.warning(
                self,
                "Предупреждение",
                "Введите скорость соединения!",
                QMessageBox.Ok
            )
            return False
        return True

    def get_settings(self):
        connect.COM = self.number_com.text()
        connect.ADDRESS = int(self.serial.text())
        connect.BAUD = int(self.speed.text())

    def start_command(self):
        try:
            if not self.check_fields():
                return
            self.text_edit.clear()

            self.get_settings()

            self.file_name = 'data.txt'
            # f"\n<font color={color} size='5'>{message}</font>\n"
            with open(self.file_name, 'w', encoding='utf-8') as file:
                file.write("Проверка на соответствие СПОДЭС")

            self.update_text("Проверка на соответствие СПОДЭС\n", 'yellow')
            spodes()

            with open(self.file_name, 'a', encoding='utf-8') as file:
                file.write("Проверка остальных объектов\n")

            self.update_text("Проверка остальных объектов\n", 'yellow')
            debug()

        except Exception as e:
            print(e)


        #
        # com = self.number_com.text()
        # try:
        #     instrument, meter_type = config(com)
        #     instrument.write_register(registeraddress=147, value=170)
        #     self.update_text("УСПЕХ!", "green")
        #     print()
        #     self.update_text("Перезапустите счетчик!", "green")
        # except Exception as e:
        #     self.update_text(f"Ошибка {e}.", "red")
        #     print()
        #     self.update_text(f"Проверьте настройки.", "red")

    def applyDarkTheme(self):
        # Определяем стили для темной темы
        dark_stylesheet = """
        QWidget {
            background-color: #2c313c;
            color: #ffffff;
        }

        QLineEdit {
            background-color: #363d47;
            color: #ffffff;
            border: 1px solid #444950;
            border-radius: 4px;
            padding: 5px;
        }

        QLineEdit:focus {
            border: 1px solid #61dafb;
        }

        QPushButton {
            background-color: #363d47;
            color: #ffffff;
            border: 1px solid #444950;
            border-radius: 4px;
            padding: 5px 10px;
        }

        QPushButton:hover {
            background-color: #444950;
        }

        QPushButton:pressed {
            background-color: #2c313c;
        }
        """

        # Применяем стиль к приложению
        self.setStyleSheet(dark_stylesheet)

    def update_text(self, message, color):
        self.text_edit.append(f"\n<font color={color} size='5'>{message}</font>\n")

    def redirect_stdout(self):
        self.stream = EmittingStream()
        sys.stdout = self.stream
        sys.stderr = self.stream

    def on_text_written(self, text):
        cursor = self.text_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        with open(self.file_name, 'a', encoding='utf-8') as file:
            file.write(text)
        self.text_edit.setTextCursor(cursor)
        self.text_edit.ensureCursorVisible()
        QApplication.processEvents()


def main():
    app = QApplication(sys.argv)
    ex = FileUploader()
    ex.show()
    sys.exit(app.exec_())
