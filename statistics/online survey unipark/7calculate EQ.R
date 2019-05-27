#libraries
library(dplyr)


# calculate AP-Score
EQ_recode<-EQ # duplicate data frame
#transpose negative Items
EQ_recode$EQ02n <- car::recode(EQ_recode$EQ02n, "1=4; 2=3; 3=2; 4=1") #recode negative Items; attention: Coding scheme reversed in Unipark 
EQ_recode$EQ04n <- car::recode(EQ_recode$EQ04n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ05n <- car::recode(EQ_recode$EQ05n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ06n <- car::recode(EQ_recode$EQ06n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ07n <- car::recode(EQ_recode$EQ07n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ08n <- car::recode(EQ_recode$EQ08n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ09n <- car::recode(EQ_recode$EQ09n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ10n <- car::recode(EQ_recode$EQ10n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ12n <- car::recode(EQ_recode$EQ12n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ16n <- car::recode(EQ_recode$EQ16n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ17n <- car::recode(EQ_recode$EQ17n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ18n <- car::recode(EQ_recode$EQ18n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ19n <- car::recode(EQ_recode$EQ19n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ20n <- car::recode(EQ_recode$EQ20n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ25n <- car::recode(EQ_recode$EQ25n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ30n <- car::recode(EQ_recode$EQ30n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ31n <- car::recode(EQ_recode$EQ31n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ32n <- car::recode(EQ_recode$EQ32n, "1=4; 2=3; 3=2; 4=1")
EQ_recode$EQ33n <- car::recode(EQ_recode$EQ33n, "1=4; 2=3; 3=2; 4=1")
# re-code answers into points per Item
EQ_points<-EQ_recode
EQ_points[EQ_points==1]<-0
EQ_points[EQ_points==2]<-0
EQ_points[EQ_points==3]<-1
EQ_points[EQ_points==4]<-2
EQ_points<-data.frame(EQ_points)
EQ_points<-data.matrix(EQ_points[,-1])
rownames(EQ_points)<-VP_Codes$dupl1_Code
EQ_Score <- rowSums(EQ_points)