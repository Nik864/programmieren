Noten=[] #Eine Liste wird erstellt
while True:
    Note=float(input("Gib deine Note ein: ")) #Eine Note von 1-6 kann eingetragen werden.
    Noten.append(Note) #Die Note wird in die Liste "Noten" hinzugefügt.
    print("Noten: " + str(Noten)) #Alle Noten werden ausgeschrieben.
    summe=0#Summe wird auf 0 gesetzt.
    for Note in Noten:#Für alle Note in Noten.
        summe= summe + Note#Die Summe wird mit der Note addiert.
        Durchschnitt=summe/len(Noten)#Die Summe wird durch die Anzahl Noten dividiert.
    print("Durchschnitt: " +str(Durchschnitt))#Der Durchschnitt wird gedruckt
