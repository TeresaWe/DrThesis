library(readr)
music_exp <- read_csv("~/files/Cognition/music_exp.csv")

#calculate sum of practice hours main instrument

sec1<-((music_exp$main_upper1-music_exp$main_lower1)+1)*365*music_exp$main_hours1
sec2<-((music_exp$main_upper2-music_exp$main_lower2)+1)*365*music_exp$main_hours2
sec3<-((music_exp$main_upper3-music_exp$main_lower3)+1)*365*music_exp$main_hours3
sec4<-((music_exp$main_upper4-music_exp$main_lower4)+1)*365*music_exp$main_hours4
sec5<-((music_exp$main_upper5-music_exp$main_lower5)+1)*365*music_exp$main_hours5
sec6<-((music_exp$main_upper6-music_exp$main_lower6)+1)*365*music_exp$main_hours6
sec7<-((music_exp$main_upper7-music_exp$main_lower7)+1)*365*music_exp$main_hours7
sec8<-((music_exp$main_upper8-music_exp$main_lower8)+1)*365*music_exp$main_hours8

sec1<-car::recode(sec1, "NA=0")
sec2<-car::recode(sec2, "NA=0")
sec3<-car::recode(sec3, "NA=0")
sec4<-car::recode(sec4, "NA=0")
sec5<-car::recode(sec5, "NA=0")
sec6<-car::recode(sec6, "NA=0")
sec7<-car::recode(sec7, "NA=0")
sec8<-car::recode(sec8, "NA=0")

total_main<-sec1+sec2+sec3+sec4+sec5+sec6+sec7+sec8

#calculate sum of practice hours second instrument
sec1s<-((music_exp$second_upper1-music_exp$second_lower1)+1)*365*music_exp$second_hours1
sec2s<-((music_exp$second_upper2-music_exp$second_lower2)+1)*365*music_exp$second_hours2
sec3s<-((music_exp$second_upper3-music_exp$second_lower3)+1)*365*music_exp$second_hours3
sec4s<-((music_exp$second_upper4-music_exp$second_lower4)+1)*365*music_exp$second_hours4
sec5s<-((music_exp$second_upper5-music_exp$second_lower5)+1)*365*music_exp$second_hours5
sec6s<-((music_exp$second_upper6-music_exp$second_lower6)+1)*365*music_exp$second_hours6
sec7s<-((music_exp$second_upper7-music_exp$second_lower7)+1)*365*music_exp$second_hours7

sec1s<-car::recode(sec1s, "NA=0")
sec2s<-car::recode(sec2s, "NA=0")
sec3s<-car::recode(sec3s, "NA=0")
sec4s<-car::recode(sec4s, "NA=0")
sec5s<-car::recode(sec5s, "NA=0")
sec6s<-car::recode(sec6s, "NA=0")
sec7s<-car::recode(sec7s, "NA=0")

total_second<-sec1s+sec2s+sec3s+sec4s+sec5s+sec6s+sec7s

total_both<-total_main+total_second
hours<-cbind(total_main,total_second, total_both)
rownames(hours)<-music_exp$`allresults$VP_Code`
#bind to allresults see match results table

