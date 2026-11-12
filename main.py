import random

sten=1  
sax=2
påse=3
spelomgång=1

 #dator väljer slumpat mellan sten, sax och påse(för 1=sten, 2=sax och 3=påse)
lek=print("Nu ska vi spela Sten, Sax eller Påse!") #variabel som skriver ut att vi ska spela sten, sax eller påse
Python311=print("Jag är Python311") #variabel som skriver ut datorns namn(Python311)

spelarnamn = input("Ange ditt spelarnamn: ") #variabel som frågar om vad du vill heta som spelare
antal_omgångar = int(input("Ange antal omgångar vi ska spela: "))#variabel som frågar om antalet gånger du vill spela och omvandlar från sträng till heltal
for i in range(antal_omgångar): # loopar antalet omgångar som du valt att spela
    dator = str(random.randint(1, 3)) #dator väljer slumpat mellan sten, sax och påse(för 1=sten, 2=sax och 3=påse)
    if dator==1:
        dator="sten"
    elif dator==2:
        dator="sax"
    else:
        dator="påse"
    
    print(f"Spelomgång {spelomgång}\n ----------------------")
    spelare=input("Välj sten, sax eller påse: ")

    print(f"{spelarnamn} spelar:{spelare}")
    print(f"Datorn spelar: {dator}")
    
    spelomgång=spelomgång+1

    if spelare == dator:
        print("Det blev oavgjort!")

    elif spelare == "sten" and dator == "sax":
        print("Du vann!")

    elif spelare == "sax" and dator == "påse":
        print("Du vann!")

    elif spelare == "påse" and dator == "sten":
        print("Du vann!")

    elif spelare == "sax" and dator == "sten":
        print("Du förlorade!")

    elif spelare == "påse" and dator == "sax":
        print("Du förlorade")
    
    elif spelare == "sten" and dator == "påse":
        print("Du förlorade")
    
    else:
        print("Ogiltigt val!") #
