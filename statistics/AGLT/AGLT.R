######only works if global is firt, local is second!!########

#Mean of congruent Trials, local Block, AGLT (not practice)

z=0
count=0
for (i in 104:184) {
  if (i==144){ # to skip Na lines (breaks between blocks)
    i=i+1
  }
  else {
    congruent<-NG12KLO159_AEFT170425_2017_Jun_19_0912$congruent
    KeyL.rt<-NG12KLO159_AEFT170425_2017_Jun_19_0912$KeyL.rt
    KeyL.corr<-NG12KLO159_AEFT170425_2017_Jun_19_0912$KeyL.corr
    if (congruent[i]==1 & KeyL.corr[i]==1){ #only congruent and correct trials
      z=z+KeyL.rt[i]
      count=count+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
  }
}
print(z/count)
print(count)


#Mean of incongruent Trials, local Block, AGLT (not practice)

z=0
count=0
for (i in 104:184) {
  if (i==144){ # to skip Na lines (breaks between blocks)
    i=i+1
  }
  else {
    congruent<-NG12KLO159_AEFT170425_2017_Jun_19_0912$congruent
    KeyL.rt<-NG12KLO159_AEFT170425_2017_Jun_19_0912$KeyL.rt
    KeyL.corr<-NG12KLO159_AEFT170425_2017_Jun_19_0912$KeyL.corr
    if (congruent[i]==0 & KeyL.corr[i]==1){ #only congruent and correct trials
      z=z+KeyL.rt[i]
      count=count+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
  }
}
print(z/count)
print(count)

#Mean of congruent Trials, global Block, AGLT (not practice)

z=0
count=0
for (i in 5:93) {
  if (i==53){ # to skip Na lines (breaks between blocks)
    i=i+1
  }
  else {
    congruent<-NG12KLO159_AEFT170425_2017_Jun_19_0912$congruent
    keyG.rt<-NG12KLO159_AEFT170425_2017_Jun_19_0912$keyG.rt
    keyG.corr<-NG12KLO159_AEFT170425_2017_Jun_19_0912$keyG.corr
    if (congruent[i]==1 & keyG.corr[i]==1){ #only congruent and correct trials
      z=z+keyG.rt[i]
      count=count+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
  }
}
print(z/count)
print(count)


#Mean of incongruent Trials, global Block, AGLT (not practice)

z=0
count=0
for (i in 5:93) {
  if (i==53){ # to skip Na lines (breaks between blocks)
    i=i+1
  }
  else {
    congruent<-NG12KLO159_AEFT170425_2017_Jun_19_0912$congruent
    keyG.rt<-NG12KLO159_AEFT170425_2017_Jun_19_0912$keyG.rt
    keyG.corr<-NG12KLO159_AEFT170425_2017_Jun_19_0912$keyG.corr
    if (congruent[i]==0 & keyG.corr[i]==1){ #only congruent and correct trials
      z=z+keyG.rt[i]
      count=count+1
    }
    else{
      z=z+0
      count=count+0
    }
    i=i+1
  }
}
print(z/count)
print(count)