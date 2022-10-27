import time
import os

answer_A = ["A", "a"]
answer_B = ["B", "b"]
Ja = ["J", "j", "ja", "Ja"]
Nee = ["N", "n", "nee", "Nee"]

Anders = ("\nGebruik Alleen A of B")

def eerste():
    print("\nIntroductie\n"
    "\nSteve is jongen van 23 jaar. Zijn vader was de eigenaar van"
    "\neen groot gamebedrijf, maar nadat zijn vader alles op een game had ingezet"
    "\nging zijn vader verdwenen en de game ook, Steve was 13 jaar oud toen dat gebeurde."
    "\nNiemand weet waar zijn vader is.")

    time.sleep(13)
     
    print("\nSteve werkt nu bij de bedrijf van de vriend van zijn vader'Bill'."
    "\nOp een dag komt Bill met Steve praten over de speelhal die zijn vader had."
    "\nBill zegt dat Steve het speelhaal moet boezoeken en als hij wilt mag hij het speelhaal hebben.\n"
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
        time.sleep(5)
    eerste()

def deerde():
    print("\nOp dezelfde dag wordt Steve midden in de nacht wakker na een droom"
    "\nwaarin zijn vader in een gat werd gezogen. hij denkt dat dit een signaal"
    "\nvoor hem is om naar de speelhal te gaan.\n"
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
        time.sleep(5)
    deerde()

def vierde():
    print("\nDe volgende dag gaat Steve weer werken, maar wanneer Steve"
    "\nzijn kantoor binnenkomt staat er een laptop op tafel. bij het openen"
    "\nvan de laptop begint een programma te starten en vraagt om een naam"
    "\nin te voeren.\n"
    "\nwelke naam voert Steve in?\n"
    "\nA: Zijn echte naam."
    "\nB: De naam die hij gebruikt in games")
    choice3 = input("A of B --> ")
    if choice3 in answer_A:
        vijfde()
    elif choice3 in answer_B:
        zesde()
    else:
        print(Anders)
        time.sleep(5)
    vierde()

def tweede():
    print("\nSteve gaat naar de speehal. Wanneer hij binnen loopt ziet hij"
    "\neen deur aan het einde van de gang. Hij doet de deur open en hij ziet het kantoor"
    "\nvan zijn vader en een laptop op tafel. Hij zet de laptop aan en opent plotseling een programmeercode"
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
        time.sleep(5)
    vierde()

def vijfde():
    print("\nPlotseling kan Steve niets meer zien. Hij voelt dat hij wordt"
    "\ngetrokken en wanneer zijn visie terugkeert, bevindt hij zich in een" 
    "\ngeheel witte kamer. Er verschijnt een stem die zegt aan Steve dat hij bevindt"
    "\nzich in een wereld gecreëerd door 'de maker', hier is alles geprogrammeerd"
    "\nbehalve de mensen van de uitdaging, ze zijn gebruikers die bij toeval deze wereld"
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
        time.sleep(5)
    vijfde()

def zevende():
    print("\nJe bent in deze kamer omdat de naam die je gebruikt voordat je deze wereld"
    "\nbetreedt een naam is van een heel speciaal persoon voor 'de maker'. Alle mensen"
    "\ndie binnenkomen met de naam Steve in de wereld van de maker verschijnen"
    "\nin deze kamer, zodat ze de maker kunnen ontmoeten.\n"
    "\nWat wilt Steve doen?\n"
    "\nA: Ik wil kennismaken met de maker"
    "\nB: Ik wil even nadenken")
    choice6 = input("A of B --> ")
    if choice6 in answer_A:
        negende()
    elif choice6 in answer_B:
        achtste()
    else:
        print(Anders)
        time.sleep(5)
    zevende()

def achtste():
    print("\nDe stem in de kamer zegt dat ze Steve tijd zal geven om na te denken. Twee uur"
    "\ngaan voorbij voordat plotseling een gemaskerde man de deur opent van de kamer waar"
    "\nSteve is en Steve vertelt om hem te volgen.\n"
    "\nWat doet Steve?\n"
    "\nA: Volg de gemaskerde man"
    "\nB: Blijf in de kamer")
    choice7 = input("A of B --> ")
    if choice7 in answer_A:
        twintigste()
    elif choice7 in answer_B:
        negende()
    else:
        print(Anders)
        time.sleep(5)
    achtste()

def twintigste():
    print("\nSteve volgt de gemaskerde man, hij neemt Steve mee naar een kamer een paar"
    "\ngangen verderop. Daar aangekomen zet de man zijn masker af en Steve ziet dat de"
    "\nman eigenlijk zijn vader is. Hij is 10 jaar ouder en hij zegt dat er een nep-maker is die"
    "\nhem heeft verraden toen hij deze wereld heeft gemaakt. Steve's vader zegt dat hij"
    "\nSteve nodig heeft om op de knop te klikken, deze knop zal alles en iedereen "
    "\nverwijderen en alleen Steve zal terugkeren naar de normale wereld. Het probleem is"
    "\ndat in het midden van de uitleg, bewakers de kamer binnenvallen en zeggen dat de man waar"
    "\nSteve mee praat een misleidend programma is. De bewakers zeggen dat ze gaan Steve meenemen"
    "\nom de echte maker te ontmoeten en dat hij niet op de knop moet klikken.\n"
    "\n Wat doet Steve?\n"
    "\nA: Hij gaat mee met de bewakers"
    "\nB: Hij gelooft in geen van hen en rent weg")
    choice8 = input("A of B --> ")
    if choice8 in answer_A:
        negende()
    elif choice8 in answer_B:
        eentwintigste()
    else:
        print(Anders)
        time.sleep(5)
    twintigste()

def eentwintigste():
    print("\nEr gingen 10 dagen voorbij en in die 10 dagen ontdekte Steve meer over"
    "\ndeze virtuele wereld. Van wat hij hoorde zijn er 2 manieren om uit deze wereld"
    "\nte komen. Een daarvan is het deelnemen aan de uitdaging die de stem hem had verteld"
    "\nen de ander is het kliken op de knop die de man had gezegd."
    "\nWat doet Steve?\n"
    "\nA: Geef je over aan de bewakers en de maker ontmoeten"
    "\nB: Deelnemen aan de uitdaging")
    choice9 = input("A of B --> ")
    if choice9 in answer_A:
        negende()
    elif choice9 in answer_B:
        zesde()
    else:
        print(Anders)
        time.sleep(5)
    eentwintigste()

def negende():
    print("\nSteve wordt door de bewakers meegenomen om 'de maker' te ontmoeten. als Steve daar"
    "\naankomt ontdek Steve dat “de maker” eigenlijk zijn vader is en hij legt Steve alles uit. als"
    "\nSteve daar aankomt ontdek Steve dat “de maker” eigenlijk zijn vader “Elon” is en hij legt Steve"
    "\nalles uit. Hij zegt dat hij probeerde een virtuele wereld te creëren, maar uiteindelijk vast kwam"
    "\nte zitten. Hij vertelt Steve ook dat er maar twee manieren zijn om van deze wereld af te komen. De ene"
    "\nis het winnen van de grote uitdaging en de andere is het kliken op een knop die alles en iedereen"
    "\nzou verwijderen, alleen de persoon die erop klikte zou terugkeren naar de echte wereld. Hij zegt dat"
    "\nhij niet op de knop heeft geklikt omdat hij veel geluk had dat hij een wereld kon creëren met"
    "\nkunstmatige intelligentie. Je vader neemt je mee naar de knop en laat je het zien, daar zegt je vader"
    "\ndat je moet deelnemen aan de uitdaging, zodat je terug kunt gaan naar de echte wereld en je vader van"
    "\nde laptop kunt halen. Je vindt het allemaal heel vreemd, want 10 jaar zijn verstreken sinds je vader"
    "\nverdween en hij is helemaal niet ouder geworden. De instinct van Steve zegt dat hij op de knop moet klikken."
    "\nWat doet Steve?\n"
    "\nA: Klikt op de knop"
    "\nB: Gaat naar de Uitdaging")
    choice10 = input("A of B --> ")
    if choice10 in answer_A:
        einde1()
    elif choice10 in answer_B:
        zesde()
    else:
        print(Anders)
        time.sleep(5)
    eentwintigste()

def einde1():
    while True:
        print("\nJe klikt op de knop en alles wordt weer wit, als je zicht terugkomt zie je dat"
        "\nje in het kantoor van je vader bent in de speelhaal. Als je de laptop opent zie je ook"
        "\ndat alles is verwijderd. Uiteindelijk ontdek je dat je nooit zult weten wat er echt met"
        "\nje vader is gebeurd en dat allemaal omdat je op de knop hebt geklikt.\n"
        "\nWil je Opnieuw Spelen?\n")
        choicefinish1 = input("Ja of Nee --> ")
        if choicefinish1 in Ja:
            os.system("cls")
            eerste()
        elif choicefinish1 in Nee:
            break
        else:
            print(Anders)
            time.sleep(5)
        einde1()

def zesde():
    print("\nPlotseling kan Steve niets meer zien. Opeens realiseert Steve dat hij met 14 andere"
    "\nmensen in een kring midden in een bos staat. een stem begint te zeggen dat hij in de"
    "\ngrote uitdaging zit. Deze stem vertelt alle deelnemers aan de uitdaging dat om terug te"
    "\nkeren naar de echte wereld, Een deelnemer alle andere deelnemers zou moeten elimineren en"
    "\nde uitdaging levend zou moeten winnen. De stem zegt ook dat er in het midden van de cirkel enkele"
    "\nwapens zijn om te helpen in de strijd. Daarna begint de uitdaging.\n"
    "\nWat moet Steve doen?\n"
    "\nA: Ren naar het midden van de cirkel en probeer een wapen te pakken"
    "\nB: Rennen naar het bos")
    choice11 = input("A of B --> ")
    if choice11 in answer_A:
        elfde()
    elif choice11 in answer_B:
        twaalfde()
    else:
        print(Anders)
        time.sleep(5)
    zesde()

def elfde():
    print("\nSteve rent naar het midden van de cirkel om te proberen een zwaard, bijl of boog"
    "\nte grijpen. 3 andere mensen rennen ook naar het midden om te proberen iets te vangen.\n"
    "\nWat moet Steve doen?\n")
    "\nA: Geef het op om iets te vangen en ren het bos in"
    "\nB: Sneller rennen en de bijl pakken"
    choice12 = input("A of B --> ")
    if choice12 in answer_A:
        twaalfde()
    elif choice12 in answer_B:
        dertiende()
    else:
        print(Anders)
        time.sleep(5)
    elfde()

def twaalfde():
    print("\nSteve rent het bos in. Hij weet niet wat hij moet doen, hij hoort mensen"
    "\nschreeuwen van pijn. De stem zegt dat er twee spelers zijn uitgeschakeld. Steve realiseert"
    "\nzich dat de uitdaging is om de andere spelers te doden en niet alleen om ze te elimineren"
    "\nzoals in een normaal spel\n."
    "\nWat moet Steve doen?\n"
    "A: Verberg je tot de laatste overlevende en probeer hem dan te elimineren."
    "B: Proberen een wapen te maken om een andere deelnemer te elimineren.")
    choice13 = input("A of B --> ")
    if choice13 in answer_A:
        einde2()
    elif choice13 in answer_B:
        vijftiende()
    else:
        print(Anders)
        time.sleep(5)
    twaalfde()

def dertiende():
    print("\nSteve pakt de bijl en een van de drie spelers probeer Steve te bevechten. Steve"
    "\nkon hem uit de uitdaging te elimineren, daarna rent Steve het bos in maar realiseert zich"
    "\ndat hij een snee in zijn buik heeft.\n"
    "\nWat moet Steve doen?\n"
    "\nA: vecht tegen sommige spelers en probeer iets voor ze buik te vinden."
    "\nB: Verbergen en zijn laatste krachten gebruiken om tegen de laatste speler te vechten.")
    choice13 = input("A of B --> ")
    if choice13 in answer_A:
        zeventiende()
    elif choice13 in answer_B:
        einde2()
    else:
        print(Anders)
        time.sleep(5)
    dertiende()

def einde2():
    while True:
        print("\nSteve blijft 2 dagen verborgen in een grot totdat alleen hij en de laatste overlevende"
        "\noverblijven. Het probleem is dat Steve erg zwak is omdat hij honger en dorst heeft. Bij het"
        "\nverlaten van de grot komt Steve oog in oog te staan met de laatste overlevende van de"
        "\nuitdaging. Steve kan niets doen omdat hij te zwak is en sterft door het zwaard van zijn tegenstander.\n"
        "\nWil je Opnieuw Spelen?\n")
        choicefinish2 = input("Ja of Nee --> ")
        if choicefinish2 in Ja:
            os.system("cls")
            eerste()
        elif choicefinish2 in Nee:
            break
        else:
            print(Anders)
            time.sleep(5)
        einde2()

def vijftiende():
    print("\nSteve begint te werken aan een bijl met stenen en hout die hij in het bos vindt. hij"
    "\nprobeert zoveel mogelijk te voorkomen dat hij met de andere spelers vecht omdat sommige spelers"
    "\nal bijlen, zwaarden en bogen hebben die ze in het midden van de cirkel hebben genomen aan het"
    "\nbegin van de uitdaging. Bij het afwerken en slijpen van de bijl denkt Steve aan twee mogelijkheden."
    "\nWat moet Steve doen?\n"
    "\nA: Zoeken naar voedsel en zich verstoppen totdat de laatste overlevende van de uitdaging overblijft."
    "\nB: Een aantal spelers proberen te elimineren om hun wapens te krijgen en sterker te worden. ")
    choice14 = input("A of B --> ")
    if choice14 in answer_A:
        zestiende()
    elif choice14 in answer_B:
        zeventiende()
    else:
        print(Anders)
        time.sleep(5)
    vijftiende()

def zestiende():
    print("\nNa een groot gevecht heeft Steve de laatste overlevende geëlimineerd en wint de uitdaging."
    "\nDaarna verschijnt er een portaal voor hem en wanneer hij het portaal binnengaat word alles wit, wanneer" 
    "\nzijn visie terugkeert realiseert hij zich dat hij in het kantoor van zijn vader in de speelhaal"
    "\nis. Steve opent de laptop op tafel en bekijkt de programmer code van de game om meer te begrijpen."
    "\nAls hij naar de spelerslijst kijkt, ziet hij dat er 2 makers zijn met hetzelfde uiterlijk als zijn"
    "\nvader. De eerste maker heeft een jonger uiterlijk, hetzelfde uiterlijk als toen Steve's vader"
    "\nverdween. De tweede maker heeft een ouder uiterlijk. Steve ziet dat er op beide profielen een knop"
    "\nstaat met de tekst 'vrijlaten'."
    "\nWie moet Steve vrijgeven"
    "\nA: Steve’s jonger uitziende vader"
    "\nB: Steve’s ouder uitziende vader")
    choice15 = input("A of B --> ")
    if choice15 in answer_A:
        einde3()
    elif choice15 in answer_B:
        einde4()
    else:
        print(Anders)
        time.sleep(5)
    zestiende()

def zeventiende():
    print("\nSteve heeft 2 spelers geëlimineerd en krijgt verband en een boog. Nu ontbreekt alleen"
    "\nSteve en nog een speler. Het probleem is dat Steve erg moe is en erg geblesseerd"
    "\nvan de vorige gevechten.\n"
    "\nWat moet Steve doen?\n"
    "\nA: Het laatste speler proberen te vinden."
    "\nB: Verstoppen en proberen te zich herstellen")
    choice16 = input("A of B --> ")
    if choice16 in answer_A:
        zestiende()
    elif choice16 in answer_B:
        einde2()
    else:
        print(Anders)
        time.sleep(5)
    zestiende()

def einde3():
    while True:
        print("\nSteve kiest ervoor om zijn jonger uitziende vader vrij te laten. Wat Steve niet"
        "\nwist, was dat zijn jong uitziende vader eigenlijk een programa was met het uiterlijk van zijn"
        "\nechte vader. Steve's vader heeft hem gecreëerd en noemde hem 'Jeff', Jeff had als doel de"
        "\nonvolkomenheden van die virtuele wereld te herstellen. Het probleem was dat Jeff op een dag"
        "\nbesefte dat de grootste onvolmaaktheid de mensheid was, Jeff heeft Steve's vader verraadde en hem"
        "\nbijna vermoordde. En nu dat Steve Jeff uit die virtuele wereld heeft verlost. Jeff zal het hele"
        "\nmenselijke ras elimineren.\n"
        "\nWil je Opnieuw Spelen?\n")
        choicefinish3 = input("Ja of Nee --> ")
        if choicefinish3 in Ja:
            os.system("cls")
            eerste()
        elif choicefinish3 in Nee:
            break
        else:
            print(Anders)
            time.sleep(5)
        einde3()

def einde4():
    while True:
        print("\nSteve kiest ervoor om zijn ouder uitziende vader vrij te laten. En dat was het"
        "\njuiste om te doen, want zijn jong uitziende vader was eigenlijk een programma die op zijn"
        "\nechte vader leek. Steve's vader heeft hem gecreëerd en noemde hem 'Jeff', Jeff had als doel de"
        "\nonvolkomenheden van die virtuele wereld te herstellen. Het probleem was dat Jeff op een dag besefte"
        "\ndat de grootste onvolmaaktheid de mensheid was, Jeff heeft Steve's vader verraadde en hem bijna"
        "\nvermoordde. Steve bevrijdt zijn echte vader uit die wereld en dan verwijdert Steve het hele programma"
        "\nom Jeff te vernietigen en zodat niemand ooit meer in die wereld zou kunnen komen.\n"
        "\nWil je Opnieuw Spelen?\n")
        choicefinish4 = input("Ja of Nee --> ")
        if choicefinish4 in Ja:
            os.system("cls")
            eerste()
        elif choicefinish4 in Nee:
            break
        else:
            print(Anders)
            time.sleep(5)
        einde4()

    
eerste()