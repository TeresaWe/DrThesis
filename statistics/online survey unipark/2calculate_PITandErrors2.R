# first extract the relevant clumns from your UNIPARK dataframe (see script "Data cleaning unipark.r")
#load AP solution
library(dplyr)
library(readr)
# calculation "correct" scales for under/overrating)
AP_solution_PIT <- read_csv("~/files/unipark/unipark/AP_solution_PIT.csv")
AP_solution_PIT<-mutate(AP_solution_PIT, minsem=solution-1, plussem=solution+1, minwholestep=solution-2, pluswholestep=solution+2,minquart = solution-5,plusquart = solution+5,minquint=solution-7, plusquint=solution+7) #add columns for semitone errors
View(AP_solution_PIT)
#replace not existing answers (-12)
AP_solution_PIT[AP_solution_PIT==13]<-1
AP_solution_PIT[AP_solution_PIT==14]<-2
AP_solution_PIT[AP_solution_PIT==15]<-3
AP_solution_PIT[AP_solution_PIT==16]<-4
AP_solution_PIT[AP_solution_PIT==17]<-5
AP_solution_PIT[AP_solution_PIT==18]<-6
AP_solution_PIT[AP_solution_PIT==19]<-7
AP_solution_PIT$minsem[AP_solution_PIT$minsem==0]<-12
AP_solution_PIT$minwholestep[AP_solution_PIT$minwholestep==0]<-12
AP_solution_PIT$minquart[AP_solution_PIT$minquart==0]<-12
AP_solution_PIT$minquint[AP_solution_PIT$minquint==0]<-12
AP_solution_PIT[AP_solution_PIT==-1]<-11
AP_solution_PIT[AP_solution_PIT==-2]<-10
AP_solution_PIT[AP_solution_PIT==-3]<-9
AP_solution_PIT[AP_solution_PIT==-4]<-8
AP_solution_PIT[AP_solution_PIT==-5]<-7
AP_solution_PIT[AP_solution_PIT==-6]<-6
AP_solution_PIT[AP_solution_PIT==-7]<-5

##############################
#calculate correct answers
##############################

n<-length(VP_Codes$dupl1_Code) #number of participants

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 
i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,4])
    as.vector(x) #turn into vector
    as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
    vec[(j*36-35):(j*36)] <- x #append first vector with new one
    i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_correct<-data.frame(vec) #turn into dataframe
  colnames(AP_test_correct)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_correct)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_correct)

#############################
#calculate semitone errors -1
#############################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 

i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,5])
    as.vector(x) #turn into vector
    as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
    vec[(j*36-35):(j*36)] <- x #append first vector with new one
    i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_minsem<-data.frame(vec) #turn into dataframe
  colnames(AP_test_minsem)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_minsem)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_minsem)

#############################
#calculate semitone errors +1
#############################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 

i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,6])
        as.vector(x) #turn into vector
        as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
        vec[(j*36-35):(j*36)] <- x #append first vector with new one
        i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_plussem<-data.frame(vec) #turn into dataframe
  colnames(AP_test_plussem)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_plussem)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_plussem)




#################################
#calculate (minus) whole tone errors
#################################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 
i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,7])
        as.vector(x) #turn into vector
        as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
        vec[(j*36-35):(j*36)] <- x #append first vector with new one
        i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_minwholestep<-data.frame(vec) #turn into dataframe
  colnames(AP_test_minwholestep)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_minwholestep)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_minwholestep)

#################################
#calculate (plus) whole tone errors
#################################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 
i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,8])
        as.vector(x) #turn into vector
        as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
        vec[(j*36-35):(j*36)] <- x #append first vector with new one
        i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_pluswholestep<-data.frame(vec) #turn into dataframe
  colnames(AP_test_pluswholestep)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_pluswholestep)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_pluswholestep)

#################################
#calculate minus quart
#################################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 
i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,9])
    as.vector(x) #turn into vector
    as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
    vec[(j*36-35):(j*36)] <- x #append first vector with new one
    i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_minquart<-data.frame(vec) #turn into dataframe
  colnames(AP_test_minquart)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_minquart)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_minquart)

#################################
#calculate plus quart
#################################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 
i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,10])
    as.vector(x) #turn into vector
    as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
    vec[(j*36-35):(j*36)] <- x #append first vector with new one
    i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_plusquart<-data.frame(vec) #turn into dataframe
  colnames(AP_test_plusquart)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_plusquart)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_plusquart)

#################################
#calculate minus quint
#################################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-(1:37),]
View(AP_test_transpose)
#create empty vector 
i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,11])
    as.vector(x) #turn into vector
    as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
    vec[(j*36-35):(j*36)] <- x #append first vector with new one
    i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_minquint<-data.frame(vec) #turn into dataframe
  colnames(AP_test_minquint)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_minquint)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_minquint)


#################################
#calculate plus quint
#################################

#flip ros and columns AP_test matrix:columns are VP
AP_test_transpose<-t(AP_test)
#AP_test_transpose<-AP_test_transpose[-1:37,]
View(AP_test_transpose)
#create empty vector 
i=1
for(i in 1:n){
  vec<-numeric(36*n) #initialize vector
  for (j in 1:n){
    z<-as.numeric(AP_test_transpose[38:73,j])
    x<-(z==AP_solution_PIT[,12])
    as.vector(x) #turn into vector
    as.numeric(x) #turn boolean vector in numbers: True=1, False=0,#
    vec[(j*36-35):(j*36)] <- x #append first vector with new one
    i=i+1
  }
  dim(vec)<-c(36,n) # turn long vector into array(APtone,VP)
  AP_test_plusquint<-data.frame(vec) #turn into dataframe
  colnames(AP_test_plusquint)<-VP_Codes$dupl1_Code #edit columnnames
  rownames(AP_test_plusquint)<-AP_solution_PIT$Trail_name #edit rownames
}
View(AP_test_plusquint)


#todo: 
#- resultstable
#- email with feedback
#- build function, looping errors