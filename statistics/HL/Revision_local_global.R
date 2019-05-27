#####revision of Paper 
load("~/files/Cogstyle Publication/30.08.Cogstyle.RData")
finalTable<-allresults_Navon1

#Participants characteristics
#finalTable<-finalTable[,1:159]
AP_finalTable<-filter(finalTable, finalTable$AP.0.RP.1.AP.==1)
RP_finalTable<-filter(finalTable, finalTable$AP.0.RP.1.AP.==0)

#age
hist(AP_finalTable$age) #non-normal
describe(AP_finalTable$age)
describe(RP_finalTable$age)
t.test(finalTable$age~finalTable$AP.0.RP.1.AP.)
wilcox.test(finalTable$age,finalTable$AP.0.RP.1.AP., paired=FALSE) #Man Whitney U Test

#SPM_IQ
hist(finalTable$SPM_IQ)
describe(AP_finalTable$SPM_IQ)
describe(RP_finalTable$SPM_IQ)
t.test(finalTable$SPM_IQ~finalTable$AP.0.RP.1.AP.)

#ZVT_IQ
hist(finalTable$ZVT_IQ)
describe(AP_finalTable$ZVT_IQ)
describe(RP_finalTable$ZVT_IQ)
t.test(finalTable$ZVT_IQ~finalTable$AP.0.RP.1.AP.)

#main_hours
hist(finalTable$total_main) #non-normal
describe(AP_finalTable$total_main)
describe(RP_finalTable$total_main)
t.test(finalTable$total_main~finalTable$AP.0.RP.1.AP.)
wilcox.test(finalTable$total_main,finalTable$AP.0.RP.1.AP.,paired=FALSE)

#main_hours
hist(finalTable$AMMAcomp)
describe(AP_finalTable$AMMAcomp)
describe(RP_finalTable$AMMAcomp)
t.test(finalTable$AMMAcomp~finalTable$AP.0.RP.1.AP.)

#MSI
hist(finalTable$MSI_Score)
describe(AP_finalTable$MSI_Score)
describe(RP_finalTable$MSI_Score)
t.test(finalTable$MSI_Score~finalTable$AP.0.RP.1.AP.)

#PIS
hist(finalTable$AP_sums)
describe(AP_finalTable$AP_sums)
describe(RP_finalTable$AP_sums)
t.test(finalTable$AP_sums~finalTable$AP.0.RP.1.AP.)

#PIS
hist(finalTable$AQ_Score)
describe(AP_finalTable$AQ_Score)
describe(RP_finalTable$AQ_Score)
t.test(finalTable$AQ_Score~finalTable$AP.0.RP.1.AP.)

#MAD
hist(finalTable$MAD)
describe(AP_finalTable$MAD)
describe(RP_finalTable$MAD)
t.test(finalTable$MAD~finalTable$AP.0.RP.1.AP.)

#SDfoM
hist(finalTable$SDfoM)
describe(AP_finalTable$SDfoM)
describe(RP_finalTable$SDfoM)
t.test(finalTable$SDfoM~finalTable$AP.0.RP.1.AP.)

#starting age
hist(finalTable$starting_age)
describe(AP_finalTable$starting_age)
describe(RP_finalTable$starting_age)
t.test(finalTable$starting_age~finalTable$AP.0.RP.1.AP.)

##bivariate correlations
#bivariate correlations
cor.test(finalTable$MAD,finalTable$AP_sums) #
cor.test(finalTable$MAD,finalTable$MSI_Score)
cor.test(finalTable$MAD,finalTable$total_main)
cor.test(finalTable$MAD,finalTable$starting_age) #
cor.test(finalTable$MAD,finalTable$SPM_IQ)
cor.test(finalTable$MAD,finalTable$ZVT_IQ)
cor.test(finalTable$MAD,finalTable$AQ_Score) #
cor.test(finalTable$MAD,finalTable$SDfoM)#

cor.test(finalTable$SDfoM,finalTable$AP_sums) #
cor.test(finalTable$SDfoM,finalTable$MSI_Score)
cor.test(finalTable$SDfoM,finalTable$total_main)
cor.test(finalTable$SDfoM,finalTable$starting_age) #
cor.test(finalTable$SDfoM,finalTable$SPM_IQ)
cor.test(finalTable$SDfoM,finalTable$ZVT_IQ)
cor.test(finalTable$SDfoM,finalTable$AQ_Score)#

cor.test(finalTable$AP_sums,finalTable$MSI_Score)
cor.test(finalTable$AP_sums,finalTable$total_main)
cor.test(finalTable$AP_sums,finalTable$starting_age)
cor.test(finalTable$AP_sums,finalTable$SPM_IQ)
cor.test(finalTable$AP_sums,finalTable$ZVT_IQ)
cor.test(finalTable$AP_sums,finalTable$AQ_Score)#


