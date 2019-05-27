setwd("~/files")
allresults10.10 <- read_csv("allresults10.10.csv", na = "NA")
source('~/files/Cognition/music_hours.R')
index_online<-match(x=allresults10.10$VP_Code, table=rownames(hours))
resultsindex<-rbind(hours[index_online,])
allresults10.10<-cbind(allresults10.10,resultsindex) 

dat<-allresults10.10
###########################################
#Skripte Ye-Young
##########################################
# Pakete laden

library(psych)
library(car)
library(readr)

# Datensatz laden

#dat <- read_csv("Downloads/data_yeyoung.csv", na = "NA")

# SPM IQ-Werte mitteln ####

table(dat$SPM_IQ)

dat$SPM_IQ[dat$SPM_IQ=="104,5 und 107,5"] <- 106
dat$SPM_IQ[dat$SPM_IQ=="110,5 und 113,5"] <- 112
dat$SPM_IQ[dat$SPM_IQ=="112 und 115"] <- 113.5
dat$SPM_IQ[dat$SPM_IQ=="113,5 und 116,5"] <- 115
dat$SPM_IQ[dat$SPM_IQ=="118-124"] <- 121
dat$SPM_IQ[dat$SPM_IQ=="119,5 und 122,5"] <- 121
dat$SPM_IQ[dat$SPM_IQ=="121-125,5"] <- 123.25
dat$SPM_IQ[dat$SPM_IQ=="125,5 und 127"] <- 126.25
dat$SPM_IQ[dat$SPM_IQ=="130-134,5"] <- 132.25
dat$SPM_IQ[dat$SPM_IQ=="98,5 und 100"] <- 99.25
dat$SPM_IQ[dat$SPM_IQ=="128,5"] <- 128.5
dat$SPM_IQ[dat$SPM_IQ=="125,5"] <- 125.5
dat$SPM_IQ[dat$SPM_IQ=="131,5"] <- 131.5
dat$SPM_IQ[dat$SPM_IQ=="86,5"] <- 86.5
dat$SPM_IQ[dat$SPM_IQ=="98,5"] <- 98.5
dat$SPM_IQ[dat$SPM_IQ=="74,5"] <- 74.5
dat$SPM_IQ[dat$SPM_IQ=="89,5"] <- 89.5
dat$SPM_IQ[dat$SPM_IQ=="106"] <- 106
dat$SPM_IQ[dat$SPM_IQ=="88"] <- 88
dat$SPM_IQ[dat$SPM_IQ=="134,4"] <- 134.4

is.numeric(dat$SPM_IQ)
dat$SPM_IQ = as.numeric(dat$SPM_IQ)

# SPM T-Werte mitteln ####

table(dat$SPM_T)

dat$SPM_T[dat$SPM_T== "49 und 50"] <- 49.5
dat$SPM_T[dat$SPM_T== "53 und 55"] <- 54
dat$SPM_T[dat$SPM_T== "56 und 58"] <- 57
dat$SPM_T[dat$SPM_T== "57 und 59"] <- 58
dat$SPM_T[dat$SPM_T== "58 und 60"] <- 59
dat$SPM_T[dat$SPM_T== "59 und 61"] <- 60
dat$SPM_T[dat$SPM_T== "62-66"] <- 64
dat$SPM_T[dat$SPM_T== "63 und 65"] <- 64
dat$SPM_T[dat$SPM_T== "64-67"] <- 65.5
dat$SPM_T[dat$SPM_T== "67 und 68"] <- 67.5
dat$SPM_T[dat$SPM_T== "70-73"] <- 71.5

is.numeric(dat$SPM_T)
dat$SPM_T = as.numeric(dat$SPM_T)

# ZVT IQ-Werte ####

is.numeric(dat$ZVT_IQ)

table(nchar(dat$ZVT_IQ)==4) 

