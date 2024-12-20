import random
rules = []
orders = []
pageOrder = []
sum = 0
wrongOrders = []


with open('input.txt') as f:
    rules = f.read().split("\n\n")
    for i in rules[1].split("\n"):
        orders.append(i.split(","))
    print(orders[-1])
    rules = rules[0].split("\n")
    

def checkPrinter(pages):
    for i in range(len(pages)):
        for j in range(len(pages)):
            if str(pages[i])+"|"+str(pages[j]) in rules:
                if j<i:
                    return [False, i, j] 
    return [True, 0, 0]

#Part 1            
'''for k in orders:
    if checkPrinter(k)[0]:
        sum += int(k[int(len(k)/2-.05)])
'''

#Part 2 
def reshuffle(pages):
    while True:
        result = checkPrinter(pages)
        if result[0]:
            return pages
        swapA, swapB = result[1], result[2]
        pages[swapA], pages[swapB] = pages[swapB], pages[swapA]
        

for k in orders:
    if not checkPrinter(k)[0]:
        wrongOrders.append(k)

for k in wrongOrders:
    k = reshuffle(k)
    print(k)
    sum += int(k[int(len(k)/2-.05)])

print(sum)



