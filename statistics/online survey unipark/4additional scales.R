#calculate AP_definition
AP_sums<-sapply(AP_test_correct,sum,na.rm=TRUE)
minsem<-sapply(AP_test_minsem,sum,na.rm=TRUE)
plussem<-sapply(AP_test_plussem,sum,na.rm=TRUE)

#calculate semerror
semerror<-minsem+plussem
AP_Score<-AP_sums+semerror
#APdefinition 80% correct oder Halbton
APdef=AP_Score
APdef[APdef<28]<-0
APdef[APdef<28]<-0
#define cutoff absolutepitch
APdef[APdef>=28]<-1

#additionalscales
demographics<-mutate(demographics, psy=depression+schizophrenia+OCD+social_phobia+schizotypic_disorder+other_psy)
demographics<-as.data.frame.array(demographics, row.names=VP_Codes,stringAsFactors = FALSE)
music_experience<-as.data.frame.array(music_experience, row.names=VP_Codes,stringAsFactors = FALSE)
musical_situation<-music_experience$musical_situation
begin_instr<-exp_mus$begin_instr
psy<-demographics$psy
main_years<-as.numeric(as.character(music_experience$main_years))
second_years<-as.numeric(as.character(music_experience$second_years))
lfdn<-as.numeric(as.character(personal_info$lfdn))
code<-as.character(personal_info$dupl1_Code)
AP_gen<-as.numeric(as.character(AP_questions$AP_gen))
Syn_gen<-as.numeric(as.character(AP_questions$Syn_gen))

