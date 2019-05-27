library(ggplot2)

#group statistics

#relation latency and final devation
cor.test(RP_PAT$latency_sec,abs(RP_PAT$final_dev))
cor.test(AP_PAT$latency_sec,abs(AP_PAT$final_dev))

#create full data frame with both groups
AP_PAT<-mutate(AP_PAT, group=rep(1,dim(AP_PAT)[1]))
RP_PAT<-mutate(RP_PAT, group=rep(0,dim(RP_PAT)[1]))
AP_PAT<-rbind(AP_PAT,RP_PAT)

#relation minimum latency and final RT
cor.test(RP_PAT$latency_sec,RP_PAT$finalRT)
cor.test(AP_PAT$latency_sec,AP_PAT$finalRT)
cor.test(all_PAT$latency_sec,all_PAT$finalRT)

#descriptive statistics minimum latency
t.test(all_PAT$latency_sec~all_PAT$group)
medianlatencyAP<-median(AP_PAT$latency_sec,na.rm = TRUE)
hist(AP_PAT$latency_sec)
hist(RP_PAT$latency_sec)
describe(AP_PAT$latency_sec, quant=c(.25,.75))
describe(RP_PAT$latency_sec, quant=c(.25,.75))
medianlatencyRP<-median(RP_PAT$latency_sec,na.rm = TRUE)
rangelatencyAP<-range(AP_PAT$latency_sec,na.rm = TRUE)
rangelatencyRP<-range(RP_PAT$latency_sec,na.rm = TRUE)

#relation minimum deviation and final deviation
t.test((all_PAT$finalRT-all_PAT$latency_sec)~all_PAT$group)
mediantimeAP<-median(AP_PAT$finalRT-AP_PAT$latency_sec,na.rm = TRUE)
mediantimeRP<-median(RP_PAT$finalRT-RP_PAT$latency_sec,na.rm = TRUE)


cor.test(RP_PAT$minimum,abs(RP_PAT$final_dev))
cor.test(AP_PAT$minimum,abs(AP_PAT$final_dev))
cor.test(all_PAT$minimum,abs(all_PAT$final_dev))

cor.test(RP_PAT$min_dev,abs(RP_PAT$final_dev))
cor.test(AP_PAT$min_dev,abs(AP_PAT$final_dev))
cor.test(all_PAT$min_dev,abs(all_PAT$final_dev))

t.test((all_PAT$min_dev-all_PAT$final_dev)~all_PAT$group)
mediandevAP<-median(AP_PAT$min_dev-AP_PAT$final_dev,na.rm = TRUE)
mediandevRP<-median(RP_PAT$min_dev-RP_PAT$final_dev,na.rm = TRUE)

#calculate group differences

#latency
t.test(all_PAT$latency_sec~all_PAT$group)
#final deviation
t.test(abs(all_PAT$final_dev)~all_PAT$group)
#final deviations by target note
PAT_C<-filter(all_PAT,all_PAT$target=="C")
t.test(abs(PAT_C$final_dev)~PAT_C$group)
t.test(PAT_C$final_dev~PAT_C$group)

PAT_Cis<-filter(all_PAT,all_PAT$target=="C# / Db")
t.test(abs(PAT_Cis$final_dev)~PAT_Cis$group)
t.test(PAT_Cis$final_dev~PAT_Cis$group)

PAT_D<-filter(all_PAT,all_PAT$target=="D")
t.test(abs(PAT_D$final_dev)~PAT_D$group)
t.test(PAT_D$final_dev~PAT_D$group)

PAT_Dis<-filter(all_PAT,all_PAT$target=="D# / Eb")
t.test(abs(PAT_Dis$final_dev)~PAT_Dis$group)
t.test(PAT_Dis$final_dev~PAT_Dis$group)

PAT_E<-filter(all_PAT,all_PAT$target=="E")
t.test(abs(PAT_E$final_dev)~PAT_E$group)
t.test(PAT_E$final_dev~PAT_E$group)

PAT_F<-filter(all_PAT,all_PAT$target=="F")
t.test(abs(PAT_F$final_dev)~PAT_F$group)
t.test(PAT_F$final_dev~PAT_F$group)