cor.test(finalTable$MSI_Score,finalTable$total_main) #
cor.test(finalTable$MSI_Score,finalTable$starting_age) #
cor.test(finalTable$MSI_Score,finalTable$SPM_IQ) #
cor.test(finalTable$MSI_Score,finalTable$ZVT_IQ)
cor.test(finalTable$MSI_Score,finalTable$AQ_Score)

cor.test(finalTable$total_main,finalTable$starting_age) #
cor.test(finalTable$total_main,finalTable$SPM_IQ)
cor.test(finalTable$total_main,finalTable$ZVT_IQ)
cor.test(finalTable$total_main,finalTable$AQ_Score)

cor.test(finalTable$starting_age,finalTable$SPM_IQ)#
cor.test(finalTable$starting_age,finalTable$ZVT_IQ)
cor.test(finalTable$starting_age,finalTable$AQ_Score)

cor.test(finalTable$SPM_IQ,finalTable$ZVT_IQ) #
cor.test(finalTable$SPM_IQ,finalTable$AQ_Score)


cor.test(finalTable$ZVT_IQ,finalTable$AQ_Score)

###########################
#post hoc tests for interactions
###########################
##RT
#Navon
allresults_Navonlong <- gather(allresults_Navon1, condition, median, medianL_con,medianL_inc,medianG_con,medianG_inc)
LG<-character(220)
LG[1:110]<-"L"
LG[111:220]<- "G"
congruency<-character(220)
congruency[1:55]<-"inc"
congruency[111:165]<- "inc"
congruency[56:110]<-"con"
congruency[166:220]<-"con"
allresults_longvis <- data.frame(allresults_Navonlong,LG,congruency)
aov_vis <- aov(median ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis)
summary(aov_vis)
lm_vis <- lm(median ~ AP.0.RP.1.AP.*LG*congruency, data=allresults_longvis)
summary(lm_vis)

#AGLT
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
aov_vis <- aov(median ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis)
summary(aov_vis)
lm_vis <- lm(median ~ AP.0.RP.1.AP.+LG+congruency, data=allresults_longvis)
summary(lm_vis)

##correct

#Navon
allresults_Navonlong1 <- gather(allresults_Navon1, condition, correct, vcorrect_Lcon,vcorrect_Linc,vcorrect_Gcon,vcorrect_Ginc)
LG<-character(220)
LG[1:110]<-"L"
LG[111:220]<- "G"
congruency<-character(220)
congruency[1:55]<-"con"
congruency[111:165]<-"con"
congruency[56:110]<-"inc"
congruency[166:220]<-"inc"
allresults_longvis1 <- data.frame(allresults_Navonlong1,LG,congruency)
aov_vis <- aov(correct ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis1)
lm_vis <- lm(correct ~ AP.0.RP.1.AP.+LG+congruency, data=allresults_longvis1)
summary(lm_vis)

#AGLT
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
aov_vis <- aov(correct ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis1)
lm_vis <- lm(correct ~ AP.0.RP.1.AP.+LG+congruency, data=allresults_longvis1)
summary(lm_vis)

##SACS
#Navon
allresults_Navonlong1 <- gather(allresults_Navon1, condition, correct,med_vis_SACS_Lcon, med_vis_SACS_Linc,med_vis_SACS_Gcon,med_vis_SACS_Ginc)
LG<-character(220)
LG[1:110]<-"L"
LG[111:220]<- "G"
congruency<-character(220)
congruency[1:55]<-"con"
congruency[111:165]<-"con"
congruency[56:110]<-"inc"
congruency[166:220]<-"inc"
allresults_longvis1 <- data.frame(allresults_Navonlong1,LG,congruency)
aov_vis <- aov(correct ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis1)
lm_vis <- lm(correct ~ AP.0.RP.1.AP.+LG+congruency, data=allresults_longvis1)
summary(lm_vis)

#AGLT
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
aov_vis <- aov(correct ~ AP.0.RP.1.AP.*LG*congruency+Error(code/(LG*congruency)), data=allresults_longvis1)
lm_vis <- lm(correct ~ AP.0.RP.1.AP.+LG+congruency, data=allresults_longvis1)
summary(lm_vis)

##correlation MAD and RTS on AGLT congruent trials. 
AP_allresults_AGLT<-filter(allresults_AGLT, allresults_AGLT$AP.0.RP.1.AP.==1)
allresults_AGLTcongruent <- gather(AP_allresults_AGLT, condition, median, medianL_con,medianG_con)
lm_AGLTcon <- lm(median ~ MAD, data=allresults_AGLTcongruent)
summary(lm_AGLTcon)
