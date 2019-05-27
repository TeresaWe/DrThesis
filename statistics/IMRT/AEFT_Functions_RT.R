
library(dplyr)
###Functions###

##Inside
#Mean of Melodies, inside, 0ST separated
z=0
count=0
AEFT_ins_0_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="True_0"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="True_0"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("Ins_0_RT", z, envir=globalenv())
    assign("Ins_0_corr", count, envir=globalenv())
    assign("Ins_0_meanRT", Ins_0_RT/Ins_0_corr, envir=globalenv())
    assign("N_Ins_0", trial,envir=globalenv())
  }
  return (c(Ins_0_RT))
}


#Mean of Melodies, inside, 6ST separated
z=0
count=0
AEFT_ins_6_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="True_6"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="True_6"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("Ins_6_RT", z, envir=globalenv())
    assign("Ins_6_corr", count, envir=globalenv())
    assign("Ins_6_meanRT", Ins_6_RT/Ins_6_corr, envir=globalenv())
    assign("N_Ins_6", trial,envir=globalenv())
  }
  return (c(Ins_6_RT))
}


#Mean of Melodies, inside, 12ST separated
z=0
count=0
AEFT_ins_12_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="True_12"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="True_12"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("Ins_12_RT", z, envir=globalenv())
    assign("Ins_12_corr", count, envir=globalenv())
    assign("Ins_12_meanRT", Ins_12_RT/Ins_12_corr, envir=globalenv())
    assign("N_Ins_12", trial,envir=globalenv())
  }
  return (c(Ins_12_RT))
}


#Mean of Melodies, inside, 24ST separated

z=0
count=0
AEFT_ins_24_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="True_24"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="True_24"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("Ins_24_RT", z, envir=globalenv())
    assign("Ins_24_corr", count, envir=globalenv())
    assign("Ins_24_meanRT", Ins_24_RT/Ins_24_corr, envir=globalenv())
    assign("N_Ins_24", trial,envir=globalenv())
  }
  return (c(Ins_24_RT))
}




## NOT Inside
#Mean of Melodies, imissing, 0ST separated
z=0
count=0
AEFT_miss_0_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="False_0"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="False_0"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("miss_0_RT", z, envir=globalenv())
    assign("miss_0_corr", count, envir=globalenv())
    assign("miss_0_meanRT", miss_0_RT/miss_0_corr, envir=globalenv())
    assign("N_miss_0", trial,envir=globalenv())
  }
  return (c(miss_0_RT))
}


#Mean of Melodies, missing, 6ST separated
z=0
count=0
AEFT_miss_6_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="False_6"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="False_6"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("miss_6_RT", z, envir=globalenv())
    assign("miss_6_corr", count, envir=globalenv())
    assign("miss_6_meanRT", miss_6_RT/miss_6_corr, envir=globalenv())
    assign("N_miss_6", trial,envir=globalenv())
  }
  return (c(miss_6_RT))
}


#Mean of Melodies, missing, 12ST separated
z=0
count=0
AEFT_miss_12_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="False_12"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="False_12"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("miss_12_RT", z, envir=globalenv())
    assign("miss_12_corr", count, envir=globalenv())
    assign("miss_12_meanRT", miss_12_RT/miss_12_corr, envir=globalenv())
    assign("N_miss_12", trial,envir=globalenv())
  }
  return (c(miss_12_RT))
}


#Mean of Melodies, missing, 24ST separated

z=0
count=0
AEFT_miss_24_RT<-function(AEFTtable){
  z=numeric()
  count=0
  trial=0
  Keyrt<-as.numeric(as.character(AEFTtable$time))
  Keycorr<-as.numeric(as.character(AEFTtable$correct.answer.))
  cond<-as.character(AEFTtable$cond)
  for (i in 17:144) {#skip practice trials
    if (Keycorr[i]==1 & cond[i]=="False_24"){ #only congruent and correct trials
      count=count+1
      z[count]=Keyrt[i]
      trial=trial+1
    }
    if (Keycorr[i]==0 & cond[i]=="False_24"){ #only congruent and correct trials
      count=count+0
      trial=trial+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("miss_24_RT", z, envir=globalenv())
    assign("miss_24_corr", count, envir=globalenv())
    assign("miss_24_meanRT", miss_24_RT/miss_24_corr, envir=globalenv())
    assign("N_miss_24", trial,envir=globalenv())
  }
  return (c(miss_24_RT))
}

