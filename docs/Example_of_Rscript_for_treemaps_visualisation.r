# This R script was modified from the treemap R script that has been produced by the REVIGO server at http://revigo.irb.hr/

# -----------------------------------------------------------------------------

# 1. Install required package
# If you don't have the treemap package installed, uncomment the following line:
#install.packages( "treemap" );
library(treemap) 								# treemap package by Martijn Tennekes


# 2. Set working directory, and read a file
setwd("C:/Users/username/workingdir");   # Set the working directory if necessary

bp_file = read.table(file="Input_to_visual_Treemaps.txt", sep="\t") 
dim(bp_file)    # 48 3
head(bp_file)
stuff <- data.frame(bp_file);
colnames(stuff)=c("description","abslog10pvalue","representative")
head(stuff)


# 3. Extract required values, and plot a treemap.
stuff$abslog10pvalue <- as.numeric( (as.character(abs(stuff$abslog10pvalue))));
pdf( file="example_treemap_for_paper.pdf", width=16, height=9 ) # width and height are in inches
treemap(
  stuff,
  index = c("representative","description"),
  vSize = "abslog10pvalue",
  type = "categorical",
  vColor = "representative",
  title = "REVIGO Gene Ontology treemap",
  inflate.labels = FALSE,        # set this to TRUE for space-filling group labels - good for posters
  lowerbound.cex.labels = 0,     # try to draw as many labels as possible (still, some small squares may not get a label)
  bg.labels = '#CCCCCCAA',       # define background color of group labels
                                 # "#CCCCCC00" is fully transparent, "#CCCCCCAA" is semi-transparent grey, NA is opaque
  position.legend = "right",     # position of the legend: "bottom", "right", or "none"
  fontsize.legend = 10           # legend on the right site
)
dev.off()



