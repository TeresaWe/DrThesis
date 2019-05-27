##version A vs. B
version_A<-subset(dat_filter,version==1)
version_B<-subset(dat_filter,version==0)

#age
hist(version_A$age) #non-normal
describe(version_A$age)
describe(version_B$age)
t.test(dat_filter$age~dat_filter$version)
wilcox.test(dat_filter$age,dat_filter$version, paired=FALSE) #Man Whitney U Test

#SPM_IQ
hist(dat_filter$SPM_IQ)
describe(version_A$SPM_IQ)
describe(version_B$SPM_IQ)
t.test(dat_filter$SPM_IQ~dat_filter$version)

#ZVT_IQ
hist(dat_filter$ZVT_IQ)
describe(version_A$ZVT_IQ)
describe(version_B$ZVT_IQ)
t.test(dat_filter$ZVT_IQ~dat_filter$version)

#main_hours
hist(dat_filter$total_main) #non-normal
describe(version_A$total_main)
describe(version_B$total_main)
t.test(dat_filter$total_main~dat_filter$version)
wilcox.test(dat_filter$total_main,dat_filter$version,paired=FALSE)

#AMMA
hist(dat_filter$AMMAcomp)
describe(version_A$AMMAcomp)
describe(version_B$AMMAcomp)
t.test(dat_filter$AMMAcomp~dat_filter$version)

#AMMA tonal
hist(dat_filter$AMMAtonal)
describe(version_A$AMMAtonal)
describe(version_B$AMMAtonal)
t.test(dat_filter$AMMAtonal~dat_filter$version)

#AMMA rhythmic
hist(dat_filter$AMMAryth)
describe(version_A$AMMAryth)
describe(version_B$AMMAryth)
t.test(dat_filter$AMMAryth~dat_filter$version)

#MSI
hist(dat_filter$MSI_Score)
describe(version_A$MSI_Score)
describe(version_B$MSI_Score)
t.test(dat_filter$MSI_Score~dat_filter$version)

#PIS
hist(dat_filter$AP_sums)
describe(version_A$AP_sums)
describe(version_B$AP_sums)
t.test(dat_filter$AP_sums~dat_filter$version)

#PIS
hist(dat_filter$AQ_Score)
describe(version_A$AQ_Score)
describe(version_B$AQ_Score)
t.test(dat_filter$AQ_Score~dat_filter$version)

#MAD
hist(dat_filter$MAD)
describe(version_A$MAD)
describe(version_B$MAD)
t.test(dat_filter$MAD~dat_filter$version)

#SDfoM
hist(dat_filter$SDfoM)
describe(version_A$SDfoM)
describe(version_B$SDfoM)
t.test(dat_filter$SDfoM~dat_filter$version)

#starting age
hist(dat_filter$starting_age)
describe(version_A$starting_age)
describe(version_B$starting_age)
t.test(dat_filter$starting_age~dat_filter$version)

