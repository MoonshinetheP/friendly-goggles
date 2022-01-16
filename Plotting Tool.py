"""Modules"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit as cf


"""Custom Functions"""
def space():
    print ('\n')


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

noise = 0.5 * np.random.normal(size = ydummy.size)
    # Generates random numbers from a Gaussian distribution that simulate noise
    # size = output shape of distribution
ydummy = ydummy + noise


"""Data Generation"""
filename = 'sampledata.txt'
x, y = np.genfromtxt(filename, unpack = True, delimiter = '', skip_header = 2)
    # Stores data from a .txt file in two separate parameters 
    # unpack = allows data to be extracted from columns (True or False)
    # delimiter = describes the symbol that separates columns (string)
    # skip_header = skips any headers in the .txt file (integer)

# Alternative method: x, y = np.loadtxt(filename, unpack = True, delimiter = '', skiprows = 1)
    # Stores data from a .csv file in two separate parameters
    # unpack = allows data to be extracted from columns (True or False)
    # delimiter = describes the symbol that separates columns (string)
    # skiprows = skips the titles row (integer)


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


"""Title and Labels"""
#ax.set_title('Voltammetry of a nanoelectrode', loc = 'center', pad = 20, fontsize = 25)
    # Prints text as a title above the figure
    # '' = text to be added (string)
    # loc = horizontal position of title (string)
    # pad = gap between title and axes (integer or float)
    # fontsize = font size of title (integer or float)

ax.set_xlabel(r'$E\ vs.$ SMSE / V', labelpad = 15, fontsize = 25)
    # Prints text as a label next to the primary x axis
    # '' = text to be added (string)
    # labelpad = gap between the label and the axis (integer or float)
    # fontsize = font size of label (integer or label)
ax.set_ylabel('$i$ / pA', labelpad = 15, fontsize = 25)
    # Prints text as a label next to primary y axis
    # '' = text to be added (string)
    # labelpad = gap between the label and the axis (integer or float)
    # fontsize = font size of label (integer or float)


"""Major Ticks"""
ax.xaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', top = False)
    # Sets the appearance and visibility of the major tick labels on the primary x axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # pad = gap between the tick and the tick labels (integer or float)
    # labelsize = font size of the tick labels (integer or float)
    # labelrotation = angle of the tick label rotation (integer or float)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary x axis are displayed (True or False)
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
    # Sets the positions of the major ticks on the primary x axis to the multiples of a specified base (integer or float)
# Alternative method: ax.xaxis.set_major_locator(mpl.ticker.LogLocator(base = 10))
    # Sets the positions of the major ticks on the primary x axis to the logarithmic scale of a specified base (integer or float)
# Alternative method: ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(np.linspace(1, 10, 10)))
    # Sets the positions of the major ticks on the primary x axis to the list of numbers specified 

ax.yaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', right = False)
    # Sets the appearance and visibility of the major tick labels on the primary y axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # pad = gap between the tick and the tick labels (integer or float)
    # labelsize = font size of the tick labels (integer or float)
    # labelrotation = angle of the tick label rotation (integer or float)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary y axis are displayed (True or False)
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
    # Sets the positions of the major ticks on the primary y axis to the multiples of a specified base (integer or float)

ax_xcopy.xaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', top = True)
    # Sets the appearance and visibility of the major tick labels on the secondary x axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # pad = gap between the tick and the tick labels (integer or float)
    # labelsize = font size of the tick labels (integer or float)
    # labelrotation = angle of the tick label rotation (integer or float)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary x axis are displayed (True or False)
ax_xcopy.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.1))
    # Sets the positions of the major ticks on the secondary x axis to the multiples of a specified base (integer or float)
ax_xcopy.set_xticklabels([])
    # Removes the major tick labels of the secondary x axis
# Alternative method: ax_xcopy.set_xticklabels([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # Sets the major tick labels of the secondary x axis to the specified list (list of integers or floats)

ax_ycopy.yaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', right = True)
    # Sets the appearance and visibility of the major tick labels on the secondary y axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # pad = gap between the tick and the tick labels (integer or float)
    # labelsize = font size of the tick labels (integer or float)
    # labelrotation = angle of the tick label rotation (integer or float)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary y axis are displayed (True or False)
ax_ycopy.yaxis.set_major_locator(mpl.ticker.MultipleLocator(10))
    # Sets the positions of the major ticks on the secondary y axis to the multiples of a specified base (integer or float)
ax_ycopy.set_yticklabels([])
    # Removes the major tick labels of the secondary y axis


"""Minor Ticks"""
ax.xaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'out', top = False)
    # Sets the appearance and visibility of the minor tick labels on the primary x axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary x axis are displayed (True or False)
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))
    # Sets the positions of the minor ticks on the primary x axis to the multiples of a specified base (integer or float)

ax.yaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'out', right = False)
    # Sets the appearance and visibility of the minor tick labels on the primary y axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary y axis are displayed (True or False)
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
    # Sets the positions of the minor ticks on the primary y axis to the multiples of a specified base (integer or float)

ax_xcopy.xaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'in', top = True)
    # Sets the appearance and visibility of the minor tick labels on the secondary x axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary x axis are displayed (True or False)
ax_xcopy.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.05))
    # Sets the positions of the minor ticks on the secondary x axis to the multiples of a specified base (integer or float)

ax_ycopy.yaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'in', right = True)
    # Sets the appearance and visibility of the minor tick labels on the secondary y axis
    # which = whether these tick settings apply to major or minor ticks (string)
    # size = length of the ticks (integer or float)
    # width = width of the ticks (integer or float)
    # color = colour of the ticks (string)
    # direction = whether the ticks point in or out (string)
    # top/right = whether the ticks on the secondary y axis are displayed (True or False)
ax_ycopy.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(5))
    # Sets the positions of the minor ticks on the secondary y axis to the multiples of a specified base (integer or float)


"""Plot add-ons"""
ax.grid(which = 'major', axis = 'both', color = 'grey', linestyle = '--', linewidth = 0.5)
    # Draws the gridlines on the axes
    # which = whether the gridlines are applied to the major or minor ticks (string)
    # axis = whether the gridlines are applied to the x or the y axis, or to both (string)
    # color = colour of the gridlines (string)
    # linestyle = symbol/linestyle used for the gridlines (string)
    # linewidth = thickness of the gridlines (integer or float)
ax.axhline(y = y.min()*(10**12), xmin = 0, xmax = 1, linestyle = '--', linewidth = 2, color = 'blue', label = '', marker = '')
    # Displays a horizontal line on the axes
    # y = position of the line on the y axis (integer or float)
    # xmin = start of the line in terms of fraction of the x axis (integer or float)
    # xmax = end of the line in terms of fraction of the x axis (integer or float)
    # linestyle = linestyle used for the line (string)
    # linewidth = thickness of the line (integer or float)
    # color = colour of the line (string)
    # label = text used to denote the line in the legend (string)
    # marker = symbol used to draw the line (string)
#ax.legend(title ='Legend', fontsize = 16, loc = (0.5,0.5), facecolor = 'inherit', frameon = True, fancybox = True, framealpha = 1, edgecolor = 'black', ncol = 1)
    # Generates a legend for all specified labels
    # title = the title applied to the top of the legend (string)
    # fontsize = the default font size used in the legend (integer or float)
    # loc = coordinates of the bottom left corner of the legend in terms of fraction of axes ((float,float))
    # facecolor = what colour the legend box will be (string or inherit from figure)
    # frameon = whether to show box in which legend is placed (True or False)
    # fancybox = rounds the edges of the legend frame (True or False)
    # framealpha = transparency (0 - 1 = transparent to opaque) of the legend box background (float)
    # edgecolor = colour of the frame edge (string)
    # ncol = number of columns the legend is displayed in (integer)
#ax.annotate(s = "", xy = (-0.95, -60), xytext = (-0.95, -30), arrowprops = dict(arrowstyle = "-|>", color = 'black'))
    # Used to annotate the figure with text, or with arrows (other options available)
    # s = the text to be added to the annotation (string)
    # xy = the position of the text, or the head of an arrow ((float,float))
    # xytext = the position of  end of an arrow, or the text at the end of an arrow ((float,float))
    # arrowprops = properties of the arrow in dictionary form, or empty if no arrow is to be made (dictionary)
    # arrowstyle = pre-prepared style used for the arrow (string)
    # color = fill colour of the arrow (string)


"""Fitting"""
def function(x, a, b):
    y = a*np.exp(b*x)
    #y = a* np.power(x,b)
    return y

#pars, cov = cf(f = function, xdata = xdummy, ydata = ydummy, p0 = [0,0], bounds = (-np.inf, np.inf))
    # Applies the curve fitting module to a data set, returning fitting parameters and coefficient of variants
    # f = the function (should be defined earlier) used to fit the data (function name)
    # xdata = the x axis data of the plot that is to be fitted
    # ydata = the y axis data of the plot that is to be fitted
    # p0 = initial guesses for the fitting parameters ([float,float])
    # bounds = boundaries for the fitting parameters ((float,float)) 
#ax.plot(x, dummy(x, *pars), linestyle = '-', linewidth = 2, color = 'black')
    # Plots the curve of best fit using the parameters derived from the curve fitting
    # *pars = unpacks the parameters from the tuple they are stored in after fitting
# standarddeviation = np.sqrt(np.diag(covs))
    # Returns the standard deviation by square rooting the diagonal of the coefficient of variants
# residuals = y - dummy(x, *pars)
    # Returns the residuals by subtracting the line of best fit from the y axis data


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