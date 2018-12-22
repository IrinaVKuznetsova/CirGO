# CirGO

*CirGO (Circular Gene Ontologies) Version 1.0 01/03/2018  
© Copyright (C) 2018  
Irina Kuznetsova, irina.kuznetsova@uwa.edu.au  
https://github.com/IrinaVKuznetsova/CirGO.git  

*This manual was designed to help people with limited or no programming experience to install the CirGO software.*


 
General Usage Notes
------

**Description:** CirGO (Circular Gene Ontologies) is an alternative way of visualizing GO terms in 2D space that is suitable for publishing and presenting gene expression ontologies data.  

**Dependencies:** The software package was developed under **Python 2.7** with specific versions of **NumPy 1.13.1**, and **Matplotlib 2.1.0**. CirGO software can be run on *Windows, Unix\Linux, or Mac OS*. There are two folders that contains scripts requires for running the CirGO software on:  
* [Windows and Unix](https://github.com/IrinaVKuznetsova/CirGO/tree/master/CirGO_Wind_Unix)   
* [Mac OS](https://github.com/IrinaVKuznetsova/CirGO/tree/master/CirGO_Mac) contains own scripts.

**Software architecture:**  
CirGO can be run on Windows, Unix/Linux and Mac OS as:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Graphical User Interface (GUI)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2)  Command Line (CMD)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) Interactive Command Line (INT)  

Brief Algorithm Description
------

Briefly, CirGO visualization algorithm consists of three steps that are described at the Supplementary Material of the [X]() publication:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Formatting of the *csv* input file obtained from the TreeMap tab on [REVIGIO page](http://revigo.irb.hr/).    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Values calculation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) GO Visualization as two-layer full hierarchies.


Input Data Format
------

#### REVIGIO csv input file 
Note: four header lines are omitted.  

| term_ID | description | frequencyInDb | log10pvalue | uniqueness | dispensability | representative
| - | - | - | - | - | - | - | 
GO:0002376 | immune system process | 0.6% | -7.6615 | 0.994 | 0 | immune system process
GO:0006950 | response to stress | 4.58%  | -24.6003 | 0.937 | 0 | response to stress
GO:1901700 | response to oxygen-containing compound | 0.5%  | -9.8297 | 0.943 | 0.683 | response to stress
GO:0023051 | regulation of signaling | 0.93% | -9.5272 | 0.817 | 0.636 | response to stress
... | ... | ... | ... | ... | ... | ...  


#### Formatted three columns input for visualization   
Note: there is no header.  

| | | |
|-|-|-|
immune system process | 7.6615 | immune system process
response to stress | 24.6003 | response to stress
response to oxygen-containing compound | 9.8297 | response to stress
regulation of signaling | 9.5272 | response to stress
... | ... | ... 





Running under Windows 
======

### INSTALLATION GUIDE

1. Download  [Anaconda distribution](https://www.anaconda.com/download/) also called Anaconda Prompt for Python 2.7 on your Windows machine. 

1. Open Anaconda Prompt terminal.
 
1. Create a virtual environment. Virtual environment acts as an isolated platform where you can install all required packages for the specific project without modifying existing projects. For example, if your computer has Python 2.7, you can easily install Python 3+ without affecting Python 2+.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a new environment ): `> conda create --name SelectEnvirName`

1. Activate created virtual environment.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Activate created environment): `> activate SelectEnvirName`       
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Check installed packages. Note: Empty environment has no installed packages): `(SelectEnvirName)> conda list`       
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install  *pip*, which is package manager, and enables installation of required software): `(SelectEnvirName)> conda install pip`      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Check installed packages): `(SelectEnvirName)> conda list`  

1. Download the CirGO software from GitHub repository as zip folder (*Clone or Download*; *Download ZIP*). Unzip folder into a directory of your choice. For example, to the desktop.

1. Navigate Anaconda Prompt terminal to the *setup.py* script of the CirGO software, which is located at the *docs* folder.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to *docs* folder): `(SelectEnvirName)> cd YOURPATH\CirGO_Py_VisualSoftware-master\docs`

1. Create a source distribution for CirGO package. This step generates two folders *CirGO.egg-info* and *dist*.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a source distribution) : `(SelectEnvirName)> python setup.py sdist`

1. Navigate to the *dist* folder and install CirGO package.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to a folder):`(SelectEnvirName)> cd dist`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install CirGO package);`(SelectEnvirName)> pip install CirGO-0.1.0.tar.gz`

