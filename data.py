#!/usr/bin/env python
"""
Maak een functie die data (bv. van een sensor) in een lijst stopt. Er worden steeds 20 items in de lijst gestoken,
het gemiddelde print je af. Zorg dat je de loop kan onderbreken met een door jou gekozen symbool/letter/nummer/...
"""

# import


__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"

import random
import time
import keyboard


def put_data_in_list(data, data_list):
    if len(data_list) >= 20:
        print_average(data_list)
        data_list.clear()
        time.sleep(0.5)

    data_list.append(data)



def print_average(data_list):
    print("the average from the last 20 readings are:", sum(data_list) / len(data_list))


def main():
    data_list = []
    print("press q to quit")
    while True:
        data = random.randint(1, 100)
        put_data_in_list(data, data_list)

        if keyboard.is_pressed('q'):
            break


if __name__ == '__main__':
    main()
