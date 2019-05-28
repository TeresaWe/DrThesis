# Statistical Analysis of IMRT

(AEFT = previous name of IMRT!)

Order of Processing:
- readloopAEFT.R
- AEFT_Functions_RT.R
- AEFT_loopRTfunctions.R
- SDT_measures.R

This gives the raw measures of signal detection theory (d' and c), but without adjustment of calculations, etc. 
The other files can be used in the order of enumeration to adjust signal detection measurements to trial characteristics (e.g. perfect hit scores)
and to adjust for randomisation problems in the first version of the experiment. Furthermore, a comparison to GEFT (Group embedded figures test) in our sample is calculated.
