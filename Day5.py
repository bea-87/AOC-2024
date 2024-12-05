import random
rules = []
orders = []
pageOrder = []
sum = 0
wrongOrders = []
with open('bob.txt') as f:
    rules = f.read().split("\n\n")
    for i in rules[1].split("\n"):
        orders.append(i.split(","))
    print(orders[-1])
    rules = rules[0].split("\n")
    

def checkPrinter(pages):
    for i in range(len(pages)):
        for j in range(1, len(pages)):
            if str(pages[i])+"|"+str(pages[j]) in rules:
                if j<i:
                    return [False, i, j] 
    return True

#Part 1            
'''for k in orders:
    if checkPrinter(k)[0]:
        sum += int(k[int(len(k)/2-.05)])
'''

#Part 2 
def reshuffle(pages):
    p    

for k in orders:
    if not checkPrinter(k)[0]:
        wrongOrders.append(k)

for k in wrongOrders:
    reshuffle(k)
    sum += int(k[int(len(k)/2-.05)])
    print(sum)



