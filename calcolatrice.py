#calcolatrice

from math import sqrt

hello_message = """
Benvenuti in calcolatrice.

░░░░░░░░░░░║░░░░░░░░░░░░
░░▄█▀▄░░░░░║░░░░░░▄▀▄▄░░
░░░░░░▀▄░░░║░░░░▄▀░░░░░░
░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄░
▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀
░░░░░░██░░▀▐▌▀░░██░░░░░░
░▄█▀▀▀████████████▀▀▀█░░
█░░░░░░██████████░░░░░▀▄
█▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█
░▀█░░░█░░░░░░░░░░█░░░█▀░

Di seguito un elenco delle varie funzioni disponibili:

-per effettuare un addizione, seleziona 1;
-per effettuare una sottrazione, seleziona 2;
-per effettuare una moltiplicazione, seleziona 3;
-per effettuare una divisione, seleziona 4;
-per effettuare un calcolo esponenziale seleziona 5;
-per effettuare una radice quaadrata, seleziona 6;
-per uscire dal programma digita ESC';
"""


while True:
    print (hello_message)

    action = input  ("inserisci il numero corrispondente per effettuare la tua operazione: ") 

############corpo delle scelte per effettuare le operazioni#### 

    if action == "1":
        print("hai scelto un addizione\n")
        a = float (input ("inserisci il primo numero ->"))
        b = float (input ("inserisci il secondo numero ->"))
        print ("il risultato dell'addizione é:", str(a+b))


    elif action == "2":
       print("hai scelto una sottrazione\n")
       a = float (input ("inserisci il primo numero ->"))
       b = float (input ("inserisci il secondo numero ->"))
       print ("il risultato della sottrazione é:", str(a-b))


    elif action == "3":
       print("hai scelto una moltiplicazione\n")
       a = float (input ("inserisci il primo numero ->"))
       b = float (input ("inserisci il secondo numero ->"))
       print ("il risultato della moltiplicazione é:", str(a*b))


    elif action == "4":
       print("hai scelto una divisione\n")
       a = float (input ("inserisci il primo numero ->"))
       b = float (input ("inserisci il secondo numero ->"))
       print ("il risultato della divisione é:", str(a/b))

    elif action == "5":
       print("hai scelto un calcolo esponenziale\n")
       a = float (input ("inserisci la base ->"))
       b = float (input ("inserisci l'esponente ->"))
       print ("il risultato del calcolo esponenziale é:", str(a**b))

    
    elif action == "6":
       print("hai scelto: radice quadrata\n")
       a = float (input ("inserisci il primo numero ->"))
       print ("il risultato della'operazione é:", str(sqrt(a)))

##########################################################################
#scelte dei cicli per uscire e chiudere o continuare.

    elif action == "ESC":
       print ("l'applicazione verra chiusa!.\n")
       break

    new_action = input ("\n Desideri continuare a uilizzare l'applicazione? S/N")
    if new_action == "S" or new_action == "s":
        print ("Sto tornando al meenù principale!\n")
        continue
    else:
        print("""
          
░░░░░░░░░░░║░░░░░░░░░░░░
░░▄█▀▄░░░░░║░░░░░░▄▀▄▄░░
░░░░░░▀▄░░░║░░░░▄▀░░░░░░
░▄▄▄░░░░█▄▄▄▄▄▄█░░░░▄▄▄░
▀░░░▀█░█▀░░▐▌░░▀█░█▀░░░▀
░░░░░░██░░▀▐▌▀░░██░░░░░░
░▄█▀▀▀████████████▀▀▀█░░
█░░░░░░██████████░░░░░▀▄
█▄░░░█▀░░▀▀▀▀▀▀░░▀█░░░▄█
░▀█░░░█░░░░░░░░░░█░░░█▀░    

A presto!\n""")
        break
