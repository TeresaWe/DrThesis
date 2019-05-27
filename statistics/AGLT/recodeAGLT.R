#script to recode AGLT results, if participant has missunderstood the conditions global/local

z=0
count=0
AGLT_L_recode<-function(AGLTtable_L){
  z=0
  count=0
  AGLTtable_L<-dplyr::filter(AGLTtable_L,congruent %in% c(1,0))
  congruent<-as.numeric(as.character(AGLTtable_L$congruent))
  KeyL.rt<-as.numeric(as.character(AGLTtable_L$KeyL.rt_raw))
  KeyL.corr<-as.numeric(as.character(AGLTtable_L$KeyL.corr_raw))
  for (i in 1:80) {
    if (congruent[i]==0 & KeyL.corr[i]==1){ #change correct to false answer
      KeyL.corr[i]<-0
    }
    if (congruent[i]==0 & KeyL.corr[i]==0){ #change false to correct answer
      KeyL.corr[i]<-1
    }
    i=i+1
  }
}