dat$ZVT_IQ[dat$ZVT_IQ==1405] <- 1405/10
dat$ZVT_IQ[dat$ZVT_IQ==1315] <- 1315/10
dat$ZVT_IQ[dat$ZVT_IQ==1195] <- 1195/10
dat$ZVT_IQ[dat$ZVT_IQ==1135] <- 1135/10
dat$ZVT_IQ[dat$ZVT_IQ==1255] <- 1255/10
dat$ZVT_IQ[dat$ZVT_IQ==1375] <- 1375/10
dat$ZVT_IQ[dat$ZVT_IQ==1435] <- 1435/10
dat$ZVT_IQ[dat$ZVT_IQ==1285] <- 1285/10
dat$ZVT_IQ[dat$ZVT_IQ==1165] <- 1165/10
dat$ZVT_IQ[dat$ZVT_IQ==1225] <- 1225/10
dat$ZVT_IQ[dat$ZVT_IQ==1345] <- 1345/10
dat$ZVT_IQ[dat$ZVT_IQ==1335.0] <- 1335.0/10
dat$ZVT_IQ[dat$ZVT_IQ==1105.0] <- 1105.0/10
dat$ZVT_IQ[dat$ZVT_IQ==1045.0] <- 1045.0/10
dat$ZVT_IQ[dat$ZVT_IQ==1075.0] <- 1075.0/10
dat$ZVT_IQ[dat$ZVT_IQ==1015.0] <- 1015.0/10
dat$ZVT_IQ[dat$ZVT_IQ==13350] <- 13350/100
dat$ZVT_IQ[dat$ZVT_IQ==11050] <- 11050/100
dat$ZVT_IQ[dat$ZVT_IQ==10450] <- 10450/100
dat$ZVT_IQ[dat$ZVT_IQ==10750] <- 10750/100
dat$ZVT_IQ[dat$ZVT_IQ==10150] <- 10150/100

# neue Spalten ####
# Version A/B

dat["version"] <- 0 
dat$version[dat$condition.A.B.=="B"] <- 1

# Instrument, 0=harmonic, 1=melodic bzw. nicht hauptsächlich "mehrstimmig" (Schlagzeug, E-Bass??)

dat["instrument"] <- NA
table(dat$main_instrument)
dat$instrument[dat$main_instrument=="Klavier"] <- 0
dat$instrument[dat$main_instrument=="Akkordeon"] <- 0
dat$instrument[dat$main_instrument=="Violine"] <- 1
dat$instrument[dat$main_instrument=="Bratsche"] <- 1
dat$instrument[dat$main_instrument=="Gesang"] <- 1
dat$instrument[dat$main_instrument=="Posaune"] <- 1
dat$instrument[dat$main_instrument=="Querfloete"] <- 1
dat$instrument[dat$main_instrument=="Trompete"] <- 1
dat$instrument[dat$main_instrument=="Violoncello"] <- 1
dat$instrument[dat$main_instrument=="Waldhorn"] <- 1
dat$instrument[dat$main_instrument=="E-Bass"] <- 1
dat$instrument[dat$main_instrument=="Schlagzeug"] <- 1


# d', c ####

# Hit Rates

dat["d_HR"] <- NA
dat$d_HR <- (dat$Ins_0_corr+dat$Ins_6_corr+dat$Ins_12_corr+dat$Ins_24_corr)/(dat$N_Ins_0+dat$N_Ins_6+dat$N_Ins_12+dat$N_Ins_24)

dat["d0_HR"] <- NA
dat$d0_HR <- dat$Ins_0_corr/dat$N_Ins_0

dat["d6_HR"] <- NA
dat$d6_HR <- dat$Ins_6_corr/dat$N_Ins_6

dat["d12_HR"] <- NA
dat$d12_HR <- dat$Ins_12_corr/dat$N_Ins_12

dat["d24_HR"] <- NA
dat$d24_HR <- dat$Ins_24_corr/dat$N_Ins_24


# False Alarm Rates

dat["d_FA"] <- NA
dat$d_FA <- (dat$N_miss_0+dat$N_miss_6+dat$N_miss_12+dat$N_miss_24-dat$miss_0_corr-dat$miss_6_corr-dat$miss_12_corr-dat$miss_24_corr)/(dat$N_miss_0+dat$N_miss_6+dat$N_miss_12+dat$N_miss_24)

dat["d0_FA"] <- NA
dat$d0_FA <- (dat$N_miss_0-dat$miss_0_corr)/dat$N_miss_0

dat["d6_FA"] <- NA
dat$d6_FA <- (dat$N_miss_6-dat$miss_6_corr)/dat$N_miss_6

dat["d12_FA"] <- NA
dat$d12_FA <- (dat$N_miss_12-dat$miss_12_corr)/dat$N_miss_12

dat["d24_FA"] <- NA
dat$d24_FA <- (dat$N_miss_24-dat$miss_24_corr)/dat$N_miss_24


# Umkodieren Werte 0, 1

table(dat$d_HR)
table(dat$d_FA)
table(dat$d0_HR)
table(dat$d0_FA)
table(dat$d6_HR)
table(dat$d6_FA)
table(dat$d12_HR)
table(dat$d12_FA)
table(dat$d24_HR)
table(dat$d24_FA)

