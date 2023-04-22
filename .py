from  PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QSizePolicy, QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QGridLayout, QSizePolicy
from PyQt5.QtGui import QFont

my_font = QFont('Segoe UI', 18)

class Strechbutton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(40, 40)
        self.setFont(my_font)
        self.setStyleSheet('QPushButton {background-color: #2a362d; color: #d0d6d1; border: none; border-radius: 15px; padding: 10px;}')

class Display(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(40, 40)
        self.setFont(my_font)
        self.setStyleSheet('QLineEdit {background-color: #2a362d; color: c0c0c0; border: 2px solid #c0c0c0; border-radius: 15px; padding: 10px;}')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.to_solve = ''
        
        self.setStyleSheet('QWidget { background-color: #8a0303}')

        self.display = Display()

        layout = QGridLayout()
        self.setLayout(layout)

        btn_0 = Strechbutton('0')
        btn_1 = Strechbutton('1')
        btn_2 = Strechbutton('2')
        btn_3 = Strechbutton('3')
        btn_4 = Strechbutton('4')
        btn_5 = Strechbutton('5')
        btn_6 = Strechbutton('6')
        btn_7 = Strechbutton('7')
        btn_8 = Strechbutton('8')
        btn_9 = Strechbutton('9')
        
        btn_back = Strechbutton('<-')
        btn_clear = Strechbutton('C')
        btn_result = Strechbutton('=')
        btn_add = Strechbutton('+')
        btn_substrakt = Strechbutton('-')
        btn_myltiory = Strechbutton('*')
        btn_divide = Strechbutton('/')
        btn_point = Strechbutton('.')

        layout.addWidget(self.display, 0, 0, 1, 4)
        layout.addWidget(btn_back, 1, 0)
        layout.addWidget(btn_clear, 1, 1)
        layout.addWidget(btn_add, 1, 2)
        layout.addWidget(btn_substrakt, 1, 3)

        layout.addWidget(btn_7, 2, 0)
        layout.addWidget(btn_8, 2, 1)
        layout.addWidget(btn_9, 2, 2)
        layout.addWidget(btn_myltiory, 2, 3)

        layout.addWidget(btn_4, 3, 0)
        layout.addWidget(btn_5, 3, 1)
        layout.addWidget(btn_6, 3, 2)
        layout.addWidget(btn_divide, 3, 3)

        layout.addWidget(btn_1, 4, 0)
        layout.addWidget(btn_2, 4, 1)
        layout.addWidget(btn_3, 4, 2)
        layout.addWidget(btn_result, 4, 3, 2, 1)

        layout.addWidget(btn_0, 5, 0, 1, 2)
        layout.addWidget(btn_point, 5, 2)

        btn_0.clicked.connect(self.btn_handler)
        btn_1.clicked.connect(self.btn_handler)
        btn_2.clicked.connect(self.btn_handler)
        btn_3.clicked.connect(self.btn_handler)
        btn_4.clicked.connect(self.btn_handler)
        btn_5.clicked.connect(self.btn_handler)
        btn_6.clicked.connect(self.btn_handler)
        btn_7.clicked.connect(self.btn_handler)
        btn_8.clicked.connect(self.btn_handler)
        btn_9.clicked.connect(self.btn_handler)
        
        btn_back.clicked.connect(self.btn_handler)
        btn_clear.clicked.connect(self.btn_handler)
        btn_result.clicked.connect(self.btn_handler)
        btn_add.clicked.connect(self.btn_handler)
        btn_substrakt.clicked.connect(self.btn_handler)
        btn_myltiory.clicked.connect(self.btn_handler)
        btn_divide.clicked.connect(self.btn_handler)
        btn_point.clicked.connect(self.btn_handler)
        

    def btn_handler(self):
        if self.to_solve == 'Упс! в поле ввода ничего не написано':
            self.to_solve = ''
        btn = self.sender()
        if btn.text() in '0123456789.+-*/':
            self.to_solve += btn.text()
        if btn.text() == '<-':
            self.to_solve = self.to_solve[0:-1]
        if btn.text() == 'C':
            self.to_solve = ''
        if btn.text() == '=':
            try:
                self.to_solve = str(eval(self.to_solve))
            except:
                self.to_solve = 'Упс! в поле ввода ничего не написано'
        self.display.setText(self.to_solve)

app = QApplication([])
win = MainWindow()
win.show()
app.exec()
