GEFT_28_09_18 <- read_csv("Cognition/GEFT_28.09.18.csv")
GEFT_28_09_18[is.na(GEFT_28_09_18)]<-0

vec<-seq(2,36, by=2)

vecRT<-numeric(64)
vecPR<-numeric(64)
for (i in 1:64){
  RT=0
  count=0
  for (j in vec){
    if(GEFT_28_09_18[i,j]==1){
      RT=RT+as.numeric(as.character(GEFT_28_09_18[i,j+1]))
      count=count+1
    }
    else{
      count=count
      RT=RT
    }
    j=j+1
  }
  meanRT=RT/count
  PRcorrect=count/18
  vecRT[i]<-meanRT
  vecPR[i]<-PRcorrect
  i=i+1
}

GEFT<-cbind(GEFT_28_09_18,vecRT,vecPR)

GEFT_PRcorrect<-vecPR
GEFT_meanRT<-vecRT
dat<-cbind(dat,GEFT_meanRT,GEFT_PRcorrect)
