""" CirGO 
    Version 2.0 for Py3+ 22/04/2020
    
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
    Kuznetsova I, Lugmayr A, Siira SJ, Rackham O, Filipovska A. 
    CirGO: an alternative circular way of visualising gene ontology terms. BMC Bioinformatics [Internet]. 
    2019 Feb 18;20(1):84. Available from: https://doi.org/10.1186/s12859-019-2671-2
    
    Conract info:   irina.kuznetsova@uwa.edu.au 
    GitHub:         https://github.com/IrinaVKuznetsova/CirGO.git 
"""
  
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
## I. Import required modules
## ----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
##----------------------------------------------------------------------------------------------------
# import os # temporaray 21.04.20
from operator import abs
import csv
import os.path

def ConvertToThreeCoulmnsInput(inputfilename, outputfilename='', outputfilepath=''):
    if (outputfilename == ''):
        outputfilename, ex = os.path.splitext(inputfilename)
        outputfilename = outputfilename + "_converted.csv"
        outputfilename = outputfilepath + outputfilename
        print(("Converting input file " + inputfilename + " to intermediate three columns input file " + outputfilename + " in path " + outputfilepath + " ..."))
        
    # open output file
    with open(outputfilename, 'w') as outputFile:     # 'wb' is changed to 'w'
        outputFileWriter = csv.writer(outputFile, delimiter="\t")  
        
        # open input file
        with open(inputfilename) as inputFile:
            inputFileReader = csv.reader(inputFile, delimiter=',')
            
            # skip all rows that contain comments and begin with '%' at the beginning of the file
            x=next(inputFileReader)
            while (x[0].startswith("%")):
                x=next(inputFileReader)
                print ("Skipping comments in header...")
                
            # skip the header for further processing, but write it into the output file
            outputFileWriter.writerow([x[1], x[3], x[6]])   
            
            for row in inputFileReader:
                # skip eventual comment lines that are contained inside the csv file
                if not row[0].startswith("%"):
                    # perform data cleaning upon special characters
                    # - replace any eventual " in the term_ID
                    
                    row[1] = row[1].replace("\"", "")
                    # - convert log10pvalues to absolute values
                    row[3]  = abs(float(row[3]))
                    # - replace any eventual " in the representative
                    row[6] = row[6].replace("\"", "")
                    
                    # write the final output file
                    outputFileWriter.writerow([row[1], row[3], row[6]])
                    
            inputFile.close()
        outputFile.close()
        print(("Input file " + inputfilename + " cleaned and converted to tab deliminated file " + outputfilename + " in path " + outputfilepath + " ..."))