1. Navigate to the *CirGO_Wind_Unix* folder.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to the *CirGO_Wind_Unix* folder):`(SelectEnvirName)> cd YOURPATH\CirGO_Py_VisualSoftware-master\CirGO_Wind_Unix`



### HELP PAGE  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page):`(SelectEnvirName)> python CirGO.py –h`



### CirGO PACKAGE USAGE

There are three options on CirGO usage:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Graphical User Interface (GUI);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Command Line (CMD);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) Interactive Command Line (INT).

#### (1) Graphical User Interface (GUI)  
Graphical User Interface (GUI) is the simplest option for visualizing GO terms. When the command *python CirGO.py -gui* is executed an interactive window will pop-up. The required parameters can be changed or left as default, an input file can be opened with the *Open File* button, and visualized by pressing *Visualize* button. The output file will be automatically saved in *svg* format to the same folder with the input file, or the output file name can be changed by pressing *Save output as SVG* button. Please note, that the legend name should be changed depending on what process (biological process, cellular component, or molecular function) is visualized. To leave GUI press *Exit*.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Graphical user interface):`(SelectEnvirName)> python CirGO.py –gui`

#### (2) Command Line (CMD)  
Command Line (CMD) requires a user to provide parameters in the command line space as described at the help page:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page): `(SelectEnvirName)> python CirGO.py -h`  
&nbsp;  
*CirGO - inputFile INPUTFILE [-outputFile OUTPUTFILE] [-fontSize FONTSIZE] [-numCat NRCATEGORIES] [-leg FIGURE_LEGEND]*  
&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example:** `(SelectEnvirName)> python CirGO.py -inputFile Example_REVIGO_Input_BP.csv -outputFile Visual_BP.svg -fontSize 6.5 -numCat 40 -legend "Name & Proportion of Biological process (inner ring)"`  

#### (3) Interactive Command Line (INT) 
Interactive (INT) command line option enables to run the CirGO software in the interactive mode.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Interactive command line (INT)):`(SelectEnvirName)> python CirGO.py -int`  
**CirGO [-int]**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**inputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input path and filename of an REVIGO file. **NOTE**, provide a file directory as a string, where a PATH backslashes '\' has to be changed to the forward slashes '/'.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**outputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output path and filename in svg format. **NOTE**, provide a file directory as a string, where a PATH backslashes '\' has to be changed to the forward slashes '/'.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**fontSize:** [float]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive float value (Example: 7). It is advised to select one from 6.0 -7.0.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**numCat:** [int]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive integer value of categories to be visualized (Example: 40).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**legend:** [str]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Legend title to be displayed in the figure. A string (Example: Name & Proportion of Biological process (inner ring)). Select relevant example of the legend name:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Name & Proportion of Biological process (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Name & Proportion of Cellular component (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3 )Name & Proportion of Molecular function (inner ring)   

![Snapshot of -INT option](https://github.com/IrinaVKuznetsova/CirGO/blob/master/docs/Visual_BPWind_INToption_example.svg)
 
**Version control:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tested on Windows 7 Professional / Windows 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Conda 4.3.25  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python 2.7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NumPy 1.13.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Matplotlib 2.1.0    




Running under Unix/Linux
======

### INSTALLATION GUIDE

1. Open Unix terminal

2. Install *virtualenv* tool on your Unix terminal if you have not installed already. This tool allows to create isolated Python environment.     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install virtual environment): `$ pip install virtualenv`

3. Also install *pip* tool if you have not installed yet. Pip designed for managing software written in Python. A good introduction on how to setup virtual environment, and install required modules can be found at the [blog](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/).  
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install pip): `$ sudo apt-get install python-pip`  

4. Create a virtual environment. Virtual environment acts as an isolated platform where you can install all required packages for the specific project without modifying existing projects. For example, if your computer has Python 2.7, you can easily install Python 3+ without affecting Python 2+.       
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a new environment ): `$ virtualenv SelectEnvirName`

5. Activate created virtual environment.     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a new environment ): `$ source SelectEnvirName/bin/activate`

7. Download the CirGO software from GitHub repository as zip folder (*Clone or Download*; *Download ZIP*). Unzip folder into a directory of your choice. For example, to the desktop.

