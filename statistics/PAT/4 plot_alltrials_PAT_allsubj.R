#####create data frame
library(stringi)



file_list_raw = ls(pattern="^dev_sounds_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
length(file_list_raw)
#file_list_raw<-file_list_raw[12]
file_list_raw<-file_list_raw[1:55]

#name_lookup<-vector(mode= "character", length=length(file_list_raw))
for (j in seq_along(file_list_raw)) {
        data_list = get(file_list_raw[[j]])
        print(j)
        subj_name<-file_list_raw[j]
        subj_name<-substr(subj_name,12,22)
        ## Compute maximum length
        max.length <- 163
        ## Add NA values to list elements
        trial_dev_sounds <- lapply(data_list, function(v) { c(v, rep(NA, max.length-length(v)))})
        max.length<-numeric(max.length)
        max.length<-1:length(max.length)
        timescale<-max.length*0.09287983
        trial_dev_sounds<-as.data.frame(trial_dev_sounds,max.length)
        abs_trial_dev_sounds<-abs(trial_dev_sounds)
        trial_dev_sounds$mean = apply(abs(trial_dev_sounds),1,mean,na.rm=TRUE)
        trial_dev_sounds$median = apply(abs(trial_dev_sounds),1,median,na.rm=TRUE)
        trial_dev_sounds$sd = apply(abs(trial_dev_sounds),1,sd,na.rm=TRUE)
        trial_dev_sounds$meanplussd<-trial_dev_sounds$mean+trial_dev_sounds$sd
        trial_dev_sounds$meanminussd<-trial_dev_sounds$mean-trial_dev_sounds$sd
        #save new data lists per subjec
        name1<-paste("trial_dev_",subj_name, sep="")
        assign(name1,trial_dev_sounds)
        name2<-paste("abs_trial_dev_",subj_name, sep="")
        assign(name2,abs_trial_dev_sounds)
        ###plot all
        f<-ggplot(trial_dev_sounds, aes(x=timescale,y=vec))
        print(f+geom_smooth(color="red")+
                      geom_smooth(aes(x=timescale, y=vec.1),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.2),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.3),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.4),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.5),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.6),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.7),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.8),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.9),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.10),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.11),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.12),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.13),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.14),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.15),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.16),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.17),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.18),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.19),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.20),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.21),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.22),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.23),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.24),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.25),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.26),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.27),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.28),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.29),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.30),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.31),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.32),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.33),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.34),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.35),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.36),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.37),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.38),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.39),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.40),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.41),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.42),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.43),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.44),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.45),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.46),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.47),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.48),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.49),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.50),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.51),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.52),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.53),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.54),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.55),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.56),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.57),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.58),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.59),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.60),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.61),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.62),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.63),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.64),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.65),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.66),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.67),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.68),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.69),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.70),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.71),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.72),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.73),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.74),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.75),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.76),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.77),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.78),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.79),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.80),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.81),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.82),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.83),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.84),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.85),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.86),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.87),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.88),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.89),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.90),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.91),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.92),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.93),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.94),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.95),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.96),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.97),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.98),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.99),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.100),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.101),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.102),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.103),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.104),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.105),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.106),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.107),color="red")+
                      geom_smooth(aes(x=timescale, y=mean),color="blue")+
                      geom_smooth(aes(x=timescale, y=meanplussd),color="black")+
                      geom_smooth(aes(x=timescale, y=meanminussd),color="black")+
                      
                      
                      coord_cartesian(ylim=c(-1200,1200),xlim=c(0,15))+ 
                      theme(axis.text.x=element_text(color="black", size=18),
                            axis.text.y=element_text(color="black", size=18), 
                            axis.title=element_text(face="bold",size=18),title=element_text(size=16))+
                      labs(x="time in sec", y="deviation to closest target (cent)", title=paste(subj_name)))#C1-C3
        
        ggsave(filename = paste(subj_name,"-PAT.pdf",sep=""), plot = last_plot(),
               path = "~/files/PAT_SingleTrials/graphics")
}
###########################################################
#################################################################################
file_list_raw = ls(pattern="^dev_sounds_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
length(file_list_raw)
file_list_raw<-file_list_raw[57:length(file_list_raw)]
#name_lookup<-vector(mode= "character", length=length(file_list_raw))
#name_lookup<-vector(mode= "character", length=length(file_list_raw))
for (j in seq_along(file_list_raw)) {
        data_list = get(file_list_raw[[j]])
        print(j)
        subj_name<-file_list_raw[j]
        subj_name<-substr(subj_name,12,22)
        ## Compute maximum length
        max.length <- 163
        ## Add NA values to list elements
        trial_dev_sounds <- lapply(data_list, function(v) { c(v, rep(NA, max.length-length(v)))})
        max.length<-numeric(max.length)
        max.length<-1:length(max.length)
        timescale<-max.length*0.09287983
        trial_dev_sounds<-as.data.frame(trial_dev_sounds,max.length)
        abs_trial_dev_sounds<-abs(trial_dev_sounds)
        trial_dev_sounds$mean = apply(abs(trial_dev_sounds),1,mean,na.rm=TRUE)
        trial_dev_sounds$median = apply(abs(trial_dev_sounds),1,median,na.rm=TRUE)
        trial_dev_sounds$sd = apply(abs(trial_dev_sounds),1,sd,na.rm=TRUE)
        trial_dev_sounds$meanplussd<-trial_dev_sounds$mean+trial_dev_sounds$sd
        trial_dev_sounds$meanminussd<-trial_dev_sounds$mean-trial_dev_sounds$sd
        #save new data lists per subjec
        name1<-paste("trial_dev_",subj_name, sep="")
        assign(name1,trial_dev_sounds)
        name2<-paste("abs_trial_dev_",subj_name, sep="")
        assign(name2,abs_trial_dev_sounds)
        ###plot all
        f<-ggplot(trial_dev_sounds, aes(x=timescale,y=vec))
        print(f+geom_smooth(color="red")+
                      geom_smooth(aes(x=timescale, y=vec.1),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.2),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.3),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.4),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.5),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.6),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.7),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.8),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.9),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.10),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.11),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.12),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.13),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.14),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.15),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.16),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.17),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.18),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.19),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.20),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.21),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.22),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.23),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.24),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.25),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.26),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.27),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.28),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.29),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.30),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.31),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.32),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.33),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.34),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.35),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.36),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.37),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.38),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.39),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.40),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.41),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.42),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.43),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.44),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.45),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.46),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.47),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.48),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.49),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.50),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.51),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.52),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.53),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.54),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.55),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.56),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.57),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.58),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.59),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.60),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.61),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.62),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.63),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.64),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.65),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.66),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.67),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.68),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.69),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.70),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.71),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.72),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.73),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.74),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.75),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.76),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.77),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.78),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.79),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.80),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.81),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.82),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.83),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.84),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.85),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.86),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.87),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.88),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.89),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.90),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.91),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.92),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.93),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.94),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.95),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.96),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.97),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.98),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.99),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.100),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.101),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.102),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.103),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.104),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.105),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.106),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.107),color="red")+
                      geom_smooth(aes(x=timescale, y=mean),color="blue")+
                      geom_smooth(aes(x=timescale, y=meanplussd),color="black")+
                      geom_smooth(aes(x=timescale, y=meanminussd),color="black")+
                      
                      
                      coord_cartesian(ylim=c(-1200,1200),xlim=c(0,15))+ 
                      theme(axis.text.x=element_text(color="black", size=18),
                            axis.text.y=element_text(color="black", size=18), 
                            axis.title=element_text(face="bold",size=18),title=element_text(size=18))+
                      labs(x="time in sec", y="deviation to closest target (cent)", title=paste(subj_name)))#C1-C3
        
        ggsave(filename = paste(subj_name,"-PAT.pdf",sep=""), plot = last_plot(),
               path = "~/files/PAT_SingleTrials/graphics")
}
#################################################################################
#has one trial less because no sound for first trial (button press too early)
#################################################################################

