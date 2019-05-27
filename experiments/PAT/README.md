# Anleitung Parallelport

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

# Kodierung der EEG-Trigger

| Event    | Kodierung|
| -------- | -------- |
| Ton-Start| 101-112 (via Zielton)  |
| Erste Berührung | 200   |
| Bestätigung | 201   |
| t > 15s | 202 |

# Kodierung der Zieltöne
| Ton | Kodierung |
| ---- | ---- |
| A | 101 |
| A# / B | 102 |
| H | 103 |
| C | 104 |
| C# / Db | 105 |
| D | 106 |
| D# / Eb | 107 |
| E | 108 |
| F | 109 |
| F# / Gb | 110 |
| G | 111 |
|G# / Ab | 112 |
