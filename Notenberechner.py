Noten=[] #Eine Liste wird erstellt
##################################################################################


#Das Programm fragt den Benutzer unendlich oft nach einer Note, die das Programm danach in die Liste speicher kann
while True:
    Note=float(input("Gib deine Note ein: ")) 
    Noten.append(Note) 
    print("Noten: " + str(Noten)) 
    summe=0
    
    
#############################################################################
#In der for-Schleife wird der Durchschnitt berechnet, indem es alle Noten zuammenrechnet und danach den Durchschnitt berechnet.    
    for Note in Noten:
        summe= summe + Note
        Durchschnitt=summe/len(Noten)
######################################################################################

#Der Durchschnitt wird gedruckt
 print("Durchschnitt: " +str(Durchschnitt))
