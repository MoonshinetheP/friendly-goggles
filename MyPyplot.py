"""MODULES"""
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

import matplotlib as mpl 
import matplotlib.pyplot as plt

from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler

import numpy as np
import os
from scipy.optimize import curve_fit as cf


"""MATPLOTLIB SETTINGS"""
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'cm'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 20


"""TK FUNCTIONS"""
def openfile():
    global filepath
    filepath = str(os.getcwd())
    root.filename = filedialog.askopenfilename(initialdir = filepath, title = 'Select a file to open', filetypes = (('.txt','*.txt'),('.csv','*.csv'),('Any File', '*.*')))
    if str(root.filename) != '':
        open_entry.delete(0, tk.END)
    fileonly = root.filename[len(filepath) + 1:len(root.filename)]
    open_entry.insert(0, fileonly)
    return root.filename

def upload():
    global plt
    global fig
    global ax
    global filename
    global x
    global y


    filename = open_entry.get()
    if len(filename) != 0:
        try:
            plt.close()
            
            x, y = np.genfromtxt(filename, unpack = True, delimiter = '', skip_header = 2)
            fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
            ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])
            ax.plot(x, y, linewidth = 2, linestyle = '-', color = 'black', marker = None, label = '')
            
            for axis in ['left', 'right', 'top', 'bottom']:
                ax.spines[axis].set_visible(True)
                ax.spines[axis].set_linewidth(1.5)
                ax.spines[axis].set_color('black')

            ax.set_axisbelow(True)
            
            ax_xcopy = ax.twiny()
            ax_ycopy = ax.twinx()

            ax.set_xlim(xmin = None, xmax = None, auto = True)
            ax_xcopy.set_xlim(ax.get_xlim())
            ax.set_ylim(ymin = None, ymax = None, auto = True)
            ax_ycopy.set_ylim(ax.get_ylim())

            ax.set_title('', loc = 'center', pad = 20, fontsize = 25)

            ax.set_xlabel('', labelpad = 15, fontsize = 25)
            ax.set_ylabel('', labelpad = 15, fontsize = 25)

            ax.xaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', top = False)
            ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator())

            ax.yaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', right = False)
            ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator())

            ax_xcopy.xaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', top = True)
            ax_xcopy.xaxis.set_major_locator(mpl.ticker.MultipleLocator())
            ax_xcopy.set_xticklabels([])

            ax_ycopy.yaxis.set_tick_params(which = 'major', size = 10, width = 2, color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', right = True)
            ax_ycopy.yaxis.set_major_locator(mpl.ticker.MultipleLocator())
            ax_ycopy.set_yticklabels([])

            ax.xaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'out', top = False)
            ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator())

            ax.yaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'out', right = False)
            ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator())

            ax_xcopy.xaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'in', top = True)
            ax_xcopy.xaxis.set_minor_locator(mpl.ticker.MultipleLocator())

            ax_ycopy.yaxis.set_tick_params(which = 'minor', size = 5, width = 1.5, color = 'black', direction = 'in', right = True)
            ax_ycopy.yaxis.set_minor_locator(mpl.ticker.MultipleLocator())

            ax.grid(which = 'major', axis = 'both', color = 'grey', linestyle = '--', linewidth = 0.5)
            fig.tight_layout()
            display()
            update_btn['state'] = tk.NORMAL
        except Exception:
            messagebox.showerror(title = 'Error', message = 'No file with that name could be found')
            open_entry.delete(0, tk.END)

