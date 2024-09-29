import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton

app = QApplication(sys.argv)
 
window = QWidget()
window.setWindowTitle('PyQt5 Demo')
 
button = QPushButton('Click Me')
button.clicked.connect(lambda: print('Button clicked!'))
 
#window.setLayout(window.addWidget(button))
button.setParent(window)

window.show() 
sys.exit(app.exec_())
