#set wirking directory
setwd("~/files/unipark/unipark")

###to run the script replace raw171012 with STRG+F-->search and replace with filename (+replace in read.csv)###

# load data file (".csv")
library(readr)
raw181108 <- read.csv("~/files/unipark/unipark/Workspaces/raw181108.csv") #### insert path and name for "raw181108"
#remove missing value indices from UNIPARK; replace with NA
raw181108[raw181108==-99] <-NA
raw181108[raw181108==-77] <-NA
raw181108[raw181108==-66] <-NA
#select columns of MSI and create new dataframe "MSI"
MSI<-dplyr::select(raw181108,dupl1_Code,dplyr::starts_with("MSI"))
View(MSI)
#same for music experience
music_experience<-dplyr::select(raw181108,dupl1_Code,54:106)
View(music_experience)
#read in new music experience file
exp_mus <- read.csv("~/files/unipark/unipark/music exp.csv") #### insert path and name for "exp_mus"
#same for GÜF
GUF<-dplyr::select(raw181108,dupl1_Code,107:126)
View(GUF)
#same for AP questions
AP_questions<-dplyr::select(raw181108,dupl1_Code,127:143)
View(AP_questions)
#same for AP_test
AP_test<-dplyr::select(raw181108,dupl1_Code,dplyr::starts_with("play"),dplyr::starts_with("ANS"))
View(AP_test)
#same for EQ
EQ<-dplyr::select(raw181108,dupl1_Code,dplyr::starts_with("EQ"))
View(EQ)
#same for SQ
SQ<-dplyr::select(raw181108,dupl1_Code,dplyr::starts_with("SQ"))
View(SQ)
#same for AQ
AQ<-dplyr::select(raw181108,dupl1_Code,dplyr::starts_with("AQ"))
View(AQ)
#same for EHD
EHD<-dplyr::select(raw181108,dupl1_Code,dplyr::starts_with("EHD"))
View(EHD)
#same with personal info
personal_info<-dplyr::select(raw181108,dupl1_Code,1,12,13,432)
View(personal_info)
#same with demographics
demographics<-dplyr::select(raw181108,dupl1_Code,14,381:409,420-431,433)
View(demographics)
# create variable with VP-codes
VP_Codes<-dplyr::select(raw181108,dupl1_Code)
as.vector(VP_Codes)

###todo: work on references (numbers not correct yet)###