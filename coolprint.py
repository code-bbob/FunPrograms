import time

letters = "HELLO WORLD"
length = len(letters)

for i in range(length):
    order=65
    while order <=ord(letters[i]):
        if (i==0):
            print(chr(order))
            time.sleep(0.08)
        else:
            for j in range(i):  
                print(letters[j],end='')
            print(chr(order))
            time.sleep(0.08)
        order += 1