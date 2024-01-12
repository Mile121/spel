#lägger till kommentar

def skriv_Framdörr ():
    Framdörr="Du står framför banken och du ska välja mellan att, 1 spränga dörren eller 2 öppna dörren"
    print(Framdörr)


skriv_Framdörr()




while True:

    menyval = input("""
                    1.Spränga framdörren
                    2.Öppna dörren



                       """)
    
    if menyval == '1': 
         print("Du sprängde framdörren till banken, perfekt. Nu är du inne i banken") 

    
    if menyval == '2':
        print("Du valde att öppna dörren till banken nu är du i banken utan att någon har märkt")





def ja ():
    print()
    print()

