
#Vi leta efter inromation om hur man gör en skjut scen
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
        print("En vakt kommer framför dig och du måste skjuta honom")

       

import os
import random
import time

# Funktion för att rita spelplanen
def draw_board(player_pos, enemy_pos, projectiles):
    os.system("clear" if os.name == "posix" else "cls")
    for i in range(10):
        row = ""
        for j in range(20):
            if (i, j) == player_pos:
                row += "P"
            elif (i, j) == enemy_pos:
                row += "E"
            elif (i, j) in projectiles:
                row += "*"
            else:
                row += "-"
        print(row)
    print("Use A and D to move, and space to shoot.")

# Funktion för att uppdatera positionerna
def update_positions(player_pos, enemy_pos, projectiles):
    projectiles = [(x, y - 1) for x, y in projectiles if y > 0]
    return player_pos, enemy_pos, projectiles

# Huvudspelloop
def main():
    player_pos = (9, 9)
    enemy_pos = (0, random.randint(0, 19))
    projectiles = []

    while True:
        draw_board(player_pos, enemy_pos, projectiles)

        # Uppdatera positioner
        player_pos, enemy_pos, projectiles = update_positions(player_pos, enemy_pos, projectiles)

        # Kontrollera kollision med fienden
        if player_pos == enemy_pos:
            print("Game Over!")
            break

        # Skapa en ny fiende om den tidigare har nått botten
        if enemy_pos[0] == 9:
            enemy_pos = (0, random.randint(0, 19))

        # Läs in tangenttryckningar
        move = input()
        if move == "a" and player_pos[1] > 0:
            player_pos = (player_pos[0], player_pos[1] - 1)
        elif move == "d" and player_pos[1] < 19:
            player_pos = (player_pos[0], player_pos[1] + 1)
        elif move == " ":
            projectiles.append((player_pos[0] - 1, player_pos[1]))

        time.sleep(0.1)

if __name__ == "__main__":
    main()




        







