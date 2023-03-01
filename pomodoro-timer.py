#!/usr/bin/python

import sys
import time
import vlc

total_runs = 0
total_mins = 0
player_end = vlc.MediaPlayer('/usr/local/bin/sounds/Bernd_Ungerer_T2')
player_start = vlc.MediaPlayer('/usr/local/bin/sounds/Hans_freetts.mp3')
player_long_break = vlc.MediaPlayer('/usr/local/bin/sounds/bernd-15-min')

def pomodoro():
    global total_mins
    global mins
    global total_runs
    global player

    mins = 0
    while mins <= 24: 
        time.sleep(60) 
        mins += 1 
        total_mins += 1 
        print(25 - mins, "Minuten verbleibend.")
    print("Ende der 25 Minuten.")
    player_end.play()
    time.sleep(6)
    total_runs +=1
    print("Totale Pomodoro-Timer: ", total_runs)
    player_end.stop()

def breaks():
    global total_runs
    
    mins = 0
    if total_runs < 4:
        print('Es geht los! 5 Minuten ab jetzt.')
        while mins != 5:
            time.sleep(60)
            mins += 1
            print(mins, " Minuten Pause beendet.")
        player_start.play()
        time.sleep(6)

    elif total_runs >= 4:
        print('Nimm eine Pause von 15 Minuten.')
        print('Es geht los! 15 Minuten ab jetzt.')
        while mins != 15:
            time.sleep(60)
            mins += 1
            print(mins, " Minuten Pause beendet.")
        total_runs = 0
        player_long_break.play()
        time.sleep(6)
    
    player_start.stop()
    player_long_break.stop()


def main():
    carry_on = 'y'
    while carry_on=='y'or carry_on=='Y':
        print('Es geht los! 25 Minuten starten jetzt.')
        pomodoro()
        breaks()
        carry_on = input("Bereit für weitere 25 Minuten? (y/n)")
    
    end_session = 'n'

    # print("End of task ",task,". \nTotal time worked was minutes ", total_mins, " minutes.")

if __name__ == '__main__':
    main()
