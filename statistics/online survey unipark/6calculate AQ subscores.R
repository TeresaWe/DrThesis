library(dplyr)
AQ_recode<-AQ_recode[,-1]
# subscale social skills (SK):  (items 1,11,13,15,22,36,44,45,47,48)
AQ_SK<-select(AQ_recode,1,11,13,15,22,36,44,45,47,48)
AQ_SK[AQ_SK==1]<-0
AQ_SK[AQ_SK==2]<-0
AQ_SK[AQ_SK==3]<-1
AQ_SK[AQ_SK==4]<-1
AQ_SK<-data.frame(AQ_SK)
AQ_SK<-data.matrix(AQ_SK)
rownames(AQ_SK)<-VP_Codes$dupl1_Code
AQ_SK_Score<- rowSums(AQ_SK)
# subscale attention switching (SW): (items 2,4,10,16,25,32,34,37,43,46)
AQ_SW<-select(AQ_recode,2,4,10,16,25,32,34,37,43,46)
AQ_SW[AQ_SW==1]<-0
AQ_SW[AQ_SW==2]<-0
AQ_SW[AQ_SW==3]<-1
AQ_SW[AQ_SW==4]<-1
AQ_SW<-data.frame(AQ_SW)
AQ_SW<-data.matrix(AQ_SW)
rownames(AQ_SW)<-VP_Codes$dupl1_Code
AQ_SW_Score<- rowSums(AQ_SW)
#subscale  attention to detail (AD):  (items 5,6,9,12,19,23,28,29,30,49)
AQ_AD<-select(AQ_recode,5,6,9,12,19,23,28,29,30,49)
AQ_AD[AQ_AD==1]<-0
AQ_AD[AQ_AD==2]<-0
AQ_AD[AQ_AD==3]<-1
AQ_AD[AQ_AD==4]<-1
AQ_AD<-data.frame(AQ_AD)
AQ_AD<-data.matrix(AQ_AD)
rownames(AQ_AD)<-VP_Codes$dupl1_Code
AQ_AD_Score<- rowSums(AQ_AD)
#subscale communication (CO):  (items 7,17,18,26,27,31,33,35,38,39)
AQ_CO<-select(AQ_recode,7,17,18,26,27,31,33,35,38,39)
AQ_CO[AQ_CO==1]<-0
AQ_CO[AQ_CO==2]<-0
AQ_CO[AQ_CO==3]<-1
AQ_CO[AQ_CO==4]<-1
AQ_CO<-data.frame(AQ_CO)
AQ_CO<-data.matrix(AQ_CO)
rownames(AQ_CO)<-VP_Codes$dupl1_Code
AQ_CO_Score<- rowSums(AQ_CO)
#subscale imagination (IM): (items 3,8,14,20,21,24,40,41,42,50)
AQ_IM<-select(AQ_recode,3,8,14,20,21,24,40,41,42,50)
AQ_IM[AQ_IM==1]<-0
AQ_IM[AQ_IM==2]<-0
AQ_IM[AQ_IM==3]<-1
AQ_IM[AQ_IM==4]<-1
AQ_IM<-data.frame(AQ_IM)
AQ_IM<-data.matrix(AQ_IM)
rownames(AQ_IM)<-VP_Codes$dupl1_Code
AQ_IM_Score<- rowSums(AQ_IM)