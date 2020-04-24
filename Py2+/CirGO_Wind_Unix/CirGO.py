""" CirGO 
    Version 1.0 01/03/2018
    
    CirGO (Circular Gene Ontology) software is an alternative way of visualising GO terms in 2D space 
    that is suitable for publishing and presenting gene expression ontology data.

    Copyright (C) 2018 Irina Kuznetsova
    This software is licensed under the terms of the GNU general public license (version 3).
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
 
    If you are using the software as a part of your research work, please cite the following publication:
    Kuznetsova I, Lugmayr A, Siira SJ, Rackham O, Filipovska A. 
    CirGO: an alternative circular way of visualising gene ontology terms. BMC Bioinformatics [Internet]. 
    2019 Feb 18;20(1):84. Available from: https://doi.org/10.1186/s12859-019-2671-2
    
    Contact info:   irina.kuznetsova@uwa.edu.au 
    GitHub:         https://github.com/IrinaVKuznetsova/CirGO.git 
"""
   
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## I. Import required modules
## ----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
import os
import sys
import argparse
import numpy as np                     
import matplotlib as mpl
#mpl.use("TkAgg")       #  for Mac OS
from matplotlib import pyplot as plt
from collections import OrderedDict   
from argparse import RawTextHelpFormatter

import Tkinter as tk
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

import GUIElements
import CirGoFileConversion
import CirGOVisualGO
import traceback


##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## II. Default constants utilized in the software package
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------
DEFAULT_FONT_SIZE = 7
DEFAULT_NUM_OF_CATEGORIES = 40
DEFAULT_LEGEND_NAME = "Name and Proportion of the Biological Process (Inner Ring)"     


