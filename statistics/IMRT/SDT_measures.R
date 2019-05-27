#script to calculate the SDT measures from AEFTresults table

# d= z(Hits)-z(FA) Sensitivity
# c= -0.5*(z(Hits)+z(FA)) Response Bias

# calculate this for each ST separation condition  and all trials 

library(dplyr)
AEFTresults<-data.frame(AEFTresults)
######### 0 ST ##############

Hits<-AEFTresults[,1]/AEFTresults[,3]
Hits[Hits==1]<-0.9999
Hits[Hits==0]<-0.0001
FA<-(AEFTresults[,15]-AEFTresults[,13])/AEFTresults[,15]
FA[FA==1]<-0.9999
FA[FA==0]<-0.0001
d0=qnorm(Hits)-qnorm(FA)
c0=-0.5*(qnorm(Hits)+qnorm(FA))
rm(Hits,FA)

######### 6 ST ##############

Hits<-AEFTresults[,4]/AEFTresults[,6]
Hits[Hits==1]<-0.9999
Hits[Hits==0]<-0.0001
FA<-(AEFTresults[,18]-AEFTresults[,16])/AEFTresults[,18]
FA[FA==1]<-0.9999
FA[FA==0]<-0.0001
d6=qnorm(Hits)-qnorm(FA)
c6=-0.5*(qnorm(Hits)+qnorm(FA))
rm(Hits,FA)

######### 12 ST ##############

Hits<-AEFTresults[,7]/AEFTresults[,9]
Hits[Hits==1]<-0.9999
Hits[Hits==0]<-0.0001
FA<-(AEFTresults[,21]-AEFTresults[,19])/AEFTresults[,21]
FA[FA==1]<-0.9999
FA[FA==0]<-0.0001
d12=qnorm(Hits)-qnorm(FA)
c12=-0.5*(qnorm(Hits)+qnorm(FA))
rm(Hits,FA)

######### 24 ST ##############

Hits<-AEFTresults[,10]/AEFTresults[,12]
Hits[Hits==1]<-0.9999
Hits[Hits==0]<-0.0001
FA<-(AEFTresults[,24]-AEFTresults[,22])/AEFTresults[,24]
FA[FA==1]<-0.9999
FA[FA==0]<-0.0001
d24=qnorm(Hits)-qnorm(FA)
c24=-0.5*(qnorm(Hits)+qnorm(FA))
rm(Hits,FA)

######### all ###############

Hits<-(AEFTresults[,1]+AEFTresults[,4]+AEFTresults[,7]+AEFTresults[,10])/(AEFTresults[,3]+AEFTresults[,6]+AEFTresults[,9]+AEFTresults[,12])
Hits[Hits==1]<-0.9999
Hits[Hits==0]<-0.0001
N_miss<-AEFTresults[,15]+AEFTresults[,18]+AEFTresults[,21]+AEFTresults[,24]
FA<-(N_miss-(AEFTresults[,13]+AEFTresults[,16]+AEFTresults[,19]+AEFTresults[,22]))/N_miss
FA[FA==1]<-0.9999
FA[FA==0]<-0.0001
d_all=qnorm(Hits)-qnorm(FA)
c_all=-0.5*(qnorm(Hits)+qnorm(FA))
rm(Hits,FA)

AEFT_SDT<-cbind(c_all,c0,c6,c12,c24,d_all,d0,d6,d12,d24)
AEFT_SDT<-data.frame(AEFT_SDT)
colnames(AEFT_SDT)<-c("c_all","c0","c6","c12","c24","d_all","d0","d6","d12","d24")
rownames(AEFT_SDT)<-rownames(AEFTresults)

#ggf

AEFTresults<-cbind(AEFTresults,AEFT_SDT)
