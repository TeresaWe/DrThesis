 


PIT_Score<-function(subject){
#### calculate interesting scores
correct<-sum(AP_test_correct[,subject],na.rm=TRUE) #calculate sum of correct answers per subject
corr_perc<-round(correct/36*100, digits=2) #calculate percentage of correct responses
semitones<-(sum(AP_test_minsem[,subject],na.rm=TRUE))+(sum(AP_test_plussem[,subject],na.rm=TRUE)) #calculate sum of correct answers per subject
semitones_perc<-round(semitones/36*100, digits=2) 
other_errors<-(36-correct-semitones)
othererr_perc<-round(other_errors/36*100, digits=2)
cat("\n", "richtig benannt\t\t", paste(correct), " (",paste(corr_perc)," %)", "\n", 
    "Halbtonfehler\t\t", paste(semitones), " (",paste(semitones_perc)," %)", "\n", 
    "andere Fehler\t\t", paste(other_errors), " (",paste(othererr_perc)," %)", "\n", sep="")
}

    ##### use function:

subject<- VP_Codes=="#string of VP_Code#" # compute index of VP_Code to calculate one subject OR
n<-length(VP_Codes$dupl1_Code) # calculate for every subject, insert n
for(i in 1:n){
  cat(paste(VP_Codes[i,1], "\n"), paste(PIT_Score(i),"\n"), sep="\n\t")
}