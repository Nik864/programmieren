Noten=[]
while True:
    Note=float(input("Gib deine Note ein: "))
    Noten.append(Note)
    print("Noten: " + str(Noten))
    summe=0
    for Note in Noten:
        summe= summe + Note
        Durchschnitt=summe/len(Noten)
    print("Durchschnitt: " +str(Durchschnitt))