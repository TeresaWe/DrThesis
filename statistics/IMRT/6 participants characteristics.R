
#Participants characteristics
dat_filter<-dat_filter[,1:159]
AP_dat_filter<-filter(dat_filter, dat_filter$AP.0.RP.1.AP.==1)
RP_dat_filter<-filter(dat_filter, dat_filter$AP.0.RP.1.AP.==0)

#age
hist(AP_dat_filter$age) #non-normal
describe(AP_dat_filter$age)
describe(RP_dat_filter$age)
t.test(dat_filter$age~dat_filter$AP.0.RP.1.AP.)
wilcox.test(dat_filter$age,dat_filter$AP.0.RP.1.AP., paired=FALSE) #Man Whitney U Test

#SPM_IQ
hist(dat_filter$SPM_IQ)
describe(AP_dat_filter$SPM_IQ)
describe(RP_dat_filter$SPM_IQ)
t.test(dat_filter$SPM_IQ~dat_filter$AP.0.RP.1.AP.)

#ZVT_IQ
hist(dat_filter$ZVT_IQ)
describe(AP_dat_filter$ZVT_IQ)
describe(RP_dat_filter$ZVT_IQ)
t.test(dat_filter$ZVT_IQ~dat_filter$AP.0.RP.1.AP.)

#main_hours
hist(dat_filter$total_main) #non-normal
describe(AP_dat_filter$total_main)
describe(RP_dat_filter$total_main)
t.test(dat_filter$total_main~dat_filter$AP.0.RP.1.AP.)
wilcox.test(dat_filter$total_main,dat_filter$AP.0.RP.1.AP.,paired=FALSE)

#AMMA
hist(dat_filter$AMMAcomp)
describe(AP_dat_filter$AMMAcomp)
describe(RP_dat_filter$AMMAcomp)
t.test(dat_filter$AMMAcomp~dat_filter$AP.0.RP.1.AP.)

#AMMA tonal
hist(dat_filter$AMMAtonal)
describe(AP_dat_filter$AMMAtonal)
describe(RP_dat_filter$AMMAtonal)
t.test(dat_filter$AMMAtonal~dat_filter$AP.0.RP.1.AP.)

#AMMA rhythmic
hist(dat_filter$AMMAryth)
describe(AP_dat_filter$AMMAryth)
describe(RP_dat_filter$AMMAryth)
t.test(dat_filter$AMMAryth~dat_filter$AP.0.RP.1.AP.)

#MSI
hist(dat_filter$MSI_Score)
describe(AP_dat_filter$MSI_Score)
describe(RP_dat_filter$MSI_Score)
t.test(dat_filter$MSI_Score~dat_filter$AP.0.RP.1.AP.)

#PIS
hist(dat_filter$AP_sums)
describe(AP_dat_filter$AP_sums)
describe(RP_dat_filter$AP_sums)
t.test(dat_filter$AP_sums~dat_filter$AP.0.RP.1.AP.)

#PIS
hist(dat_filter$AQ_Score)
describe(AP_dat_filter$AQ_Score)
describe(RP_dat_filter$AQ_Score)
t.test(dat_filter$AQ_Score~dat_filter$AP.0.RP.1.AP.)

#MAD
hist(dat_filter$MAD)
describe(AP_dat_filter$MAD)
describe(RP_dat_filter$MAD)
t.test(dat_filter$MAD~dat_filter$AP.0.RP.1.AP.)

#SDfoM
hist(dat_filter$SDfoM)
describe(AP_dat_filter$SDfoM)
describe(RP_dat_filter$SDfoM)
t.test(dat_filter$SDfoM~dat_filter$AP.0.RP.1.AP.)

#starting age
hist(dat_filter$starting_age)
describe(AP_dat_filter$starting_age)
describe(RP_dat_filter$starting_age)
t.test(dat_filter$starting_age~dat_filter$AP.0.RP.1.AP.)