range(dat$N_Ins_0)
range(dat$N_Ins_6)
range(dat$N_Ins_12)
range(dat$N_Ins_24)

range(dat$N_miss_0)
range(dat$N_miss_6)
range(dat$N_miss_12)
range(dat$N_miss_24)

dat$AEFT_totalIns<-dat$N_Ins_0+dat$N_Ins_6+dat$N_Ins_12+dat$N_Ins_24
dat$AEFT_totalmiss<-dat$N_miss_0+dat$N_miss_6+dat$N_miss_12+dat$N_miss_24

dat$d_HR[dat$d_HR==1&dat$AEFT_totalIns==65] <- 64.5/65
dat$d_HR[dat$d_HR==1&dat$AEFT_totalIns==64] <- 63.5/64
dat$d_HR[dat$d_HR==1&dat$AEFT_totalIns==63] <- 62.5/63
dat$d_HR[dat$d_HR==1&dat$AEFT_totalIns==62] <- 61.5/62
dat$d_HR[dat$d_HR==1&dat$AEFT_totalIns==61] <- 60.5/61
dat$d_HR[dat$d_HR==1&dat$AEFT_totalIns==60] <- 59.5/60
dat$d_FA[dat$d_FA==0&dat$AEFT_totalmiss==70] <- 0.5/70
dat$d_FA[dat$d_FA==0&dat$AEFT_totalmiss==69] <- 0.5/69
dat$d_FA[dat$d_FA==0&dat$AEFT_totalmiss==68] <- 0.5/68
dat$d_FA[dat$d_FA==0&dat$AEFT_totalmiss==67] <- 0.5/67
dat$d_FA[dat$d_FA==0&dat$AEFT_totalmiss==66] <- 0.5/66
dat$d_FA[dat$d_FA==0&dat$AEFT_totalmiss==65] <- 0.5/65
dat$d_FA[dat$d_FA==0&dat$AEFT_totalmiss==64] <- 0.5/64

dat$d0_HR[dat$d0_HR==1&dat$N_Ins_0==15] <- 14.5/15
dat$d0_HR[dat$d0_HR==1&dat$N_Ins_0==16] <- 15.5/16
dat$d0_HR[dat$d0_HR==1&dat$N_Ins_0==17] <- 16.5/17
dat$d0_HR[dat$d0_HR==0&dat$N_Ins_0==15] <- 0.5/15
dat$d0_HR[dat$d0_HR==0&dat$N_Ins_0==16] <- 0.5/16
dat$d0_HR[dat$d0_HR==0&dat$N_Ins_0==17] <- 0.5/17

dat$d0_FA[dat$d0_FA==0&dat$N_miss_0==17] <- 0.5/17
dat$d0_FA[dat$d0_FA==0&dat$N_miss_0==16] <- 0.5/16
dat$d0_FA[dat$d0_FA==0&dat$N_miss_0==15] <- 0.5/15
dat$d0_FA[dat$d0_FA==1&dat$N_miss_0==17] <- 16.5/17
dat$d0_FA[dat$d0_FA==1&dat$N_miss_0==16] <- 15.5/16
dat$d0_FA[dat$d0_FA==1&dat$N_miss_0==15] <- 14.5/15



dat$d6_HR[dat$d6_HR==1&dat$N_Ins_6==16] <- 15.5/16
dat$d6_HR[dat$d6_HR==1&dat$N_Ins_6==15] <- 14.5/15
dat$d6_HR[dat$d6_HR==1&dat$N_Ins_6==14] <- 13.5/14
dat$d6_HR[dat$d6_HR==1&dat$N_Ins_6==13] <- 12.5/13
dat$d6_HR[dat$d6_HR==0&dat$N_Ins_6==16] <- 0.5/16
dat$d6_HR[dat$d6_HR==0&dat$N_Ins_6==15] <- 0.5/15
dat$d6_HR[dat$d6_HR==0&dat$N_Ins_6==14] <- 0.5/14
dat$d6_HR[dat$d6_HR==0&dat$N_Ins_6==13] <- 0.5/13

dat$d6_FA[dat$d6_FA==0&dat$N_miss_6==15] <- 0.5/15
dat$d6_FA[dat$d6_FA==0&dat$N_miss_6==16] <- 0.5/16
dat$d6_FA[dat$d6_FA==0&dat$N_miss_6==17] <- 0.5/17
dat$d6_FA[dat$d6_FA==1&dat$N_miss_6==15] <- 14.5/15
dat$d6_FA[dat$d6_FA==1&dat$N_miss_6==16] <- 15.5/16
dat$d6_FA[dat$d6_FA==1&dat$N_miss_6==17] <- 16.5/17



