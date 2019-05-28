# Pitch adjustment test

Start of the experiment is possible by a shell-skript, which opens a GUI to select the condition and type in the participant#s code. The experiment consists of 108 trials in three blocks of 36 (3 per musical label) and 15 seconds are given for each trial. By the use of a parallel port triggers can be send to an EEG system to record the EEG at the same time and mark the trials begin, end and target in the EEG file. 

Many thanks to Hannes Schmidt & Arthur Ehle for their help and contribution in programming the experiment. 

# Coding of EEG-Trigger

| Event    | Code|
| -------- | -------- |
| start of tone| 101-112 (via Zielton)  |
| first touch of controller | 200   |
| confirmation by participant | 201   |
| t > 15s | 202 |

# Coding Zieltöne
| musical label, trial | Code |
| ---- | ---- |
| A | 101 |
| A# / Bb | 102 |
| B | 103 |
| C | 104 |
| C# / Db | 105 |
| D | 106 |
| D# / Eb | 107 |
| E | 108 |
| F | 109 |
| F# / Gb | 110 |
| G | 111 |
|G# / Ab | 112 |


## Anleitung Parallelport (GERMAN)

Wenn `dmesg` folgendes ausgibt:

```
[114958.160728] parport0: cannot grant exclusive access for device ppdev0
[114958.160735] ppdev0: failed to register device!
```

Dann überprüfe, ob `lp` oder ein Drucker-Treiber geladen ist via:
```
lsmod | egrep '(par|lp[[:blank:]$])'
```

Sollte dies der Fall sein, `lp` oder andere Treiber via:

```
sudo rmmod lp 
```

aus dem Kernel "unloaden". Soll das Modul dauerhaft beim Start nicht mehr geladen werden, je nach Distribution das Modul blacklisten:
```
blacklist lp
```

