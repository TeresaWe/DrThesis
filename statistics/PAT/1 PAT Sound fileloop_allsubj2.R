library(tuneR)
library(ggplot2)


file_list_raw = ls(pattern="^soundlist_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
#file_list_raw<-file_list_raw[12]


for (j in seq_along(file_list_raw)) {
  data_list = get(file_list_raw[[j]])
  freq_list<-list()
  print(j)
  subj_name<-file_list_raw[j]
#loop that creates one image per trial and saves frequency- 
#and note-sequence of trial into one list
  for (i in seq_along(data_list)) {
    print(i)
    testwave <- data_list[[i]]
    testwave <- mono(testwave, "both")
    perioWav <- periodogram(testwave, width = 4096)
    freqWav <- FF(perioWav)
    freqWav<-freqWav[-1] #remove artefact frame (1st frame), 
    freqWav<-freqWav[1:(length(freqWav)-1)] #ggf. last also
    noteWav <- noteFromFF(freqWav) 
    count<-numeric(length(freqWav))
    count<-1:length(freqWav) # length(count)/10=seconds 
    data<-data.frame(freqWav,noteWav)
    data<-list(data)
    freq_list<-c(freq_list,data)
  }
  name<-substr(subj_name,11,20)
  name<-paste("freqlist_",name, sep="")
  assign(name,freq_list)
}

rm(list=ls(pattern="^soundlist_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}"))
