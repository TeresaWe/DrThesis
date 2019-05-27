
#### calculate interesting scores
AP_sums<-sapply(AP_test_correct,sum,na.rm=TRUE) #calculate sum of correct answers per subject
AP_sum_plussem<-sapply(AP_test_plussem,sum,na.rm=TRUE)
AP_sum_pluswholestep<-sapply(AP_test_pluswholestep,sum,na.rm=TRUE)
AP_sum_minsem<-sapply(AP_test_minsem,sum,na.rm=TRUE)
AP_sum_minwholestep<-sapply(AP_test_minwholestep,sum,na.rm=TRUE)
AP_percent<-AP_sums/36*100 #calculate percentage of correct responses
AP_plussem_perc<-AP_sum_plussem/36*100 
AP_pluswholestep_perc<-AP_test_pluswholestep/36*100 
AP_minsem_perc<-AP_sum_minsem/36*100 
AP_minwholestep_perc<-AP_sum_minwholestep/36*100 
AP_poss<-AP_percent[AP_percent>=50] #show AP-posessors (>=50% correct)
AP_vl<-AP_percent[AP_percent>=20] #show maybe AP-posessors (>=20% correct)
underrate1<-AP_minsem_perc[AP_minsem_perc>=20]
underrate2<-AP_minwholestep_perc[AP_minwholestep_perc>=20]
overrate1<-AP_plussem_perc[AP_plussem_perc>=20]
overrate2<-AP_pluswholestep_perc[AP_pluswholestep_perc>=20]

#results<-cbind(AQ_Score, EQ_Score, SQ_Score, AP_sums) # create resultstable

#todo: 
# -error distribution
#- email with feedback
#- build function?
