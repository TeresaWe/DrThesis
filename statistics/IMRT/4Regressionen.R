#######################
#Z_MAD
######################
AP_dat_filter<-subset(dat_filter,AP.0.RP.1.AP.==1)
RP_dat_filter<-subset(dat_filter,AP.0.RP.1.AP.==0)
MADmeanRP<-mean(RP_dat_filter$MAD)
MADsdRP<-sd(RP_dat_filter$MAD)
dat_filter$Z_MAD<-((dat_filter$MAD-MADmeanRP)/MADsdRP)
#SDfoMmeanRP<-mean(RP_dat_filter$SDfoM)
#SDfoMsdRP<-sd(RP_dat_filter$SDfoM)
#dat_filter$Z_SDfoM<-((dat_filter$SDfoM-SDfoMmeanRP)/SDfoMsdRP)


########################################
#Regressionen Teresa AEFT
########################################
#AMMA korrelliert tw. mit MAD (tonal), und sehr ähnlich zu AEFT; Regressionen 
#nicht signifikant, nur AMA prediktiv (s. YeYoung)--> selbe Analysen mit MSI
######################################

#Allgemein
#1.Modell
reg_d <- lm(d ~ MSI_Score +Z_MAD+ZVT_IQ, data = dat_filter)
reg_d <- lm(d ~ MSI_Score +Z_MAD, data = dat_filter) #weaker
summary(reg_d)
reg_d <- lm(d ~ Z_MAD, data = dat_filter)
summary(reg_d)
reg_d <- lm(d ~ MSI_Score+AP_sums, data = dat_filter)
summary(reg_d)
reg_d <- lm(d ~ AP_sums, data = dat_filter)
summary(reg_d)
# Genauere Betrachtung der Distraktorbedingung
# 2. Modell für d' bei 0 ST

reg_d0 <- lm(d_0 ~ MSI_Score +Z_MAD+ZVT_IQ, data = dat_filter)
reg_d0 <- lm(d_0 ~ MSI_Score +Z_MAD, data = dat_filter)#weaker
summary(reg_d0)

reg_d0 <- lm(d_0 ~ Z_MAD, data = dat_filter)
summary(reg_d0)
reg_d0 <- lm(d_0 ~ AP_sums, data = dat_filter)
summary(reg_d0)

# 3. Modell für d' bei 6 ST

reg_d6 <- lm(d_6 ~ MSI_Score +Z_MAD+ZVT_IQ, data = dat_filter) # not significant
#reg_d6 <- lm(d_6 ~ MSI_Score +MAD, data = dat_filter)
summary(reg_d6)

reg_d6 <- lm(d_6 ~ Z_MAD, data = dat_filter) #significant
summary(reg_d6)
# 4. Modell für d' bei 12 ST

reg_d12 <- lm(d_12 ~ MSI_Score +Z_MAD+ZVT_IQ, data = dat_filter) #significant
#reg_d12 <- lm(d_12 ~ MSI_Score +MAD, data = dat_filter)
summary(reg_d12)

reg_d12 <- lm(d_12 ~ Z_MAD, data = dat_filter) #significant
summary(reg_d12)

# 5. Modell für d' bei 24 ST

reg_d24 <- lm(d_24 ~ MSI_Score +Z_MAD+ZVT_IQ, data = dat_filter) # not significant
#reg_d24 <- lm(d_24 ~ MSI_Score +MAD, data = dat_filter)
summary(reg_d24)

reg_d24 <- lm(d_24 ~ Z_MAD, data = dat_filter) #not significant
summary(reg_d24)

############################################################
#Regressionen GEFT
############################################################

cor.test(dat_filter$d,dat_filter$GEFT_meanRT) # signifikante Korrelation zwschen visuellem und auditivem figure embedding
lm<-lm(d~GEFT_meanRT,data=dat_filter)
summary(lm)
lm_GEFT<-lm(GEFT_meanRT~SPM_T+d,data=dat_filter)
summary(lm_GEFT)
lm_GEFT<-lm(GEFT_meanRT~d,data=dat_filter)
summary(lm_GEFT)

##################################################
#joint modell
#################################################

##no influence of training hours, AQ-Score (auch subscores)
reg_d <- lm(d ~ Z_MAD+MSI_Score+GEFT_meanRT+ZVT_IQ+version, data = dat_filter) 
reg_d <- lm(d ~ MSI_Score +Z_MAD+GEFT_meanRT+version, data = dat_filter) # better but ZVT not significant
summary(reg_d)

