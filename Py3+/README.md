# CirGO

*CirGO (Circular Gene Ontology) Version 2.0 Py3 24/04/2020  
© Copyright (C) 2020  
https://github.com/IrinaVKuznetsova/CirGO.git  
  
Software development by:  

Irina Kuznetsova, irina.kuznetsova@perkins.org.au  
Artur Lugmayr, lartur@acm.org  

```diff
! Version 2.0 | Python 3+ | 24/04/2020 
```
*This manual was designed to help people with limited or no programming experience to install the CirGO software*  


Running under Windows  
======

### INSTALLATION GUIDE PYTHON 3+  



1. Download  [Anaconda distribution](https://www.anaconda.com/distribution/) also called Anaconda Prompt for Python 3.7 on your Windows machine  

1. Open Anaconda Prompt terminal  
1. Create a virtual environment with Python 3.7 version. Virtual environment acts as an isolated platform where you can install all required packages for the specific project without modifying existing projects. For example, if your computer has Python 2.7, you can easily install Python 3+ without affecting Python 2+  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a new environment ): `conda create -n YourEnvirName python=3.7`  
 
1. Activate created virtual environment   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Activate created environment): `> activate YourEnvirName`       
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Check installed packages. Note: Should have Python 3+ installed): `(YourEnvirName)> conda list`       
 
1. Download the CirGO software from GitHub repository as zip folder (*Clone or Download*; *Download ZIP*). Unzip folder into a directory of your choice. For example, to the desktop  

1. Navigate Anaconda Prompt terminal to the *setup.py* script of the CirGO software, which is located at the *docs* folder  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to *docs* folder): `(YourEnvirName)> cd YOURPATH\CirGO-master\docs`  

1. Create a source distribution for CirGO package. This step generates two folders *CirGO.egg-info* and *dist*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a source distribution) : `(YourEnvirName)> python setup.py sdist`

1. Navigate to the *dist* folder and install CirGO package  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to a folder):`(YourEnvirName)> cd dist`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install CirGO package);`(YourEnvirName)> pip install CirGO-0.1.0.tar.gz`  

1. Navigate to the *CirGO_Wind_Unix* folder  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to the *CirGO_Wind_Unix* folder):`(YourEnvirName)> cd YOURPATH\CirGO-master\CirGO_Wind`  

### HELP PAGE  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page):`(YourEnvirName)> python CirGO.py –h`  



### CirGO PACKAGE USAGE  

There are three options on CirGO usage:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Graphical User Interface (GUI);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Command Line (CMD);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) Interactive Command Line (INT)  

#### (1) Graphical User Interface (GUI)  
Graphical User Interface (GUI) is the simplest option for visualising GO terms. When the command *python CirGO.py -gui* is executed an interactive window will pop-up. The required parameters can be changed or left as default, an input file can be opened with the *Open File* button, and visualised by pressing *Visualize* button. The output file will be automatically saved in *svg* format to the same folder with the input file, or the output file name can be changed by pressing *Save output as SVG* button. Please note, that the legend name should be changed depending on what process (biological process, cellular component, or molecular function) is visualised. To leave GUI press *Exit*   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Graphical user interface):`(YourEnvirName)> python CirGO.py –gui`  

#### (2) Command Line (CMD)  
Command Line (CMD) requires a user to provide parameters in the command line space as described at the help page:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page): `(YourEnvirName)> python CirGO.py -h`  
&nbsp;  
*CirGO - inputFile INPUTFILE [-outputFile OUTPUTFILE] [-fontSize FONTSIZE] [-numCat NRCATEGORIES] [-leg FIGURE_LEGEND]*  
&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example:** `(YourEnvirName)> python CirGO.py -inputFile Example_REVIGO_Input_BP.csv -outputFile Visual_BP.svg -fontSize 6.5 -numCat 40 -legend "Name & Proportion of Biological process (inner ring)"`  

#### (3) Interactive Command Line (INT) 
Interactive (INT) command line option enables to run the CirGO software in the interactive mode  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Interactive command line (INT)):`(YourEnvirName)> python CirGO.py -int`  
**CirGO [-int]**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**inputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input path and filename of an REVIGO file. **NOTE**, provide a file directory as a string, where PATH backslashes '\\' have to be changed to forward slashes '/'    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**outputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output path and filename in svg format. **NOTE**, provide a file directory as a string, where PATH backslashes '\\' have to be changed to forward slashes '/'      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**fontSize:** [float]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive float value (Example: 7.0). It is advised to select one from 6.0 -7.0   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**numCat:** [int]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive integer value of categories to be visualised (Example: 40)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**legend:** [str]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Legend title to be displayed in the figure. A string (Example: Name & Proportion of Biological process (inner ring)). Select relevant example of the legend name:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Name & Proportion of Biological process (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Name & Proportion of Cellular component (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3 )Name & Proportion of Molecular function (inner ring)   


### CirGO PACKAGE RE-USAGE  
1. Open Anaconda Prompt terminal  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Activate created environment): `> activate YourEnvirName`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to *CirGO_Wind_Unix* folder): `(YourEnvirName)> cd YOURPATH\CirGO_Wind_Unix`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page):`(YourEnvirName)> python CirGO.py –h`  

 
**Version control CirGO Version 2.0 Python 3+:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tested on Windows 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Conda 4.8.3  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python 3.7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NumPy 1.18.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Matplotlib 3.2.1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Seaborn 0.10.1    


## Visualisation Example  
![visualisation of GO terms for Biological Process](https://github.com/IrinaVKuznetsova/CirGO/blob/master/Py2%2B/docs/Visual_BP.svg)  

## Example Dataset  
The example dataset was obtained from [GSE83471](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE83471)  

## Copyright Notice  
This project is licensed under the terms of the **GNU version 3** general public license  

## Cite  
Kuznetsova I, Lugmayr A, Siira SJ, Rackham O, Filipovska A. CirGO: an alternative circular way of visualising gene ontology terms. BMC Bioinformatics [Internet]. 2019 Feb 18;20(1):84. Available from: https://doi.org/10.1186/s12859-019-2671-2  
 




