#filter of psychiatric deseases
filterpsy<-filter(results, psy==0)

#filter only musicians
filterpsymus<-filter(filterpsy,filterpsy$musical_situation==3|filterpsy$musical_situation==4|filterpsy$musical_situation==5|filterpsy$musical_situation==6|filterpsy$musical_situation==7|filterpsy$musical_situation==8)
#filter according to absolute pitch performance
filter5<-filter(results, AP_sums>=7) #filter condition, class must be data.frame!
filter1<-filter(results, AP_sums<12)
filter2<-filter(results, AP_sums>=12)
filter3<-filter(results, AP_sums<16)
filter4<-filter(results, D_Score<=0.3)
filterAP<-filter(results,APdef==1)

#calculate AP_sum-Cutoffs
#insert correct filter variable,
percent=c(0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95)#variable for quantile steps
AP_quantiles<-quantile(filterpsymus[,8],c(0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95))
plot(percent,AP_quantiles)
APsums_freq<-table(AP_sums) # frequencies of APsums, all cases
plot(APsums_freq)
APsums_mus_freq<-table(filterpsymus[,8]) #only musicians
plot(APsums_mus_freq)
APsumspsy_freq<-table(filterpsy[,8]) #demographic exclusions
plot(APsumspsy_freq)
#semitoneerrors
percent=c(0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95)#variable for quantile steps
AP_semquantiles<-quantile(filterpsymus[,9],c(0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95))
plot(percent,AP_semquantiles)
APsemerror_freq<-table(semerror)
plot(APsemerror_freq)
APsem_mus_freq<-table(filterpsymus[,9]) #only musicians
plot(APsem_mus_freq)
APsempsy_freq<-table(filterpsy[,9]) #demographic exclusions
plot(APsempsy_freq)