def update():
    global plt
    global fig
    global ax
    global x
    global y
    global x_label
    global y_label
    global tick_xmajorsize
    global tick_xmajorpos
    global tick_xminorsize
    global tick_xminorpos
    global tick_ymajorsize
    global tick_ymajorpos
    global tick_yminorsize
    global tick_yminorpos

    plt.close()
            
    fig = plt.figure(num = 1, figsize = (6.4, 4.8), dpi = 100, facecolor = 'white', edgecolor = 'white', frameon = True)
    ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

    if colourvar.get() == '--Select a line colour--':
        line_colour = 'black'
    else:
        line_colour = colourvar.get()

    ax.plot(x/float(factor_xentry.get()), y/float(factor_yentry.get()), linewidth = float(line_widthentry.get()), linestyle = '-', color = line_colour, marker = None, label = '')
            
    for axis in ['left', 'bottom', 'right', 'top']:        
        ax.spines[axis].set_linewidth(float(spine_widthentry.get()))
        ax.spines[axis].set_color('black')
    for axis in ['right', 'top']:
        ax.spines[axis].set_visible(spinevar.get())

    ax.set_axisbelow(True)
            
    ax_xcopy = ax.twiny()
    ax_ycopy = ax.twinx()

    if scalexvar.get() == 1:
        x_auto = True
        x_min = None
        x_max = None
    elif scalexvar.get() == 0:
        x_auto = False
        x_min = float(scale_xminentry.get())
        x_max = float(scale_xmaxentry.get())

    if scaleyvar.get() == 1:
        y_auto = True
        y_min = None
        y_max = None
    elif scaleyvar.get() == 0:
        y_auto = False
        y_min = float(scale_yminentry.get())
        y_max = float(scale_ymaxentry.get())

    ax.set_xlim(xmin = x_min, xmax = x_max, auto = x_auto)
    ax_xcopy.set_xlim(ax.get_xlim())
    ax.set_ylim(ymin = y_min, ymax = y_max, auto = y_auto)
    ax_ycopy.set_ylim(ax.get_ylim())

    ax.set_title(title_entry.get(), loc = 'center', pad = 20, fontsize = 25)

    ax.set_xlabel(x_label, labelpad = 15, fontsize = 25)
    ax.set_ylabel(y_label, labelpad = 15, fontsize = 25)

    ax.xaxis.set_tick_params(which = 'major', size = tick_xmajorsize, width = float(spine_widthentry.get()), color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', top = False)
    ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(tick_xmajorpos))

    ax.yaxis.set_tick_params(which = 'major', size = tick_ymajorsize, width = float(spine_widthentry.get()), color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'out', right = False)
    ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(tick_ymajorpos))

    ax_xcopy.xaxis.set_tick_params(which = 'major', size = tick_xmajorsize, width = float(spine_widthentry.get()), color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', top = tickvar.get())
    ax_xcopy.xaxis.set_major_locator(mpl.ticker.MultipleLocator(tick_xmajorpos))
    ax_xcopy.set_xticklabels([])

    ax_ycopy.yaxis.set_tick_params(which = 'major', size = tick_ymajorsize, width = float(spine_widthentry.get()), color = 'black', pad = 6, labelsize = 15, labelrotation = 0, direction = 'in', right = tickvar.get())
    ax_ycopy.yaxis.set_major_locator(mpl.ticker.MultipleLocator(tick_ymajorpos))
    ax_ycopy.set_yticklabels([])

    ax.xaxis.set_tick_params(which = 'minor', size = tick_xminorsize, width = 0.75 * float(spine_widthentry.get()), color = 'black', direction = 'out', top = False)
    ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(tick_xminorpos))

    ax.yaxis.set_tick_params(which = 'minor', size = tick_yminorsize, width = 0.75 * float(spine_widthentry.get()), color = 'black', direction = 'out', right = False)
    ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(tick_yminorpos))

    ax_xcopy.xaxis.set_tick_params(which = 'minor', size = tick_xminorsize, width = 0.75 * float(spine_widthentry.get()), color = 'black', direction = 'in', top = tickvar.get())
    ax_xcopy.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(tick_xminorpos))

    ax_ycopy.yaxis.set_tick_params(which = 'minor', size = tick_yminorsize, width = 0.75 * float(spine_widthentry.get()), color = 'black', direction = 'in', right = tickvar.get())
    ax_ycopy.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(tick_yminorpos))

    if gridcolourvar.get() == '--Select a grid colour--':
        grid_colour = 'grey'
    else:
        grid_colour = gridcolourvar.get()

    ax.grid(which = gridtickvar.get(), axis = gridaxisvar.get(), color = grid_colour, linestyle = '--', linewidth = float(grid_widthentry.get()))
    fig.tight_layout()
    display()