##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## III. Graphical User Interface (GUI) implementation
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
class Application(tk.Frame):
    inputFileName = None
    fileNameLabel = None
    outputFileName = None

    def __init__(self, master = None, nrCategories = DEFAULT_NUM_OF_CATEGORIES, fontSize = DEFAULT_FONT_SIZE, figureLegend = DEFAULT_LEGEND_NAME):
        # initialize variables and constant, and assign the default values to them
        self.nrCategories = IntVar()
        self.fontSize = DoubleVar()
        self.figureLegend = StringVar()
        self.nrCategories.set(nrCategories)
        self.fontSize.set(fontSize)
        self.figureLegend.set(figureLegend)
        self.InputFileName = None
        self.OutputFileName = None

        # initialize the frame
        self.frame = Frame.__init__(self, master, relief = RAISED, borderwidth = 2, padx = 2, pady = 2)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.columnconfigure(0, pad = 3)
        self.rowconfigure(3, pad = 3)

        # buttons and actions as toolbar
        toolbar = Frame(self)
        self.openFileButton = tk.Button(toolbar, width = 10, text = 'Open File...', command = self.openInputFile)
        self.openFileButton.pack(side = LEFT, fill = X, padx = 2, pady = 2)
    
        self.batchProcessDirectory = tk.Button(toolbar, width = 10, text = 'Batch Proc...', command = self.batchProcess)
        self.batchProcessDirectory.pack(side = LEFT, fill = X, padx = 2, pady = 2)
        self.batchProcessDirectory.config(state = 'disabled')

        self.visualiseButton = tk.Button(toolbar, width = 10, text = 'Visualise', command = self.createVisualisation)  
        self.visualiseButton.pack(side = LEFT, fill = X, padx = 2, pady = 2)
        self.visualiseButton.config(state = DISABLED)
        self.closeButton = tk.Button(toolbar, width = 10, text = 'Close File', command = self.closeFile)       
        self.closeButton.pack(side = LEFT, fill = X, padx = 2, pady = 2)
        self.closeButton.config(state = DISABLED)

        self.quitButton = tk.Button(toolbar, width = 10, text = 'Exit', command = self.quit)
        self.quitButton.pack(side = RIGHT, fill = X, padx = 2, pady = 2)
        toolbar.grid(row = 6, columnspan = 2, sticky = tk.W + tk.E)

        # windows components
        self.numberOfCategoriesLabel = tk.Label(self, justify = tk.LEFT, text = "Number of Categories (default: " + str(DEFAULT_NUM_OF_CATEGORIES) + "): ")
        self.numberOfCategoriesLabel.grid(row = 0, column = 0, sticky = tk.W)        
        self.numberOfCategoriesEntry = tk.Entry(self, width = 50, textvariable = self.nrCategories, validate = "key")
        self.numberOfCategoriesEntry.grid(row = 0, column = 1)
        self.numberOfCategoriesEntry['validatecommand'] = (self.numberOfCategoriesEntry.register(GUIElements.testValInt), '%P', '%i', '%d')

        self.fontSizeLabel = tk.Label(self, justify = tk.LEFT, text = "Font Size (default: " + str(DEFAULT_FONT_SIZE) + "): ")
        self.fontSizeLabel.grid( row = 1, column = 0, sticky = tk.W)
        self.fontSizeEntry = tk.Entry(self, width = 50, textvariable = self.fontSize, validate = "key")
        self.fontSizeEntry.grid(row = 1, column = 1)        
        self.fontSizeEntry['validatecommand'] = (self.fontSizeEntry.register(GUIElements.testValFloat), '%P', '%i', '%d')

        self.figureLegendLabel = tk.Label(self, justify = tk.LEFT, text = "Figure Legend: \n (default: " + str(DEFAULT_LEGEND_NAME) + ") ")
        self.figureLegendLabel.grid(row = 2, column = 0, sticky = tk.W)
        self.figureLegendEntry = tk.Entry(self, width = 50, textvariable = self.figureLegend)
        self.figureLegendEntry.grid(row = 2, column = 1)

        self.saveFileButton = tk.Button(self, width = 30, text = 'Save output as SVG...', command = self.saveOutputFile)
        self.saveFileButton.grid(row = 3, column = 0, sticky = tk.W)
        self.saveFileLegendLabel = tk.Label(self, justify = tk.LEFT, width = 50, text = self.outputFileName)
        self.saveFileLegendLabel.grid(row = 3, column = 1,  sticky = tk.W)
        
        # windows component for information dispay
        self.fileNameLabel = tk.Label(self, justify = tk.LEFT, text = "Current File/Path: " + str(self.inputFileName))
        self.fileNameLabel.grid(row = 4, columnspan = 2, sticky = tk.W) 

        # create the status bar
        self.statusBar = GUIElements.GUIStatusBar(master = self)
        self.statusBar.setMessage("Ok.")
        self.statusBar.grid(row = 5, columnspan = 2, sticky = tk.W + tk.E)

        self.pack()
    
    def openInputFile(self):
        self.inputFileName = tkFileDialog.askopenfilename(title = "Open REVIGO Comma Separated File...", initialdir = (os.path.expanduser('~/')), filetypes = [("csv file","*.csv")], defaultextension = '.csv')
        if (self.inputFileName):
            print(self.inputFileName)
            self.visualiseButton.config(state = "normal")
            self.closeButton.config(state = "normal")
            self.fileNameLabel.config(text = "Current File/Path: " + str(self.inputFileName))
            self.statusBar.setMessage("File opened: " + str(self.inputFileName))

        if (self.outputFileName == None):
            ofn, ofp = os.path.splitext(self.inputFileName)
            self.outputFileName = ofn + ".svg"
            self.saveFileLegendLabel.configure(text = str(self.outputFileName))
    
    def batchProcess(self):
        print("ddd")                

    def saveOutputFile(self):
        outputFilenameDialogue = tkFileDialog.asksaveasfilename(initialdir = "/", title = "Select file", filetypes = [("svg files","*.svg")])
        if not (outputFilenameDialogue == ""):
            ofn, ofp = os.path.splitext(outputFilenameDialogue)
            self.outputFileName = ofn + ".svg"
            self.saveFileLegendLabel.configure(text = ofn + ".svg")

    def closeFile(self):
        self.inputFileName = None
        self.visualiseButton.config(state = "disabled")
        self.closeButton.config(state = "disabled")
        inputFileName = None
        self.fileNameLabel.config(text = "Current File/Path: " + str(inputFileName))
        self.statusBar.setMessage("File closed.")

    def createVisualisation(self):
        try:
            CirGoFileConversion.ConvertToThreeCoulmnsInput(self.inputFileName)
        except:
            self.statusBar.setMessage("File could not be converted. Please check the file format and it's content!")
            traceback.print_exc()
        else:
            try:
                ifn, ife = os.path.splitext(self.inputFileName)
                CirGOVisualGO.CircularVisualGO(ifn + "_converted.csv", int(self.nrCategories.get()), float(self.fontSize.get()), self.figureLegendEntry.get(), self.outputFileName)    ########### Propoer file naming
            except:
                self.statusBar.setMessage("File could not be visualised!")
                traceback.print_exc()


##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## IV. MAIN
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
def printArgs(args):                          
    print (args)