reg_d0 <- lm(d_0 ~ Z_MAD+MSI_Score+GEFT_meanRT+ZVT_IQ+version, data = dat_filter) 
reg_d0 <- lm(d_0 ~ MSI_Score +Z_MAD+GEFT_meanRT+version, data = dat_filter)
summary(reg_d0)

reg_d6 <- lm(d_6 ~ Z_MAD+MSI_Score+GEFT_meanRT+ZVT_IQ+version, data = dat_filter) 
reg_d6 <- lm(d_6 ~ Z_MAD+GEFT_meanRT, data = dat_filter) #better
summary(reg_d6)


reg_d12 <- lm(d_12 ~ MSI_Score+Z_MAD+version, data = dat_filter) #better but MSI not significant
summary(reg_d12)

reg_d12 <- lm(d_12 ~ Z_MAD+MSI_Score+GEFT_meanRT+ZVT_IQ+version, data = dat_filter) 
reg_d12 <- lm(d_12 ~ Z_MAD+MSI_Score+version, data = dat_filter) 
reg_d12 <- lm(d_12 ~ Z_MAD+version, data = dat_filter) 
summary(reg_d12)

reg_d24 <- lm(d_24 ~ ZVT_IQ+version+Z_MAD+MSI_Score+GEFT_meanRT, data = dat_filter)
reg_d24 <- lm(d_24 ~ ZVT_IQ+version, data = dat_filter) #marginally significant, no other relations!
summary(reg_d24)


##########################################
#plots
##########################################
###AEFT (d) by MAD,MSI-Score,GEFT_meanRT
ggplot(data=dat_filter,aes(x=Z_MAD, y=d))+
  geom_point(mapping=aes(x=Z_MAD, y=d))+
  geom_abline(aes(intercept=3.03519, slope=-0.18316))+
  geom_point(aes(size=MSI_Score, color=GEFT_meanRT))+theme_classic()+labs(x="MAD",
                                                   y= "d'", 
                                                   title="", 
                                                   subtitle="")+
  coord_cartesian(ylim=c(-1,5.1),xlim=c(-4,2))+scale_y_continuous(breaks = seq(-1, 5.1, by = 1))+
  theme(axis.text.x=element_text(color="black", size=20),
        axis.text.y=element_text(color="black", size=20),
        legend.title=element_text(color="black", size=24,face="bold"),
        legend.text=element_text(color="black", size=24),
        axis.title=element_text(face="bold",size=28),
        title=element_text(size=24),panel.grid.major.y = element_line(colour = "grey"))

###AEFT (d0) by MAD,MSI-Score,GEFTmeanRT
ggplot(data=dat_filter,aes(x=Z_MAD, y=d_0))+
  geom_point(mapping=aes(x=Z_MAD, y=d_0))+
  geom_abline(aes(intercept=1.78675, slope=-0.23370 ))+
  geom_point(aes(size=MSI_Score, color=GEFT_meanRT))+theme_classic()+labs(x="MAD",
                                                                    y= "d0'", 
                                                                    title="", 
                                                                    subtitle="")+
  coord_cartesian(ylim=c(-1,5.1),xlim=c(-4,2))+scale_y_continuous(breaks = seq(-1, 5.1, by = 1))+
  theme(axis.text.x=element_text(color="black", size=20),
        axis.text.y=element_text(color="black", size=20),
        legend.title=element_text(color="black", size=24,face="bold"),
        legend.text=element_text(color="black", size=24),
        axis.title=element_text(face="bold",size=28),
        title=element_text(size=24),panel.grid.major.y = element_line(colour = "grey"))

###AEFT (d6) by MAD,(MSI-Score),GEFTmeanRT
ggplot(data=dat_filter,aes(x=Z_MAD, y=d_6))+
  geom_point(mapping=aes(x=Z_MAD, y=d_6))+
  geom_abline(aes(intercept=2.85429, slope=-0.09730 ))+
  geom_point(aes(size=MSI_Score, color=GEFT_meanRT))+theme_classic()+labs(x="MAD",
                                                                         y= "d6'", 
                                                                         title="", 
                                                                         subtitle="")+
  coord_cartesian(ylim=c(-1,5.1),xlim=c(-4,2))+scale_y_continuous(breaks = seq(-1, 5.1, by = 1))+
  theme(axis.text.x=element_text(color="black", size=20),
        axis.text.y=element_text(color="black", size=20),
        legend.title=element_text(color="black", size=24,face="bold"),
        legend.text=element_text(color="black", size=24),
        axis.title=element_text(face="bold",size=28),
        title=element_text(size=24),panel.grid.major.y = element_line(colour = "grey"))

