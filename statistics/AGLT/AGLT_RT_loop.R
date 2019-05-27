#working directory
setwd("~/files/AGLT")
#packages
library(dplyr)
# first read in ALL .csv tables (local and global)!
# e.g. AR20RED171_AGLT <- read.csv("~/files/AGLT/AR20RED171_AGLT_2017_Jul_05_1408.csv")
##loop over all AGLT result files##

file_list_AGLTlocal<-ls(pattern="[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}_AGLT{1}_local{1}")
file_list_AGLTglobal<-ls(pattern="[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}_AGLT{1}_global{1}")
#AGLTresults<-numeric(8*length(file_list_AGLTlocal))

#file_list_AGLTlocal<-ls(pattern="[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}_AGLT{1}_local{1}")
fileloop<-function(local, global){
  AGLT_RT<-numeric(length(local)) 
  for (i in 1:length(local)) {
    tablelocal<-get(local[i])
    tableglobal<-get(global[i])
    L_con<- AGLT_L_conRT(tablelocal)
    L_incon<-AGLT_L_inconRT(tablelocal)
    G_con<-AGLT_G_conRT(tableglobal)
    G_incon<-AGLT_G_inconRT(tableglobal)
    AGLT_RT[((320*i)-319):(320*i)]<- c(L_con,L_incon,G_con,G_incon)
    i=i+1
  }
  dim(AGLT_RT)<-c(320,length(local))
  #rownames(AGLT_RT)<-c("aud_L_con_corr", "aud_L_con_meanRT",
  #                         "aud_L_incon_corr", "aud_L_incon_meanRT","aud_G_con_corr", 
   #                       "aud_G_con_meanRT","aud_G_incon_corr", "aud_G_incon_meanRT")
  colnames(AGLT_RT)<-substr(file_list_AGLTglobal, start=1, stop=10) 
  AGLT_RT<-t(AGLT_RT)
  assign("AGLT_RT", AGLT_RT, envir=globalenv())
  return (AGLT_RT)
}
fileloop(file_list_AGLTlocal, file_list_AGLTglobal)