def main (argv):
    print (argv)
    argsparser = argparse.ArgumentParser(
        prog = "CirGO",
        usage = 
        'This is the command line interface for the CirGO visualisation software.\n'+
        '\n HELP: help for using the software. python CirGO.py -h\n' +
        '\n GUI: usage for the graphical user interface option of the CirGO software. python CirGO.py -gui\n' +
        '\n COMMAND LINE (CMD): usage for the command line option of the CirGO software. python CirGO.py - inputFile INPUTFILE [-outputFile OUTPUTFILE] [-fontSize FONTSIZE] [-numCat NRCATEGORIES] [-leg FIGURE_LEGEND]\n' +
        '\n INTERACTIVE MODE (INT): interactive option of the CirGO software. python CirGO.py -int\n ',
        formatter_class = RawTextHelpFormatter,
        epilog = "Copyright (C) 2018. This software is licensed under the terms of the GNU general public license (version 3).\nIf you use this software, please cite the following publication: .......")
    
    arg_group_dummy = argsparser.add_argument_group('', '--------------------------------------------------------------------------------------------------------------------')
    
    arg_group_gui = argsparser.add_argument_group('GUI', 'Graphical User Interface (GUI) option of the CirGO software.\nExample: python CirGO.py -gui')
    arg_group_gui.add_argument("-gui", action = 'store_true', help = "GUI option of the CirGO software. If this option is selected, all other command line parameters will be ignored.\n")
    arg_group_gui.add_argument("    ", action = 'store_true')
    
    arg_group_cmd = argsparser.add_argument_group('CMD', 'Command line option of the CirGO software. \nExample: python CirGO.py -inputFile C:\\mydir\Example_REVIGO_Input_BP.csv -outputFile C:\\mydir\\Visual_BP.svg -fontSize 6.5 -numCat 40 -legend "Name & Proportion of Biological process (inner ring)"')
    arg_group_cmd.add_argument("-inputFile", default = None, type = str, help = "[csv] Input path and filename of a REVIGO file. \nExample: C:\\mydir\\Example_REVIGO_Input_BP.csv")
    arg_group_cmd.add_argument("-outputFile", default = None, type = str, help = "[svg] Output path and filename. \nExample: C:\\mydir\\Visual_BP.svg")
    arg_group_cmd.add_argument('-fontSize', type = float, default = DEFAULT_FONT_SIZE, help = "[float] Font Size (Default: " + str(DEFAULT_FONT_SIZE) +  "). Select one from the range 6.0 -7.5 \nExample: 6.5")
    arg_group_cmd.add_argument('-numCat', type = int, default = DEFAULT_NUM_OF_CATEGORIES, help = "[int] Number of Categories to be visualised. (Default: " + str(DEFAULT_NUM_OF_CATEGORIES) + "). \nExample: 60 or lower")
    arg_group_cmd.add_argument('-legend', type = str, default = DEFAULT_LEGEND_NAME, help = "[str] Legend title to be displayed in the figure. Select relevant example of the legend name. \nExample:\n   (1) Name & Proportion of Biological process (inner ring)\n   (2) Name & Proportion of Cellular component (inner ring)\n   (3) Name & Proportion of Molecular function (inner ring) ")
    arg_group_cmd.add_argument("    ", action = 'store_true')

    arg_group_int = argsparser.add_argument_group('INT', 'Interactive option of the CirGO software. \nExample: python CirGO.py -int\n')
    arg_group_int.add_argument("-int", action = 'store_true', help = "Interactive option of the CirGO software. \nInput file from REVIGO as CSV [str]: 'C://mydir/Example_REVIGO_Input_BP.csv'    ***NOTE*** provide a file directory as a string, where a backslash '\\' has to be changed to the forward slash '/'.\n      \nFont Size (Example - 7.0) [float]: 7.0\n      \nNumber of Categories (Example - 40) [int]: 40\n     \nLegend name. Example: 'Name & Proportion of Biological process (inner ring)' [str]: 'Name & Proportion of Biological process (inner ring)'    ***NOTE*** Select relevant example of the legend name.\n        \nOutput file in svg format (Example: input filename + svg) [str]: 'C://mydir/Visual_BP.svg'    ***NOTE*** provide a file directory as a string, where a backslash '\\' has to be changed to the forward slash '/'.\n ") 


    args = argsparser.parse_args()

    # validate arguments
    if (args.fontSize <=1) or (args.numCat <1):
        print ("Wrong command line parameters: fontSize must be a positive float value, and numCat must be an positive integer value!")
        sys.exit()
    try:
        args.fontSize = float(args.fontSize)
        args.numCat = int(args.numCat)
    except:
        print ("Wrong command line parameters: fontSize must be a positive float value, and numCat must be an positive integer value!")
        traceback.print_exc()
        sys.exit()

    if (not args.gui) and (args.inputFile == None) and (not args.int):
        print("To see a help page, python CirGO.py -h. Otherwise select the GUI, command line or interactive mode of the software!")
        traceback.print_exc()
        sys.exit()
    
    if args.gui:
        root = Tk()  
        app = Application(master = root)
        app.master.title('CirGO - Circular Gene Ontology terms Visualisation')
        app.mainloop()
        root.destroy()

    elif args.int:
