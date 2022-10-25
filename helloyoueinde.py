import time

answer_A = ["A", "a"]
answer_B = ["B", "b"]

Anders = ("\nGebruik Alleen A of B")

print("\nIntroductie\n"
"\nSteve is jongen van 23 jaar. Zijn vader was de eigenaar van"
"\neen groot gamebedrijf, maar nadat zijn vader alles op een game had ingezet"
"\nging zijn vader verdwenen en de game ook. Steve was 13 jaar oud toen dat gebeurde."
"\nNiemand weet waar zijn vader is.")
time.sleep(13)

def eerste():
    print("\nSteve werkt bij de bedrijf van de vriend van zijn vader “Bill”."
    "\nOp een dag komt Bill met Steve praten over de speelhal die zijn vader had"
    "\nen die niet door de bank was ingenomen. Bill zegt dat Steve het speelhaal moet"
    "\nboezoeken en als hij wilt mag hij het speelhaal hebben.\n"
    "\nWat doet Steve?\n"
    "\nA: Steve zegt dat hij geen interrese heeft in de speelhal."
    "\nB: Steve zegt dat hij de speelhal gaat bezoeken.")
    choice1 = input("A of B --> ")
    if choice1 in answer_A:
        deerde()
    elif choice1 in answer_B:
        tweede()
    else:
        print(Anders)
        eerste()

def deerde():
    print("\nOp dezelfde dag wordt Steve midden in de nacht wakker na een droom"
    "\nwaarin zijn vader in een gat werd gezogen. hij denkt dat dit een signaal"
    "\nvoor hem is om naar de speelhal te gaan, maar hij weet het niet zeker.\n"
    "\nWat moet hij doen?\n"
    "\nA: Steve kiest om naar de speelhaal."
    "\nB: Steve kiest om niet te gaan.")
    choice2 = input("A of B --> ")
    if choice2 in answer_A:
        tweede()
    elif choice2 in answer_B:
        vierde()
    else:
        print(Anders)
        deerde()

def vierde():
    print("\nDe volgende dag gaat Steve weer werken, maar wanneer Steve"
    "\nzijn kantoor binnenkomt staat er een laptop op tafel. bij het openen"
    "\nvan de laptop begint een programma te starten en vraagt om een naam"
    "\nin te voeren.\n"
    "\nwelke naam moet steve schrijven?\n"
    "\nA: Zijn echte naam."
    "\nB: De naam die hij gebruikt in games")
    choice3 = input("A of B --> ")
    if choice3 in answer_A:
        vijfde()
    elif choice3 in answer_B:
        zesde()
    else:
        print(Anders)
        vierde()

def tweede():
    print("\nSteve gaat naar de speehal. Wanneer hij binnen loopt begint een"
    "\nnummer af te spelen, hij ziet een deur aan het einde van de gang. Hij doet de"
    "\ndeur open en hij ziet het kantoor van zijn vader en een laptop"
    "\nop tafel. Hij zet de laptop aan en opent plotseling een programmeercode"
    "\nop het laptopscherm. Hij moet een naam invoeren om de programmercode te runnen.\n"
    "\nWelke naam schrijft Steve?\n"
    "\nA: Zijn echte naam."
    "\nB: De naam die hij gebruikt in games")
    choice4 = input("A of B --> ")
    if choice4 in answer_A:
        vijfde()
    elif choice4 in answer_B:
        zesde()
    else:
        print(Anders)
        vierde()

def vijfde():
    print("\nPlotseling kan Steve niets meer zien. Hij voelt dat hij wordt"
    "\ngetrokken en wanneer zijn visie terugkeert, bevindt hij zich in een" 
    "\ngeheel witte kamer. Er verschijnt een stem die zegt aan Steve dat hij bevindt"
    "\nzich in een wereld gecreëerd door “de maker”, hier is alles geprogrammeerd"
    "\nbehalve de mensen van de uitdaging, ze zijn gebruikers die bij toeval de wereld"
    "\nbetreden. Er zijn maar 2 manieren om uit deze wereld te komen. Een van de manieren"
    "\nis het winnen van de uitdaging.\n"
    "\nWat zegt Steve?\n"
    "\nA: Dit kan alleen maar een nachtmerrie zijn"
    "\nB: Waarom ben ik in een witte kamer en niet in de uitdaging dan?")
    choice5 = input("A of B --> ")
    if choice5 in answer_A:
        achtste()
    elif choice5 in answer_B:
        zevende()
    else:
        print(Anders)
        vijfde()

def zevende():
    print("\nJe bent in deze kamer omdat de naam die je gebruikt voordat je deze wereld"
    "\nbetreedt een naam is van een heel speciaal persoon voor “de maker”. Alle mensen"
    "\ndie binnenkomen met de naam Steve in de wereld van de maker verschijnen"
    "\nin deze kamer, zodat ze de maker kunnen ontmoeten.\n"
    "\nWat wilt Steve doen?\n"
    "A: Ik wil kennismaken met de maker"
    "B: Ik wil even nadenken")
    choice6 = input("A of B --> ")
    if choice6 in answer_A:
        negende()
    elif choice6 in answer_B:
        achtste()
    else:
        print(Anders)
        zevende()

def achtste():
    print("\nDe stem in de kamer zegt dat het Steve tijd zal geven om na te denken. Twee uur"
    "\ngaan voorbij voordat plotseling een gemaskerde man de deur opent van de kamer waar"
    "\nSteve is en Steve vertelt om hem te volgen.\n"
    "\nWat doet Steve?\n"
    "A: Volg de gemaskerde man"
    "B: Blijf in de kamer")
    choice7 = input("A of B --> ")
    if choice7 in answer_A:
        twintigste()
    elif choice7 in answer_B:
        negende()
    else:
        print(Anders)
        achtste()

def twintigste():
    print("\nSteve volgt de gemaskerde man, hij neemt Steve mee naar een kamer een paar"
    "\ngangen verderop. Daar aangekomen zet de man zijn masker af en Steve ziet dat de"
    "\nman eigenlijk zijn vader is. Hij is 10 jaar ouder, hij zegt dat er een nep-maker is die"
    "\nhem heeft verraden en hij heeft Steve nodig om op de knop te klikken, deze knop zal alles"
    "\nen iedereen verwijderen en Steve zal terugkeren naar de normale wereld. Het probleem is"
    "\ndat in het midden van de uitleg, bewakers de kamer binnenvallen en zeggen dat de man waar"
    "\nSteve mee praat een misleidend programma is. De bewakers zeggen dat ze gaan Steve meenemen"
    "\nom de echte maker te ontmoeten en dat hij niet op de knop moet klikken.\n"
    "\n Wat doet Steve?\n"
    "A: Meegenomen worden door bewakers"
    "B: Niet in een van hen geloven en wegrennen ")
    choice8 = input("A of B --> ")
    if choice8 in answer_A:
        negende()
    elif choice8 in answer_B:
        eentwintigste()
    else:
        print(Anders)
        achtste()


eerste()