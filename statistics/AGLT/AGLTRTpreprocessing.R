#Workspace AGLTRT2607
#new scripts to save raw RT values per subject and trial for all trials in AGLT (incorrect answers --> NA)
AGLT_RT
#matched with allresults to obtain only 64 participants, plus additional variables
allresults<- read_csv("~/files/allresults12.06.csv")
index<-match(x=allresults$VP_Code, table=rownames(AGLT_RT))
resultsindex<-rbind(AGLT_RT[index,])
#cbind tables together
AGLT_RT_allresults<-cbind(allresults,resultsindex) 
#only RT values but only for 64 participants (without additional variables)
AGLT_RTreduced<-resultsindex
AGLT_RTreduced[,1:160]<-(AGLT_RTreduced[,1:160]-0.210) #local RT after 3third tone
AGLT_RTreduced[,161:320]<-(AGLT_RTreduced[,161:320]-0.630) #global RT after first tone
AGLT_RTreduced[AGLT_RTreduced<=0]<-NA #remove all unusual RT (before 2nd tone)
#AGLT_RTreduced[AGLT_RTreduced>2.9]<-NA #one second after last tone ended

hist(AGLT_RTreduced)
hist(AGLT_RTreduced[,1:80])
hist(AGLT_RTreduced[,81:160])
hist(AGLT_RTreduced[,161:240])
hist(AGLT_RTreduced[,241:320])
shapiro.test(AGLT_RTreduced)
for (i in 1:64){
  print(shapiro.test(AGLT_RTreduced[i,]))
  i=i+1
} #Normalverteilung für alle Probanden abgelehnt (except one)
AGLT_RTreduced_t<-t(AGLT_RTreduced)
AGLT_RTreduced_t<-data.frame(AGLT_RTreduced_t)
ggplot(gather(AGLT_RTreduced_t), aes(value)) + 
  geom_histogram(binwidth=0.01)+facet_wrap(~key, scales = 'free_x')

#exclusions
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="LU05KON175") #change back to all if exclusions eeg not needed,#or change to other EEG_results table (eeg. delta)
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="UD20DAV449")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="YL24DRO161")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="RI15SON966")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="AT26IMM177")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="EO11MAR171")#
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="EO11KIC453")#
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="LU05KON175")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="IG26GNE175")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="ER17ARN275")#
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="EI19WOH163")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="HE17KLE175")
allresults_AGLT<-subset(allresults_AGLT, VP_Code!="HR07HER419")

#filter values according to subjects distribution (median and deviation from median), across all conditions
copy<-AGLT_RTreduced
for (i in 1:64){
  abw=0
  count=0
  median<-median(AGLT_RTreduced[i,],na.rm=TRUE)
  print(median)
  for (j in 1:320){
    if (is.na(AGLT_RTreduced[i,j])==TRUE){
      j=j+1
      abw=abw
    }
    else {
    diff<-abs(AGLT_RTreduced[i,j]-median)
    abw=abw+diff
    #print(diff)
    j=j+1
    count=count+1
    }
  }
  MAD=abw/count #mittlere abweichung vom Median
  print(MAD)
  values<-AGLT_RTreduced[i,]
  values[values>(median+2*MAD)]<-NA
  values[values<(median-2*MAD)]<-NA
  AGLT_RTreduced[i,]<-values
  i=i+1
}
AGLT_RTreduced_t<-t(AGLT_RTreduced)
AGLT_RTreduced_t<-data.frame(AGLT_RTreduced_t)
ggplot(gather(AGLT_RTreduced_t), aes(value)) + 
  geom_histogram(binwidth=0.01)+facet_wrap(~key, scales = 'free_x')

