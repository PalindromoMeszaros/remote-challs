
import sys

morse_letters = {'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'} 

def morse_conversion(message):
    morse_string = ''
    for letter in message:
        if (letter >= 'A' and letter <= 'Z'):
            morse_string += morse_letters[letter]
        elif (letter == ' '):
            morse_string += ' '
        else:
            print("usage: " + sys.argv[0] + " <a-zA-Z string>")
            exit (1)         
    return (morse_string)

if (len(sys.argv) != 2 or len(sys.argv[1]) < 1):
    print("usage: " + sys.argv[0] + " <a-zA-Z string>")
    exit (1)
if (len(sys.argv) == 2):
    print(morse_conversion(str(sys.argv[1].upper())))