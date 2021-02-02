from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
import sys
from shower import Ui_MainWindow
import apitools
from PIL.ImageQt import *


class Map(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.search.clicked.connect(self.search_object)

    def search_object(self):
        toponym_to_find = self.enter.text()
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": toponym_to_find,
            "format": "json"}
        pos = apitools.get_pos(geocoder_params)
        spn = apitools.extract_size(geocoder_params)

        map_params = {
            "ll": f'{pos[0]},{pos[1]}',
            "spn": f'{spn[0]},{spn[1]}',
            "l": "map",
            'pt': f'{pos[0]},{pos[1]},pm2rdm'
        }

        self.pixmap = QPixmap.fromImage(ImageQt(apitools.get_map(map_params)))
        self.map.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    window = Map()
    window.show()
    sys.exit(app.exec())