def titleexpand():
    """Opens another window to allow longer graph titles to be typed"""
    global title_expand_entry
    global textbox
    global title_entry
    textbox = tk.Toplevel(height = 2, width = 30)
    textbox.title('Enter the graph title')
    textbox.geometry('300x30')
    title_expand_entry = tk.Entry(textbox, width = 40)
    title_expand_entry.grid(row = 0, column = 0, padx = 2, pady = 2)
    title_expand_entry.insert(0, title_entry.get())
    confirm = tk.Button(textbox, text = 'Enter', padx = 2, pady = 2, command = titleconfirm)
    confirm.grid(row = 0, column = 1)

def titleconfirm():
    """Empties the graph title entry and updates it with the title from the new window"""
    global title_expand_entry
    global textbox
    entered = title_expand_entry.get()
    title_entry.delete(0, tk.END)
    title_entry.insert(0, entered)
    textbox.destroy()

def titleclear():
    """Clears the graph title entry field"""
    global title_entry
    title_entry.delete(0, tk.END)

def labelentry():
    global labelbox
    global x_label
    global y_label
    global label_xvarentry
    global label_yvarentry
    global label_xextraentry
    global label_yextraentry
    global label_xunitentry
    global label_yunitentry

    labelbox = tk.Toplevel(height = 30, width = 50)
    labelbox.title('Change axis titles')
    labelbox.geometry('600x150')
    
    label_xlbl = tk.Label(labelbox, text = 'x-axis:')
    label_xlbl.grid(row = 0, column = 0)
    label_xvarlbl = tk.Label(labelbox, text = 'Variable (italics):')
    label_xvarlbl.grid(row = 1, column = 0)
    label_xvarentry = tk.Entry(labelbox, width = 20)
    label_xvarentry.grid(row = 1, column = 1, padx = 2, pady = 2)
    label_xextralbl = tk.Label(labelbox, text = 'Additional (non-italic):')
    label_xextralbl.grid(row = 1, column = 2)
    label_xextraentry = tk.Entry(labelbox, width = 20)
    label_xextraentry.grid(row = 1, column = 3, padx = 2, pady = 2)
    label_xunitlbl = tk.Label(labelbox, text = 'Units:')
    label_xunitlbl.grid(row = 1, column = 4)
    label_xunitentry = tk.Entry(labelbox, width = 20)
    label_xunitentry.grid(row = 1, column = 5, padx = 2, pady = 2)

    label_ylbl = tk.Label(labelbox, text = 'y-axis:')
    label_ylbl.grid(row = 2, column = 0)
    label_yvarlbl = tk.Label(labelbox, text = 'Variable (italics):')
    label_yvarlbl.grid(row = 3, column = 0)
    label_yvarentry = tk.Entry(labelbox, width = 20)
    label_yvarentry.grid(row = 3, column = 1, padx = 2, pady = 2)
    label_yextralbl = tk.Label(labelbox, text = 'Additional (non-italic):')
    label_yextralbl.grid(row = 3, column = 2)
    label_yextraentry = tk.Entry(labelbox, width = 20)
    label_yextraentry.grid(row = 3, column = 3, padx = 2, pady = 2)
    label_yunitlbl = tk.Label(labelbox, text = 'Units:')
    label_yunitlbl.grid(row = 3, column = 4)
    label_yunitentry = tk.Entry(labelbox, width = 20)
    label_yunitentry.grid(row = 3, column = 5, padx = 2, pady = 2)

    label_confirm = tk.Button(labelbox, text = 'Enter', padx = 2, pady = 2, command = labelupdate)
    label_confirm.grid(row = 4, column = 0)

def labelupdate():
    global labelbox
    global x_label
    global y_label
    global label_xvarentry
    global label_yvarentry
    global label_xextraentry
    global label_yextraentry
    global label_xunitentry
    global label_yunitentry

    x_label = r'$' + label_xvarentry.get() + '$ ' + label_xextraentry.get() + ' / ' + label_xunitentry.get()
    y_label = r'$' + label_yvarentry.get() + '$ ' + label_yextraentry.get() + ' / ' + label_yunitentry.get()
    
    labelbox.destroy()

