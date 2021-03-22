import sys
import template_matching
import ViolaJones
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *


class mainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn_t = QPushButton('Choose files')
        self.btn_t.clicked.connect(self.on_click_t)

        # Обработка сигнала через лямбду
        self.button_v = QPushButton('Choose file')
        self.button_v.clicked.connect(self.on_click_v)

        self.label = QLabel(self)
        self.tab_1 = QFrame()
        self.layout_tab_1 = QVBoxLayout()
        self.layout_tab_1.addWidget(self.btn_t,  alignment=Qt.AlignTop)
        # self.layout_tab_1.setAlignment(Qt.AlignCenter)
        self.tab_1.setLayout(self.layout_tab_1)

        self.label2 = QLabel(self)
        self.tab_2 = QFrame()
        self.layout_tab_2 = QVBoxLayout()
        self.layout_tab_2.addWidget(self.button_v, alignment=Qt.AlignTop)
        # self.layout_tab_2.addStretch(1)
        self.tab_2.setLayout(self.layout_tab_2)

        tab_3 = QFrame()
        layout_tab_3 = QVBoxLayout()
        # layout_tab_3.addWidget(self.button_prev, alignment=Qt.AlignBottom)
        tab_3.setLayout(layout_tab_3)

        self.tab = QTabWidget()
        self.tab.addTab(self.tab_1, "Template matching")
        self.tab.addTab(self.tab_2, "Viola-Jones")
        self.tab.addTab(tab_3, "SymmetryLines")

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tab)
        self.setLayout(main_layout)

        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('Detection')
        self.show()

    def on_click_t(self):
        file1 = QFileDialog.getOpenFileName(self, 'Choose image', None, 'Images (*.png *.xpm *.jpg)')[0]
        file2 = QFileDialog.getOpenFileName(self, 'Choose template', None, 'Images (*.png *.xpm *.jpg)')[0]
        self.label.clear()
        image = template_matching.template_matching(file1, file2)
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        image = QImage.rgbSwapped(image)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())
        self.layout_tab_1.addWidget(self.label, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.tab_1.setLayout(self.layout_tab_1)

    def on_click_v(self):
        file = QFileDialog.getOpenFileName(self, 'Choose image', None, 'Images (*.png *.xpm *.jpg)')[0]
        self.label2.clear()
        image = ViolaJones.viola_jones(file)
        height, width, channel = image.shape
        bytesPerLine = 3 * width
        image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        image = QImage.rgbSwapped(image)
        pixmap = QPixmap.fromImage(image)
        self.label2.setPixmap(pixmap)
        self.label2.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())
        self.layout_tab_2.addWidget(self.label2, alignment=Qt.AlignCenter | Qt.AlignTop)
        self.tab_2.setLayout(self.layout_tab_2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    ex.show()
    sys.exit(app.exec_())