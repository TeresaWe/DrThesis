
# Formula from Dohn, 2012: they used 768 steps on the scroll wheel per octave. 
#Therefore they have a complicated way to measure the distance between target and selected frequency in cent (modulo etc.)
#c=(((log2(fselected/ftarget)*Nsteps+Nsteps/2) Mod(Nsteps)-Nsteps/2)*1200/Nsteps)
# e.g. c = (((log2(451.3616/440)*768+768/2)Mod(768)-768/2)*1200/768)
#c=(Mod((log2(451.3616/440)*1200+(1200/2))/1200)-(1200/2))*1200/1200 #(in R)

rm(freqlist_AR13ROB161,PAT_AR13ROB161)
# for us, the short part is sufficient,as we have a resolution of 1200 cent per octave (100 per semitone)
# this ist: log2(fselected/ftarget)*1200
# e.g. log2(466.164/440)*1200 --> 100.0009
# log2(932.328/880)*1200 --> 100.0009

## first load data table:
# lookup table frequencies: (CAUTION:lookup takes position of letter/factor level, if not changed to class character!
big<-c("C"=65.4064, "C# / Db"=69.2957, "D"=73,4162, "D# / Eb"=77.7817, "E"=82.4069, "F"=87.3071, "F# / Gb"=92.4986,
          "G"=97.9989, "G# / Ab"=103.826, "A"=110.000, "A# / B"=116.541, "H"=123.471)
small<-c("C"=130.813, "C# / Db"=138.591, "D"=146.832, "D# / Eb"=155.563, "E"=164.814, "F"=174.614, "F# / Gb"=184.997,
         "G"=195.998, "G# / Ab"=207.652, "A"=220.000, "A# / B"=233.082, "H"=246.942)
one<-c( "C"=261.626, "C# / Db"=277.183, "D"= 293.665, "D# / Eb"= 311.127, "E"=329.628, "F"=349.228, "F# / Gb"=369.994,
       "G"=391.995, "G# / Ab"=415.305, "A"=440.000,"A# / B"=466.164, "H"=493.883)
two<-c("C"=523.251, "C# / Db"=554.365, "D"= 587.330, "D# / Eb"= 622.254, "E"=659.255, "F"=698.456, "F# / Gb"=739.989,
       "G"=783.991, "G# / Ab"=830.609,"A"=880.000, "A# / B"=932.328, "H"=987.767)
three<-c("C"=1046.50, "C# / Db"=1108.73, "D"=1174.66, "D# / Eb"=1244.51, "E"=1318.51, "F"=1396.91, "F# / Gb"=1479.98,
         "G"=1567.98, "G# / Ab"=1661.22, "A"=1760.00, "A# / B"=1864.66, "H"=1975.53)


file_list_raw = ls(pattern="^freqlist_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
file_list_csv = ls(pattern="^PAT_[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}")
#file_list_raw<-file_list_raw[12]
#name_lookup<-vector(mode= "character", length=length(file_list_raw))
for (j in seq_along(file_list_raw)) {
  data_list = get(file_list_raw[[j]])
  PAT_csv = get(file_list_csv[[j]])
  dev_sounds<- list()
  target.note<-PAT_csv$target.note
  print(j)
  subj_name<-file_list_raw[j]
  for (k in seq_along(data_list)) {
    #rm(dev_raw, vec, nam)
    print(k)
    dev_raw<-data_list[[k]]
    entered<-as.numeric(PAT_csv[k,4])
    label<-PAT_csv[k,6] #table
    target<-as.character(target)
    label<-as.character(label)
    l_big<-unname(big[label])
    l_sm<-unname(small[label])
    l_one<-unname(one[label])
    l_two<-unname(two[label])
    l_three<-unname(three[label])
    vec<-numeric(length(dev_raw[,1]))
    target_freqs<-c(l_big,l_sm,l_one,l_two,l_three)
    distance_final<-log2(entered/c(l_big,l_sm,l_one,l_two,l_three))*1200 #distanzen zu zieltönen in verschiedenen Oktaven
    abs_distance_final<-abs(distance_final) #Betrag
    octave_final<-which(abs_distance_final==min(abs_distance_final))
    c<-distance_final[octave_final]
    target_freq<-target_freqs[octave_final]
    for (i in 1:length(dev_raw[,1])) {
      current<-as.numeric(dev_raw[i,1]) #get current frequency
      if (is.na(current)) {
        vec[i]<-NA
        i=i+1
      }
      else {
        distance<-log2(current/target_freq)*1200 #distanzen zu zieltönen in verschiedenen Oktaven
        vec[i]<-round(distance,4) #table
        i=i+1
      }
    }
    vec<-data.frame(vec)
    dev_sounds<-c(dev_sounds,vec)
    k=k+1
  }
  name<-substr(subj_name,10,20)
  name<-paste("dev_sounds_",name, sep="")
  assign(name,dev_sounds)
}  

#####all PAT_ files needed later
setwd("~/files/PAT_SingleTrials")
sub.folders <- list.files(path=getwd(), pattern="[A-Z]{2}[0-9]{2}[A-Z]{3}[0-9]{3}_[0-9]{4}_[A-Za-z]{3}_[0-9]{2}_[0-9]{4}",include.dirs = TRUE)
for (j in sub.folders) {
  path<-paste(getwd(),"/",j,sep="")
  filenames = list.files(path=path,pattern="Absolute Pitch Experiment.csv")
  for (i in filenames) {
    name<-substr(j,1,10)
    name <- gsub("Absolute Pitch Experiment",name,i)# gsub(pattern, replacement, x)
    name <- gsub(".csv","",name)
    name <-gsub("/","_",name)
    name<-paste("PAT_",name, sep="")
    assign(name,read.csv(paste(path,"/",i,sep=""))) #read in the table and name as "name"
  }
}
rm(PAT_RI15SON966)