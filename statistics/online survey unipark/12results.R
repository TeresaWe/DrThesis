#libraries
library(dplyr)
library(psych)


#bind relevant result scores together

results<-data.frame(code,APdef,AP_gen,Syn_gen, AQ_Score, EQ_Score, SQ_Score, 
               AP_sums,semerror,AQ_AD_Score,AQ_IM_Score,AQ_SK_Score,AQ_SW_Score,
               AQ_CO_Score, main_years, second_years, MSI_Score,MSI_F1_Score,
               MSI_F2_Score,MSI_F3_Score,MSI_F4_Score,MSI_F5_Score,MSI_FG_Score,
               GUF_ASV_Score,GUF_ERG_Score,GUF_KRH_Score,GUF_Score, 
               musical_situation,handedness, stringsAsFactors = FALSE)
# results<-as.data.frame.array(results,row.names=VP_Codes)
#results<-as.data.frame(results,row.names=VP_Codes, stringAsFactors = FALSE)
results<-mutate(results,D_Score=(((SQ_Score-55.6)/150)-((EQ_Score-44.3)/80))/2) #calculate brain type
#results<-dplyr::rename(results,lfdn=V1, AP_gen=V3, Syn_gen=V4, begin_isntr=V15, main_years=V16,second_years=V17) #rename columns

#semerror, begin instr. missing (vector length...)

