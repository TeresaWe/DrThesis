
#Clustering EO beta
p<-c(0.728,0.604,0.153,0.208,0.513,0.154,0.124,0.026,0.027)
p.adjust.methods<-c("holm", "hochberg", "hommel", "bonferroni", "BH", "BY","fdr", "none")
p.adjust(p, method = "bonferroni", n = length(p))

#path length EC delta
p<-c(0.075,0.227,0.237,0.388,0.03,0.172,0.008,0.08,0.049,0.011)
p.adjust.methods<-c("holm", "hochberg", "hommel", "bonferroni", "BH", "BY","fdr", "none")
p.adjust(p, method = "holm", n = length(p))

#EC T7 Path length
p<-c(0.645,0.616,0.731,0.008,0.824)
p.adjust.methods<-c("holm", "hochberg", "hommel", "bonferroni", "BH", "BY","fdr", "none")
p.adjust(p, method = "fdr", n = length(p))
#EO T1 Path length
p<-c(0.969,0.876,0.095,0.018,0.505)
p.adjust.methods<-c("holm", "hochberg", "hommel", "bonferroni", "BH", "BY","fdr", "none")
p.adjust(p, method = "fdr", n = length(p))

(1/25)*0.25

##############Permutation test
library(coin)
test<-coin::oneway_test(formula=`Crand_ T10`~factor(AP.0.RP.1.AP.), data=EO_beta_network,
            alternative=c("two.sided", "less", "greater"))
summary(test)            
