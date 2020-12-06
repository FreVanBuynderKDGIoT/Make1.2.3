#!/usr/bin/env python
"""
Een python script dat random wachtwoorden genereert.
zowel kleine letters als grote, cijfers en tekens
op aanvraag de complexiteit (aantal tekens en soort tekens)
maak gebruik van flowcontrol en functies!
"""

__author__ = "Fre Van Buynder"
__email__ = "fre.vanbuynder@student.kdg.be"
__status__ = "Development"

from init import Password


def get_length():
    try:
        length = int(input("Hoe lang moet uw wachtwoord zijn: "))
    except ValueError as err:
        print("Dit is geen juiste waarde:", err)
        get_length()
    return length


def get_digits():
    digits = input("Wilt u cijfers gebruiken? Ja/Nee: ")
    if digits == "Ja":
        return True
    elif digits == "Nee":
        return False
    else:
        print("Dit is geen goede waarde: ")
        get_digits()


def get_locase():
    lowercase = input("Wilt u kleine letters gebruiken? Ja/Nee: ")
    if lowercase == "Ja":
        return True
    elif lowercase == "Nee":
        return False
    else:
        print("Dit is geen goede waarde")
        get_locase()


def get_upcase():
    uppercase = input("Wilt u grote letters gebruiken? Ja/Nee: ")
    if uppercase == "Ja":
        return True
    elif uppercase == "Nee":
        return False
    else:
        print("Dit is geen goede waarde")
        get_upcase()


def get_special():
    special = input("Wilt u speciale tekens gebruiken? Ja/Nee: ")
    if special == "Ja":
        return True
    elif special == "Nee":
        return False
    else:
        print("Dit is geen goede waarde")
        get_special()


def main():
    passwordsettings = Password(get_length(), get_digits(), get_upcase(), get_locase(), get_special())

    print("\n\nUw gegenereerde wachtwoord is:", passwordsettings.generate_password())


if __name__ == '__main__':
    main()