PAT_Fis<-filter(all_PAT,all_PAT$target=="F# / Gb")
t.test(abs(PAT_Fis$final_dev)~PAT_Fis$group)
t.test(PAT_Fis$final_dev~PAT_Fis$group)

PAT_G<-filter(all_PAT,all_PAT$target=="G")
t.test(abs(PAT_G$final_dev)~PAT_G$group)
t.test(PAT_G$final_dev~PAT_G$group)

PAT_Gis<-filter(all_PAT,all_PAT$target=="G# / Ab")
t.test(abs(PAT_Gis$final_dev)~PAT_Gis$group)
t.test(PAT_Gis$final_dev~PAT_Gis$group)

PAT_A<-filter(all_PAT,all_PAT$target=="A")
t.test(abs(PAT_A$final_dev)~PAT_A$group)
t.test(PAT_A$final_dev~PAT_A$group)

PAT_Ais<-filter(all_PAT,all_PAT$target=="A# / B")
t.test(abs(PAT_Ais$final_dev)~PAT_Ais$group)
t.test(PAT_Ais$final_dev~PAT_Ais$group)

PAT_H<-filter(all_PAT,all_PAT$target=="H")
t.test(abs(PAT_H$final_dev)~PAT_H$group)
t.test(PAT_H$final_dev~PAT_H$group)

aov_target <- aov(final_dev ~ group*target, data=all_PAT)
summary(aov_target)
aov_latency <- aov(latency_sec ~ group*target, data=all_PAT)
summary(aov_latency)
pairwise.t.test(all_PAT$final_dev,all_PAT$target)
pairwise.t.test(all_PAT$latency_sec,all_PAT$target)

###plot final deviation
#plot error bars
means_PAT<-tapply(X=abs(all_PAT$final_dev),
                  INDEX=list(all_PAT$target,
                             all_PAT$group),FUN=mean,na.rm=TRUE)
sd_PAT<-tapply(X=abs(all_PAT$final_dev),
               INDEX=list(all_PAT$target,
                          all_PAT$group),FUN=sd,na.rm=TRUE)
length_xPAT<-tapply(X=all_PAT$final_dev,
                    INDEX=list(all_PAT$target,
                               all_PAT$group),FUN=length)
se_PAT<-sd_PAT/sqrt(length_xPAT)
se_PAT<-se_PAT[1:12,]
dim(se_PAT)<-c(24,1)
means_PAT<-means_PAT[1:12,]
dim(means_PAT)<-c(24,1)
descr_PAT<-cbind(group= c(1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12),means_PAT,se_PAT)
#descr_PAT<-cbind(descr_PAT,congruency=c("con","inc","con","inc","con","inc","con","inc"),pitch=c("RP","RP","RP","RP","AP","AP","AP","AP"),focus=c("G","G","L","L","G","G","L","L"),stringsAsFactors=FALSE)
rownames(descr_PAT)<-c("A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H")
colnames(descr_PAT)<-c("group","means_PAT", "se_PAT")
descr_PAT<-data.frame(descr_PAT)
j<-ggplot(descr_PAT,aes(x=group,y=means_PAT,ymin=means_PAT-1.96*se_PAT,ymax=means_PAT+1.96*se_PAT))
j+geom_point(size=3)+geom_errorbar(color=c("#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33",
                        "blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"),size=0.7, width=0.5)+theme_classic()+ labs(x="target note",
                                                                                                            y= "absolute deviation to closest target (cent)", 
                                                                                  title="",subtitle="")+ #AP blue, RP green
  coord_cartesian(ylim=c(0,400))+
  xlim(labels=c("A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H"))+
  theme(axis.text.x=element_text(color="black", size=18),
        axis.text.y=element_text(color="black", size=18),
        axis.title=element_text(face="bold",size=18),
        title=element_text(size=18),panel.grid.major.y = element_line(colour = "grey"))+
  #annotate(geom="text",x=7.5,y=-1.8, label="Means & Confidence Intervals")

ggsave(filename = "PAT-deviation.pdf", plot = last_plot(),
       path = "~/files/PAT_SingleTrials/graphics")

## plot latency

means_PAT<-tapply(X=all_PAT$latency_sec,
                  INDEX=list(all_PAT$target,
                             all_PAT$group),FUN=mean,na.rm=TRUE)
