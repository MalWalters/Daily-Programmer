input = open('280-input.txt').read().split()

def countfingers(fingerpos):
    
    left = fingerpos[:5]
    right = fingerpos[5:]
    valid = True
    number = 0

# Count right
    for i in range(4,1,-1):
        if (right[i] == "0" and number > i):
            valid = False
        elif (right[i] == "1" and number < i):
            number += i
    if right[0] == "1":
        number +=5

# Count left
    for i in range(1,4):
        if (left[i] == "0" and number >= 40 - i * 10):
            valid = False
        elif (left[i] == "1" and number <= 40 - i * 10):
            number += i * 10   
    if left[4] == "1":
        number += 50
    
    if valid:
        return str(number)
    else:
        return "Invalid"

for lines in input:
    print(lines + " -> " + countfingers(lines))
