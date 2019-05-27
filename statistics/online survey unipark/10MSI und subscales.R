#libraries
library(dplyr)
# calculate MSI-Score
MSI_recode<-MSI[,-1] # duplicate data frame
#recode negative items
MSI_recode$MSI09n <- car::recode(MSI_recode$MSI09n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")
#MSI_recode$MSI11n <- recode(MSI_recode$MSI11n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")
MSI_recode$MSI13n <- car::recode(MSI_recode$MSI13n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")
MSI_recode$MSI14n <- car::recode(MSI_recode$MSI14n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")
MSI_recode$MSI21n <- car::recode(MSI_recode$MSI21n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")
MSI_recode$MSI23n <- car::recode(MSI_recode$MSI23n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")
MSI_recode$MSI25n <- car::recode(MSI_recode$MSI25n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")
MSI_recode$MSI27n <- car::recode(MSI_recode$MSI27n, "1=7;2=6;3=5;4=4;5=3;6=2;7=1")

#subscale Faktor 1 "aktiver umgang mit Musik" (F1):  (items 1,3,8,15,21,24,28,34,38)
MSI_F1<-MSI<-dplyr::select(MSI_recode,1,3,8,15,21,24,28,34,38)
MSI_F1<-data.frame(MSI_F1)
MSI_F1<-data.matrix(MSI_F1)
rownames(MSI_F1)<-VP_Codes$dupl1_Code
MSI_F1_Score<- rowSums(MSI_F1)
#subscale Faktor 2 "musikalische Wahrnehmungsfähigkeiten" (F2):  (items 5,6,11,12,13,18,22,23,26)
MSI_F2<-dplyr::select(MSI_recode,5,6,11,12,13,18,22,23,26)
MSI_F2<-data.frame(MSI_F2)
MSI_F2<-data.matrix(MSI_F2)
rownames(MSI_F2)<-VP_Codes$dupl1_Code
MSI_F2_Score<- rowSums(MSI_F2)
#subscale Faktor 3 "musikalische Ausbildung" (F3):  (items 14,27,32,33,35,36,37)
MSI_F3<-dplyr::select(MSI_recode,14,27,32,33,35,36,37)
MSI_F3<-data.frame(MSI_F3)
MSI_F3<-data.matrix(MSI_F3)
rownames(MSI_F3)<-VP_Codes$dupl1_Code
MSI_F3_Score<- rowSums(MSI_F3)
#subscale Faktor 4 "Gesangsfähigkeiten" (F4):  (items 4,7,10,17,25,29,30)
MSI_F4<-dplyr::select(MSI_recode,4,7,10,17,25,29,30)
MSI_F4<-data.frame(MSI_F4)
MSI_F4<-data.matrix(MSI_F4)
rownames(MSI_F4)<-VP_Codes$dupl1_Code
MSI_F4_Score<- rowSums(MSI_F4)
#subscale Faktor 5 "Emotionen" (F5):  (items 2,9,16,19,20,31)
MSI_F5<-dplyr::select(MSI_recode,2,9,16,19,20,31)
MSI_F5<-data.frame(MSI_F5)
MSI_F5<-data.matrix(MSI_F5)
rownames(MSI_F5)<-VP_Codes$dupl1_Code
MSI_F5_Score<- rowSums(MSI_F5)

#Genereller Faktor Faktor G "Allgemeine Erfahrenheit" (FG):  (items 1,3,4,7,10,12,14,15,17,19,23,24,25,27,29,32,33,37)
MSI_FG<-dplyr::select(MSI_recode,1,3,4,7,10,12,14,15,17,19,23,24,25,27,29,32,33,37)
MSI_FG<-data.frame(MSI_FG)
MSI_FG<-data.matrix(MSI_FG)
rownames(MSI_FG)<-VP_Codes$dupl1_Code
MSI_FG_Score<- rowSums(MSI_FG)




#change format
MSI_recode<-data.frame(MSI_recode)
MSI_recode<-data.matrix(MSI_recode)
rownames(MSI_recode)<-VP_Codes$dupl1_Code
MSI_Score <- rowSums(MSI_recode[,1:38])#calculate score