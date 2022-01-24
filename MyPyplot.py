"""MODULES"""
import sys
import os

import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg


mpl.use('Qt5Agg')


"""Font Settings"""
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'cm'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 20





class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        self.centralwidget = qtg.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowTitle('Plotting Tool')

        sc = MplCanvas(self, width=5, height=4, dpi=100)
        sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])
        self.setCentralWidget(sc)
        
        
        self.updateButton = qtg.QPushButton(self.centralwidget, 'Update graph', clicked = lambda: update())
        self.updateButton.setGeometry(qtc.QRect(539, 600, 521, 51))


        self.show()
        

        def update():
            pass
            

app = qtw.QApplication(sys.argv)
mw = MainWindow()
app.exec_()


"""Dummy Data"""
"""
def dummy(x, a, b):
    y = a*x + b
    return y

xdummy = np.linspace(start = 0, stop = 100, num = 50, endpoint = True)
    # Generates dummy data consisting of a list of evenly spaced sequential numbers
    # start = first number in the list (integer or float)
    # stop = last number in the list (integer or float)
    # num = number of data points between the start and the stop (integer)
    # endpoint = whether to include the stop in the list (True or False)
ydummy = dummy(xdummy, 2, 5)
"""

"""Figure and Axes Generation"""
"""
fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
    # Creates a figure object (i.e. a blank canvas) using the matplotlib.pyplot package
    # num = number assigned to the figure (integer)
    # figsize = dimensions of the figure in inches (float,float)
    # dpi = picture quality (integer)
    # facecolor = color of the background (string)
    # edgecolor = color of the border (string)
    # frameon = draws the figure frame (True or False)

ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

for axis in ['left', 'right', 'top', 'bottom']:
    ax.spines[axis].set_visible(True)
    ax.spines[axis].set_linewidth(1.5)
    ax.spines[axis].set_color('black')

ax.set_axisbelow(True)

ax_xcopy = ax.twiny()
ax_ycopy = ax.twinx()



ax.plot(x, y*(10**12), linewidth = 2, linestyle = '-', color = 'green', marker = None, label = 'W nanoelectrode')


ax.set_xlim(xmin = None, xmax = None, auto = True)

ax_xcopy.set_xlim(ax.get_xlim())

ax.set_ylim(ymin = None, ymax = None, auto = True)

ax_ycopy.set_ylim(ax.get_ylim())



fig.tight_layout()

output = 'example.png'
plt.savefig(output, dpi = 100, quality = 95, transparent = False)
plt.show()
plt.close()
"""