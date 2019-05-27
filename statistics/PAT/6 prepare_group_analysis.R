Cognition_final <- read.csv("~/files/Cognition/final_Testauswertung20181212.csv")
VP_Codes<-as.character(Cognition_final$VP_Code)
groups<-Cognition_final$AP.0.RP.1.AP.
VP_list<-data.frame(VP_Codes,groups)

# first load PAT result (.csv) 
source('~/files/PAT/readloopPAT.R')
source('~/files/PAT/APdeviation_loop.R')
source('~/files/PAT/PAT_AR13case.R')
source('~/files/PAT/PAT_RI15SON966case.R')#hat zwei trials weniger
source('~/files/PAT/PAT_measures2.R')
source('~/files/PAT/APtime_loop.R')
rm(dev_PAT_RI15SON966)


minimum_RI12DRE449<-as.data.frame(minimum_RI12DRE449)
minimum_RI12DRE449<-add_row(minimum_RI12DRE449,.before=1)

library(dplyr)
file_list_raw = ls(pattern="^trial_dev_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
file_list_minimum = ls(pattern="^minimum_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
file_list_trials = ls(pattern="^dev_PAT_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
AP_raw<-get(file_list_raw[[1]])
AP_raw<-AP_raw[,1:108]
RP_raw<-get(file_list_raw[[1]])
RP_raw<-RP_raw[,1:108]
AP_PAT<-data.frame()
RP_PAT<-data.frame()
for (j in seq_along(file_list_raw)) {
  print(j)
  data = get(file_list_raw[[j]])
  data=data[,1:108]
  trials=get(file_list_trials[[j]])
  minimum=get(file_list_minimum[[j]])
  finalRT<-PAT_trialRT[,j]
  final_dev<-trials$vec
  target<-trials$target
  if (groups[j]==0){
  RP_raw<-bind_cols(RP_raw,data) 
  all<-data.frame(minimum,final_dev,finalRT,target)
  RP_PAT<-bind_rows(RP_PAT,all) 
  }
  if (groups[j]==1){
  AP_raw<-bind_cols(AP_raw,data) 
  all<-data.frame(minimum,final_dev,finalRT, target)
  AP_PAT<-bind_rows(AP_PAT,all) 
  }
}
AP_raw<-AP_raw[,109:length(AP_raw)]
RP_raw<-RP_raw[,109:length(RP_raw)]