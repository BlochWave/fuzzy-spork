# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

# First construct a dictionary
import time

start = time.time();
dict = { 
    '1'  : 'one',
    '2'  : 'two',
    '3'  : 'three',
    '4'  : 'four',
    '5'  : 'five',
    '6'  : 'six',
    '7'  : 'seven',
    '8'  : 'eight',
    '9'  : 'nine',
    '10' : 'ten',
    '11' : 'eleven',
    '12' : 'twelve',
    '13' : 'thirteen',
    '14' : 'fourteen',
    '15' : 'fifteen',
    '16' : 'sixteen',
    '17' : 'seventeen',
    '18' : 'eighteen',
    '19' : 'nineteen',
    '20' : 'twenty',
    '30' : 'thirty',
    '40' : 'forty',
    '50' : 'fifty',
    '60' : 'sixty',
    '70' : 'seventy',
    '80' : 'eighty',  
    '90' : 'ninety',
    '00' : 'hundred',
    };


total = 0;
for x in range(1,1001):
    digits = len(str(x));
    word = '';
    # print x
    if digits == 1:
        total += len(dict.get(str(x)));
        word = dict.get(str(x))
    elif digits == 2:
        if int(str(x)) < 20 or int(str(x)[1]) == 0:
            total += len(dict.get(str(x)));
            word = dict.get(str(x));
        else:
            total += len(dict.get(str(x)[0]+'0')) + len(dict.get(str(x)[1]));
            word = dict.get(str(x)[0]+'0') + dict.get(str(x)[1]);
    elif digits == 3:
        if int(str(x)[1:]) == 0:
            total += len(dict.get(str(x)[0])) + len('hundred');
            word = dict.get(str(x)[0]) + 'hundred'
        else:
            total += len(dict.get(str(x)[0])) + len('hundred') + len('and');
            word = dict.get(str(x)[0]) + 'hundred' + 'and';
            if int(str(x)[1:]) < 20 or int(str(x)[2]) == 0:
                total += len(dict.get(str(int(str(x)[1:]))));
                word += dict.get(str(int(str(x)[1:])));
            else:
                total += len(dict.get(str(x)[1]+'0')) + len(dict.get(str(x)[2]));
                word += dict.get(str(x)[1]+'0') + dict.get(str(x)[2]);
    else:
        total += len('onethousand')
        word = 'onethousand'
    # print x, word

print total, time.time() - start ;






# def two_digits(n):
#     y = len(str(n)) - 2;
#     x = int(str(n)[y:]);
#     if int(str(x)) < 20 or int(str(x)[1]) == 0:
#         return len(dict.get(str(x)));
#     else:
#         return len(dict.get(str(x)[0]+'0')) + len(dict.get(str(x)[1]));
