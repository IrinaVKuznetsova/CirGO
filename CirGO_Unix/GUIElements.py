""" CirGO 
    Version 1.0 01/03/2018
    
    CirGO (Circular Gene Ontologies) is an alternative way of visualizing GO terms in 2D space 
    that is suitable for publishing and presenting gene expression ontologies data.

    Copyright (C) 2018 Irina Kuznetsova
    This software is licensed under the terms of the GNU general public license (version 3).
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
    If you are using the softwareas a part of your research work, please cite the following publication
    
    Conract info:   irina.kuznetsova@uwa.edu.au 
    GitHub:         https://github.com/KIVMito/CirGO.git 
"""

##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## I. Import required modules
## ----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
from Tkinter import *
import Tkinter as tk




def testValInt( str, i, action):
    value = int(i)
    if action == '1':
        if not str[value].isdigit():
            return False
        return True

def testValFloat( str, i, action):
    print(str)
    print (i)
    print(action)
    value = int(i)
    if action == '1':
        if not str[value].isdigit():
            if not str[value] == '.':
                return False
            else:
                if str.count('.')>1:
                    return False
        return True


class GUIStatusBar(tk.Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.label = Message(self, text = "", width = 2000, anchor = W, relief = SUNKEN, justify=tk.LEFT, fg="red", bg="white", bd=1)
        self.label.pack(fill=X)

    def setMessage(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()
