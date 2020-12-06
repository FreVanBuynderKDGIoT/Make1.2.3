#!/usr/bin/env python
"""
info about our project
"""

from init import Liedje

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


def main():
    try:
        choice = int(input("welk liedje wil je horen?:\n"
                           "1) bohemian rhapsody by queen\n"
                           "2) someone to you by banners\n"))
        if choice == 1:
            tekst = "bohemian rhapsody/Bohemian Rhapsody by Queen.lrc"
            mp3_file = "bohemian rhapsody/QueenBohemian Rhapsody (Official Video Remastered).mp3"
        elif choice == 2:
            tekst = "someone to you/someone to you by banners.lrc"
            mp3_file = "someone to you/Banners - Someone To You.mp3"
        else:
            print("dit is geen nummer.")
            main()

    except ValueError as err:
        print("dit is geen juiste waarde:", err)
        main()

    song = Liedje(tekst, mp3_file)
    song.zingen()


if __name__ == '__main__':
    main()
