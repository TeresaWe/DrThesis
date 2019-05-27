library(dplyr)

Cognition_final <- read.csv("~/files/Cognition/final_Testauswertung20181212.csv")
VP_Codes<-as.character(Cognition_final$VP_Code)
groups<-Cognition_final$AP.0.RP.1.AP.
VP_list<-data.frame(VP_Codes,groups)

file_list_raw = ls(pattern="^trial_dev_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
AP_medians<-get(file_list_raw[[1]])
AP_medians<-AP_medians[,1:108]
RP_medians<-get(file_list_raw[[1]])
RP_medians<-RP_medians[,1:108]
for (j in seq_along(file_list_raw)) {
  print(j)
  data = get(file_list_raw[[j]])
  if (groups[j]==0){
    RP_medians<-bind_cols(RP_medians,select(data, median)) 
  }
  if (groups[j]==1){
    AP_medians<-bind_cols(AP_medians,select(data, median)) 
  }
}
AP_medians<-AP_medians[,109:length(AP_medians)]
RP_medians<-RP_medians[,109:length(RP_medians)]

#####create data frame
library(stringi)
library(reshape2)


file_list_raw = ls(pattern="^[A-Z]{2}_medians")
length(file_list_raw)
#file_list_raw<-file_list_raw[12]

#name_lookup<-vector(mode= "character", length=length(file_list_raw))
for (j in seq_along(file_list_raw)) {
  data_list = get(file_list_raw[[j]])
  print(j)
  subj_name<-file_list_raw[j]
  subj_name<-substr(subj_name,1,2)
  ## Compute maximum length
  max.length <- 163
  max.length<-numeric(max.length)
  max.length<-1:length(max.length)
  timescale<-max.length*0.09287983
  trial_dev_sounds<-cbind(data_list,timescale)
  trial_dev_sounds<-as.data.frame(trial_dev_sounds)
  trial_dev_sounds$grandmean = apply(trial_dev_sounds,1,mean,na.rm=TRUE)
  trial_dev_sounds$grandmedian = apply(trial_dev_sounds,1,median,na.rm=TRUE)
  trial_dev_sounds$grandsd = apply(trial_dev_sounds,1,sd,na.rm=TRUE)
  trial_dev_sounds$grandmeanplussd<-trial_dev_sounds$grandmean+trial_dev_sounds$grandsd
  trial_dev_sounds$grandmeanminussd<-trial_dev_sounds$grandmean-trial_dev_sounds$grandsd
  melted <- melt(trial_dev_sounds, id.vars = c("timescale", "grandmean", "grandmedian", 
                                               "grandsd","grandmeanplussd","grandmeanminussd"))
  p <- ggplot(data=trial_dev_sounds,aes(x = timescale, y = value))+
    coord_cartesian(ylim=c(0,1200),xlim=c(0,15))+ theme_classic()+
    theme(axis.text.x=element_text(color="black", size=30),
          axis.text.y=element_text(color="black", size=30), 
          axis.title=element_text(face="bold",size=24),title=element_text(size=30))+
    labs(x="time in sec", y="absolute deviation to closest target (cent)", 
         title=paste(subj_name))+#C1-C3)
    scale_y_continuous(breaks=seq(0,1000,200),sec.axis = dup_axis())+
    scale_x_continuous(breaks=seq(0,15,1))+
    geom_smooth(aes(x = timescale, y = value, group=variable,
                  color="red"), data=melted)+
    geom_smooth(aes(x=timescale, y=grandmean),color="blue")+
    geom_smooth(aes(x=timescale, y=grandmedian),color="green")+
    geom_smooth(aes(x=timescale, y=grandmeanplussd),color="black")+
    geom_smooth(aes(x=timescale, y=grandmeanminussd),color="black")
  print(p)
  ggsave(filename = paste(subj_name,"-PATaverage2.jpg",sep=""), plot = last_plot(),
         path = "~/files/PAT_SingleTrials/graphics")
}