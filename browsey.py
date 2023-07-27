import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon("browser.png"))
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #nav

        navbar = QToolBar()
        self.addToolBar(navbar)

        back = QAction("←", self)
        back.triggered.connect(self.browser.back)
        navbar.addAction(back)

        forward = QAction("→", self)
        forward.triggered.connect(self.browser.forward)
        navbar.addAction(forward)

        reloadBtn = QAction("⟳", self)
        reloadBtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadBtn)


app = QApplication(sys.argv)
QApplication.setApplicationName("Browsey")
QApplication.setApplicationDisplayName("Browsey")
window=MainWindow()
app.exec_()