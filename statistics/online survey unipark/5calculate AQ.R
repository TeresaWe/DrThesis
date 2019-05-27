#libraries
library(car)
library(dplyr)

# calculate AP-Score
AQ_recode<-AQ # duplicate data frame
#transpose negative Items
AQ_recode$AQ01n <- car::recode(AQ_recode$AQ01n, "1=4; 2=3; 3=2; 4=1") #recode negative Items
AQ_recode$AQ03n <- car::recode(AQ_recode$AQ03n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ08n <- car::recode(AQ_recode$AQ08n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ10n <- car::recode(AQ_recode$AQ10n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ11n <- car::recode(AQ_recode$AQ11n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ14n <- car::recode(AQ_recode$AQ14n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ15n <- car::recode(AQ_recode$AQ15n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ17n <- car::recode(AQ_recode$AQ17n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ24n <- car::recode(AQ_recode$AQ24n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ25n <- car::recode(AQ_recode$AQ25n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ27n <- car::recode(AQ_recode$AQ27n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ28n <- car::recode(AQ_recode$AQ28n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ29n <- car::recode(AQ_recode$AQ29n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ30n <- car::recode(AQ_recode$AQ30n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ31n <- car::recode(AQ_recode$AQ31n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ32n <- car::recode(AQ_recode$AQ32n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ34n <- car::recode(AQ_recode$AQ34n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ36n <- car::recode(AQ_recode$AQ36n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ37n <- car::recode(AQ_recode$AQ37n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ38n <- car::recode(AQ_recode$AQ38n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ40n <- car::recode(AQ_recode$AQ40n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ44n <- car::recode(AQ_recode$AQ44n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ47n <- car::recode(AQ_recode$AQ47n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ48n <- car::recode(AQ_recode$AQ48n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ49n <- car::recode(AQ_recode$AQ49n, "1=4; 2=3; 3=2; 4=1")
AQ_recode$AQ50n <- car::recode(AQ_recode$AQ50n, "1=4; 2=3; 3=2; 4=1")
# re-code answers into points per Item
AQ_points<-AQ_recode
AQ_points[AQ_points==1]<-0
AQ_points[AQ_points==2]<-0
AQ_points[AQ_points==3]<-1
AQ_points[AQ_points==4]<-1
AQ_points<-data.frame(AQ_points)
AQ_points<-data.matrix(AQ_points[,-1])
rownames(AQ_points)<-VP_Codes$dupl1_Code
AQ_Score <- rowSums(AQ_points)
