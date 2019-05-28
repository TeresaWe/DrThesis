#Hierarchical letters

Two conditions randomizing the order of blocks (focus on local vs. global aspects of the hierarchical letters first). One half of the participants should undergo the one condition, the other half the other one.

'GlobalZuerst' = This condition starts with the global block, followed by the local block.

'LocalZuerst' = This condition starts with the local block, followed by the global block.

Many thanks to Pablo Carra for his help and contribution in programming the experiment. 

##German explanation of solution for technical issues:

-globale Antwortstatistiken für den Benutzer werden noch direkt in den Code eingebaut (etwas schmutzig, aber das schnellste, und die genauen daten werden ja sowiseo gespeichert...)

UM DAS BUILDER-PROJEKT ZUM LAUFEN ZU BRINGEN:
-Nachdem man alle Änderungen gemacht hat erstmal kompilieren
-In der Coder-view bei win= visual.Window in den Parametern useFBO=False einstellen
-globalen count einführen:
	  --> globale variablen deklarieren (oben)
			#Global variables for Feedback at the end of the run
			totalCorrect_global = 0
			totalCorrect_local = 0
	  --> beim jeweils zweiten und dritten trials_L und trials_G aktualisieren
			global totalCorrect_local #bzw. totalcorrect_global
                        totalCorrect_local += 1
	  --> das output am Ende modifizieren
			msg = "Lokale Buchstaben (Elemente): Sie haben %i Stimuli richtig beantwortet \n)" %(totalCorrect_local)

	[Kopieren und einfügen aus der vorigen Version ist eigentlich das schnellste]

-Speichern-unter --> Überschreiben (normal speichern funktioniert meistens nicht)
-Run
