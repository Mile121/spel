import time
import os
# Vi har 
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def scroll_text(text, speed=0.2):
    width = 30
    x = 0
    while True:
        clear_console()
        print(text[x:x+width].ljust(width))
        time.sleep(speed)
        x += 1
        if x >= len(text):
            x = 0
            break

if __name__ == "__main__":
    text_to_scroll = (
    """
    Välkommen till Mazebank rånet, du och din kompis är profesionella bankrånare. Erat mål är att komma in i banken utan att bli sädda. Vilken väg väljer ni?"""
    )
    scroll_text(text_to_scroll)

