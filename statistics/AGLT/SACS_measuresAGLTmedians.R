#script to calculate the SACS measures from AGLTresults table

# SACS = Z(%)-Z(RT) Speed accuracy composite scores
# high score--> efficient performance, low score --> poor performance

# calculate this for each congruency separation condition  and all trials 

library("dplyr", lib.loc="/usr/local/lib/R/site-library")
#AGLT_medianresults<-data.frame(AGLT_medianresults)
######### L_con ##############
ACC_Lcon<-AGLT_medianresults$correct_Lcon/40
ACC_Gcon<-AGLT_medianresults$correct_Gcon/40
ACC_Linc<-AGLT_medianresults$correct_Linc/40
ACC_Ginc<-AGLT_medianresults$correct_Ginc/40



mean_ACC<-mean(c(ACC_Lcon,ACC_Gcon,
                 ACC_Linc,ACC_Ginc))
sd_ACC<-sd(c(ACC_Lcon,ACC_Gcon,
             ACC_Linc,ACC_Ginc))
mean_RT<-mean(c(AGLT_medianresults$MAD_Lcon,AGLT_medianresults$MAD_Gcon,
                 AGLT_medianresults$MAD_Linc,AGLT_medianresults$MAD_Ginc),na.rm=TRUE)
sd_RT<-sd(c(AGLT_medianresults$MAD_Lcon,AGLT_medianresults$MAD_Gcon,
             AGLT_medianresults$MAD_Linc,AGLT_medianresults$MAD_Ginc),na.rm=TRUE)



ACC<-AGLT_medianresults$correct_Lcon/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLT_medianresults$MAD_Lcon
SACS_Lcon=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)

######### L_incon ##############

ACC<-AGLT_medianresults$correct_Linc/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLT_medianresults$MAD_Linc
SACS_Linc=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)


######### G_con ##############

ACC<-AGLT_medianresults$correct_Gcon/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLT_medianresults$MAD_Gcon
SACS_Gcon=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)


######### G_incon ##############

ACC<-AGLT_medianresults$correct_Ginc/40
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-AGLT_medianresults$MAD_Ginc
SACS_Ginc=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)


######### all ###############

ACC<-(AGLT_medianresults$correct_Lcon+AGLT_medianresults$correct_Linc+AGLT_medianresults$correct_Gcon+AGLT_medianresults$correct_Ginc)/160
ACC[ACC==1]<-0.95
ACC[ACC==0]<-0.0001
RT<-(AGLT_medianresults$MAD_Lcon+AGLT_medianresults$MAD_Linc+AGLT_medianresults$MAD_Gcon+AGLT_medianresults$MAD_Ginc)/4
SACS_all=((ACC-mean_ACC)/sd_ACC)-((RT-mean_RT)/sd_RT)
rm(ACC,RT)

AGLT_SACSmedian<-cbind(SACS_Lcon,SACS_Linc,SACS_Gcon,SACS_Ginc,SACS_all)
AGLT_SACSmedian<-data.frame(AGLT_SACSmedian)
colnames(AGLT_SACSmedian)<-c("med_aud_SACS_Lcon","med_aud_SACS_Linc","med_aud_SACS_Gcon","med_aud_SACS_Ginc","aud_SACS_all")

AGLT_medianresults<-cbind(AGLT_medianresults,AGLT_SACSmedian) 

