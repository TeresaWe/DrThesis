allresults_AGLT<-cbind(allresults, AGLT_medianresults)  

#AGLT group analysis, medians, filtered across conditions, per subjcet
hist(allresults_AGLT$medianL_inc) #bimodal, outliers
hist(allresults_AGLT$medianL_con)#bimodal, outliers
hist(allresults_AGLT$medianG_con)
hist(allresults_AGLT$medianG_inc)

#exclusions: missunderstanding
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="IG26GNE175")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="HE17KLE175")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="UD20DAV449")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="LU05KON175") 
#exclusions
#change back to all if exclusions eeg not needed,#or change to other EEG_results table (eeg. delta)

allresults_AGLT<-subset(allresults_AGLT, VP_Code!="YL24DRO161")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="RI15SON966")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="AT26IMM177")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="EI19WOH163")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="HR07HER419")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="LU05KON175")
#allresults_AGLT<-subset(allresults_AGLT, VP_Code!="EO11MAR171")#
#allresults_AGLT<-subset(allresults_AGLT, VP_Code!="EO11KIC453")#
#allresults_AGLT<-subset(allresults_AGLT, VP_Code!="ER13ARN275")#
#allresults_AGLT<-subset(allresults_AGLT, VP_Code!="AD28VAH165")#

histBy(allresults_AGLT,"medianG_con","AP.0.RP.1.AP.")
histBy(allresults_AGLT,"medianL_con","AP.0.RP.1.AP.")
histBy(allresults_AGLT,"medianL_inc","AP.0.RP.1.AP.")
histBy(allresults_AGLT,"medianL_con","AP.0.RP.1.AP.")
allresults_AGLTlong <- gather(allresults_AGLT, condition, median, medianL_con,medianL_inc,medianG_con,medianG_inc)
LG<-character(220)
LG[1:110]<-"L"
LG[111:220]<- "G"
congruency<-character(220)
congruency[1:55]<-"con"
congruency[111:165]<-"con"
congruency[56:110]<-"inc"
congruency[166:220]<-"inc"
allresults_longvis <- data.frame(allresults_AGLTlong,LG,congruency)
aov_vis <- aov(median ~ condition.A.B.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis)
boxplot(median ~ LG*congruency*condition.A.B., data=allresults_longvis, main= "AGLT")

#aov_vis <- aov(value ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis)
pairwise.t.test(allresults_longvis$median,allresults_longvis$condition)
summary(aov_vis)
AGLT_L<-allresults_longvis[1:110,]
aov_vis_L <- aov(median ~ condition.A.B.*congruency+Error(code), data=AGLT_L)
summary(aov_vis_L)
AGLT_G<-allresults_longvis[111:220,]
aov_vis_G <- aov(median ~ condition.A.B.*congruency+Error(code), data=AGLT_G)
summary(aov_vis_G)
#plot error bars
means_vis<-tapply(X=allresults_longvis$median,
                  INDEX=list(allresults_longvis$congruency,allresults_longvis$LG,
                             allresults_longvis$AP.0.RP.1.AP.),FUN=mean)
sd_vis<-tapply(X=allresults_longvis$median,
               INDEX=list(allresults_longvis$congruency,allresults_longvis$LG,
                          allresults_longvis$AP.0.RP.1.AP.),FUN=sd)
length_xvis<-tapply(X=allresults_longvis$median,
                    INDEX=list(allresults_longvis$congruency,allresults_longvis$LG,
                               allresults_longvis$AP.0.RP.1.AP.),FUN=length)
se_vis<-sd_vis/sqrt(length_xvis)
descr_vis<-cbind(group=c(1,2,3,4,5,6,7,8),means_vis,se_vis)
#descr_vis<-cbind(descr_vis,congruency=c("con","inc","con","inc","con","inc","con","inc"),pitch=c("RP","RP","RP","RP","AP","AP","AP","AP"),focus=c("G","G","L","L","G","G","L","L"),stringsAsFactors=FALSE)
rownames(descr_vis)<-c("G_con_0","G_inc_0","L_con_0","L_inc_0",
                       "G_con_1","G_inc_1","L_con_1","L_inc_1")