8. Navigate Unix/Linux terminal to the *setup.py* script of the CirGO software, which is located at the *docs* folder.     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to *docs* folder): `(SelectEnvirName)$ cd YOURPATH\CirGO_Py_VisualSoftware-master\docs`

9. Create a source distribution for the CirGO package. This step generates two folders *CirGO.egg-info* and *dist*.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a source distribution) : `(SelectEnvirName)$ python setup.py sdist`

10. Navigate to the *dist* folder and install CirGO package.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to the *dist* folder):`(SelectEnvirName)$ cd dist`     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install CirGO package);`(SelectEnvirName)$ pip install CirGO-0.1.0.tar.gz`

11. Navigate to the *CirGO_Wind_Unix* folder.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to the *CirGO_Wind_Unix* folder):`(SelectEnvirName)$ cd YOURPATH\CirGO_Py_VisualSoftware-master\CirGO_Wind_Unix`


### HELP PAGE  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page):`(SelectEnvirName)> python CirGO.py –h`


### CirGO PACKAGE USAGE
There are three options on CirGO usage:  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Graphical User Interface (GUI);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Command Line (CMD);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) Interactive Command Line (INT).

#### (1) Graphical User Interface (GUI)  
Graphical User Interface (GUI) is the simplest option for visualizing GO terms. When the command *python CirGO.py -gui* is executed an interactive window will pop-up. The required parameters can be changed or left as default, an input file can be opened with the *Open File* button, and visualized by pressing *Visualize* button. The output file will be automatically saved in *svg* format to the same folder with the input file, or the output file name can be changed by pressing *Save output as SVG* button. Please note, that the legend name should be changed depending on what process (biological process, cellular component, or molecular function) is visualized. To leave GUI press *Exit*. 
&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Graphical user interface):`(SelectEnvirName)$ python CirGO.py –gui`

#### (2) Command Line (CMD)  
Command Line (CMD) requires a user to provide parameters in the command line space as described at the help page:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page): `(SelectEnvirName)$ python CirGO.py -h`  
&nbsp;  
*CirGO - inputFile INPUTFILE [-outputFile OUTPUTFILE] [-fontSize FONTSIZE] [-numCat NRCATEGORIES] [-leg FIGURE_LEGEND]*

&nbsp; 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example:** `(SelectEnvirName)$ python CirGO.py -inputFile Example_REVIGO_Input_BP.csv -outputFile Visual_BP.svg -fontSize 6.5 -numCat 40 -legend "Name & Proportion of Biological process (inner ring)"`  


#### (3) Interactive Command Line (INT) 
Interactive (INT) command line option enables to run the CirGO software in the interactive mode.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Interactive command line (INT)):`(SelectEnvirName)$ python 
CirGO.py -int`
&nbsp;  
**CirGO [-int]**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**inputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input path and filename of an REVIGO file.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**outputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output path and filename in svg format.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**fontSize:** [float]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive float value (Example: 7). It is advised to select one from 6.0 -7.0.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**numCat:** [int]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive integer value of categories to be visualized (Example: 40).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**legend:** [str]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Legend title to be displayed in the figure. A string (Example: Name & Proportion of Biological process (inner ring)). Select relevant example of the legend name:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Name & Proportion of Biological process (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Name & Proportion of Cellular component (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3 )Name & Proportion of Molecular function (inner ring)  
 
**Version control:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tested on Windows 7 Professional / Windows 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Conda 4.3.25  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python 2.7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NumPy 1.13.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Matplotlib 2.1.0    




Running under Mac
======
### INSTALLATION GUIDE
1. Open Mac terminal.
  
1. Install *xcode-select* utility on your Mac OS if you have not installed already. This utilities enables usage of common Unix-based tools.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install xcode-select utility): `$ xcode-select --install`  

1. Install [Homebrew](https://brew.sh/), which is free open source software package, if you have not installed already. It facilitates software installation on Mac OS. Note: please always check the command from the [Homebrew](https://brew.sh/) website, as it frequently modified.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install Homebrew): `$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

1. Check Python version. Python 2+ is required version for the CirGO software. Note: Python 2.7 generally comes with Mac OS.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Check Python version): `$ python --version`

1. Create a virtual environment. Virtual environment acts as an isolated platform where you can install all required packages for the specific project without modifying existing projects. For example, if your computer has Python 2.7, you can easily install Python 3+ without affecting Python 2+.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create virtual environment) `$ virtualenv -p /usr/bin/python2.7 SelectEnvirName`

