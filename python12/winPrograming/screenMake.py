import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.Qt import QPushButton

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("나는윈도우야.")
w.setWindowIcon(QIcon('web.png'))
w.setGeometry(1000,300,300,300)

btn = QPushButton('Quit',w)
btn.move(50, 50)
btn.resize(btn.sizeHint())
btn.clicked.connect(QCoreApplication.instance().quit)
w.show()
app.exec()