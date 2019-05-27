#5 cases excludd!
###################################################

describe(GEFT_meanRT)
21.43+2*13.14
dat$exclude_GEFT<-NA
dat$exclude_GEFT[dat$GEFT_meanRT>50]<-1 #2 cases
dat$exclude_GEFT[dat$GEFT_meanRT<=50]<-0
dat_filter<-dplyr::filter(dat,dat$exclude_GEFT==0)

####
#AEFT exlcusions
#case 21?, gekfft vor 2. Termin, Ausreißer bei AEFT
dat_filter[21,dim(dat_filter)[2]]<-1
#case SPM-IQ=73, extrem unmotiviert
dat_filter[47,dim(dat_filter)[2]]<-1
#keine GEFT RT's
dat_filter[1,dim(dat_filter)[2]]<-1 
dat_filter<-dplyr::filter(dat_filter,exclude_GEFT==0)
