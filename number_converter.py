#!/usr/bin/env python3
'''
convert decimal number to binary
via standard python function
'''
def convert_to_bin(number):
    return bin(number)[2:]
'''
convert decimal number to octal
via standard python function
'''
def convert_to_oct(number):
    return oct(number)[2:]
'''
convert decimal number to hexadecimal
via standard python function
'''
def convert_to_hex(number):
    return hex(number)[2:].upper()
'''
convert decimal number any counting system given by x
'''
def convert_to_x(number,x):
    numberlist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    finish = False
    converted_num = ''
    tmp_num = number
    while not finish:
        if tmp_num // x > 0:
            rest = tmp_num % x
            converted_num = numberlist[rest]+converted_num
            tmp_num = tmp_num // x
        else:
            rest = tmp_num % x
            converted_num = numberlist[rest]+converted_num
            finish = True
    return converted_num
'''
Main Program here
'''
print("this tool converts decimal numbers to any other numbering system")
input_not_ok = True
#
# ask until you get a correct integer
#
while input_not_ok:
    dec_number = input("give me a decimal number: ")
    try:
        dec_number = int(dec_number)
        input_not_ok = False
    except:
        print(" THIS is not a Integer")
#
# print out the different conversion
print("\n")
print("bin : \t {}".format(convert_to_bin(dec_number)))
print("3   : \t {}".format(convert_to_x(dec_number,3)))
print("4   : \t {}".format(convert_to_x(dec_number,4)))
print("5   : \t {}".format(convert_to_x(dec_number,5)))
print("6   : \t {}".format(convert_to_x(dec_number,6)))
print("7   : \t {}".format(convert_to_x(dec_number,7)))
print("oct : \t {}".format(convert_to_oct(dec_number)))
print("9   : \t {}".format(convert_to_x(dec_number,9)))
print("dec : \t {}".format(dec_number))
print("11  : \t {}".format(convert_to_x(dec_number,11)))
print("12  : \t {}".format(convert_to_x(dec_number,12)))
print("13  : \t {}".format(convert_to_x(dec_number,13)))
print("1   : \t {}".format(convert_to_x(dec_number,14)))
print("5   : \t {}".format(convert_to_x(dec_number,15)))
print("hex : \t {}".format(convert_to_hex(dec_number)))
print("1   : \t {}".format(convert_to_x(dec_number,17)))