#
AGLTmedians<-numeric(4*64)
for (i in 1:64){
  medianL_con<-median(AGLT_RTreduced[i,1:80],na.rm=TRUE)
  medianL_inc<-median(AGLT_RTreduced[i,81:160],na.rm=TRUE)
  medianG_con<-median(AGLT_RTreduced[i,161:240],na.rm=TRUE)
  medianG_inc<-median(AGLT_RTreduced[i,241:320],na.rm=TRUE)
  AGLTmedians[((4*i)-3):(4*i)]<- c(medianL_con,medianL_inc,medianG_con,medianG_inc)
  i=i+1
}
dim(AGLTmedians)<-c(4,64)
colnames(AGLTmedians)<-rownames(AGLT_RTreduced)
rownames(AGLTmedians)<-c("medianL_con","medianL_inc","medianG_con","medianG_inc")
AGLTmedians<-t(AGLTmedians)




plot(allresults_AGLT$medianG_con,allresults_AGLT$medianG_inc)
plot(allresults_AGLT$medianL_con,allresults_AGLT$medianL_inc)
plot(allresults_AGLT$medianG_con,allresults_AGLT$medianL_inc)
plot(allresults_AGLT$medianL_con,allresults_AGLT$medianG_inc)
plot(allresults_AGLT$medianL_inc,allresults_AGLT$medianG_inc)
plot(allresults_AGLT$medianL_con,allresults_AGLT$medianG_con)
plot(AGLT_RTreduced[1,],AGLT_RTreduced[2,])

###calculate counting trials after RT exclusions and deviations from median
MAD_Lcon<-numeric(0)
MAD_Linc<-numeric(0)
MAD_Gcon<-numeric(0)
MAD_Ginc<-numeric(0)
correct_Lcon<-numeric(0)
correct_Linc<-numeric(0)
correct_Gcon<-numeric(0)
correct_Ginc<-numeric(0)
for (i in 1:64){
  abw=0
  count=0
  median<-median(AGLT_RTreduced[i,],na.rm=TRUE)
  print(median)
  for (j in 1:80){
    if (is.na(AGLT_RTreduced[i,j])==TRUE){
      j=j+1
      abw=abw
    }
    else {
      diff<-abs(AGLT_RTreduced[i,j]-median)
      abw=abw+diff
      #print(diff)
      j=j+1
      count=count+1
    }
  }
  MAD_Lcon[i]=abw/count #mittlere abweichung vom Median
  correct_Lcon[i]<-count
  count=0
  abw=0
  for (j in 81:160){
    if (is.na(AGLT_RTreduced[i,j])==TRUE){
      j=j+1
      abw=abw
    }
    else {
      diff<-abs(AGLT_RTreduced[i,j]-median)
      abw=abw+diff
      #print(diff)
      j=j+1
      count=count+1
    }
  }
  MAD_Linc[i]=abw/count #mittlere abweichung vom Median
  correct_Linc[i]<-count
  count=0
  abw=0
  for (j in 161:240){
    if (is.na(AGLT_RTreduced[i,j])==TRUE){
      j=j+1
      abw=abw
    }
    else {
      diff<-abs(AGLT_RTreduced[i,j]-median)
      abw=abw+diff
      #print(diff)
      j=j+1
      count=count+1
    }
  }
  MAD_Gcon[i]=abw/count #mittlere abweichung vom Median
  correct_Gcon[i]<-count
  count=0
  abw=0
  for (j in 241:320){
    if (is.na(AGLT_RTreduced[i,j])==TRUE){
      j=j+1
      abw=abw
    }
    else {
      diff<-abs(AGLT_RTreduced[i,j]-median)
      abw=abw+diff
      #print(diff)
      j=j+1
      count=count+1
    }
  }
  MAD_Ginc[i]=abw/count #mittlere abweichung vom Median
  correct_Ginc[i]<-count
  i=i+1
}
AGLT_medianresults<-data.frame(AGLTmedians,MAD_Lcon,MAD_Linc,MAD_Gcon,MAD_Ginc,
             correct_Lcon,correct_Linc,correct_Gcon,correct_Ginc)

allresults_AGLT<-cbind(allresults, AGLT_medianresults)  