dat$d12_HR[dat$d12_HR==1&dat$N_Ins_12==16] <- 15.5/16
dat$d12_HR[dat$d12_HR==1&dat$N_Ins_12==15] <- 14.5/15
dat$d12_HR[dat$d12_HR==1&dat$N_Ins_12==14] <- 13.5/14
dat$d12_HR[dat$d12_HR==0&dat$N_Ins_12==16] <- 0.5/16
dat$d12_HR[dat$d12_HR==0&dat$N_Ins_12==15] <- 0.5/15
dat$d12_HR[dat$d12_HR==0&dat$N_Ins_12==14] <- 0.5/14

dat$d12_FA[dat$d12_FA==1&dat$N_miss_12==18] <- 17.5/18
dat$d12_FA[dat$d12_FA==1&dat$N_miss_12==17] <- 16.5/17
dat$d12_FA[dat$d12_FA==1&dat$N_miss_12==16] <- 5.5/16
dat$d12_FA[dat$d12_FA==1&dat$N_miss_12==15] <- 14.5/15
dat$d12_FA[dat$d12_FA==0&dat$N_miss_12==18] <- 0.5/18
dat$d12_FA[dat$d12_FA==0&dat$N_miss_12==17] <- 0.5/17
dat$d12_FA[dat$d12_FA==0&dat$N_miss_12==16] <- 0.5/16
dat$d12_FA[dat$d12_FA==0&dat$N_miss_12==15] <- 0.5/15

dat$d24_HR[dat$d24_HR==1&dat$N_Ins_24==17] <- 16.5/17
dat$d24_HR[dat$d24_HR==1&dat$N_Ins_24==16] <- 15.5/16
dat$d24_HR[dat$d24_HR==1&dat$N_Ins_24==15] <- 14.5/15
dat$d24_HR[dat$d24_HR==1&dat$N_Ins_24==14] <- 13.5/14
dat$d24_HR[dat$d24_HR==0&dat$N_Ins_24==17] <- 0.5/17
dat$d24_HR[dat$d24_HR==0&dat$N_Ins_24==16] <- 0.5/16
dat$d24_HR[dat$d24_HR==0&dat$N_Ins_24==15] <- 0.5/15
dat$d24_HR[dat$d24_HR==0&dat$N_Ins_24==14] <- 0.5/14

dat$d24_FA[dat$d24_FA==0&dat$N_miss_24==18] <- 0.5/18
dat$d24_FA[dat$d24_FA==0&dat$N_miss_24==17] <- 0.5/17
dat$d24_FA[dat$d24_FA==0&dat$N_miss_24==16] <- 0.5/16
dat$d24_FA[dat$d24_FA==0&dat$N_miss_24==15] <- 0.5/15
dat$d24_FA[dat$d24_FA==1&dat$N_miss_24==18] <- 17.5/18
dat$d24_FA[dat$d24_FA==1&dat$N_miss_24==17] <- 16.5/17
dat$d24_FA[dat$d24_FA==1&dat$N_miss_24==16] <- 15.5/16
dat$d24_FA[dat$d24_FA==1&dat$N_miss_24==15] <- 14.5/15




# d'

dat["d"] <- NA
dat$d <- qnorm(dat$d_HR)-qnorm(dat$d_FA)

dat["d_0"] <- NA
dat$d_0 <- qnorm(dat$d0_HR)-qnorm(dat$d0_FA)

dat["d_6"] <- NA
dat$d_6 <- qnorm(dat$d6_HR)-qnorm(dat$d6_FA)

dat["d_12"] <- NA
dat$d_12 <- qnorm(dat$d12_HR)-qnorm(dat$d12_FA)

dat["d_24"] <- NA
dat$d_24 <- qnorm(dat$d24_HR)-qnorm(dat$d24_FA)


# c 

dat["c"] <- NA
dat$c <- -0.5*(qnorm(dat$d_HR)+qnorm(dat$d_FA))

dat["c_0"] <- NA
dat$c_0 <- -0.5*(qnorm(dat$d0_HR)+qnorm(dat$d0_FA))

dat["c_6"] <- NA
dat$c_6 <- -0.5*(qnorm(dat$d6_HR)+qnorm(dat$d6_FA))

