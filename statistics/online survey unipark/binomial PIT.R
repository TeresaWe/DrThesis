#binom for correct answers
PIT_trials<- seq(0,36,by = 1)
binom_PIT <- dbinom(PIT_trials,36,1/12)
bdistr_corr<-plot(PIT_trials,binom_PIT) #distribution
luck <- qbinom(0.95,36,1/12) #number of correct trails by change, error likelihood 0.05

#binom for semiton errors
PIT_trials<- seq(0,36,by = 1)
binom_PITsem <- dbinom(PIT_trials,36,2/12)
bdistr_sem<-plot(PIT_trials,binom_PITsem) #distribution
luck_sem <- qbinom(0.95,36,2/12) #number of semiton errors by change, error likelihood 0.05

#binom for correct OR semiton errors
PIT_trials<- seq(0,36,by = 1)
binom_PITweak <- dbinom(PIT_trials,36,3/12)
bdistr_weak<-plot(PIT_trials,binom_PITweak) #distribution
luck_weak <- qbinom(0.95,36,3/12) #number of semiton errors by change, error likelihood 0.05