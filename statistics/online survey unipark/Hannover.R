#find Hannover relativ/absolut Pitch posessors

city<-test_dataframe$city #cave: new vector is class: factor!!
email<-personal_info$Email
email2<-personal_info$Email2
#for(i in 1:n){
#    is.na(email[i]) <-email2[i]
#    }
Hannover<-mutate(results, city = city, email=email, email2=email2)
Hannover<-filter(Hannover, city=="Hannover")
write.csv(Hannover,file= "Hannover") #export as csv