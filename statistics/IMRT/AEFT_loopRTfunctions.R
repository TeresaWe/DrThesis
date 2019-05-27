#working directory
setwd("~/files/AEFT")
#packages
library(dplyr)
# first read in ALL .csv tables (local and global)!
# e.g. AR20RED171_AEFT <- read.csv("~/files/AGLT/AR20RED171_AEFT_2017_Jul_05_1408.csv")
##loop over all AGLT result files##



file_list_AEFT<-ls(pattern="[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}_AEFT{1}")
AEFTloop<-function(filelist){
  AEFTresultsRT<-numeric(8*16*length(filelist)) 
  for (i in 1:length(filelist)) {
    tableAEFT<-get(filelist[i])
    ins_0 <- AEFT_ins_0_RT(tableAEFT)
    ins_6 <- AEFT_ins_6_RT(tableAEFT)
    ins_12<-AEFT_ins_12_RT(tableAEFT)
    ins_24<-AEFT_ins_24_RT(tableAEFT)
    miss_0 <- AEFT_miss_0_RT(tableAEFT)
    miss_6 <- AEFT_miss_6_RT(tableAEFT)
    miss_12<-AEFT_miss_12_RT(tableAEFT)
    miss_24<-AEFT_miss_24_RT(tableAEFT)
    AEFTresults[((8*16*i)-(8*16-1)):(8*16*i)]<- c(ins_0,ins_6,ins_12,ins_24,miss_0,miss_6,miss_12,miss_24)
    i=i+1
  }
  dim(AEFTresultsRT)<-c(8*16,length(filelist))
  
  colnames(AEFTresultsRT)<-substr(file_list_AEFT, start=1, stop=10) 
  AEFTresultsRT<-t(AEFTresultsRT)
  #colnames(AEFTresults)<-c("Ins_0_corr", "Ins_0_meanRT","N_Ins_0","Ins_6_corr", "Ins_6_meanRT","N_Ins_6","Ins_12_corr","Ins_12_meanRT","N_Ins_12","Ins_24_corr","Ins_24_meanRT", "N_Ins_24","miss_0_corr","miss_0_meanRT","N_miss_0", "miss_6_corr", "miss_6_meanRT","N_miss_6","miss_12_corr", "miss_12_meanRT","N_miss_12","miss_24_corr", "miss_24_meanRT","N_miss_24")
  assign("AEFTresultsRT", AEFTresultsRT, envir=globalenv())
  return (AEFTresultsRT)
}
AEFTloop(file_list_AEFT)
