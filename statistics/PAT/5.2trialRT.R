## compare latency minimum and final RT
library(dplyr)

Cognition_final <- read.csv("~/files/Cognition/final_Testauswertung20181212.csv")
VP_Codes<-as.character(Cognition_final$VP_Code)
groups<-Cognition_final$AP.0.RP.1.AP.
VP_list<-data.frame(VP_Codes,groups)

rm(PAT_RI15SON966)
file_list_raw = ls(pattern="^PAT_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
name_lookup<-vector(mode= "character", length=length(file_list_raw))
PAT_trialRT<-get(file_list_raw[[1]])
PAT_trialRT<-PAT_trialRT[,5:7]
for (j in seq_along(file_list_raw)) {
      dev_raw = get(file_list_raw[[j]])
      PAT_trialRT<-bind_cols(PAT_trialRT,select(dev_raw, time)) 
      j=j+1
}
PAT_trialRT<-PAT_trialRT[,4:length(PAT_trialRT)]
