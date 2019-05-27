##mediation
#betaClustering predicted by MAD trough mediationby AQ?
lm<-lm(`Crand_ T10`~MAD+AQ_Score, data=EO_beta_network )
summary(lm)##beide significant, keine vollstänbdige Mediation

lm<-lm(`Crand_ T10`~MAD, data=EO_beta_network )
summary(lm)
beta_AP=1.576e-04 #prädiktor
t_AP=2.287

lm<-lm(`Crand_ T10`~MAD+AQ_Score, data=EO_beta_network )
summary(lm)
beta_AQ=4.060e-03 #mediator
t_AQ=2.517

SE_AP=beta_AP/t_AP
SE_AQ=beta_AQ/t_AQ
SE_APAQ=sqrt((beta_AP^2 * SE_AQ^2)+(beta_AQ^2 * SE_AP^2)-(SE_AP^2 * SE_AQ^2))
Sobel= (beta_AP*beta_AQ)/SE_APAQ ##n.s.--> keine partielle mediation
#compare to z-value 1.96 ---> Sobel>1.96 --> indirekter Pfad significant!
########################################################################
#MAD predicted by beta Clustering trough mediationby AQ?
lm<-lm(MAD~`Crand_ T10`+AQ_Score, data=EO_beta_network )
summary(lm)##beide significant, keine vollstänbdige Mediation

lm<-lm(MAD~`Crand_ T10`, data=EO_beta_network )
summary(lm)
beta_C=501.19  #prädiktor
t_C=2.287

lm<-lm(MAD~`Crand_ T10`+AQ_Score, data=EO_beta_network )
summary(lm)
beta_AQ=-8.359 #mediator
t_AQ=-3.031

SE_C=beta_C/t_C
SE_AQ=beta_AQ/t_AQ
SE_CAQ=sqrt((beta_C^2 * SE_AQ^2)+(beta_AQ^2 * SE_C^2)-(SE_C^2 * SE_AQ^2))
Sobel= (beta_C*beta_AQ)/SE_CAQ ##n.s.--> keine partielle mediation
#compare to z-value 1.96 ---> Sobel>1.96 --> indirekter Pfad significant!
######################################################################
##mediation
#betaClustering predicted by MAD trough mediationby AQ?
lm<-lm(`Lrand_ T10`~AQ_Score+MAD, data=EC_delta_network) 
summary(lm)##nur AP significant, keine vollstänbdige Mediation

lm<-lm(`Lrand_ T10`~MAD, data=EC_delta_network) 
summary(lm)
beta_AP=-8.881e-05 #prädiktor
t_AP=-2.176

lm<-lm(`Lrand_ T10`~AQ_Score+MAD, data=EC_delta_network) 
summary(lm)
beta_AQ=4.405e-04  #mediator
t_AQ=0.439

SE_AP=beta_AP/t_AP
SE_AQ=beta_AQ/t_AQ
SE_APAQ=sqrt((beta_AP^2 * SE_AQ^2)+(beta_AQ^2 * SE_AP^2)-(SE_AP^2 * SE_AQ^2))
Sobel= (beta_AP*beta_AQ)/SE_APAQ ##n.s.--> keine partielle mediation
#compare to z-value 1.96 ---> Sobel>1.96 --> indirekter Pfad significant!
########################################################################
#MAD predicted by beta Clustering trough mediationby AQ?
lm<-lm(MAD~AQ_Score+`Lrand_ T10`, data=EC_delta_network) 
summary(lm)##beide marginal significant, keine vollstänbdige Mediation

lm<-lm(MAD~`Lrand_ T10`, data=EC_delta_network) 
summary(lm)
beta_AP=-811.2 #prädiktor
t_AP=-2.176

lm<-lm(MAD~AQ_Score+`Lrand_ T10`, data=EC_delta_network) 
summary(lm)
beta_AQ=-5.958  #mediator
t_AQ=-2.104

SE_AP=beta_AP/t_AP
SE_AQ=beta_AQ/t_AQ
SE_APAQ=sqrt((beta_AP^2 * SE_AQ^2)+(beta_AQ^2 * SE_AP^2)-(SE_AP^2 * SE_AQ^2))
Sobel= (beta_AP*beta_AQ)/SE_APAQ ##n.s.--> keine partielle mediation
#compare to z-value 1.96 ---> Sobel>1.96 --> indirekter Pfad significant!