#Überprüfung Effekt der fehlerhaften randomisierung

t.test(d~AEFT_falseVersion,data=dat_filter)
t.test(d_0~AEFT_falseVersion,data=dat_filter)
t.test(d_6~AEFT_falseVersion,data=dat_filter)
t.test(d_12~AEFT_falseVersion,data=dat_filter)
t.test(d_24~AEFT_falseVersion,data=dat_filter)
#effect general version
t.test(d~version,data=dat_filter) # significant --> include into linear model!
t.test(d_0~version,data=dat_filter)#
t.test(d_6~version,data=dat_filter)
t.test(d_12~version,data=dat_filter)#
t.test(d_24~version,data=dat_filter)#

wrong_dat_filter<-filter(dat_filter, dat_filter$AEFT_falseVersion==1)
correct_dat_filter<-filter(dat_filter, dat_filter$AEFT_falseVersion==0)


###analyses only correct version participants
t.test(d~AP.0.RP.1.AP.,data=correct_dat_filter)#**
t.test(d_0~AP.0.RP.1.AP.,data=correct_dat_filter) #**
t.test(d_6~AP.0.RP.1.AP.,data=correct_dat_filter)#tendency
t.test(d_12~AP.0.RP.1.AP.,data=correct_dat_filter)#tendency
t.test(d_24~AP.0.RP.1.AP.,data=correct_dat_filter)#n.s.

reg_d <- lm(d ~ MSI_Score +Z_MAD+GEFT_meanRT, data = correct_dat_filter) 
summary(reg_d)

reg_d0 <- lm(d_0 ~ MSI_Score +Z_MAD+GEFT_meanRT, data = correct_dat_filter)
summary(reg_d0)

reg_d6 <- lm(d_6 ~ Z_MAD+GEFT_meanRT, data = correct_dat_filter) 
summary(reg_d6)

reg_d12 <- lm(d_12 ~ MSI_Score+Z_MAD, data = correct_dat_filter) 
summary(reg_d12)

reg_d12 <- lm(d_12 ~ Z_MAD, data = correct_dat_filter) 
summary(reg_d12)

reg_d24 <- lm(d_24 ~ ZVT_IQ, data = correct_dat_filter) 
summary(reg_d24)

###analyses only wrong version participants

t.test(d~AP.0.RP.1.AP.,data=wrong_dat_filter)#n.s
t.test(d_0~AP.0.RP.1.AP.,data=wrong_dat_filter) #n.s.
t.test(d_6~AP.0.RP.1.AP.,data=wrong_dat_filter)#n.s.
t.test(d_12~AP.0.RP.1.AP.,data=wrong_dat_filter)#n.s.
t.test(d_24~AP.0.RP.1.AP.,data=wrong_dat_filter)#n.s.

reg_d <- lm(d ~ MSI_Score +Z_MAD+GEFT_meanRT, data = wrong_dat_filter) 
summary(reg_d)

reg_d0 <- lm(d_0 ~ MSI_Score +Z_MAD+GEFT_meanRT, data = wrong_dat_filter)
summary(reg_d0)

reg_d6 <- lm(d_6 ~ Z_MAD+GEFT_meanRT, data = wrong_dat_filter) 
summary(reg_d6)

reg_d12 <- lm(d_12 ~ MSI_Score+Z_MAD, data = wrong_dat_filter) 
summary(reg_d12)

reg_d12 <- lm(d_12 ~ Z_MAD, data = wrong_dat_filter) 
summary(reg_d12)

reg_d24 <- lm(d_24 ~ ZVT_IQ, data = wrong_dat_filter) 
summary(reg_d24)
