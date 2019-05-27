#####create data frame
library(stringi)
library(reshape2)


file_list_raw = ls(pattern="^[A-Z]{2}_raw")
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
        abs_trial_dev_sounds<-abs(trial_dev_sounds)
        trial_dev_sounds$mean = apply(abs_trial_dev_sounds,1,median,na.rm=TRUE)
        trial_dev_sounds$sd = apply(abs_trial_dev_sounds,1,sd,na.rm=TRUE)
        trial_dev_sounds$meanplussd<-trial_dev_sounds$mean+trial_dev_sounds$sd
        trial_dev_sounds$meanminussd<-trial_dev_sounds$mean-trial_dev_sounds$sd
        #save new data lists per subjec
        name1<-paste("allPATtrials_",subj_name, sep="")
        assign(name1,trial_dev_sounds)
        name2<-paste("abs_allPATtrials_",subj_name, sep="")
        assign(name2,abs_trial_dev_sounds)
        melted <- melt(trial_dev_sounds, id.vars = c("timescale","mean", "meanplussd", "meanminussd"))
        p <- ggplot(data=trial_dev_sounds,aes(x = timescale, y = value))+
                coord_cartesian(ylim=c(-1200,1200),xlim=c(0,15))+ 
                theme(axis.text.x=element_text(color="black", size=18),
                      axis.text.y=element_text(color="black", size=18), 
                      axis.title=element_text(face="bold",size=18),title=element_text(size=18))+
                labs(x="time in sec", y="deviation to closest target (cent)", 
                     title=paste(subj_name))+#C1-C3)
                scale_y_continuous(breaks=seq(-1000,1000,200),sec.axis = dup_axis())+
                scale_x_continuous(breaks=seq(0,15,1))+
        geom_line(aes(x = timescale, y = value, group=variable,
                        color="red"), data=melted)+
                geom_smooth(aes(x=timescale, y=mean),color="blue")+
                geom_smooth(aes(x=timescale, y=meanplussd),color="black")+
                geom_smooth(aes(x=timescale, y=meanminussd),color="black")
        print(p)
        ggsave(filename = paste(subj_name,"-PAT.pdf",sep=""), plot = last_plot(),
               path = "~/files/PAT_SingleTrials/graphics")
}