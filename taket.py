import time 
import random

def taket():
    print("Välkommen! du har valt taket ")
    print("Du och din kompis ska ta er genom taket in till banken utan att bli tagna")
    print("Nedan har du 2 påståenden du ska välja för att starta spelet")
    return print("Lycka till!")
# detta gjorde jag senast (2023-12-15)

def taket1():
    print("Du tar sönder glaset på taket och hoppar ner")

def taket2():
    print("Du får en kofot och ett rep och sedan skall du ta dig ner")  
    
while True:
    menyval1 = input(
    """
    1. Ta sönder glaset och ta dig ner
    2. Använd kofot och rep och ta dig ner
    
    """
    )
    print("\n".join(menyval1))
    menyval2 = input("Välj en siffra 1 eller 2:")
# hit kom jag senast (2023-12-18)
    
    if menyval2 == "1":
        taket1()
    
    elif menyval2 == "2":
        taket2()
        