sd_PAT<-tapply(X=all_PAT$latency_sec,
               INDEX=list(all_PAT$target,
                          all_PAT$group),FUN=sd,na.rm=TRUE)
length_xPAT<-tapply(X=all_PAT$latency_sec,
                    INDEX=list(all_PAT$target,
                               all_PAT$group),FUN=length)
se_PAT<-sd_PAT/sqrt(length_xPAT)
se_PAT<-se_PAT[1:12,]
dim(se_PAT)<-c(24,1)
means_PAT<-means_PAT[1:12,]
dim(means_PAT)<-c(24,1)
descr_PAT<-cbind(group= c(1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12),means_PAT,se_PAT)
#descr_PAT<-cbind(descr_PAT,congruency=c("con","inc","con","inc","con","inc","con","inc"),pitch=c("RP","RP","RP","RP","AP","AP","AP","AP"),focus=c("G","G","L","L","G","G","L","L"),stringsAsFactors=FALSE)
rownames(descr_PAT)<-c("A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H")
colnames(descr_PAT)<-c("group","means_PAT", "se_PAT")
descr_PAT<-data.frame(descr_PAT)
j<-ggplot(descr_PAT,aes(x=group,y=means_PAT,ymin=means_PAT-1.96*se_PAT,ymax=means_PAT+1.96*se_PAT))
j+geom_point(size=3)+geom_errorbar(color=c("#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33",
                                           "blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"),size=0.7, width=0.5)+theme_classic()+ labs(x="target note",
                                                                                                                                                                           y= "latency (s) of first minimum deviation", 
                                                                                                                                                                           title="",subtitle="")+
  coord_cartesian(ylim=c(3,8))+
  xlim(labels=c("A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H"))+
  theme(axis.text.x=element_text(color="black", size=18),
        axis.text.y=element_text(color="black", size=18),
        axis.title=element_text(face="bold",size=18),
        title=element_text(size=18),panel.grid.major.y = element_line(colour = "grey"))+
  #annotate(geom="text",x=7.5,y=-1.8, label="Means & Confidence Intervals")


ggsave(filename = "PAT-latency.pdf", plot = last_plot(),
       path = "~/files/PAT_SingleTrials/graphics")

## plot Ap difference minimum- final
means_minimum<-tapply(X=abs(AP_PAT$minimum),
                  INDEX=list(AP_PAT$target),FUN=mean,na.rm=TRUE)
sd_minimum<-tapply(X=abs(AP_PAT$minimum),
               INDEX=list(AP_PAT$target),FUN=sd,na.rm=TRUE)
length_xminimum<-tapply(X=AP_PAT$minimum,
                    INDEX=list(AP_PAT$target),FUN=length)
means_final<-tapply(X=abs(AP_PAT$final_dev),
                      INDEX=list(AP_PAT$target),FUN=mean,na.rm=TRUE)
sd_final<-tapply(X=abs(AP_PAT$final_dev),
                   INDEX=list(AP_PAT$target),FUN=sd,na.rm=TRUE)
length_xfinal<-tapply(X=AP_PAT$final_dev,
                        INDEX=list(AP_PAT$target),FUN=length)
se_minimum<-sd_minimum/sqrt(length_xminimum)
dim(se_minimum)<-c(12,1)
se_final<-sd_final/sqrt(length_xfinal)
dim(se_final)<-c(12,1)
se_descr<-rbind(se_minimum,se_final)
dim(means_minimum)<-c(12,1)
dim(means_final)<-c(12,1)
means_descr<-rbind(means_minimum,means_final)
descr_PAT<-cbind(means_descr,se_descr)

