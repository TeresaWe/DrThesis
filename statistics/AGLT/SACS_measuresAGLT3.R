#script to calculate the SACS measures from AGLTresults table

# SACS = Z(%)-Z(RT) Speed accuracy composite scores
# high score--> efficient performance, low score --> poor performance

# calculate this for each congruency separation condition  and all trials 

library(dplyr)
AGLTresults<-data.frame(AGLTresults)
######### L_con ##############

ACC_Lcon<-AGLTresults$aud_L_con_corr/40
ACC_Gcon<-AGLTresults$aud_G_con_corr/40
ACC_Linc<-AGLTresults$aud_L_incon_corr/40
ACC_Ginc<-AGLTresults$aud_G_incon_corr/40

mean_ACC<-mean(c(ACC_Lcon,ACC_Gcon,
                 ACC_Linc,ACC_Ginc))
sd_ACC<-sd(c(ACC_Lcon,ACC_Gcon,
             ACC_Linc,ACC_Ginc))
mean_RT<-mean(c(AGLTresults$aud_L_con_meanRT,AGLTresults$aud_G_con_meanRT,
                AGLTresults$aud_L_incon_meanRT,AGLTresults$aud_G_incon_meanRT),na.rm=TRUE)
sd_RT<-sd(c(AGLTresults$aud_L_con_meanRT,AGLTresults$aud_G_con_meanRT,
            AGLTresults$aud_L_incon_meanRT,AGLTresults$aud_G_incon_meanRT),na.rm=TRUE)


ACC<-AGLTresults[,1]/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLTresults[,2]
SACS_Lcon=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)

######### L_incon ##############

ACC<-AGLTresults[,3]/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLTresults[,4]
SACS_Linc=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)


######### G_con ##############

ACC<-AGLTresults[,5]/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLTresults[,6]
SACS_Gcon=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)


######### G_incon ##############

ACC<-AGLTresults[,7]/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLTresults[,8]
SACS_Ginc=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)


######### all ###############

ACC<-(AGLTresults[,1]+AGLTresults[,3]+AGLTresults[,5]+AGLTresults[,7])/160
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-(AGLTresults[,2]+AGLTresults[,4]+AGLTresults[,6]+AGLTresults[,8])/4
SACS_all=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)

AGLT_SACS<-cbind(SACS_Lcon,SACS_Linc,SACS_Gcon,SACS_Ginc,SACS_all)
AGLT_SACS<-data.frame(AGLT_SACS)
colnames(AGLT_SACS)<-c("aud_SACS_Lcon","aud_SACS_Linc","aud_SACS_Gcon","aud_SACS_Ginc","aud_SACS_all")
rownames(AGLT_SACS)<-rownames(AGLTresults)

#ggf

AGLTresults<-cbind(AGLTresults,AGLT_SACS)
