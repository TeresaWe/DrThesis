####SACS
#################################################################################
#################################################################################

#AGLT
############################################################
##global advantage: G-L

##congruency interaction effect: Ginc-Gcon-linc+lcon
t.test(allresults_AGLT$med_aud_SACS_Ginc-allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Linc+allresults_AGLT$med_aud_SACS_Lcon~ allresults_AGLT$AP.0.RP.1.AP.)
cor.test(allresults_AGLT$med_aud_SACS_Ginc-allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Linc+allresults_AGLT$med_aud_SACS_Lcon, allresults_AGLT$AQ_Score)#
cor.test(allresults_AGLT$med_aud_SACS_Ginc-allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Linc+allresults_AGLT$med_aud_SACS_Lcon, allresults_AGLT$Z_MAD)
cor.test(allresults_AGLT$med_aud_SACS_Ginc-allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Linc+allresults_AGLT$med_aud_SACS_Lcon, allresults_AGLT$SDfoM)
lm<-lm(allresults_AGLT$med_aud_SACS_Ginc-allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Linc+allresults_AGLT$med_aud_SACS_Lcon~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
plot(lm)

##global-to-local interference: Lcon-Linc
t.test(allresults_AGLT$med_aud_SACS_Lcon-allresults_AGLT$med_aud_SACS_Linc~ allresults_AGLT$AP.0.RP.1.AP.)
cor.test(allresults_AGLT$med_aud_SACS_Lcon-allresults_AGLT$med_aud_SACS_Linc, allresults_AGLT$AQ_Score)
cor.test(allresults_AGLT$med_aud_SACS_Lcon-allresults_AGLT$med_aud_SACS_Linc, allresults_AGLT$MAD)
cor.test(allresults_AGLT$med_aud_SACS_Lcon-allresults_AGLT$med_aud_SACS_Linc, allresults_AGLT$SDfoM)#
lm<-lm(allresults_AGLT$med_aud_SACS_Lcon-allresults_AGLT$med_aud_SACS_Linc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
plot(lm)
##local-to-global interference: Gcon-Ginc
t.test(allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Ginc~ allresults_AGLT$AP.0.RP.1.AP.)
cor.test(allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Ginc, allresults_AGLT$AQ_Score)
cor.test(allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Ginc, allresults_AGLT$MAD)
cor.test(allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Ginc, allresults_AGLT$SDfoM)
lm<-lm(allresults_AGLT$med_aud_SACS_Gcon-allresults_AGLT$med_aud_SACS_Ginc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
###########################################################
#Navon
###########################################################

##congruency interaction effect: Ginc-Gcon-linc+lcon
t.test(allresults_Navon1$med_vis_SACS_Ginc-allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Linc+allresults_Navon1$med_vis_SACS_Lcon~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$med_vis_SACS_Ginc-allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Linc+allresults_Navon1$med_vis_SACS_Lcon, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$med_vis_SACS_Ginc-allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Linc+allresults_Navon1$med_vis_SACS_Lcon, allresults_Navon1$MAD)
cor.test(allresults_Navon1$med_vis_SACS_Ginc-allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Linc+allresults_Navon1$med_vis_SACS_Lcon, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$med_vis_SACS_Ginc-allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Linc+allresults_Navon1$med_vis_SACS_Lcon~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
##global-to-local interference: Lcon-Linc
t.test(allresults_Navon1$med_vis_SACS_Lcon-allresults_Navon1$med_vis_SACS_Linc~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$med_vis_SACS_Lcon-allresults_Navon1$med_vis_SACS_Linc, allresults_Navon1$AQ_Score)#
cor.test(allresults_Navon1$med_vis_SACS_Lcon-allresults_Navon1$med_vis_SACS_Linc, allresults_Navon1$MAD)
cor.test(allresults_Navon1$med_vis_SACS_Lcon-allresults_Navon1$med_vis_SACS_Linc, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$med_vis_SACS_Lcon-allresults_Navon1$med_vis_SACS_Linc~allresults_AGLT$MAD+allresults_Navon1$AQ_Score)
summary(lm)
plot(lm)
##local-to-global interference: Gcon-Ginc
t.test(allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Ginc~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Ginc, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Ginc, allresults_Navon1$MAD)
cor.test(allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Ginc, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$med_vis_SACS_Gcon-allresults_Navon1$med_vis_SACS_Ginc~allresults_AGLT$MAD+allresults_Navon1$AQ_Score)
summary(lm)

####RT
#################################################################################
#################################################################################

#AGLT
############################################################
##global advantage: G-L

##congruency interaction effect: Ginc-Gcon-linc+lcon
t.test(allresults_AGLT$medianG_inc-allresults_AGLT$medianG_con-allresults_AGLT$medianL_inc+allresults_AGLT$medianL_con~ allresults_AGLT$AP.0.RP.1.AP.)#
cor.test(allresults_AGLT$medianG_inc-allresults_AGLT$medianG_con-allresults_AGLT$medianL_inc+allresults_AGLT$medianL_con, allresults_AGLT$AQ_Score)
cor.test(allresults_AGLT$medianG_inc-allresults_AGLT$medianG_con-allresults_AGLT$medianL_inc+allresults_AGLT$medianL_con, allresults_AGLT$MAD) #
cor.test(allresults_AGLT$medianG_inc-allresults_AGLT$medianG_con-allresults_AGLT$medianL_inc+allresults_AGLT$medianL_con, allresults_AGLT$SDfoM) #
lm<-lm(allresults_AGLT$medianG_inc-allresults_AGLT$medianG_con-allresults_AGLT$medianL_inc+allresults_AGLT$medianL_con~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)#
summary(lm)
##global-to-local interference: Lcon-Linc
t.test(allresults_AGLT$medianL_con-allresults_AGLT$medianL_inc~ allresults_AGLT$AP.0.RP.1.AP.)
cor.test(allresults_AGLT$medianL_con-allresults_AGLT$medianL_inc, allresults_AGLT$AQ_Score)#
cor.test(allresults_AGLT$medianL_con-allresults_AGLT$medianL_inc, allresults_AGLT$MAD)
cor.test(allresults_AGLT$medianL_con-allresults_AGLT$medianL_inc, allresults_AGLT$SDfoM)
lm<-lm(allresults_AGLT$medianL_con-allresults_AGLT$medianL_inc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
##local-to-global interference: Gcon-Ginc
t.test(allresults_AGLT$medianG_con-allresults_AGLT$medianG_inc~ allresults_AGLT$AP.0.RP.1.AP.)#
cor.test(allresults_AGLT$medianG_con-allresults_AGLT$medianG_inc, allresults_AGLT$AQ_Score)
cor.test(allresults_AGLT$medianG_con-allresults_AGLT$medianG_inc, allresults_AGLT$MAD) #
cor.test(allresults_AGLT$medianG_con-allresults_AGLT$medianG_inc, allresults_AGLT$SDfoM) #
lm<-lm(allresults_AGLT$medianG_con-allresults_AGLT$medianG_inc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)#
summary(lm)

###########################################################
#Navon
###########################################################

##congruency interaction effect: Ginc-Gcon-linc+lcon
t.test(allresults_Navon1$medianG_inc-allresults_Navon1$medianG_con-allresults_Navon1$medianL_inc+allresults_Navon1$medianL_con~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$medianG_inc-allresults_Navon1$medianG_con-allresults_Navon1$medianL_inc+allresults_Navon1$medianL_con, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$medianG_inc-allresults_Navon1$medianG_con-allresults_Navon1$medianL_inc+allresults_Navon1$medianL_con, allresults_Navon1$MAD)
cor.test(allresults_Navon1$medianG_inc-allresults_Navon1$medianG_con-allresults_Navon1$medianL_inc+allresults_Navon1$medianL_con, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$medianG_inc-allresults_Navon1$medianG_con-allresults_Navon1$medianL_inc+allresults_Navon1$medianL_con~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)#
summary(lm)
##global-to-local interference: Lcon-Linc
t.test(allresults_Navon1$medianL_con-allresults_Navon1$medianL_inc~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$medianL_con-allresults_Navon1$medianL_inc, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$medianL_con-allresults_Navon1$medianL_inc, allresults_Navon1$MAD)
cor.test(allresults_Navon1$medianL_con-allresults_Navon1$medianL_inc, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$medianL_con-allresults_Navon1$medianL_inc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
##local-to-global interference: Gcon-Ginc
t.test(allresults_Navon1$medianG_con-allresults_Navon1$medianG_inc~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$medianG_con-allresults_Navon1$medianG_inc, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$medianG_con-allresults_Navon1$medianG_inc, allresults_Navon1$MAD)
cor.test(allresults_Navon1$medianG_con-allresults_Navon1$medianG_inc, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$medianG_con-allresults_Navon1$medianG_inc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score) #
summary(lm)

####correct
#################################################################################
#################################################################################

#AGLT
############################################################
##global advantage: G-L

##congruency interaction effect: Ginc-Gcon-linc+lcon
t.test(allresults_AGLT$correct_Ginc-allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Linc+allresults_AGLT$correct_Lcon~ allresults_AGLT$AP.0.RP.1.AP.)
cor.test(allresults_AGLT$correct_Ginc-allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Linc+allresults_AGLT$correct_Lcon, allresults_AGLT$AQ_Score)#
cor.test(allresults_AGLT$correct_Ginc-allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Linc+allresults_AGLT$correct_Lcon, allresults_AGLT$MAD)
cor.test(allresults_AGLT$correct_Ginc-allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Linc+allresults_AGLT$correct_Lcon, allresults_AGLT$SDfoM)
lm<-lm(allresults_AGLT$correct_Ginc-allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Linc+allresults_AGLT$correct_Lcon~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
##global-to-local interference: Lcon-Linc
t.test(allresults_AGLT$correct_Lcon-allresults_AGLT$correct_Linc~ allresults_AGLT$AP.0.RP.1.AP.)
cor.test(allresults_AGLT$correct_Lcon-allresults_AGLT$correct_Linc, allresults_AGLT$AQ_Score)
cor.test(allresults_AGLT$correct_Lcon-allresults_AGLT$correct_Linc, allresults_AGLT$MAD)
cor.test(allresults_AGLT$correct_Lcon-allresults_AGLT$correct_Linc, allresults_AGLT$SDfoM)#
lm<-lm(allresults_AGLT$correct_Lcon-allresults_AGLT$correct_Linc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
##local-to-global interference: Gcon-Ginc
t.test(allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Ginc~ allresults_AGLT$AP.0.RP.1.AP.)
cor.test(allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Ginc, allresults_AGLT$AQ_Score)
cor.test(allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Ginc, allresults_AGLT$MAD)
cor.test(allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Ginc, allresults_AGLT$SDfoM)
lm<-lm(allresults_AGLT$correct_Gcon-allresults_AGLT$correct_Ginc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
###########################################################
#Navon
###########################################################

##congruency interaction effect: Ginc-Gcon-linc+lcon
t.test(allresults_Navon1$vcorrect_Ginc-allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Linc+allresults_Navon1$vcorrect_Lcon~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$vcorrect_Ginc-allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Linc+allresults_Navon1$vcorrect_Lcon, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$vcorrect_Ginc-allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Linc+allresults_Navon1$vcorrect_Lcon, allresults_Navon1$MAD)
cor.test(allresults_Navon1$vcorrect_Ginc-allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Linc+allresults_Navon1$vcorrect_Lcon, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$vcorrect_Ginc-allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Linc+allresults_Navon1$vcorrect_Lcon~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
##global-to-local interference: Lcon-Linc
t.test(allresults_Navon1$vcorrect_Lcon-allresults_Navon1$vcorrect_Linc~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$vcorrect_Lcon-allresults_Navon1$vcorrect_Linc, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$vcorrect_Lcon-allresults_Navon1$vcorrect_Linc, allresults_Navon1$MAD)
cor.test(allresults_Navon1$vcorrect_Lcon-allresults_Navon1$vcorrect_Linc, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$vcorrect_Lcon-allresults_Navon1$vcorrect_Linc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)
##local-to-global interference: Gcon-Ginc
t.test(allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Ginc~ allresults_Navon1$AP.0.RP.1.AP.)
cor.test(allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Ginc, allresults_Navon1$AQ_Score)
cor.test(allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Ginc, allresults_Navon1$MAD)
cor.test(allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Ginc, allresults_Navon1$SDfoM)
lm<-lm(allresults_Navon1$vcorrect_Gcon-allresults_Navon1$vcorrect_Ginc~allresults_AGLT$MAD+allresults_AGLT$AQ_Score)
summary(lm)








#############################################
#############################################
#############################################
##Grafics

###auditory global-to-local interference
ggplot(data=allresults_AGLT,aes(x=SDfoM, y=(correct_Lcon-correct_Linc)))+
  geom_point(mapping=aes(x=SDfoM, y=(correct_Lcon-correct_Linc)))+
  geom_abline(aes(intercept=3.623150, slope=0.010561), color="red")+
  geom_point(aes(color=AQ_Score,size=2))+theme_classic()+labs(x="SDfoM",
                                                              y= "Lcon-Linc (ACC)", 
                                                              title="Auditory global-to-local interference")+
  coord_cartesian(ylim=c(-10,30),xlim=c(0,500))+
  theme(axis.text.x=element_text(color="black", size=16),
        axis.text.y=element_text(color="black", size=16),
        legend.title=element_text(color="black", size=16,face="bold"),
        legend.text=element_text(color="black", size=16),
        axis.title=element_text(face="bold",size=16),
        title=element_text(size=12),panel.grid.major.y = element_line(colour = "grey"))

###auditory local-to-global interference
ggplot(data=allresults_AGLT,aes(x=SDfoM, y=(medianG_con-medianG_inc)))+
  geom_point(mapping=aes(x=SDfoM, y=(medianG_con-medianG_inc)))+
  geom_abline(aes(intercept=-3.406e-02, slope=-3.010e-04), color="red")+
  geom_point(aes(color=AQ_Score,size=2))+theme_classic()+labs(x="SDfoM",
                                                              y= "Gcon-Ginc (RT)", 
                                                              title="Auditory local-to-global interference")+
  coord_cartesian(ylim=c(-0.5,0.25),xlim=c(0,500))+
  theme(axis.text.x=element_text(color="black", size=16),
        axis.text.y=element_text(color="black", size=16),
        legend.title=element_text(color="black", size=16,face="bold"),
        legend.text=element_text(color="black", size=16),
        axis.title=element_text(face="bold",size=16),
        title=element_text(size=12),panel.grid.major.y = element_line(colour = "grey"))

###visual global-to-local interference
ggplot(data=allresults_Navon1,aes(x=AQ_Score, y=(med_vis_SACS_Lcon-med_vis_SACS_Linc)))+
  geom_point(mapping=aes(x=AQ_Score, y=(med_vis_SACS_Lcon-med_vis_SACS_Linc)))+
  geom_abline(aes(intercept=0.49986, slope=-0.02112), color="red")+
  geom_point(aes(color=MAD,size=2))+theme_classic()+labs(x="AQ_Score",
                                                              y= "Lcon-Linc (SACS)", 
                                                              title="Visual global-to-local interference")+
  coord_cartesian(ylim=c(-1.5,2),xlim=c(0,36))+
  theme(axis.text.x=element_text(color="black", size=16),
        axis.text.y=element_text(color="black", size=16),
        legend.title=element_text(color="black", size=16,face="bold"),
        legend.text=element_text(color="black", size=16),
        axis.title=element_text(face="bold",size=16),
        title=element_text(size=12),panel.grid.major.y = element_line(colour = "grey"))


