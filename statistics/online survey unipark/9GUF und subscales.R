#libraries
library(dplyr)
#recode 
GUF_points<-GUF[,-(1:6)]
GUF_points[GUF_points==1]<-0
GUF_points[GUF_points==2]<-1
GUF_points[GUF_points==3]<-2
GUF_points[GUF_points==4]<-3

#subscale (KRH):  (items 4,5,7,12,15)
GUF_KRH<-dplyr::select(GUF_points,4,5,7,12,15)
GUF_KRH<-data.frame(GUF_KRH)
GUF_KRH<-data.matrix(GUF_KRH)
rownames(GUF_KRH)<-VP_Codes$dupl1_Code
GUF_KRH_Score<- rowSums(GUF_KRH)
#subscale "Aktionales/somatisches Verhalten" (ASV):  (items 3,8,9,11,13)
GUF_ASV<-dplyr::select(GUF_points,3,8,9,11,13)
GUF_ASV<-data.frame(GUF_ASV)
GUF_ASV<-data.matrix(GUF_ASV)
rownames(GUF_ASV)<-VP_Codes$dupl1_Code
GUF_ASV_Score<- rowSums(GUF_ASV)
#subscale "emotionale reaktion auf externale Geräuschquellen" (ERG):  (items 1,2,6,10,14)
GUF_ERG<-dplyr::select(GUF_points,1,2,6,10,14)
GUF_ERG<-data.frame(GUF_ERG)
GUF_ERG<-data.matrix(GUF_ERG)
rownames(GUF_ERG)<-VP_Codes$dupl1_Code
GUF_ERG_Score<- rowSums(GUF_ERG)


#change format GUF_points
GUF_points<-data.frame(GUF_points)
GUF_points<-data.matrix(GUF_points[,-1])
rownames(GUF_points)<-VP_Codes$dupl1_Code
GUF_Score <- rowSums(GUF_points)