dat["c_12"] <- NA
dat$c_12 <- -0.5*(qnorm(dat$d12_HR)+qnorm(dat$d12_FA))

dat["c_24"] <- NA
dat$c_24 <- -0.5*(qnorm(dat$d24_HR)+qnorm(dat$d24_FA))





# Antwortkriterium c
# range
-0.5*(qnorm(64.5/65)+qnorm(69.5/70)) # -2.436597 alle "ja"
-0.5*(qnorm(0.5/65)+qnorm(0.5/70)) # 2.436597 alle "nein"

####################################
#Voraussetzungen
####################################

# Korrelationsmatrizen d', AMMA(tonal), PIT, ZVT, Instrument, Version ####

corr_d1 <- c("d", "AMMAtonal", "AP_sums", "MSI_FG_Score", "ZVT_IQ", "instrument", "version")
corrdat_d1 <- dat[corr_d1]
chart.Correlation(corrdat_d1, histogram = T, pch= 19)

corr_d2 <- c("d_0", "AMMAtonal", "AP_sums", "MSI_FG_Score", "ZVT_IQ", "instrument", "version")
corrdat_d2 <- dat[corr_d2]
chart.Correlation(corrdat_d2, histogram = T, pch= 19)

corr_d3 <- c("d_6", "AMMAtonal", "AP_sums", "MSI_FG_Score", "ZVT_IQ", "instrument", "version")
corrdat_d3 <- dat[corr_d3]
chart.Correlation(corrdat_d3, histogram = T, pch= 19)

corr_d4 <- c("d_12", "AMMAtonal", "AP_sums", "MSI_FG_Score", "ZVT_IQ", "instrument", "version")
corrdat_d4 <- dat[corr_d4]
chart.Correlation(corrdat_d4, histogram = T, pch= 19)

corr_d5 <- c("d_24", "AMMAtonal", "AP_sums", "MSI_FG_Score", "ZVT_IQ", "instrument", "version")
corrdat_d5 <- dat[corr_d5]
chart.Correlation(corrdat_d5, histogram = T, pch= 19)

# AMMAtonal und MSI_FG_Score korrelieren zu 0.42 (recht hoch)  
# -> möglicherweise Multikollinearität?
# -> AMMAtonal korreliert auch über die Bedingungen konsistenter und höher mit d -> AMMA als Maß beibehalten, MSI ausschließen?
# -> oder beide Variablen aggregieren?


# Konfidenzintervalle

confint(reg_d, level=0.95)
confint(reg_d0, level=0.95)
confint(reg_d6, level=0.95)
confint(reg_d12, level=0.95)
confint(reg_d24, level=0.95)



# Voraussetzungen ####

# Normalverteilung

shapiro.test(dat$d)
shapiro.test(dat$d_0)
shapiro.test(dat$d_6) # H0 wird abgelehnt
shapiro.test(dat$d_12) # H0 wird abgelehnt
shapiro.test(dat$d_24) # H0 wird abgelehnt

# Linearer Zusammenhang s. Korrelationsplots

# Homoskedastizität (vgl. auch Residuenanalyse) ####

ncvTest(reg_d)
ncvTest(reg_d0)
ncvTest(reg_d6) # Heteroskedastizität
ncvTest(reg_d12) # Heteroskedastizität
ncvTest(reg_d24) # Heteroskedastizität


# Unabhängigkeit der Residuen

# Multikollinearität ####
# tol <- 1/vif

# 1. Modell
vif(reg_d)
tol_Mus1 <- 1/1.088315 
tol_ZVT1 <- 1/1.195689
tol_ins1 <- 1/1.203005 

# 2. Modell
vif(reg_d0)
tol_Mus2 <- 1/1.088315
tol_ZVT2 <- 1/1.195689
tol_ins2 <- 1/1.203005



# Residuenanalyse ####

par(mfrow=c(2,2))
plot(reg_d, main= "model 1")

par(mfrow=c(2,2))
plot(reg_d0, main= "model 2")

par(mfrow=c(2,2))
plot(reg_d6, main= "model 3")

par(mfrow=c(2,2))
plot(reg_d12, main= "model 4")

par(mfrow=c(2,2))
plot(reg_d24, main= "model 5")



# Adjustierte p-Werte/ Bonferroni-Holm-Korrektur

p_reg <- c(0.0002915, 0.003274, 0.03836, 0.1227, 0.1066)
p.adjust(p_reg, method = "holm")
# Modell 1 und 2 signifikant (p < .05)



