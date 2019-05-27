library("tidyr", lib.loc="~/R/win-library/3.2")
library("ggplot2", lib.loc="~/R/win-library/3.2")
library("dplyr", lib.loc="~/R/win-library/3.2")

#statistics on network parameters
EO_all_network_filter<-na.omit(EO_all_network)
#(age, sec, SPM, ZVT no group differences: five non native speakers within AP...)

#run all t.tests for one frequency band (EO)
lapply(EO_all_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EO_all_network$AP.0.RP.1.AP., var.equal = TRUE))
#Lrand_T3 (0.0394)

lapply(EO_alpha_network[,c(143:215,235:242)], 
       function(x) t.test(x ~ EO_alpha_network$AP.0.RP.1.AP., var.equal = TRUE,na.rm=TRUE))
#SW_T4 reduced (.01)

#L_T4 slightly reduced (.14), E_T4 slightly higher (.14)
#Crand_T3,C_T7 slightly lower (.12,.17)

lapply(EO_beta_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EO_beta_network$AP.0.RP.1.AP., var.equal = TRUE))
#Lrand_T7 higher (.095)
#Crand_T09 and T10 lower (.057,.061)
# Erand_T7 (.11)

lapply(EO_delta_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EO_delta_network$AP.0.RP.1.AP., var.equal = TRUE))
#lower E_T7,T6,T5 (T4,T3),T2,T1 (.009-.05)
#Lrand_T1,T2 lower (.03-.01)
#L_T1-T10 higher (.13-.01)
#Crand T2 lower (.035),C_T2 (.10)
#CE_T1-10 reduced (.05-.10), CErand_T1,T2 (.016,.039)
#E_T1-T10 reduced(.01-0.10), Erand_T1 (.016), Erand_T2 (.0.039), Erand_T8 (.067))

lapply(EO_gamma_network[,c(141:213,234:240)], 
       function(x) t.test(x ~ EO_gamma_network$AP.0.RP.1.AP., var.equal = TRUE))
#nothing

lapply(EO_theta_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EO_theta_network$AP.0.RP.1.AP., var.equal = TRUE))
#L_T6-T10 slightly lower (.19-.08)
#C_T2 higher (0.005)
#CE_T9,T8 higher (.09,.08) (+E_T8,T9)
#Crand_T9 higher (.03)


###################
#EC

lapply(EC_all_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EC_all_network$AP.0.RP.1.AP., var.equal = TRUE))

#L_ T6 lower (.18), _T5 (.08), _T4(.10), _T3 (.13)
#Lrand_T4 lower (.09), _T3 (.12)
#Crand_T4,T3 higher (.14), _T2 lower (.03)
#SW_T6-T10 lower (.01-.05)


lapply(EC_alpha_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EC_alpha_network$AP.0.RP.1.AP., var.equal = TRUE))
#Crand_T2 lower(.09), C_T6 lower (.09)
#SW_T6,T7,T9 lower (.15-.19)

lapply(EC_beta_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EC_beta_network$AP.0.RP.1.AP., var.equal = TRUE))
#C_T2, Crand_T8 higher (.15)
#SW_T8 lower (.06)

lapply(EC_delta_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EC_delta_network$AP.0.RP.1.AP., var.equal = TRUE)) 
#Lrand_T10 higher (0.02), T9 (.07), T8 (.20), T7 (.03), T6 (.24), T5(.08), 
#L_T10, L_T9 higher (.05), T8 (.07)
#CErand_T10,T9,T7 lower (.009-.03),  T8 (.20)
#CE_T10,T9 lower (.08)
#Erand_T7, T9, T10 (.03,.05,.02), 
#E_T10,T9 (.08), T8 (.11)


lapply(EC_gamma_network[,c(141:213,233:240)], 
       function(x) t.test(x ~ EC_gamma_network$AP.0.RP.1.AP., var.equal = TRUE)) 
#SW_T4 reduced (.01),, SW_T3(.03) SW_T6 (.05)
#C_T2 lower (.0005), C_T3 (.16), C_T4 (.06)

lapply(EC_theta_network[,c(143:215,235:242)], 
       function(x) t.test(x ~ EC_theta_network$AP.0.RP.1.AP., var.equal = TRUE)) 
#nothing


############filter excluded participants e.g.
#(sex, age, SPM,ZVT no group differences)


german_alpha_EC<-filter(EC_alpha_network,
                        EC_alpha_network$exclude.0.no.1.elec.2.med.3.exp.==0)
##electrodes interpolated, medication, bad experimants behaviour (total 5)
#basically does not change effects (only reduces a bit the alpha level.

#exclude asian AP
german_delta_EC<-filter(EC_delta_network,
                        EC_delta_network$german_native==1)
#basically does not change effects (only changes a bit the alpha level, more towards higher significance!)

german_beta_EO<-filter(EO_beta_network,
                       EO_beta_network$german_native==1)

german_delta_EO<-filter(EO_delta_network,
                        EO_delta_network$german_native==1)