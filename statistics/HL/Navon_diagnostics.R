#Navon outlier and RT diagnostics

allresults_Navon<-subset(allresults, VP_Code!="OS12GRO173") #change back to all if exclusions eeg not needed,#or change to other EEG_results table (eeg. delta)
allresults_Navon<-subset(allresults_Navon, VP_Code!="EL01KES159")
allresults_Navon<-subset(allresults_Navon, VP_Code!="YL24DRO161")
allresults_Navon<-subset(allresults_Navon, VP_Code!="RI15SON966")
allresults_Navon<-subset(allresults_Navon, VP_Code!="AZ17FRA106")




hist(allresults_Navon$vis_G_con_meanRT)
hist(allresults_Navon$vis_G_incon_meanRT)
hist(allresults_Navon$vis_L_con_meanRT)
hist(allresults_Navon$vis_L_incon_meanRT)
multi.hist(allresults_Navon$vis_G_con_meanRT,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(allresults_Navon$vis_G_incon_meanRT,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(allresults_Navon$vis_L_con_meanRT,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(allresults_Navon$vis_L_incon_meanRT,dcol=c("red","blue"),dlty=c("dashed","dotted"))
histBy(allresults_Navon,"vis_G_con_meanRT","AP.0.RP.1.AP.")
histBy(allresults_Navon,"vis_G_incon_meanRT","AP.0.RP.1.AP.")
histBy(allresults_Navon,"vis_L_con_meanRT","AP.0.RP.1.AP.")
histBy(allresults_Navon,"vis_L_incon_meanRT","AP.0.RP.1.AP.")

plot(allresults_Navon$vis_L_incon_meanRT,allresults_Navon$vis_L_con_meanRT)
plot(allresults_Navon$vis_G_incon_meanRT,allresults_Navon$vis_G_con_meanRT)

describe(allresults_Navon$vis_G_con_meanRT)
describe(allresults_Navon$vis_G_incon_meanRT)
describe(allresults_Navon$vis_L_con_meanRT)
describe(allresults_Navon$vis_L_incon_meanRT)
describeBy(allresults_Navon$vis_G_con_meanRT,allresults_Navon$AP.0.RP.1.AP.)
describeBy(allresults_Navon$vis_G_incon_meanRT,allresults_Navon$AP.0.RP.1.AP.)
describeBy(allresults_Navon$vis_L_con_meanRT,allresults_Navon$AP.0.RP.1.AP.)
describeBy(allresults_Navon$vis_L_incon_meanRT,allresults_Navon$AP.0.RP.1.AP.)




Gconscaled<-scale(allresults_Navon$vis_G_con_meanRT,scale = TRUE, center=TRUE)
multi.hist(Gconscaled,dcol=c("red","blue"),dlty=c("dashed","dotted"))
Ginconscaled<-scale(allresults_Navon$vis_G_incon_meanRT,scale = TRUE, center=TRUE)
multi.hist(Ginconscaled,dcol=c("red","blue"),dlty=c("dashed","dotted"))
Lconscaled<-scale(allresults_Navon$vis_L_con_meanRT,scale = TRUE, center=TRUE)
multi.hist(Lconscaled,dcol=c("red","blue"),dlty=c("dashed","dotted"))
Linconscaled<-scale(allresults_Navon$vis_L_incon_meanRT,scale = TRUE, center=TRUE)
multi.hist(Linconscaled,dcol=c("red","blue"),dlty=c("dashed","dotted"))
Gdiffscaled<-scale(Gdiff,scale = TRUE,center=TRUE)
Ldiffscaled<-scale(Ldiff,scale = TRUE,center=TRUE)
NavonRTscaled<-cbind(allresults_Navon$AP.0.RP.1.AP.,Gconscaled,
                     Ginconscaled,Lconscaled,Linconscaled,Gdiff,Ldiff,Gdiffscaled,Ldiffscaled)

describeBy(NavonRTscaled[,4],NavonRTscaled[,1])
describeBy(NavonRTscaled[,5],NavonRTscaled[,1])
describeBy(NavonRTscaled[,3],NavonRTscaled[,1])
describeBy(NavonRTscaled[,2],NavonRTscaled[,1])
describeBy(NavonRTscaled[,6],NavonRTscaled[,1])
describeBy(NavonRTscaled[,7],NavonRTscaled[,1])
describeBy(NavonRTscaled[,8],NavonRTscaled[,1])
describeBy(NavonRTscaled[,9],NavonRTscaled[,1])
multi.hist(Ldiffscaled,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(Gdiffscaled,dcol=c("red","blue"),dlty=c("dashed","dotted"))

# relation G L (quotient); RT
Gdiff<-allresults_Navon$vis_G_con_meanRT/allresults_Navon$vis_G_incon_meanRT
Ldiff<-allresults_Navon$vis_L_con_meanRT/allresults_Navon$vis_L_incon_meanRT
GminusL<-Gdiff/Ldiff
plot(GminusL)
NavonSACS<-data.frame(allresults_Navon$VP_Code,allresults_Navon$AP.0.RP.1.AP.,allresults_Navon$AQ_Score,Gdiff,Ldiff,GminusL)
colnames(NavonSACS)<-c("VP_Codes","APdef","AQ_Score","Gdiff","Ldiff","GminusL")
NavonSACS<-filter(NavonSACS,GminusL<1.2)
NavonSACS<-filter(NavonSACS,Gdiff>0.9)
NavonSACS<-filter(NavonSACS,Ldiff>0.9)
multi.hist(NavonSACS$Gdiff,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(NavonSACS$Ldiff,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(NavonSACS$GminusL,dcol=c("red","blue"),dlty=c("dashed","dotted"))
describeBy(NavonSACS$Gdiff,NavonSACS$APdef)
describeBy(NavonSACS$Ldiff,NavonSACS$APdef)
describeBy(NavonSACS$GminusL,NavonSACS$APdef)
t.test(NavonSACS$GminusL~NavonSACS$APdef)
t.test(NavonSACS$Gdiff~NavonSACS$APdef)
t.test(NavonSACS$Ldiff~NavonSACS$APdef)
histBy(NavonSACS,"Gdiff","APdef")
histBy(NavonSACS,"Ldiff","APdef")
histBy(NavonSACS,"GminusL","APdef")








############# SACS
hist(allresults_Navon$vis_SACS_Gcon)
hist(allresults_Navon$vis_SACS_Ginc)
hist(allresults_Navon$vis_SACS_Lcon)
hist(allresults_Navon$vis_SACS_Linc)
multi.hist(allresults_Navon$vis_SACS_Gcon,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(allresults_Navon$vis_SACS_Ginc,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(allresults_Navon$vis_SACS_Lcon,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(allresults_Navon$vis_SACS_Linc,dcol=c("red","blue"),dlty=c("dashed","dotted"))
histBy(allresults_Navon,"vis_G_con_meanRT","AP.0.RP.1.AP.")
histBy(allresults_Navon,"vis_G_incon_meanRT","AP.0.RP.1.AP.")
histBy(allresults_Navon,"vis_L_con_meanRT","AP.0.RP.1.AP.")
histBy(allresults_Navon,"vis_L_incon_meanRT","AP.0.RP.1.AP.")

plot(GminusL)
multi.hist(Gdiff,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(Ldiff,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(GminusL,dcol=c("red","blue"),dlty=c("dashed","dotted"))
plot(allresults_Navon$vis_L_incon_meanRT,allresults_Navon$vis_L_con_meanRT)
plot(allresults_Navon$vis_G_incon_meanRT,allresults_Navon$vis_G_con_meanRT)

describe(allresults_Navon$vis_G_con_meanRT)
describe(allresults_Navon$vis_G_incon_meanRT)
describe(allresults_Navon$vis_L_con_meanRT)
describe(allresults_Navon$vis_L_incon_meanRT)
describeBy(allresults_Navon$vis_G_con_meanRT,allresults_Navon$AP.0.RP.1.AP.)
describeBy(allresults_Navon$vis_G_incon_meanRT,allresults_Navon$AP.0.RP.1.AP.)
describeBy(allresults_Navon$vis_L_con_meanRT,allresults_Navon$AP.0.RP.1.AP.)
describeBy(allresults_Navon$vis_L_incon_meanRT,allresults_Navon$AP.0.RP.1.AP.)
describeBy(Gdiff,allresults_Navon$AP.0.RP.1.AP.)
describeBy(Ldiff,allresults_Navon$AP.0.RP.1.AP.)
describeBy(NavonSACS$GminusL,NavonSACS$APdef)


################# take relation  (quotient) of G vs L quotients; SACS
Gdiff<-allresults_Navon$vis_SACS_Gcon/allresults_Navon$vis_SACS_Ginc
Ldiff<-allresults_Navon$vis_SACS_Lcon/allresults_Navon$vis_SACS_Linc
GminusL<-Gdiff/Ldiff
NavonSACS<-data.frame(allresults_Navon$VP_Code,allresults_Navon$AP.0.RP.1.AP.,allresults_Navon$AQ_Score,Gdiff,Ldiff,GminusL)
colnames(NavonSACS)<-c("VP_Codes","APdef","AQ_Score","Gdiff","Ldiff","GminusL")
NavonSACS<-filter(NavonSACS,GminusL>-2)
NavonSACS<-filter(NavonSACS,GminusL<2)
NavonSACS<-filter(NavonSACS,Gdiff>-10)
NavonSACS<-filter(NavonSACS,Gdiff<10)
NavonSACS<-filter(NavonSACS,Ldiff>-10)
NavonSACS<-filter(NavonSACS,Ldiff<10)
multi.hist(NavonSACS$Gdiff,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(NavonSACS$Ldiff,dcol=c("red","blue"),dlty=c("dashed","dotted"))
multi.hist(NavonSACS$GminusL,dcol=c("red","blue"),dlty=c("dashed","dotted"))
histBy(NavonSACS,"Gdiff","APdef")
histBy(NavonSACS,"Ldiff","APdef")
histBy(NavonSACS,"GminusL","APdef")
describeBy(NavonSACS$Gdiff,NavonSACS$APdef)
describeBy(NavonSACS$Ldiff,NavonSACS$APdef)
describeBy(NavonSACS$GminusL,NavonSACS$APdef)
t.test(NavonSACS$GminusL~NavonSACS$APdef)
t.test(NavonSACS$Gdiff~NavonSACS$APdef)
t.test(NavonSACS$Ldiff~NavonSACS$APdef)
lm<-lm(NavonSACS$GminusL~NavonSACS$AQ_Score)
summary(lm)
lm<-lm(NavonSACS$Gdiff~NavonSACS$AQ_Score)
summary(lm)
lm<-lm(NavonSACS$Ldiff~NavonSACS$AQ_Score)
summary(lm)