def labelclear():
    global x_label
    global y_label
    x_label = ''
    y_label = ''

def ticksettings():
    global tick_xmajorsize
    global tick_xmajorpos
    global tick_xminorsize
    global tick_xminorpos
    global tick_ymajorsize
    global tick_ymajorpos
    global tick_yminorsize
    global tick_yminorpos
    global tick_xmajorsizeentry
    global tick_xmajorposentry
    global tick_xminorsizeentry
    global tick_xminorposentry
    global tick_ymajorsizeentry
    global tick_ymajorposentry
    global tick_yminorsizeentry
    global tick_yminorposentry
    global tickbox

    tickbox = tk.Toplevel(height = 2, width = 30)
    tickbox.title('Edit tick settings')
    tickbox.geometry('300x150')
    
    tick_size = tk.Label(tickbox, text = 'Size:')
    tick_size.grid(row = 1, column = 1)
    tick_pos = tk.Label(tickbox, text = 'Position:')
    tick_pos.grid(row = 1, column = 2, columnspan = 2)
    tick_xmajorlbl = tk.Label(tickbox, text = 'Major x-axis ticks:')
    tick_xmajorlbl.grid(row = 2, column = 0)
    tick_xmajorsizeentry = tk.Entry(tickbox, width = 5)
    tick_xmajorsizeentry.grid(row = 2, column = 1)
    tick_xmajorsizeentry.insert(0, str(tick_xmajorsize))
    tick_xmajorposlbl = tk.Label(tickbox, text = 'Every:')
    tick_xmajorposlbl.grid(row = 2, column = 2)
    tick_xmajorposentry = tk.Entry(tickbox, width = 5)
    tick_xmajorposentry.grid(row = 2, column = 3)
    tick_xmajorposentry.insert(0, str(tick_xmajorpos))
    tick_xminorlbl = tk.Label(tickbox, text = 'x-axis minor:')
    tick_xminorlbl.grid(row = 3, column = 0)
    tick_xminorsizeentry = tk.Entry(tickbox, width = 5)
    tick_xminorsizeentry.grid(row = 3, column = 1)
    tick_xminorsizeentry.insert(0, str(tick_xminorsize))
    tick_xminorposlbl = tk.Label(tickbox, text = 'Every:')
    tick_xminorposlbl.grid(row = 3, column = 2)
    tick_xminorposentry = tk.Entry(tickbox, width = 5)
    tick_xminorposentry.grid(row = 3, column = 3)
    tick_xminorposentry.insert(0, str(tick_xminorpos))
    tick_ymajorlbl = tk.Label(tickbox, text = 'y-axis major:')
    tick_ymajorlbl.grid(row = 4, column = 0)
    tick_ymajorsizeentry = tk.Entry(tickbox, width = 5)
    tick_ymajorsizeentry.grid(row = 4, column = 1)
    tick_ymajorsizeentry.insert(0, str(tick_ymajorsize))
    tick_ymajorposlbl = tk.Label(tickbox, text = 'Every:')
    tick_ymajorposlbl.grid(row = 4, column = 2)
    tick_ymajorposentry = tk.Entry(tickbox, width = 5)
    tick_ymajorposentry.grid(row = 4, column = 3)
    tick_ymajorposentry.insert(0, str(tick_ymajorpos))
    tick_yminorlbl = tk.Label(tickbox, text = 'y-axis minor:')
    tick_yminorlbl.grid(row = 5, column = 0)
    tick_yminorsizeentry = tk.Entry(tickbox, width = 5)
    tick_yminorsizeentry.grid(row = 5, column = 1)
    tick_yminorsizeentry.insert(0, str(tick_yminorsize))
    tick_yminorposlbl = tk.Label(tickbox, text = 'Every:')
    tick_yminorposlbl.grid(row = 5, column = 2)
    tick_yminorposentry = tk.Entry(tickbox, width = 5)
    tick_yminorposentry.grid(row = 5, column = 3)
    tick_yminorposentry.insert(0, str(tick_yminorpos))
    tickbox_exitbtn = tk.Button(tickbox, text = 'Update tick settings', command = tickupdate)
    tickbox_exitbtn.grid(row = 6, column = 0, columnspan = 4)