###AEFT (d12) by MAD,(MSI-Score,GEFTmeanRT)
ggplot(data=dat_filter,aes(x=Z_MAD, y=d_12))+
  geom_point(mapping=aes(x=Z_MAD, y=d_12))+
  geom_abline(aes(intercept=3.33673, slope=-0.08680))+
  geom_point(aes(size=MSI_Score, color=GEFT_meanRT))+theme_classic()+labs(x="MAD",
                                                                         y= "d12'", 
                                                                         title="", 
                                                                         subtitle="")+
  coord_cartesian(ylim=c(-1,5.1),xlim=c(-4,2))+scale_y_continuous(breaks = seq(-1, 5.1, by = 1))+
  theme(axis.text.x=element_text(color="black", size=20),
        axis.text.y=element_text(color="black", size=20),
        legend.title=element_text(color="black", size=24,face="bold"),
        legend.text=element_text(color="black", size=24),
        axis.title=element_text(face="bold",size=28),
        title=element_text(size=24),panel.grid.major.y = element_line(colour = "grey"))

###AEFT (d24) by (MAD,MSI-Score,GEFTmeanRT,) ZVT_IQ
ggplot(data=dat_filter,aes(x=Z_MAD, y=d_24))+
  geom_point(mapping=aes(x=Z_MAD, y=d_24))+
  geom_abline(aes(intercept=3.5355512, slope=-0.0009359))+
  geom_point(aes(size=MSI_Score, color=GEFT_meanRT))+theme_classic()+labs(x="MAD",
                                                                         y= "d24'", 
                                                                         title="", 
                                                                         subtitle="")+
  coord_cartesian(ylim=c(-1,5.1),xlim=c(-4,2))+scale_y_continuous(breaks = seq(-1, 5.1, by = 1))+
  theme(axis.text.x=element_text(color="black", size=20),
        axis.text.y=element_text(color="black", size=20),
        legend.title=element_text(color="black", size=24,face="bold"),
        legend.text=element_text(color="black", size=24),
        axis.title=element_text(face="bold",size=28),
        title=element_text(size=24),panel.grid.major.y = element_line(colour = "grey"))


## AEFT +GEFT
dat_filter$version<-as.numeric(as.character(dat_filter$version))
ggplot(data=dat_filter,aes(x=GEFT_meanRT, y=d))+
  geom_point(mapping=aes(x=GEFT_meanRT, y=d))+
  geom_abline(aes(intercept=4.09624, slope=-0.04179))+geom_point(aes(size=2, color=version))+theme_classic()+labs(x="GEFT (mean RT in s)",
                                                                    y= "d'", 
                                                                    title="",subtitle="")+
  coord_cartesian(ylim=c(0.5,5.1),xlim=c(0,50))+scale_y_continuous(breaks = seq(0.5, 5.1, by = 1))+
  theme(axis.text.x=element_text(color="black", size=24),
        axis.text.y=element_text(color="black", size=24),
        legend.title=element_text(color="black", size=24,face="bold"),
        legend.text=element_text(color="black", size=24),
        axis.title=element_text(face="bold",size=28),
        title=element_text(size=24),panel.grid.major.y = element_line(colour = "grey"))

## AEFT +GEFT
ggplot(data=dat_filter,aes(x=d, y=GEFT_meanRT))+
  geom_point(mapping=aes(x=d, y=GEFT_meanRT))+
  geom_abline(aes(intercept=32.489, slope=-3.954 ))+geom_point(aes(color=SPM_T,size=ZVT_IQ))+theme_classic()+labs(x="d'",
                                                                                                                y= "", 
                                                                                                                title="")+
  coord_cartesian(ylim=c(0,50),xlim=c(0,6))+
  theme(axis.text.x=element_text(color="black", size=24),
        axis.text.y=element_text(color="black", size=24),
        legend.title=element_text(color="black", size=24,face="bold"),
        legend.text=element_text(color="black", size=24),
        axis.title=element_text(face="bold",size=28),
        title=element_text(size=24),panel.grid.major.y = element_line(colour = "grey"))
