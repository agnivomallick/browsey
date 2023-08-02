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

        homeBtn = QAction("🏠", self)
        homeBtn.triggered.connect(self.navigate_home)
        navbar.addAction(homeBtn)

        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Browsey")
QApplication.setApplicationDisplayName("Browsey")
window=MainWindow()
app.exec_()