def tickupdate():
    global tick_xmajorsize
    global tick_xmajorpos
    global tick_xminorsize
    global tick_xminorpos
    global tick_ymajorsize
    global tick_ymajorpos
    global tick_yminorsize
    global tick_yminorpos
    global tick_xmajorsizeentry
    global tick_xmajorposentry
    global tick_xminorsizeentry
    global tick_xminorposentry
    global tick_ymajorsizeentry
    global tick_ymajorposentry
    global tick_yminorsizeentry
    global tick_yminorposentry
    global tickbox

    tick_xmajorsize = float(tick_xmajorsizeentry.get())
    tick_xmajorpos = float(tick_xmajorposentry.get())
    tick_xminorsize = float(tick_xminorsizeentry.get())
    tick_xminorpos = float(tick_xminorposentry.get())
    tick_ymajorsize = float(tick_ymajorsizeentry.get())
    tick_ymajorpos = float(tick_ymajorposentry.get())
    tick_yminorsize = float(tick_yminorsizeentry.get())
    tick_yminorpos = float(tick_yminorposentry.get())
    tickbox.destroy()
    
def display():
    global graph
    graph.destroy()
    graph = tk.LabelFrame(root, borderwidth = 5, relief = tk.GROOVE, padx = 2, pady = 2)
    graph.grid(row = 1, column = 1, padx = 2, pady = 2, sticky = tk.NSEW)
    
    global canvas
    canvas = FigureCanvasTkAgg(fig, graph)
    canvas.draw()
    canvas.get_tk_widget().pack()

    global toolbarframe
    toolbarframe = tk.Frame(graph, height = 75)
    toolbarframe.pack(side = tk.LEFT, fill = tk.BOTH)

    clear_btn = tk.Button(toolbarframe, text = 'Clear Graph', command = clear)
    clear_btn.pack(side = tk.LEFT)
    toolbar_lbl = tk.Label(toolbarframe, text = '     Toolbar:')
    toolbar_lbl.pack(side = tk.LEFT)
    
    global toolbarvar
    toolbarvar = tk.IntVar()
    
    toolbar_on = tk.Radiobutton(toolbarframe, text = 'On', variable = toolbarvar, value = 1)
    toolbar_on.pack(side = tk.LEFT)
    toolbar_off = tk.Radiobutton(toolbarframe, text = 'Off', variable = toolbarvar, value = 0)
    toolbar_off.pack(side = tk.LEFT)
    
    toolbarvar.set(0)
    
    toolbar_set = tk.Button(toolbarframe, text = 'Set', command = toolbarstate)
    toolbar_set.pack(side = tk.LEFT)
    
    global toolbar_holder    
    toolbar_holder = tk.Frame(toolbarframe)
    toolbar_holder.pack(side = tk.RIGHT)
    
def clear():
    global graph
    graph.destroy()
    graph = tk.LabelFrame(root, borderwidth = 5, relief = tk.GROOVE, padx = 2, pady = 2)
    graph.grid(row = 1, column = 1, padx = 2, pady = 2, sticky = tk.NSEW)
    
    canvas = tk.Canvas(graph, width = 400, height =500)
    canvas.pack()
    update_btn['state'] = tk.DISABLED

def toolbarstate():   
    global canvas
    global toolbar_holder
    global toolbarvar
    global toolbarframe

    if toolbarvar.get() == 1:
        toolbar = NavigationToolbar2Tk(canvas, toolbar_holder)
        toolbar.update()
        canvas.get_tk_widget().pack(fill = tk.BOTH, expand = 1)
    elif toolbarvar.get() == 0:
        toolbar_holder.destroy()
        toolbar_holder = tk.Frame(toolbarframe)
        toolbar_holder.grid(row = 0, column = 5)

