"""MODULES"""
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

import matplotlib as mpl 
import matplotlib.pyplot as plt

import numpy as np
import os
from scipy.optimize import curve_fit as cf

"""Font Settings"""
plt.rcParams['text.usetex'] = True
    # Allows tex style writing in labels (True or False)
plt.rcParams['font.family'] = 'serif'
    # Tells matplotlib to write text in a serif font (string)
plt.rcParams['font.serif'] = 'cm'
    # Sets text font to computer modern (string)
plt.rcParams['mathtext.fontset'] = 'cm'
    # Sets maths mode text font to computer modern (string)
plt.rcParams['font.size'] = 20
    # Sets default font size to 20 pt (integer)


class MainWindow(qtw.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Plotting Tool')

        self.setLayout(qtw.QVBoxLayout())


        image = qtw.QLabel()
        self.layout().addWidget(image)


        updateButton = qtw.QPushButton('Update graph', clicked = lambda: update())
        self.layout().addWidget(updateButton)
        self.show()
        

        def update(self):
            self.pixmap = qtg.QPixmap('')
            self.image.setPixmap()
            

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()





"""Dummy Data"""
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


"""Figure and Axes Generation"""
fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
    # Creates a figure object (i.e. a blank canvas) using the matplotlib.pyplot package
    # num = number assigned to the figure (integer)
    # figsize = dimensions of the figure in inches (float,float)
    # dpi = picture quality (integer)
    # facecolor = color of the background (string)
    # edgecolor = color of the border (string)
    # frameon = draws the figure frame (True or False)

ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
    # Adds an axes object (i.e. the actual plot) on top of the figure object
    # Argument list is [x_origin, y_origin, width, height] in terms of fraction of page dimension (floats)

# Alternative method: fig, ax = plt.subplots(nrows = 1, ncols = 1, sharex = False, sharey = False, num = 1)
    # Creates both a figure object and several axes objects in one go, but less customisable
    # nrows = number of rows showing plots (integer)
    # ncols = number of columns showing plots (integer)
    # sharex = uses the same x axis for all subplots (True or False)
    # sharey = uses the same y axis for all subplots (True or False)
    # num = number assigned to the figure (integer)

for axis in ['left', 'right', 'top', 'bottom']:
    ax.spines[axis].set_visible(True)
        # Whether the spines are displayed or not (True or False)
    ax.spines[axis].set_linewidth(1.5)
        # Sets the thickness of the spines (integer or float)
    ax.spines[axis].set_color('black')
        # Sets the colour of the spines (string)

ax.set_axisbelow(True)
    # Sets the gridlines and ticks to appear under (i.e. send to back) any additional artist objects (True or False)

# Additional method: ax.set_yscale('log')
    # Sets the scale of an axis to logarithmic (string)

ax_xcopy = ax.twiny()
    # Uses the primary y axis to make a new x axis on the top
ax_ycopy = ax.twinx()
    # Uses the primary x axis to make a new y axis on the right


"""Plot Details"""
ax.plot(x, y*(10**12), linewidth = 2, linestyle = '-', color = 'green', marker = None, label = 'W nanoelectrode')
    # Plots specified data onto the axes in the form of a line plot
    # x,y = data to be plotted
    # linewidth = thickness of line (integer or float)
    # linestyle = appearance of line (string)
    # color = color of line (string)
    # marker = additional symbol used to plot data on line (string)
    # label = label that appears in legend (string)

# Alternative method: ax.scatter(x, y, size = 20, color = 'green', marker = 'o', label = 'Scatter plot')
    # Plots specified data onto the axes in the form of a scatter plot
    # x,y = data to be plotted
    # size = size of the markers (integer or float)
    # color = color of markers (string)
    # marker = marker symbol used to plot data (string)
    # label = label that appears in legend (string)

ax.set_xlim(xmin = None, xmax = None, auto = True)
    # Sets the limits on the x axis
    # xmin = lower limit (integer or float)
    # xmax = upper limit (integer or float)
    # auto = whether to automatically set limits (True or False)
ax_xcopy.set_xlim(ax.get_xlim())
    # Copies the limits on the primary x axis and applies them to the secondary x axis
ax.set_ylim(ymin = None, ymax = None, auto = True)
    # Sets the limits on the y axis
    # ymin = lower limit (integer or float)
    # ymax = upper limit (integer or float)
    # auto = whether to automatically set limits (True or False)
ax_ycopy.set_ylim(ax.get_ylim())
    # Copies the limits on the primary y axis and applies them to the secondary y axis


"""Figure Viewing and Saving"""
fig.tight_layout()
    # Removes blank margins and adjusts figure dimensions to reduce any overlap or cropping
output = 'example.png'
plt.savefig(output, dpi = 100, quality = 95, transparent = False)
    # Saves the figure to a desired output file
    # output = the filename and extension that the figure will be saved as (string)  
    # dpi = sets the resolution of the figure in dots per inch (integer)
    # quality = the quality (0 - 95 = low to high) of the figure if saved as a JPG or JPEG (integer)
    # transparent = whether the figure (i.e. canvas) will be coloured in or transparent (True or False)
plt.show()
    # Displays all current figures in a separate window

plt.close()
    # Closes the current figures to prevent corruption