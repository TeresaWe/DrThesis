
#first insert data-matrix (e.g. results, filter, etc.)
#libraries
library(dplyr)
library(psych)
#convert back to data frame
results<-as.data.frame.array(results)
filterpsy<-as.data.frame.array(filterpsy)
filterpsymus<-as.data.frame.array(filterpsymus)

#scatterplots
plot(filterpsymus$AP_sums, filterpsymus$AQ_Score) #example calculation over filter condition
hist(filter1$EQ_Score) #table muss numerisch sein

#replace filter by any preferred filter variable or anything
bi.bars(results$SQ_Score, results$AP_gen)
bi.bars(results$EQ_Score, results$AP_gen)
bi.bars(results$AQ_Score, results$AP_gen) #plot for two groups
plot(filter4$D_Score,filter4$AP_sums)

#correlations
#matrix
resultsnum<-data.matrix(results)
print(corr.test(results),short=FALSE)
#single
cor.test(filter5$AP_sums, filter5$AQ_Score) #example
t.test(variable ~ group, data = results)
r.test() #difference between correlations