def savefile():
    if save_entry.get() != '':
        output = save_entry.get() + str(savevar.get())[7:] 
        plt.savefig(output, dpi = 100, quality = 95, transparent = False)
        save_entry.delete(0, tk.END)
    else:
        pass


"""ROOT"""
# Create the main graphical interface under the root variable
root = tk.Tk()
# Set the title of the main graphical interface
root.title('MyPyplot')
# Set the icon displayed next to the grahical interface title
#root.iconbitmap('graphicon.ico')


"""FRAMES"""
# Create the frames used to contain all widgets 
title = tk.LabelFrame(root, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
title.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = tk.NSEW)
file = tk.LabelFrame(root, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
file.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = tk.NSEW)
settings = tk.LabelFrame(root, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
settings.grid(row = 1, column = 0, rowspan = 2, padx = 2, pady = 2, sticky = tk.NSEW)
graph = tk.LabelFrame(root, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
graph.grid(row = 1, column = 1, padx = 2, pady = 2, sticky = tk.NSEW)
save = tk.LabelFrame(root, borderwidth = 4, relief = tk.GROOVE, padx = 2, pady = 2)
save.grid(row = 2, column = 1, padx = 2, pady = 2, sticky = tk.NSEW)


"""TITLE"""
tk.Label(title, text = 'MyPyplot ver. 1.0.0.0', pady = 10).pack()


"""FILE"""
open_label = tk.Label(file, text = 'Open File:')
open_label.grid(row = 0, column = 0, pady = 10, sticky = tk.NS)
open_entry = tk.Entry(file, width = 70)
open_entry.grid(row = 0, column = 1)
open_btn = tk.Button(file, text = 'v', command = openfile, padx = 5)
open_btn.grid(row = 0, column = 3, padx = 8)
open_upload = tk.Button(file, text = 'Upload File',command = upload)
open_upload.grid(row = 0, column = 4, padx = 30)


"""SETTINGS"""
title_frm = tk.LabelFrame(settings, text = 'Title of Graph', bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
title_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
title_entry = tk.Entry(title_frm, width = 22)
title_entry.grid(row = 0, column = 0, sticky = tk.W)
title_expand = tk.Button(title_frm, text = '...', command = titleexpand, padx = 3)
title_expand.grid(row = 0, column = 1, padx = 4)
title_clear = tk.Button(title_frm, text = 'Clear title', command = titleclear, padx = 3)
title_clear.grid(row = 0, column = 2, padx = 6)

label_frm = tk.LabelFrame(settings, text = 'Axes Titles', bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
label_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
x_label = ''
y_label = ''
label_btn = tk.Button(label_frm, text = 'Edit axes titles', command = labelentry)
label_btn.grid(row = 0, column = 0, padx = 18)
label_clear = tk.Button(label_frm, text = 'Clear axes titles', command = labelclear)
label_clear.grid(row = 0, column = 1, padx = 18)

factor_frm = tk.LabelFrame(settings, text = 'Axis Scale Factor', bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
factor_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
factor_xlbl = tk.Label(factor_frm, text = 'Divide x-axis by:', anchor = tk.W)
factor_xlbl.grid(row = 0, column = 0, sticky = tk.W)
factor_xentry = tk.Entry(factor_frm, width = 20)
factor_xentry.grid(row = 0, column = 1, padx = 4, sticky = tk.W)
factor_xentry.insert(0, '1')
factor_ylbl = tk.Label(factor_frm, text = 'Divide y-axis by:', anchor = tk.W)
factor_ylbl.grid(row = 1, column = 0, sticky = tk.W)
factor_yentry = tk.Entry(factor_frm, width = 20)
factor_yentry.grid(row = 1, column = 1, padx = 4, sticky = tk.W)
factor_yentry.insert(0, '1')

line_frm = tk.LabelFrame(settings, text = 'Line Settings',bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
line_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
line_widthlbl = tk.Label(line_frm, text = 'Line width:')
line_widthlbl.grid(row = 1, column = 0)
line_widthentry = tk.Entry(line_frm, width = 10)
line_widthentry.grid(row = 1, column = 1)
line_widthentry.insert(0, '2')
colourvar = tk.StringVar()
colours = ['--Select a line colour--', 'Black', 'Red', 'Blue', 'Green']
colourvar.set(colours[0])
line_colours = tk.OptionMenu(line_frm, colourvar, *colours)
line_colours.config(width = 20)
line_colours.grid(row = 2, column = 0, columnspan = 2)

spine_frm = tk.LabelFrame(settings, text = 'Spine Settings', bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
spine_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
spine_widthlbl = tk.Label(spine_frm, text = 'Spine width:')
spine_widthlbl.grid(row = 1, column = 0)
spine_widthentry = tk.Entry(spine_frm, width = 10)
spine_widthentry.grid(row = 1, column = 1)
spine_widthentry.insert(0, '2')
spinevar = tk.BooleanVar()
spinevar.set(True)
spine_on = tk.Radiobutton(spine_frm, text = 'Visible', variable = spinevar, value = True)
spine_on.grid(row = 2, column = 0)
spine_off = tk.Radiobutton(spine_frm, text = 'Hidden', variable = spinevar, value = False)
spine_off.grid(row = 2, column = 1)

scale_frm = tk.LabelFrame(settings, text = 'Axes Limits', bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
scale_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
scale_xlbl = tk.Label(scale_frm, text = 'x-axis:')
scale_xlbl.grid(row = 1, column = 0)
scalexvar = tk.IntVar()
scalexvar.set(1)
scale_xauto = tk.Radiobutton(scale_frm, text = 'Auto', variable = scalexvar, value = 1)
scale_xauto.grid(row = 1, column = 1)
scale_xmanual = tk.Radiobutton(scale_frm, text = 'Manual', variable = scalexvar, value = 0)
scale_xmanual.grid(row = 1, column = 2)
scale_xminlbl = tk.Label(scale_frm, text = 'Min:')
scale_xminlbl.grid(row = 1, column = 3)
scale_xminentry = tk.Entry(scale_frm, width = 5)
scale_xminentry.grid(row = 1, column = 4)
scale_xmaxlbl = tk.Label(scale_frm, text = 'Max:')
scale_xmaxlbl.grid(row = 1, column = 5)
scale_xmaxentry = tk.Entry(scale_frm, width = 5)
scale_xmaxentry.grid(row = 1, column = 6)
scale_ylbl = tk.Label(scale_frm, text = 'y-axis:')
scale_ylbl.grid(row = 2, column = 0)
scaleyvar = tk.IntVar()
scaleyvar.set(1)
scale_yauto = tk.Radiobutton(scale_frm, text = 'Auto', variable = scaleyvar, value = 1)
scale_yauto.grid(row = 2, column = 1)
scale_ymanual = tk.Radiobutton(scale_frm, text = 'Manual', variable = scaleyvar, value = 0)
scale_ymanual.grid(row = 2, column = 2)
scale_yminlbl = tk.Label(scale_frm, text = 'Min:')
scale_yminlbl.grid(row = 2, column = 3)
scale_yminentry = tk.Entry(scale_frm, width = 5)
scale_yminentry.grid(row = 2, column = 4)
scale_ymaxlbl = tk.Label(scale_frm, text = 'Max:')
scale_ymaxlbl.grid(row = 2, column = 5)
scale_ymaxentry = tk.Entry(scale_frm, width = 5)
scale_ymaxentry.grid(row = 2, column = 6)

tick_frm = tk.LabelFrame(settings, text = 'Tick Settings', bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
tick_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
tick_settingsbtn = tk.Button(tick_frm, text = 'Update tick settings', width = 35, command = ticksettings)
tick_settingsbtn.grid(row = 0, column = 0, columnspan = 3)
tick_xmajorsize = 10
tick_xmajorpos = 1
tick_xminorsize = 10
tick_xminorpos = 1
tick_ymajorsize = 5
tick_ymajorpos = 0.5
tick_yminorsize = 5
tick_yminorpos = 0.5
tick_bothlbl = tk.Label(tick_frm, text = 'Second axis ticks:')
tick_bothlbl.grid(row = 2, column = 0)
tickvar = tk.BooleanVar()
tickvar.set(True)
tick_bothon = tk.Radiobutton(tick_frm, text = 'On', variable = tickvar, value = True)
tick_bothon.grid(row = 2, column = 1)
tick_bothoff = tk.Radiobutton(tick_frm, text = 'Off', variable = tickvar, value = False)
tick_bothoff.grid(row = 2, column = 2)

grid_frm = tk.LabelFrame(settings, text = 'Grid Settings', bd = 2, relief = tk.GROOVE, padx = 2, pady = 2)
grid_frm.pack(padx = 2, pady = 2, anchor = tk.W, fill = tk.X)
grid_ticklbl = tk.Label(grid_frm, text = 'Which tick:')
grid_ticklbl.grid(row = 1, column = 0)
gridtickvar = tk.StringVar()
gridtickvar.set('major')
grid_tickmajor = tk.Radiobutton(grid_frm, text = 'Major', variable = gridtickvar, value = 'major')
grid_tickmajor.grid(row = 1, column = 1)
grid_tickminor = tk.Radiobutton(grid_frm, text = 'Minor', variable = gridtickvar, value = 'minor')
grid_tickminor.grid(row = 1, column = 2)
grid_axislbl = tk.Label(grid_frm, text = 'Which axis:')
grid_axislbl.grid(row = 2, column = 0)
gridaxisvar = tk.StringVar()
gridaxisvar.set('both')
grid_axisx = tk.Radiobutton(grid_frm, text = 'x', variable = gridaxisvar, value = 'x')
grid_axisx.grid(row = 2, column = 1)
grid_axisy = tk.Radiobutton(grid_frm, text = 'y', variable = gridaxisvar, value = 'y')
grid_axisy.grid(row = 2, column = 2)
grid_axisboth = tk.Radiobutton(grid_frm, text = 'both', variable = gridaxisvar, value = 'both')
grid_axisboth.grid(row = 2, column = 3)
grid_colourlbl = tk.Label(grid_frm, text = 'Grid color:')
grid_colourlbl.grid(row = 3, column = 0)
gridcolourvar = tk.StringVar()
gridcolours = ['--Select a grid colour--', 'Black', 'Grey']
gridcolourvar.set(gridcolours[0])
grid_colours = tk.OptionMenu(grid_frm, gridcolourvar, *gridcolours)
grid_colours.config(width = 20)
grid_colours.grid(row = 3, column = 1, columnspan = 4)
grid_widthlbl = tk.Label(grid_frm, text = 'Grid width:')
grid_widthlbl.grid(row = 4, column = 0)
grid_widthentry = tk.Entry(grid_frm, width = 5)
grid_widthentry.grid(row = 4, column = 1)
grid_widthentry.insert(0, '0.5')

update_btn = tk.Button(settings, text = 'Update Graph', state = tk.DISABLED, command = update)
update_btn.pack(side = tk.BOTTOM, fill = tk.X)


"""GRAPH"""
canvas = tk.Canvas(graph, width = 450, height =550)
canvas.pack()


"""SAVE"""
save_label = tk.Label(save, text = 'Save graph as:')
save_label.grid(row = 0, column = 0)
save_entry = tk.Entry(save, width = 50)
save_entry.grid(row = 0, column = 1)

savevar = tk.StringVar()

save_png = tk.Radiobutton(save, text = '.png', variable = savevar, value = '.png')
save_png.grid(row = 0, column = 2)
save_eps = tk.Radiobutton(save, text = '.eps', variable = savevar, value = '.eps')
save_eps.grid(row = 0, column = 3)
savevar.set('.png')

save_btn = tk.Button(save, text = 'Save Graph', command = savefile)
save_btn.grid(row = 0, column = 4, padx = 5, pady = 5)
exit = tk.Button(save, text = 'Exit Program', command = root.quit)
exit.grid(row = 0, column = 5, padx = 5, pady = 5)


"""END"""
root.mainloop()
plt.close()

