#libraries
library(dplyr)

#calculate Handedness Inventory scores
# only 1 (left), 2(ambi) 3(right) coded --> handedness inventory 
#actually uses (0|2)(2|0) (1|1)(1|0)(0|1)--< only took first three categories
EHD_recode<-EHD
EHD_recode$EHD01 <- car::recode(EHD_recode$EHD01, "3=2; 1=-2; 2=0")
EHD_recode$EHD02 <- car::recode(EHD_recode$EHD02, "3=2; 1=-2; 2=0")
EHD_recode$EHD03 <- car::recode(EHD_recode$EHD03, "3=2; 1=-2; 2=0")
EHD_recode$EHD04 <- car::recode(EHD_recode$EHD04, "3=2; 1=-2; 2=0")
EHD_recode$EHD05 <- car::recode(EHD_recode$EHD05, "3=2; 1=-2; 2=0")
EHD_recode$EHD06 <- car::recode(EHD_recode$EHD06, "3=2; 1=-2; 2=0")
EHD_recode$EHD07 <- car::recode(EHD_recode$EHD07, "3=2; 1=-2; 2=0")
EHD_recode$EHD08 <- car::recode(EHD_recode$EHD08, "3=2; 1=-2; 2=0")
EHD_recode$EHD09 <- car::recode(EHD_recode$EHD09, "3=2; 1=-2; 2=0")
EHD_recode$EHD10 <- car::recode(EHD_recode$EHD10, "3=2; 1=-2; 2=0")

EHD_recode<-data.frame(EHD_recode)
EHD_recode<-data.matrix(EHD_recode)
names<-EHD$dupl1_Code
#cumulative total LH+RH

EHD_recoded_abs<-abs(EHD_recode)
EHD_recoded_abs <- car::recode(EHD_recoded_abs, "0=2")
total=rowSums(EHD_recoded_abs[,2:11], na.rm = FALSE, dims = 1)
#Difference: Diff= RH-LH
Diff=rowSums(EHD_recode[,2:11], na.rm = FALSE, dims = 1)
#Result: R=(D/CT)*100 --> >40= right, <40=left 
R=(Diff/total)*100
hand<-R
hand[hand<41& hand>(-41)]<-2 #ambi
hand[hand<(-40)]<-0 #left
hand[hand>40]<-1 #right
handedness<-cbind(R, hand)
handedness<-data.frame(handedness)