descr_PAT<-cbind(group= c(1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12),descr_PAT)
#descr_PAT<-cbind(descr_PAT,congruency=c("con","inc","con","inc","con","inc","con","inc"),pitch=c("RP","RP","RP","RP","AP","AP","AP","AP"),focus=c("G","G","L","L","G","G","L","L"),stringsAsFactors=FALSE)
rownames(descr_PAT)<-c("A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H")
colnames(descr_PAT)<-c("group","means_PAT", "se_PAT")
descr_PAT<-data.frame(descr_PAT)
j<-ggplot(descr_PAT,aes(x=group,y=means_PAT,ymin=means_PAT-1.96*se_PAT,ymax=means_PAT+1.96*se_PAT))
j+geom_point(size=3)+geom_errorbar(color=c("#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33",
                                           "blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"),size=0.7, width=0.5)+theme_classic()+ labs(x="target note",
                                                                                                                                                                           y= "minimum deviation - final deviation", 
                                                                                                                                                                           title="PAT final adjustment (AP)",subtitle="minimum=green vs. final=blue")+
  coord_cartesian(ylim=c(0,100))+
  xlim(labels=c("A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H"))+
  theme(axis.text.x=element_text(color="black", size=18),
        axis.text.y=element_text(color="black", size=18),
        axis.title=element_text(face="bold",size=18),
        title=element_text(size=18),panel.grid.major.y = element_line(colour = "grey"))+
  #annotate(geom="text",x=10,y=10, label="Means & Confidence Intervals")


ggsave(filename = "AP-finaladjustment.pdf", plot = last_plot(),
       path = "~/files/PAT_SingleTrials/graphics")

## plot RP difference minimum- final
means_minimum<-tapply(X=abs(RP_PAT$minimum),
                      INDEX=list(RP_PAT$target),FUN=mean,na.rm=TRUE)
sd_minimum<-tapply(X=abs(RP_PAT$minimum),
                   INDEX=list(RP_PAT$target),FUN=sd,na.rm=TRUE)
length_xminimum<-tapply(X=RP_PAT$minimum,
                        INDEX=list(RP_PAT$target),FUN=length)
means_final<-tapply(X=abs(RP_PAT$final_dev),
                    INDEX=list(RP_PAT$target),FUN=mean,na.rm=TRUE)
sd_final<-tapply(X=abs(RP_PAT$final_dev),
                 INDEX=list(RP_PAT$target),FUN=sd,na.rm=TRUE)
length_xfinal<-tapply(X=RP_PAT$final_dev,
                      INDEX=list(RP_PAT$target),FUN=length)
se_minimum<-sd_minimum/sqrt(length_xminimum)
se_minimum<-se_minimum[1:12]
dim(se_minimum)<-c(12,1)
se_final<-sd_final/sqrt(length_xfinal)
se_final<-se_final[1:12]
dim(se_final)<-c(12,1)
se_descr<-rbind(se_minimum,se_final)
means_minimum<-means_minimum[1:12]
dim(means_minimum)<-c(12,1)
means_final<-means_final[1:12]
dim(means_final)<-c(12,1)
means_descr<-rbind(means_minimum,means_final)
descr_PAT<-cbind(means_descr, se_descr)

descr_PAT<-cbind(group= c(1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12),descr_PAT)
#descr_PAT<-cbind(descr_PAT,congruency=c("con","inc","con","inc","con","inc","con","inc"),pitch=c("RP","RP","RP","RP","AP","AP","AP","AP"),focus=c("G","G","L","L","G","G","L","L"),stringsAsFactors=FALSE)
rownames(descr_PAT)<-c("A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                       "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H")
colnames(descr_PAT)<-c("group","means_PAT", "se_PAT")
descr_PAT<-data.frame(descr_PAT)
j<-ggplot(descr_PAT,aes(x=group,y=means_PAT,ymin=means_PAT-1.96*se_PAT,ymax=means_PAT+1.96*se_PAT))
j+geom_point(size=3)+geom_errorbar(color=c("#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33",
                                           "blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"),size=0.7, width=0.5)+theme_classic()+ labs(x="target note",
                                                                                                                                                                           y= "minimum deviation - final deviation", 
                                                                                                                                                                           title="PAT final adjustment (RP)",subtitle="minimum=green vs. final=blue")+
  coord_cartesian(ylim=c(0,500))+
  xlim(labels=c("A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As", "H","A","Ais/B","C","Cis/Db",
                "D","Dis/Eb","E","F","Fis/Gb","G", "Gis/As","H"))+
  theme(axis.text.x=element_text(color="black", size=18),
        axis.text.y=element_text(color="black", size=18),
        axis.title=element_text(face="bold",size=18),
        title=element_text(size=18),panel.grid.major.y = element_line(colour = "grey"))+
  #annotate(geom="text",x=10,y=450, label="Means & Confidence Intervals")


ggsave(filename = "RP-finaladjustment.pdf", plot = last_plot(),
       path = "~/files/PAT_SingleTrials/graphics")

