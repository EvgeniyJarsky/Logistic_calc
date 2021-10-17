#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QSlider
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class LogisticCalc(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 400, 220)
        self.setWindowTitle('Программа расчета ставок')
        self.setWindowIcon(QIcon('web.png'))

        vertical_layout = QVBoxLayout()
        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout_for_but = QHBoxLayout()
        horizontal_layout_for_input = QHBoxLayout()

        but = QPushButton("Рассчитать ставку")
        but.clicked.connect(self.calculate)



        but_1000_minus = QPushButton("-1000")
        but_1000_minus.clicked.connect(self.minus_1000)
        # but_100_minus = QPushButton("-100")
        # but_100_minus.clicked.connect(self.minus_100)
        # but_100_plus = QPushButton("+100")
        # but_100_plus.clicked.connect(self.plus_100)
        but_1000_plus = QPushButton("+1000")
        but_1000_plus.clicked.connect(self.plus_1000)

        horizontal_layout_for_but.addWidget(but_1000_minus)
        # horizontal_layout_for_but.addWidget(but_100_minus)
        # horizontal_layout_for_but.addWidget(but_100_plus)
        horizontal_layout_for_but.addWidget(but_1000_plus)

        without_nds_lab = QLabel('Ставка без НДС')
        with_nds_lab = QLabel('Ставка с НДС')

        self.without_nds_rez = QLabel()
        self.with_nds_rez = QLabel()

        self.broker = QLabel("Посреднику")
        self.broker_value = QLineEdit("1000")
        self.broker_value.editingFinished.connect(self.calculate)
        self.broker_value.returnPressed.connect(self.calculate)
        self.slider = QSlider()


        self.input_txt = QLineEdit()
        self.input_txt.setText('30000')
        self.input_txt.editingFinished.connect(self.calculate)
        self.input_txt.returnPressed.connect(self.calculate)
        self.input_txt.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        vertical_layout2 = QVBoxLayout()
        vertical_layout2.addWidget(self.input_txt)
        vertical_layout2.addLayout(horizontal_layout_for_but)

        horizontal_layout_for_input.addLayout(vertical_layout2)
        horizontal_layout_for_input.addWidget(self.broker)
        horizontal_layout_for_input.addWidget(self.broker_value)

        horizontal_layout1.addWidget(without_nds_lab)
        horizontal_layout1.addWidget(self.without_nds_rez)

        horizontal_layout2.addWidget(with_nds_lab)
        horizontal_layout2.addWidget(self.with_nds_rez)

        vertical_layout.addWidget(but)
        vertical_layout.addLayout(horizontal_layout_for_input)
        vertical_layout.addLayout(horizontal_layout_for_but)
        vertical_layout.addLayout(horizontal_layout2)
        vertical_layout.addLayout(horizontal_layout1)

        self.setLayout(vertical_layout)

        self.show()

    def calculate(self):
        number = self.input_txt.text()
        delta = self.broker_value.text()
        if delta.isdigit():
            delta = int(delta)
        else:
            delta = 0
        if number.isdigit():
            int_num = int(number) - delta
            rez = int_num - int_num * 0.1
            self.with_nds_rez.setText(f"{int(rez)}")
            rez = int_num / 1.2
            self.without_nds_rez.setText(f"{int(rez)}")
        else:
            print("if's not number" )

    def minus_100(self):
        number = self.input_txt.text()
        number = int(number)
        rez = str(number - 100)
        self.input_txt.setText(rez)
        self.calculate()

    def minus_1000(self):
        number = self.input_txt.text()
        number = int(number)
        rez = str(number - 1000)
        self.input_txt.setText(rez)
        self.calculate()

    def plus_100(self):
        number = self.input_txt.text()
        number = int(number)
        rez = str(number + 100)
        self.input_txt.setText(rez)
        self.calculate()

    def plus_1000(self):
        number = self.input_txt.text()
        number = int(number)
        rez = str(number + 1000)
        self.input_txt.setText(rez)
        self.calculate()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex =LogisticCalc()
    sys.exit(app.exec_())