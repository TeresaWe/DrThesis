

library(dplyr)
###Functions###
#Mean of congruent Trials, local Block, AGLT (not practice)
z=0
count=0
AGLT_L_con<-function(AGLTtable_L){
  z=0
  count=0
  AGLTtable_L<-dplyr::filter(AGLTtable_L,congruent %in% c(1,0))
  congruent<-as.numeric(as.character(AGLTtable_L$congruent))
  KeyL.rt<-as.numeric(as.character(AGLTtable_L$KeyL.rt_raw))
  KeyL.corr<-as.numeric(as.character(AGLTtable_L$KeyL.corr_raw))
  for (i in 1:80) {
      if (congruent[i]==1 & KeyL.corr[i]==1){ #only congruent and correct trials
        z=z+KeyL.rt[i]
        count=count+1
      }
      else{
        z=z+0
        count=count+0
      }
      i=i+1
  assign("aud_L_con_RT", z, envir=globalenv())
  assign("aud_L_con_corr", count, envir=globalenv())
  assign("aud_L_con_meanRT", aud_L_con_RT/aud_L_con_corr, envir=globalenv())
  }
  return (c(aud_L_con_corr,aud_L_con_meanRT))
}


#Mean of incongruent Trials, local Block, AGLT (not practice)
z=0
count=0
AGLT_L_incon<-function(AGLTtable_L){
  z=0
  count=0
  AGLTtable_L<-dplyr::filter(AGLTtable_L,congruent %in% c(1,0))
  congruent<-as.numeric(as.character(AGLTtable_L$congruent))
  KeyL.rt<-as.numeric(as.character(AGLTtable_L$KeyL.rt_raw))
  KeyL.corr<-as.numeric(as.character(AGLTtable_L$KeyL.corr_raw))
  for (i in 1:80) {
    if (congruent[i]==0 & KeyL.corr[i]==1){ #only incongruent and correct trials
      z=z+KeyL.rt[i]
      count=count+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("aud_L_incon_RT", z, envir=globalenv())
    assign("aud_L_incon_corr", count, envir=globalenv())
    assign("aud_L_incon_meanRT", aud_L_incon_RT/aud_L_incon_corr, envir=globalenv())
  }
  return (c(aud_L_incon_corr,aud_L_incon_meanRT))
}
#Mean of congruent Trials, global Block, AGLT (not practice)

z=0
count=0
AGLT_G_con<-function(AGLTtable_G){
  z=0
  count=0
  AGLTtable_G<-dplyr::filter(AGLTtable_G,congruent %in% c(1,0))
  congruent<-as.numeric(as.character(AGLTtable_G$congruent))
  KeyG.rt<-as.numeric(as.character(AGLTtable_G$keyG.rt_raw))
  KeyG.corr<-as.numeric(as.character(AGLTtable_G$keyG.corr_raw))
  for (i in 1:80) {
    if (congruent[i]==1 & KeyG.corr[i]==1){ #only congruent and correct trials
      z=z+KeyG.rt[i]
      count=count+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("aud_G_con_RT", z, envir=globalenv())
    assign("aud_G_con_corr", count, envir=globalenv())
    assign("aud_G_con_meanRT", aud_G_con_RT/aud_G_con_corr, envir=globalenv())
  }
  return (c(aud_G_con_corr,aud_G_con_meanRT))
}


#Mean of incongruent Trials, global Block, AGLT (not practice)

z=0
count=0
AGLT_G_incon<-function(AGLTtable_G){
  z=0
  count=0
  AGLTtable_G<-dplyr::filter(AGLTtable_G,congruent %in% c(1,0))
  congruent<-as.numeric(as.character(AGLTtable_G$congruent))
  KeyG.rt<-as.numeric(as.character(AGLTtable_G$keyG.rt_raw))
  KeyG.corr<-as.numeric(as.character(AGLTtable_G$keyG.corr_raw))
  for (i in 1:80) {
    if (congruent[i]==0 & KeyG.corr[i]==1){ #only congruent and correct trials
      z=z+KeyG.rt[i]
      count=count+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
    assign("aud_G_incon_RT", z, envir=globalenv())
    assign("aud_G_incon_corr", count, envir=globalenv())
    assign("aud_G_incon_meanRT", aud_G_incon_RT/aud_G_incon_corr, envir=globalenv())
  }
  return (c(aud_G_incon_corr,aud_G_incon_meanRT))
}