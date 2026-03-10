import sys
import time

def start_lyrics():

    BLUE = '\u001B[34m'
    RESET = '\u001B[0m'

    ascii_art = """\

░█████╗░██╗░░██╗░█████╗░██████╗░██╗██╗░░░
██╔══██╗██║░██╔╝██╔══██╗██╔══██╗██║██║░░░
███████║█████═╝░███████║██████╔╝██║██║░░░
██╔══██║██╔═██╗░██╔══██║██╔══██╗██║██║░░░
██║░░██║██║░╚██╗██║░░██║██║░░██║██║██║██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝╚═╝"""

    print(BLUE + ascii_art)

    lyrics = [
        ("Oh, penjaga hatiku, oh", 0.5),
        ("Karna bersamamu semua terasa indah", 0.12),
        ("Gundah gulana hatiku pun hancur sirna", 0.12),
        ("Janji ku tak kan ku lepas wahai kau bidadariku dari surga", 0.12),
        ("Tuk selamanya", 0.16),
        ("Tuk selamanya", 0.16),
        ("Tuk selamanya", 0.16),
    ]

    delay = [0.5, 0.2, 0.3, 0.4, 0.8, 0.7, 0.5]

    print(f"\n{RESET}――――― {BLUE}penjaga hati - Nadhif Basalamah {RESET}―――――\n")
    
    for i, (song_line, character_delay) in enumerate(lyrics):
        for character in song_line:
            print(f"{BLUE}{character}", end='')
            sys.stdout.flush()
            time.sleep(character_delay)
        time.sleep(delay[i])
        print('')

    print(f"{RESET}\n// Code by {BLUE}Micola Arighi {RESET}- Modified by {BLUE}XzeelArcadia{RESET}\n")

start_lyrics()