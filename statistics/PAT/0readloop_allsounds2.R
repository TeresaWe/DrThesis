# first load PAT result (.csv) 
setwd("~/files/PAT_SingleTrials")
sub.folders <- list.files(path=getwd(), pattern="[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}_[0-9]{4}_[A-Za-z]{3}_[0-9]{2}_[0-9]{4}",include.dirs = TRUE)
for (j in sub.folders) {
  path<-paste(getwd(),"/",j,sep="")
  filenames = list.files(path=path,pattern="Absolute Pitch Experiment.csv")
  for (i in filenames) {
    name<-substr(j,1,10)
    name <- gsub("Absolute Pitch Experiment",name,i)# gsub(pattern, replacement, x)
    name <- gsub(".csv","",name)
    name <-gsub("/","_",name)
    name<-paste("PAT_",name, sep="")
    assign(name,read.csv(paste(path,"/",i,sep=""))) #read in the table and name as "name"
  }
}
#rm(PAT_RI15SON966)

#source('~/files/PAT/APdeviation_loop.R')
#source('~/files/PAT/PAT_AR13case.R')
#source('~/files/PAT/PAT_RI15SON966case.R')#hat zwei trials weniger
#source('~/files/PAT/PAT_measures2.R')
#source('~/files/PAT/APtime_loop.R')
#load all *.wav files per subject and save in an individual list "soundlist_*"

setwd("~/files/PAT_SingleTrials")

sub.folders <- list.files(path=getwd(), pattern="[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}_[0-9]{4}_[A-Za-z]{3}_[0-9]{2}_[0-9]{4}",include.dirs = TRUE)
for (j in sub.folders) {
  setwd("~/files/PAT_SingleTrials")
  path<-paste(getwd(),"/",j,sep="")
  print(j)
  #files named 01-99
  file_list_all = list.files(path=path,pattern="*.wav")
  data_list <- vector("list", "length" = length(file_list_all))
  file_list = list.files(path=path,pattern="*-[0-9]{2}.wav")
  for (i in seq_along(file_list)) {
    filename = file_list[[i]]
    # Read data in
    setwd(path)
    df <- tuneR::readWave(filename, from = 1, to = Inf, header = FALSE, toWaveMC = NULL)
    data_list[[i]] <- df
    print(filename)
    i=i+1
  }
  #files named 100-108
  file_list = list.files(path=path,pattern="*-[0-9]{3}.wav")
  for (i in seq_along(file_list)) {
    filename = file_list[[i]]
    # Read data in
    setwd(path)
    df <- tuneR::readWave(filename, from = 1, to = Inf, header = FALSE, toWaveMC = NULL)
    data_list[[99+i]] <- df
    print(filename)
    i=i+1
  }
  name<-substr(j,1,10)
  name<-paste("soundlist_",name, sep="")
  assign(name,data_list) 
  }