descr_vis<-data.frame(descr_vis)
j<-ggplot(descr_vis,aes(x=group,y=means_vis,ymin=means_vis-1.96*se_vis,ymax=means_vis+1.96*se_vis))
j+geom_point(size=3)+geom_errorbar(color=c("darkblue","darkblue","blue","blue","darkgreen","darkgreen","#00CC33","#00CC33"),size=0.7, width=0.5)+theme_classic()+ labs(x="Condition",
                                                                                                                                                                       y= "Reaction times", 
                                                                                                                                                                       title="AGLT",subtitle="local (L) vs. global (G), congruent (con) vs. incongruent (inc), by group (RP=blue vs. AP=green)")+
  coord_cartesian(ylim=c(1.25,1.75))+
  xlim(labels=c("G_con_RP","G_inc_RP","L_con_RP","L_inc_RP",
                "G_con_AP","G_inc_AP","L_con_AP","L_inc_AP"))+
  theme(axis.text.x=element_text(color="black", size=10),
        axis.text.y=element_text(color="black", size=10),
        axis.title=element_text(face="bold",size=12),
        title=element_text(size=13),panel.grid.major.y = element_line(colour = "grey"))+
  annotate(geom="text",x=7.5,y=-1.8, label="Means & Confidence Intervals")
##lm explaining local results!

######################### correct answers?

allresults_AGLTlong1 <- gather(allresults_AGLT, condition, correct, correct_Lcon,correct_Linc,correct_Gcon,correct_Ginc)
LG<-character(220)
LG[1:110]<-"L"
LG[111:220]<- "G"
congruency<-character(220)
congruency[1:55]<-"con"
congruency[111:165]<-"con"
congruency[56:110]<-"inc"
congruency[166:220]<-"inc"
allresults_longvis1 <- data.frame(allresults_AGLTlong1,LG,congruency)
aov_vis <- aov(correct ~ condition.A.B.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis1)
boxplot(correct ~ LG*congruency*condition.A.B., data=allresults_longvis1, main= "AGLT")
summary(aov_vis)
AGLT_L<-allresults_longvis1[1:110,]
aov_vis_L <- aov(correct ~ condition.A.B.*congruency+Error(code), data=AGLT_L)
summary(aov_vis_L)
AGLT_G<-allresults_longvis1[111:220,]
aov_vis_G <- aov(correct ~ condition.A.B.*congruency+Error(code), data=AGLT_G)
summary(aov_vis_G)
#aov_vis <- aov(value ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis)
pairwise.t.test(allresults_longvis1$correct,allresults_longvis1$condition)

#plot error bars
means_vis<-tapply(X=allresults_longvis1$correct,
                  INDEX=list(allresults_longvis1$congruency,allresults_longvis1$LG,
                             allresults_longvis1$AP.0.RP.1.AP.),FUN=mean)
sd_vis<-tapply(X=allresults_longvis1$correct,
               INDEX=list(allresults_longvis1$congruency,allresults_longvis1$LG,
                          allresults_longvis1$AP.0.RP.1.AP.),FUN=sd)
length_xvis<-tapply(X=allresults_longvis1$correct,
                    INDEX=list(allresults_longvis1$congruency,allresults_longvis1$LG,
                               allresults_longvis1$AP.0.RP.1.AP.),FUN=length)
se_vis<-sd_vis/sqrt(length_xvis)
descr_vis<-cbind(group=c(1,2,3,4,5,6,7,8),means_vis,se_vis)
#descr_vis<-cbind(descr_vis,congruency=c("con","inc","con","inc","con","inc","con","inc"),pitch=c("RP","RP","RP","RP","AP","AP","AP","AP"),focus=c("G","G","L","L","G","G","L","L"),stringsAsFactors=FALSE)
rownames(descr_vis)<-c("G_con_0","G_inc_0","L_con_0","L_inc_0",
                       "G_con_1","G_inc_1","L_con_1","L_inc_1")
descr_vis<-data.frame(descr_vis)
j<-ggplot(descr_vis,aes(x=group,y=means_vis,ymin=means_vis-1.96*se_vis,ymax=means_vis+1.96*se_vis))
j+geom_point(size=3)+geom_errorbar(color=c("darkblue","darkblue","blue","blue","darkgreen","darkgreen","#00CC33","#00CC33"),size=0.7, width=0.5)+theme_classic()+ labs(x="Condition",
                                                                                                                                                                       y= "Correct", 
                                                                                                                                                                       title="AGLT",subtitle="local (L) vs. global (G), congruent (con) vs. incongruent (inc), by group (RP=blue vs. AP=green)")+
  coord_cartesian(ylim=c(25,40))+
  xlim(labels=c("G_con_RP","G_inc_RP","L_con_RP","L_inc_RP",
                "G_con_AP","G_inc_AP","L_con_AP","L_inc_AP"))+
  theme(axis.text.x=element_text(color="black", size=10),
        axis.text.y=element_text(color="black", size=10),
        axis.title=element_text(face="bold",size=12),
        title=element_text(size=13),panel.grid.major.y = element_line(colour = "grey"))+
  annotate(geom="text",x=7.5,y=-1.8, label="Means & Confidence Intervals")
