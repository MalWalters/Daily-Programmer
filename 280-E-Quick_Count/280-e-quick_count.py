input = open('280-input.txt').read().split()

number = 0

def countright(fingers, number):
    for i in range(4,1,-1):
        if (fingers[i] == "0" and number > i):
            return "Invalid"
        elif (fingers[i] == "1" and number < i):
            number += i
    if fingers[0] == "1":
        number +=5
    return number

def countleft(fingers, number):
    for i in range(1,4):
        if (fingers[i] == "0" and number >= 40 - i * 10):
            return "Invalid"
        elif (fingers[i] == "1" and number <= 40 - i * 10):
            number += i * 10
    if fingers[4] == "1":
        number += 50
    return number

for lines in input:
    try:
        print(lines + " -> " + str(countleft(lines[:5], number) + countright(lines[5:],number)))
    except:
        print(lines + " -> Invalid")

