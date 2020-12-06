#!/usr/bin/env python
"""
Een python script dat random wachtwoorden genereert.
zowel kleine letters als grote, cijfers en tekens
op aanvraag de complexiteit (aantal tekens en soort tekens)
maak gebruik van flowcontrol en functies!
"""

# import
import random

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')']


class Password:
    def __init__(self, length, dig, upcase, lowcase, special):
        self.length = length
        self.dig = dig
        self.upcase = upcase
        self.lowcase = lowcase
        self.special = special

    def generate_password(self):
        length = self.length
        combined_list = []
        temp_pass = []
        counter = 0

        if self.dig:
            combined_list += DIGITS
            # puts at least one character this set in the password
            temp_pass.append(random.choice(DIGITS))
            counter += 1
        if self.upcase:
            combined_list += UPCASE_CHARACTERS
            # puts at least one character this set in the password
            temp_pass.append(random.choice(LOCASE_CHARACTERS))
            counter += 1

        if self.lowcase:
            combined_list += LOCASE_CHARACTERS
            # puts at least one character this set in the password
            temp_pass.append(random.choice(UPCASE_CHARACTERS))
            counter += 1

        if self.special:
            combined_list += SYMBOLS
            # puts at least one character this set in the password
            temp_pass.append(random.choice(SYMBOLS))
            counter += 1

        # - counter because there already so many characters in the password because of the if statements
        for x in range(length - counter):
            temp_pass.append(random.choice(combined_list))
            # shuffles the list otherwise it is too predictable
            random.shuffle(temp_pass)

        gen_password = ""

        for x in temp_pass:
            gen_password += x

        return gen_password


if __name__ == "__main__":
    password = Password(12, True, True, True, True)
    print(password.generate_password())
