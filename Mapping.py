ciphertext =  open('ciphertext.txt', 'r').read()
finalOut = open('out21.txt','r').read()

ciphertext = ''.join(ciphertext.split())
finalOut = ''.join(finalOut.split())



dict = {}
index = 0
while len(dict) < 26:
    dict[finalOut[index]] = ciphertext[index]
    index += 1


print dict