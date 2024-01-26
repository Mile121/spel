import time
import random

def start():
    # Välkomstmeddelande och instruktioner för spelet
    print("Du befinner dig vid bankens entré och ser två möjliga ingångar.")
    print("1. Spräng dörren och gå in")
    print("2. Gå in genom dörren")

    # Läs spelarens val
    val = input('Välj ett alternativ, (1/2): ')

    if val == '1':
        Skjutscen()
    elif val == '2':
        Hittavalvet()
    else:
        print("Ogiltigt val. Försök igen.")
        start()

def Skjutscen():
    # Spelare stöter på en vakt och måste välja mellan att övertala eller skjuta
    print('Du går genom entren och stöter på en vakt')
    print('Vill du försöka övertala honom eller skjuta honom?')
    print('1. Övertala vakten')
    print('2. Skjut honom')

    # Läs spelarens val
    val2 = input('Välj ett alternativ, (1/2): ')
    
    if val2 == '1':
        print('Du lyckades tyvärr inte och förlorade')
        start()
    elif val2 == '2':
        Vakt()
    else:
        print("Ogiltigt val. Försök igen.")
        Skjutscen()

def Vakt():
    # Spelare försöker skjuta vakten med en vattenpistol
    print("Du väljer att skjuta säkerhetsvakten.")
    print("Du tar fram din vattenpistol och siktar på vakten.")
    print("Målet är att pricka vakten för att distrahera honom.")
    
    försök = 3  # Antal försök att pricka vakten

    while försök > 0:
        print(f"Du har {försök} försök kvar.")
        skjut_val = input("Tryck 'Enter' för att skjuta: ")
        
        # Slumpmässigt beslut om skottet träffar eller inte
        if random.choice([True, False]):
            print("Du träffar vakten!")
            Hittavalvet()
        
        print("Du missade! Vakten märker dig.")
        försök -= 1

    print("Du har inga fler försök kvar. Vakten utlöser larmet.")
    start()

def Hittavalvet():
    # Spelare kommer till en korridor med två vägar
    print('Du kommer till en korridor med två vägar, vill du gå 1. Höger eller 2. vänster?')
    # Läs spelarens val
    val3 = input('Välj ett alternativ, (1/2): ')
    
    if val3 == '1':
        # Spelare hittar ett papper med koden 1234
        print('Du gick in till ett kontor där du hittade ett papper som det stod 1234 på')
        Hittavalvet()
        
    elif val3 == '2':
        # Spelare kommer till ett rum med en röd knapp
        print('Du kommer till ett rum där du ser en röd knapp')
        print('Vad vill du göra?')
        print('1. Trycka på knappen')
        print('2. Låta bli att trycka')    
        
        # Läs spelarens val
        val4 = input('Välj ett alternativ, (1/2): ')
        
        if val4 == '1':
            # Spelare trycker på knappen och låser alla dörrar
            print('Du tryckte på knappen och alla dörrar till banken låstes, ingen kan förfölja dig')
            Valvet()
        elif val4 == '2':
            # Spelare låter bli att trycka och blir gripen av polisen
            print('Alla dörrar var öppna och polisen kom och grep dig')
            start()
        else:
            print("Ogiltigt val. Försök igen.")
            Hittavalvet()

def Valvet():
    # Spelare kommer fram till valvet och måste skriva in koden
    print('Du kommer fram till valvet men du måste skriva in en kod för att ta dig in')
    print('Du har tre försök på dig')
    print('1. Skriv in koden')
    print('2. Gå runt i banken för att hitta ledtråd')
    
    # Läs spelarens val
    val5 = input('Välj ett alternativ, (1/2): ')

    if val5 == '1':
        # Spelare väljer att skriva in koden
        Koden()
    elif val5 == '2':
        # Spelare väljer att gå runt för att hitta ledtråd
        Hittavalvet()
    else:
        print("Ogiltigt val. Försök igen.")
        Valvet()

def Koden():
    # Spelare gissar koden med tre försök
    rätt_svar = "1234"
    antal_försök = 3

    while antal_försök > 0:
        gissning = input("Gissa koden (fyra siffror): ")

        if gissning == rätt_svar:
            # Spelare har gissat rätt och vunnit
            print("Grattis, du har gissat rätt! Du har vunnit!!!")
            start()
        else:
            # Felaktig gissning, spelaren förlorar ett försök
            antal_försök -= 1
            print(f"Felaktig gissning. Du har {antal_försök} försök kvar.")

    # Spelare har använt alla försök och förlorar
    if antal_försök == 0:
        print("Tyvärr, du har använt alla försök. Rätt svar var 1234.")

# Starta spelet genom att anropa start-funktionen
start()