1. Activate created virtual environment.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Activate virtual environment): `$ source SelectEnvirName/bin/activate`

1. Install the latest *pip* version.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install the latest *pip*): `(SelectEnvirName)$ curl https://bootstrap.pypa.io/get-pip.py | python`

1. Download the CirGO software from GitHub repository as zip folder (*Clone or Download*; *Download ZIP*). Unzip folder into a directory of your choice. For example, to the desktop.

1. Navigate Mac terminal to the *setup.py* script of the CirGO software, which is located at the *docs* folder.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to docs folder): `(SelectEnvirName)$ cd YOURPATH\CirGO_Py_VisualSoftware-master\docs`

1. Create a source distribution for the CirGO package. This step generates two folders *CirGO.egg-info* and *dist.*  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Create a source distribution) : `(SelectEnvirName)$ python setup.py sdist`

1. Navigate to the *dist* folder and install CirGO package.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to the *dist* folder):`(SelectEnvirName)$ cd dist`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Install CirGO package):`(SelectEnvirName)$ pip install CirGO-0.1.0.tar.gz`

1. Navigate to the *CirGO_Mac* folder.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Navigate to the CirGO_Mac folder):`(SelectEnvirName)$ cd YOURPATH\CirGO_Py_VisualSoftware-master\CirGO_Mac`


### HELP PAGE  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page):`(SelectEnvirName)> python CirGO.py –h`


### CirGO PACKAGE USAGE
 There are three options on the CirGO usage:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Graphical User Interface (GUI);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Command Line (CMD);  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) Interactive Command Line (INT).

#### (1) Graphical User Interface (GUI)  
Graphical User Interface (GUI) is the simplest option for visualizing GO terms. When the command *python CirGO.py -gui* is executed an interactive window will pop-up. The required parameters can be changed or left as default, an input file can be opened with the *Open File* button, and visualized by pressing *Visualize* button. The output file will be automatically saved in *svg* format to the same folder with the input file, or the output file name can be changed by pressing *Save output as SVG* button. Please note, that the legend name should be changed depending on what process (biological process, cellular component, or molecular function) is visualized. To leave GUI press *Exit*. 
&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Graphical user interface):`(SelectEnvirName)$ python CirGO.py –gui`

#### (2) Command Line (CMD)  
Command Line (CMD) requires a user to provide parameters in the command line space as described at the help page:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Help page): `(SelectEnvirName)$ python CirGO.py -h`  \
&nbsp;  
*CirGO - inputFile INPUTFILE [-outputFile OUTPUTFILE] [-fontSize FONTSIZE] [-numCat NRCATEGORIES] [-leg FIGURE_LEGEND]*  
&nbsp;  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example:** `(SelectEnvirName)$ python CirGO.py -inputFile Example_REVIGO_Input_BP.csv -outputFile Visual_BP.svg -fontSize 6.5 -numCat 40 -legend "Name & Proportion of Biological process (inner ring)"`  

#### (3) Interactive Command Line (INT) 
Interactive (INT) command line option enables to run the CirGO software in the interactive mode.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example** (Interactive command line (INT)):`(SelectEnvirName)$ python 
CirGO.py -int`
&nbsp;  
**CirGO [-int]**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Parameters:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**inputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Input path and filename of an REVIGO file.    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**outputFile:** [file name]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Output path and filename in svg format.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**fontSize:** [float]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive float value (Example: 7). It is advised to select one from 6.0 -7.0.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**numCat:** [int]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A positive integer value of categories to be visualized (Example: 40).  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**legend:** [str]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Legend title to be displayed in the figure. A string (Example: Name & Proportion of Biological process (inner ring)). Select relevant example of the legend name:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Name & Proportion of Biological process (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Name & Proportion of Cellular component (inner ring)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3 )Name & Proportion of Molecular function (inner ring)  
 
**Version control:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tested on Windows 7 Professional / Windows 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Conda 4.3.25  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python 2.7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NumPy 1.13.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Matplotlib 2.1.0    


## Visualization Example
![Visualization of GO terms for Biological Process](https://github.com/IrinaVKuznetsova/CirGO/blob/master/docs/Visual_BP.svg)



## Example Dataset
The example dataset was obtained from [GSE83471](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE83471).


## Copyright Notice
This project is licensed under the terms of the **GNU version 3** general public license.

## Cite
 




