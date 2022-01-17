"""MODULES"""
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

import matplotlib as mpl 
import matplotlib.pyplot as plt

import numpy as np
import os
from scipy.optimize import curve_fit as cf


"""MATPLOTLIB SETTINGS"""
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'cm'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 20

class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hello world')

        self.setLayout(qtw.QVBoxLayout())


        my_label = qtw.QLabel('Hello, what is your name?')
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)


        my_data = qtw.QLabel('')
        my_data.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_data)


        my_index = qtw.QLabel('')
        my_index.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_index)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('name_field')
        my_entry.setText('')
        self.layout().addWidget(my_entry)
    

        my_combo = qtw.QComboBox(self, editable = True, insertPolicy = qtw.QComboBox.InsertAtTop)
        my_combo.addItem('Steven', 1)
        my_combo.addItem('Ewelina', 2)
        my_combo.addItems(['Marcin', 'Emilia', 'Martin', 'Wojciech'])
        my_combo.insertItem(2, 'Third person')
        my_combo.insertItems(3, ['Fourth person','Fifth person'])
        self.layout().addWidget(my_combo)


        my_spin = qtw.QSpinBox(self, value = 10, maximum = 100, minimum = 0, singleStep = 10, prefix = 'Number')
        my_spin.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_spin)

        my_button = qtw.QPushButton('Press me!', clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        
        
        self.show()


        def press_it():
            my_label.setText(f'Hello {my_combo.currentText()}')
            my_data.setText(f'You are person {my_combo.currentData()}')
            my_index.setText(f'You are number {my_combo.currentIndex()} on the list and {my_spin.value()} on the order list')
            my_entry.setText('')


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()