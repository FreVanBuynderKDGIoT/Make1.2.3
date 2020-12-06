#!/usr/bin/env python
"""
info about our project
"""

# import
import sys
from init import *
import pylrc
import vlc

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"


def SongFinished(event):
    global song_has_finished
    print("Event reports - finished")
    song_has_finished = True
    # Show the cursor
    sys.stdout.write("\033[?25h")


class Liedje:
    def __init__(self, tekst, liedje):
        self.tekst = tekst
        self.liedje = liedje

    def zingen(self):
        lrc_file = open(self.tekst, encoding="utf8", errors='ignore')
        lrc_string = ''.join(lrc_file.readlines())
        lrc_file.close()

        subs = pylrc.parse(lrc_string)

        mp3_file = self.liedje

        song_has_finished = False

        instance = vlc.Instance()
        player = instance.media_player_new()
        media = instance.media_new_path(mp3_file)  # Your audio file here
        player.set_media(media)
        events = player.event_manager()
        events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished)

        print("Playing {0} from {1}".format(subs.title, subs.artist))
        player.play()

        line = 0
        num_lines = len(subs)
        line_printed = False

        while not song_has_finished:
            sec = player.get_time() / 1000

            if line+1 == num_lines or sec < subs[line+1].time:

                if not line_printed:
                    print("\r {0}".format(subs[line].text.rstrip(), end='', flush=True))

                    line_printed = True
            else:
                line += 1
                line_printed = False


