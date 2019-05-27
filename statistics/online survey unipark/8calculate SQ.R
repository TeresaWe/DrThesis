#libraries
library(dplyr)
# calculate AP-Score
SQ_recode<-SQ # duplicate data frame
#transpose negative Items
SQ_recode$SQ01 <- car::recode(SQ_recode$SQ01, "1=4; 2=3; 3=2; 4=1") #recode negative Items; attention: Coding scheme reversed in Unipark --> here negative Items are "positive" in Unipark, but negativ in sheet questionaire ;-)
SQ_recode$SQ02 <- car::recode(SQ_recode$SQ02, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ04 <- car::recode(SQ_recode$SQ04, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ05 <- car::recode(SQ_recode$SQ05, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ07 <- car::recode(SQ_recode$SQ07, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ09 <- car::recode(SQ_recode$SQ09, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ11 <- car::recode(SQ_recode$SQ11, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ12 <- car::recode(SQ_recode$SQ12, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ13 <- car::recode(SQ_recode$SQ13, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ14 <- car::recode(SQ_recode$SQ14, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ16 <- car::recode(SQ_recode$SQ16, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ18 <- car::recode(SQ_recode$SQ18, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ19 <- car::recode(SQ_recode$SQ19, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ20 <- car::recode(SQ_recode$SQ20, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ21 <- car::recode(SQ_recode$SQ21, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ23 <- car::recode(SQ_recode$SQ23, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ25 <- car::recode(SQ_recode$SQ25, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ27 <- car::recode(SQ_recode$SQ27, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ29 <- car::recode(SQ_recode$SQ29, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ30 <- car::recode(SQ_recode$SQ30, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ32 <- car::recode(SQ_recode$SQ32, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ36 <- car::recode(SQ_recode$SQ36, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ38 <- car::recode(SQ_recode$SQ38, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ41 <- car::recode(SQ_recode$SQ41, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ42 <- car::recode(SQ_recode$SQ42, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ43 <- car::recode(SQ_recode$SQ43, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ46 <- car::recode(SQ_recode$SQ46, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ50 <- car::recode(SQ_recode$SQ50, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ53 <- car::recode(SQ_recode$SQ53, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ55 <- car::recode(SQ_recode$SQ55, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ60 <- car::recode(SQ_recode$SQ60, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ61 <- car::recode(SQ_recode$SQ61, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ62 <- car::recode(SQ_recode$SQ62, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ66 <- car::recode(SQ_recode$SQ66, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ68 <- car::recode(SQ_recode$SQ68, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ69 <- car::recode(SQ_recode$SQ69, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ72 <- car::recode(SQ_recode$SQ72, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ74 <- car::recode(SQ_recode$SQ74, "1=4; 2=3; 3=2; 4=1")
SQ_recode$SQ75 <- car::recode(SQ_recode$SQ75, "1=4; 2=3; 3=2; 4=1")
# re-code answers into points per Item
SQ_points<-SQ_recode
SQ_points[SQ_points==1]<-5
SQ_points[SQ_points==2]<-1
SQ_points[SQ_points==3]<-0
SQ_points[SQ_points==4]<-0
SQ_points[SQ_points==5]<-2
SQ_points<-data.frame(SQ_points)
SQ_points<-data.matrix(SQ_points[,-1])
rownames(SQ_points)<-VP_Codes$dupl1_Code
SQ_Score <- rowSums(SQ_points)