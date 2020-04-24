# CirGO

```diff
! *CirGO (Circular Gene Ontology) Version 1.0 for Python 2+ is available 01/03/2018
! *CirGO (Circular Gene Ontology) Version 2.0 for Pyhton 3+ is available 24/04/2020  
```

© Copyright (C) 2020  
https://github.com/IrinaVKuznetsova/CirGO.git  
  
Software development by:  

Irina Kuznetsova, irina.kuznetsova@perkins.org.au  
Artur Lugmayr, lartur@acm.org  

**CirGO manual was designed to help people with limited or no programming experience to install the CirGO software.**  
* For CirGO installation instructions for Version 1.0 for [Python 2+](https://github.com/IrinaVKuznetsova/testCirGOpy3/tree/master/Py2%2B)  
* For CirGO installation instructions for Version 2.0 for [Python 3+](https://github.com/IrinaVKuznetsova/CirGO/tree/master/Py3%2B)  

 
General Usage Notes
------

**Description:** CirGO (Circular Gene Ontology) is an alternative way of visualising GO terms in 2D space that is suitable for publishing and presenting gene expression Ontology data.  



**Software architecture:**  
CirGO can be run on Windows, Unix/Linux and Mac OS as:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Graphical User Interface (GUI)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Command Line (CMD)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) Interactive Command Line (INT)  

Brief Algorithm Description
------

Briefly, CirGO visualisation algorithm consists of three steps that are described at the Supplementary Material of the [CirGO: an alternative circular way of visualising gene ontology terms](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2671-2) publication:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1) Formatting of the *csv* input file obtained from the TreeMap tab on [REVIGIO page](http://revigo.irb.hr/).    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2) Values calculation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(3) GO visualisation as two-layer full hierarchies.


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


#### Formatted three columns input for visualisation   
Note: there is no header.  

| | | |
|-|-|-|
immune system process | 7.6615 | immune system process
response to stress | 24.6003 | response to stress
response to oxygen-containing compound | 9.8297 | response to stress
regulation of signaling | 9.5272 | response to stress
... | ... | ... 





**Version control CirGO Version 1.0 Python 2+:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tested on Windows 7 Professional / Windows 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Conda 4.3.25  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python 2.7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NumPy 1.13.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Matplotlib 2.1.0  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Seaborn 0.8.1    

**Version control CirGO Version 2.0 Python 3+:**  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tested on Windows 10  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Conda 4.8.3  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python 3.7  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; NumPy 1.18.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Matplotlib 3.2.1  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Seaborn 0.10.0    

## visualisation Example
![visualisation of GO terms for Biological Process](https://github.com/IrinaVKuznetsova/CirGO/blob/master/docs/Visual_BP.svg)



## Example Dataset
The example dataset was obtained from [GSE83471](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE83471).


## Copyright Notice
This project is licensed under the terms of the **GNU version 3** general public license.

## Cite  
Kuznetsova I, Lugmayr A, Siira SJ, Rackham O, Filipovska A. CirGO: an alternative circular way of visualising gene ontology terms. BMC Bioinformatics [Internet]. 2019 Feb 18;20(1):84. Available from: https://doi.org/10.1186/s12859-019-2671-2
 




