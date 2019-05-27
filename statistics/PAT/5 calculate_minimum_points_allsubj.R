####
#sample rate: 44100
#window periodogramm: 4096
#number of frequency/deviation values per second: 44100/4096=10.7666 
#total time points: 15s*10.7666 ~161-163 (depending on real length of wave file 15.0-5.1)
#milliseconds per point: 1000/10.7666 = 92.87983
#seconds per point: 1/10.7666=0.09287983

file_list_raw = ls(pattern="^abs_trial_dev_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
file_list_raw2 = ls(pattern="^trial_dev_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
for (j in seq_along(file_list_raw)) {
  data = get(file_list_raw[[j]])
  data2 = get(file_list_raw2[[j]])
  subj_name<-file_list_raw[j]
  length_trials <- sapply(data, length)
  #find minimum value for each trial
  minimum<-apply(t(data),1,min,na.rm=TRUE)
  #find indices for minimums
  position<-numeric(length(minimum))
  latency_sec<-numeric(length(minimum))
  min_dev<-numeric(length(minimum))
  for (i in 1:length(minimum)) {
    index<-which(data[,i]==minimum[i])
    position[i]<-index[1] #only first closest value
    min_dev[i]<-data2[index[1],i]
    latency_sec[i]<-position[i]*0.09287983
    i=i+1
  }
  #create trial index vector
  trial_number<-numeric(length(minimum))
  trial_number<-1:length(minimum)
  
  #bind into table
  table<-cbind(trial_number,minimum,position,min_dev,latency_sec)
  name<-substr(subj_name,15,25)
  name<-paste("minimum_",name, sep="")
  assign(name,table)
}
  