file_list_raw = ls(pattern="^dev_sounds_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
file_list_raw<-file_list_raw[56]
#name_lookup<-vector(mode= "character", length=length(file_list_raw))
#name_lookup<-vector(mode= "character", length=length(file_list_raw))
for (j in seq_along(file_list_raw)) {
        data_list = get(file_list_raw[[j]])
        print(j)
        subj_name<-file_list_raw[j]
        subj_name<-substr(subj_name,12,22)
        ## Compute maximum length
        max.length <- 163
        ## Add NA values to list elements
        trial_dev_sounds <- lapply(data_list, function(v) { c(v, rep(NA, max.length-length(v)))})
        max.length<-numeric(max.length)
        max.length<-1:length(max.length)
        timescale<-max.length*0.09287983
        trial_dev_sounds<-as.data.frame(trial_dev_sounds,max.length)
        abs_trial_dev_sounds<-abs(trial_dev_sounds)
        trial_dev_sounds$mean = apply(abs(trial_dev_sounds),1,mean,na.rm=TRUE)
        trial_dev_sounds$median = apply(abs(trial_dev_sounds),1,median,na.rm=TRUE)
        trial_dev_sounds$sd = apply(abs(trial_dev_sounds),1,sd,na.rm=TRUE)
        trial_dev_sounds$meanplussd<-trial_dev_sounds$mean+trial_dev_sounds$sd
        trial_dev_sounds$meanminussd<-trial_dev_sounds$mean-trial_dev_sounds$sd
        #save new data lists per subjec
        name1<-paste("trial_dev_",subj_name, sep="")
        assign(name1,trial_dev_sounds)
        name2<-paste("abs_trial_dev_",subj_name, sep="")
        assign(name2,abs_trial_dev_sounds)
        ###plot all
        f<-ggplot(trial_dev_sounds, aes(x=timescale,y=vec))
        print(f+geom_smooth(color="red")+
                      geom_smooth(aes(x=timescale, y=vec.1),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.2),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.3),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.4),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.5),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.6),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.7),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.8),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.9),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.10),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.11),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.12),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.13),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.14),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.15),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.16),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.17),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.18),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.19),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.20),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.21),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.22),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.23),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.24),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.25),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.26),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.27),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.28),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.29),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.30),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.31),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.32),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.33),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.34),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.35),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.36),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.37),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.38),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.39),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.40),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.41),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.42),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.43),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.44),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.45),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.46),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.47),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.48),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.49),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.50),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.51),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.52),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.53),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.54),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.55),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.56),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.57),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.58),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.59),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.60),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.61),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.62),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.63),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.64),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.65),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.66),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.67),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.68),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.69),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.70),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.71),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.72),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.73),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.74),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.75),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.76),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.77),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.78),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.79),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.80),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.81),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.82),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.83),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.84),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.85),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.86),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.87),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.88),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.89),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.90),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.91),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.92),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.93),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.94),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.95),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.96),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.97),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.98),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.99),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.100),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.101),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.102),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.103),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.104),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.105),color="red")+
                      geom_smooth(aes(x=timescale, y=vec.106),color="red")+
                      geom_smooth(aes(x=timescale, y=mean),color="blue")+
                      geom_smooth(aes(x=timescale, y=meanplussd),color="black")+
                      geom_smooth(aes(x=timescale, y=meanminussd),color="black")+
                      
                      
                      coord_cartesian(ylim=c(-1200,1200),xlim=c(0,15))+ 
                      theme(axis.text.x=element_text(color="black", size=18),
                            axis.text.y=element_text(color="black", size=18), 
                            axis.title=element_text(face="bold",size=18),title=element_text(size=18))+
                      labs(x="time in sec", y="deviation to closest target (cent)", title=paste(subj_name)))#C1-C3
        
        ggsave(filename = paste(subj_name,"-PAT.pdf",sep=""), plot = last_plot(),
               path = "~/files/PAT_SingleTrials/graphics")
}