# Input File --------------------------------------------------------------------------------------------------------------------
        infl = input("Input file from REVIGO as CSV [str]: ")
        if type(infl) != str:
            print("Wrong command line parameters: Input File must be a string.")
            sys.exit()
        try:
            infl = str(infl)
        except:
            print ('Input file is not a string. Please enter a valid filename as a string.')
            traceback.print_exc()
            sys.exit() 
# Font Size --------------------------------------------------------------------------------------------------------------------
        insize = raw_input("Font Size (Example - 7.0) [float]: ")
        if insize == ""  :
            print("Default Font Size is used. [Example: 7.0]")  
            insize = DEFAULT_FONT_SIZE
        elif type(float(insize)) != float:
             print("Wrong command line parameters: Font Size must be a positive float value")
             sys.exit()
        elif float(insize) < 0:
             print("Wrong command line parameters: Font Size must be a positive float value")
             sys.exit()
        try:
            insize = float(insize) 
        except:
            print ("Font Size is not a float. Please enter Font Size as a float.")
            traceback.print_exc()
            sys.exit()
# Number of Categories--------------------------------------------------------------------------------------------------------------------
        incat = raw_input("Number of Categories (Example - 40) [int]: ")  #  a string
        if incat == "":
            print("Default Number of Categories is used [Example: 40]")
            incat = DEFAULT_NUM_OF_CATEGORIES
        elif type(int(float(incat))) != int:
            print("Wrong command line parameters: Number of Categories must be a positive integer value")
            sys.exit()
        elif int(float(incat)) < 0:
            print("Wrong command line parameters: Number of Categories must be a positive integer value")
            sys.exit()
        try:
            incat = int(float(incat))
        except:
            print ("Number of Categories is not an integer. Please enter a valid number as an integer.")
            traceback.print_exc()
            sys.exit()
# Legend--------------------------------------------------------------------------------------------------------------------
        inleg = raw_input('Legend name. Example: "Name & Proportion of Biological process (inner ring)" [str]: ')
        if inleg == "":
            print('Default Legend Name is used [Example: "Name & Proportion of Biological process (inner ring)"]')
            inleg = DEFAULT_LEGEND_NAME
        elif type(inleg) != str:
            print("Wrong command line parameters: Legend name must be a string.")
            sys.exit()
        try:
            inleg = str(inleg)
        except:
            print ("Legen Name is not a string. Please enter a valid Legend Name as a string.")
            traceback.print_exc()
            sys.exit()
# OutputFile--------------------------------------------------------------------------------------------------------------------
        outfl = input("Output file in svg format (Example: input filename + svg) [str]: ")
        if type(outfl) != str:
            print("Wrong command line parameters: Output file must be a string.")
            sys.exit()
        try:
            outfl = str(outfl)
        except:
            print ("Output file is not a string. Please enter a valid filename as a string.")
            traceback.print_exc()
            sys.exit()
        
        CirGoFileConversion.ConvertToThreeCoulmnsInput(infl, infl + "_converted.csv")
        CirGOVisualGO.CircularVisualGO(infl + "_converted.csv", int(incat), float(insize), str(inleg), str(outfl))
    
    else:
        try:
            if os.path.isfile(args.inputFile):
                print("Opening input file: " + args.inputFile)
                fn, fe = os.path.splitext(args.inputFile)
                if (args.outputFile == None):
                    args.outputFile = fn+ ".svg"
                CirGoFileConversion.ConvertToThreeCoulmnsInput(args.inputFile, fn+ "_converted.csv")
            else:
                print ("Input file could not be found. Please enter a valid filename.")
                sys.exit()
        except:
            print("File could not be converted. Please check if the file exists and if the file format is correct!")
            traceback.print_exc()
            sys.exit()
        try:
            fn, fe = os.path.splitext(args.inputFile)

            CirGOVisualGO.CircularVisualGO(fn + "_converted.csv", int(args.numCat), float(args.fontSize), args.legend, args.outputFile)
        except:
            traceback.print_exc()
            print("File could not be visualised!")
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])