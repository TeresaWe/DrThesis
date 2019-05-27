# additional plot: scatterplot AP & autistic traits
library(ggplot2)
lm2<-lm(AQ_Score~AP_sums, data=dat_filter)
ggplot(data=dat_filter,aes(x=AP_sums, y=AQ_Score))+
  geom_point(mapping=aes(x=AP_sums, y=AQ_Score))+
  geom_abline(aes(intercept=15.78434, slope=0.18491))+
  geom_abline(aes(intercept=32, slope=0),color="red")+
  geom_abline(aes(intercept=26, slope=0),color="darkgreen")+
  geom_abline(aes(intercept=16.4, slope=0),color="blue")+
  geom_point(aes(size=MAD))+theme_classic()+labs(x="PIS",
                                                   y= "AQ", 
                                                   title="", 
                                                   subtitle="")+
  coord_cartesian(ylim=c(0,40),xlim=c(0,36))+
  theme(axis.text.x=element_text(color="black", size=16),
        axis.text.y=element_text(color="black", size=16),
        legend.title=element_text(color="black", size=16,face="bold"),
        legend.text=element_text(color="black", size=16),
        axis.title=element_text(face="bold",size=16),
        title=element_text(size=12),panel.grid.major.y = element_line(colour = "grey"))

ggsave(filename = "APAQ.pdf", plot = last_plot(),
      path = "~/files/Publication AEFT/graphics/")
ggsave(filename = "APAQ.eps",device="eps", plot = last_plot(),
       path = "~/files/Publication AEFT/graphics/")
