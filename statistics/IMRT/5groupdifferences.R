library(tidyr)
library(sjstats)
dat_filter_long <- gather(dat_filter, separation, value, d,d_0,d_6,d_12,d_24)
AEFT <- aov(value ~ AP.0.RP.1.AP.*separation + Error(VP_Code/separation), data=dat_filter_long)
summary(AEFT)
eta_sq(AEFT, partial = TRUE, ci.lvl = NULL, n = 1000)
pairwise.t.test(dat_filter_long$value,dat_filter_long$separation)#
#boxplot(value ~ separation* AP.0.RP.1.AP., data=dat_filter_long)

t.test(d~AP.0.RP.1.AP.,data=dat_filter) #tendency
t.test(d_0~AP.0.RP.1.AP.,data=dat_filter) #tendency
t.test(d_6~AP.0.RP.1.AP.,data=dat_filter)
t.test(d_12~AP.0.RP.1.AP.,data=dat_filter)
t.test(d_24~AP.0.RP.1.AP.,data=dat_filter)
library(effsize)
cohen.d(d~AP.0.RP.1.AP.,data=dat_filter) #tendency
cohen.d(d_0~AP.0.RP.1.AP.,data=dat_filter) #tendency
cohen.d(d_6~AP.0.RP.1.AP.,data=dat_filter)
cohen.d(d_12~AP.0.RP.1.AP.,data=dat_filter)
cohen.d(d_24~AP.0.RP.1.AP.,data=dat_filter)

###plot
means_vis<-tapply(X=dat_filter_long$value,
                  INDEX=list(dat_filter_long$separation,
                             dat_filter_long$AP.0.RP.1.AP.),FUN=mean)
sd_vis<-tapply(X=dat_filter_long$value,
               INDEX=list(dat_filter_long$separation,
                          dat_filter_long$AP.0.RP.1.AP.),FUN=sd)
length_xvis<-tapply(X=dat_filter_long$value,
                    INDEX=list(dat_filter_long$separation,
                               dat_filter_long$AP.0.RP.1.AP.),FUN=length)
se_vis<-sd_vis/sqrt(length_xvis) # wrong for subconditions because of wrong N 
dim(means_vis)<-c(10,1)
dim(se_vis)<-c(10,1)
descr_vis<-cbind(means_vis,se_vis)
#rownames(descr_vis)<-c("d_0","d0_0","d6_0","d12_0","d24_0",
#                       "d_1","d0_1","d6_1","d12_1","d24_1")
colnames(descr_vis)<-c("means_vis","se_vis")
descr_vis<-cbind(group=c(1,3,7,9,5,2,4,8,10,6),descr_vis)
descr_vis<-data.frame(descr_vis)
j<-ggplot(descr_vis,aes(x=group,y=means_vis,ymin=means_vis-1.96*se_vis,ymax=means_vis+1.96*se_vis))
j+geom_point(size=3)+geom_errorbar(color=c("blue","blue","blue","blue","blue","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33"),size=0.7, width=0.5)+theme_classic()+ labs(x="Separation by group",
                                                                                                                                                           y= "d'", 
                                                                                                                                                           title="AEFT",subtitle="") +
  coord_cartesian(ylim=c(1,4))+
  xlim(labels=c("d_0","d_1","d0_0","d0_1","d6_0","d6_1","d12_0","d12_1","d24_0","d24_1"))+
  theme(axis.text.x=element_text(color="black", size=16),
        axis.text.y=element_text(color="black", size=16),
        axis.title=element_text(face="bold",size=16),
        title=element_text(size=16),panel.grid.major.y = element_line(colour = "grey"))+
  annotate(geom="text",x=7.5,y=-1.8, label="Means & Confidence Intervals")


###############group differences c

dat_filter_long2 <- gather(dat_filter, separation, value, c,c_0,c_6,c_12,c_24)
AEFT2 <- aov(value ~ AP.0.RP.1.AP.*separation + Error(VP_Code/separation), data=dat_filter_long2)
summary(AEFT2)
eta_sq(AEFT2, partial = TRUE, ci.lvl = NULL, n = 1000)
pairwise.t.test(dat_filter_long2$value,dat_filter_long2$separation)#
#boxplot(value ~ separation* AP.0.RP.1.AP., data=dat_filter_long)

t.test(c~AP.0.RP.1.AP.,data=dat_filter) #tendency
t.test(c_0~AP.0.RP.1.AP.,data=dat_filter) #tendency
t.test(c_6~AP.0.RP.1.AP.,data=dat_filter)
t.test(c_12~AP.0.RP.1.AP.,data=dat_filter)
t.test(c_24~AP.0.RP.1.AP.,data=dat_filter)
library(effsize)
cohen.d(c~AP.0.RP.1.AP.,data=dat_filter) #tendency
cohen.d(c_0~AP.0.RP.1.AP.,data=dat_filter) #tendency
cohen.d(c_6~AP.0.RP.1.AP.,data=dat_filter)
cohen.d(c_12~AP.0.RP.1.AP.,data=dat_filter)
cohen.d(c_24~AP.0.RP.1.AP.,data=dat_filter)

means_vis2<-tapply(X=dat_filter_long2$value,
                  INDEX=list(dat_filter_long2$separation,
                             dat_filter_long2$AP.0.RP.1.AP.),FUN=mean)
sd_vis2<-tapply(X=dat_filter_long2$value,
               INDEX=list(dat_filter_long2$separation,
                          dat_filter_long2$AP.0.RP.1.AP.),FUN=sd)
length_xvis2<-tapply(X=dat_filter_long2$value,
                    INDEX=list(dat_filter_long2$separation,
                               dat_filter_long2$AP.0.RP.1.AP.),FUN=length)
se_vis2<-sd_vis2/sqrt(length_xvis2) # wrong for subconditions because of wrong N 
dim(means_vis2)<-c(10,1)
dim(se_vis2)<-c(10,1)
descr_vis2<-cbind(means_vis2,se_vis2)
#rownames(descr_vis)<-c("d_0","d0_0","d6_0","d12_0","d24_0",
#                       "d_1","d0_1","d6_1","d12_1","d24_1")
colnames(descr_vis2)<-c("means_vis2","se_vis2")
descr_vis2<-cbind(group=c(1,3,7,9,5,2,4,8,10,6),descr_vis2)
descr_vis2<-data.frame(descr_vis2)
j<-ggplot(descr_vis2,aes(x=group,y=means_vis2,ymin=means_vis2-1.96*se_vis2,ymax=means_vis2+1.96*se_vis2))
j+geom_point(size=3)+geom_errorbar(color=c("blue","blue","blue","blue","blue","#00CC33","#00CC33","#00CC33","#00CC33","#00CC33"),size=0.7, width=0.5)+theme_classic()+ labs(x="Separation by group",
                                                                                                                                                                            y= "c", 
                                                                                                                                                                            title="AEFT",subtitle="") +
  coord_cartesian(ylim=c(-1,1))+
  xlim(labels=c("c_0","c_1","c0_0","c0_1","c6_0","c6_1","c12_0","c12_1","c24_0","c24_1"))+
  theme(axis.text.x=element_text(color="black", size=16),
        axis.text.y=element_text(color="black", size=16),
        axis.title=element_text(face="bold",size=16),
        title=element_text(size=16),panel.grid.major.y = element_line(colour = "grey"))+
  annotate(geom="text",x=7.5,y=-1.8, label="Means & Confidence Intervals")