##lm explaining local results!

######################### SACS?

allresults_AGLTlong1 <- gather(allresults_AGLT, condition, correct,med_aud_SACS_Lcon,med_aud_SACS_Linc,med_aud_SACS_Gcon,med_aud_SACS_Ginc)
LG<-character(220)
LG[1:110]<-"L"
LG[111:220]<- "G"
congruency<-character(220)
congruency[1:55]<-"con"
congruency[111:165]<-"con"
congruency[56:110]<-"inc"
congruency[166:220]<-"inc"
allresults_longvis1 <- data.frame(allresults_AGLTlong1,LG,congruency)
aov_vis <- aov(correct ~ condition.A.B.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis1)
boxplot(correct ~ LG*congruency*condition.A.B., data=allresults_longvis1, main= "AGLT")
print(model.tables(aov_vis,"means"),digits=3) 
#aov_vis <- aov(value ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis)
pairwise.t.test(allresults_longvis1$correct,allresults_longvis1$condition)
summary(aov_vis)
AGLT_L<-allresults_longvis1[1:110,]
aov_vis_L <- aov(correct ~ condition.A.B.*congruency+Error(code), data=AGLT_L)
summary(aov_vis_L)
AGLT_G<-allresults_longvis1[111:220,]
aov_vis_G <- aov(correct ~ condition.A.B.*congruency+Error(code), data=AGLT_G)
summary(aov_vis_G)
#plot error bars
means_vis<-tapply(X=allresults_longvis1$correct,
                  INDEX=list(allresults_longvis1$congruency,allresults_longvis1$LG,
                             allresults_longvis1$AP.0.RP.1.AP.),FUN=mean)
sd_vis<-tapply(X=allresults_longvis1$correct,
               INDEX=list(allresults_longvis1$congruency,allresults_longvis1$LG,
                          allresults_longvis1$AP.0.RP.1.AP.),FUN=sd)
length_xvis<-tapply(X=allresults_longvis1$correct,
                    INDEX=list(allresults_longvis1$congruency,allresults_longvis1$LG,
                               allresults_longvis1$AP.0.RP.1.AP.),FUN=length)
se_vis<-sd_vis/sqrt(length_xvis)
descr_vis<-cbind(group=c(1,2,3,4,5,6,7,8),means_vis,se_vis)
#descr_vis<-cbind(descr_vis,congruency=c("con","inc","con","inc","con","inc","con","inc"),pitch=c("RP","RP","RP","RP","AP","AP","AP","AP"),focus=c("G","G","L","L","G","G","L","L"),stringsAsFactors=FALSE)
rownames(descr_vis)<-c("G_con_0","G_inc_0","L_con_0","L_inc_0",
                       "G_con_1","G_inc_1","L_con_1","L_inc_1")
descr_vis<-data.frame(descr_vis)
j<-ggplot(descr_vis,aes(x=group,y=means_vis,ymin=means_vis-1.96*se_vis,ymax=means_vis+1.96*se_vis))
j+geom_point(size=3)+geom_errorbar(color=c("darkblue","darkblue","blue","blue","darkgreen","darkgreen","#00CC33","#00CC33"),size=0.7, width=0.5)+theme_classic()+ labs(x="Condition",
                                                                                                                                                                       y= "SACS", 
                                                                                                                                                                       title="AGLT",subtitle="local (L) vs. global (G), congruent (con) vs. incongruent (inc), by group (RP=blue vs. AP=green)")+
  coord_cartesian(ylim=c(-0.6,1.5))+
  xlim(labels=c("G_con_RP","G_inc_RP","L_con_RP","L_inc_RP",
                "G_con_AP","G_inc_AP","L_con_AP","L_inc_AP"))+
  theme(axis.text.x=element_text(color="black", size=10),
        axis.text.y=element_text(color="black", size=10),
        axis.title=element_text(face="bold",size=12),
        title=element_text(size=13),panel.grid.major.y = element_line(colour = "grey"))+
  annotate(geom="text",x=7.5,y=-1.8, label="Means & Confidence Intervals")
##lm explaining local results!




