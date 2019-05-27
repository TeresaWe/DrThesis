#bivariate correlations
cor.test(dat_filter$d,dat_filter$GEFT_meanRT,)
cor.test(dat_filter$d,dat_filter$Z_MAD)
cor.test(dat_filter$d,dat_filter$AP_sums)
cor.test(dat_filter$d,dat_filter$MSI_Score)
cor.test(dat_filter$d,dat_filter$total_main)
cor.test(dat_filter$d,dat_filter$starting_age)
cor.test(dat_filter$d,dat_filter$SPM_IQ)
cor.test(dat_filter$d,dat_filter$ZVT_IQ)
cor.test(dat_filter$d,dat_filter$AQ_Score)


cor.test(dat_filter$GEFT_meanRT,dat_filter$Z_MAD)
cor.test(dat_filter$GEFT_meanRT,dat_filter$AP_sums)
cor.test(dat_filter$GEFT_meanRT,dat_filter$MSI_Score)
cor.test(dat_filter$GEFT_meanRT,dat_filter$total_main)
cor.test(dat_filter$GEFT_meanRT,dat_filter$starting_age)
cor.test(dat_filter$GEFT_meanRT,dat_filter$SPM_IQ)
cor.test(dat_filter$GEFT_meanRT,dat_filter$ZVT_IQ)
cor.test(dat_filter$GEFT_meanRT,dat_filter$AQ_Score)


cor.test(dat_filter$Z_MAD,dat_filter$AP_sums)
cor.test(dat_filter$Z_MAD,dat_filter$MSI_Score)
cor.test(dat_filter$Z_MAD,dat_filter$total_main)
cor.test(dat_filter$Z_MAD,dat_filter$starting_age)
cor.test(dat_filter$Z_MAD,dat_filter$SPM_IQ)
cor.test(dat_filter$Z_MAD,dat_filter$ZVT_IQ)
cor.test(dat_filter$Z_MAD,dat_filter$AQ_Score)


cor.test(dat_filter$AP_sums,dat_filter$MSI_Score)
cor.test(dat_filter$AP_sums,dat_filter$total_main)
cor.test(dat_filter$AP_sums,dat_filter$starting_age)
cor.test(dat_filter$AP_sums,dat_filter$SPM_IQ)
cor.test(dat_filter$AP_sums,dat_filter$ZVT_IQ)
cor.test(dat_filter$AP_sums,dat_filter$AQ_Score)


cor.test(dat_filter$MSI_Score,dat_filter$total_main)
cor.test(dat_filter$MSI_Score,dat_filter$starting_age)
cor.test(dat_filter$MSI_Score,dat_filter$SPM_IQ)
cor.test(dat_filter$MSI_Score,dat_filter$ZVT_IQ)
cor.test(dat_filter$MSI_Score,dat_filter$AQ_Score)

cor.test(dat_filter$total_main,dat_filter$starting_age)
cor.test(dat_filter$total_main,dat_filter$SPM_IQ)
cor.test(dat_filter$total_main,dat_filter$ZVT_IQ)
cor.test(dat_filter$total_main,dat_filter$AQ_Score)

cor.test(dat_filter$starting_age,dat_filter$SPM_IQ)
cor.test(dat_filter$starting_age,dat_filter$ZVT_IQ)
cor.test(dat_filter$starting_age,dat_filter$AQ_Score)

cor.test(dat_filter$SPM_IQ,dat_filter$ZVT_IQ)
cor.test(dat_filter$SPM_IQ,dat_filter$AQ_Score)


cor.test(dat_filter$ZVT_IQ,dat_filter$AQ_Score)
