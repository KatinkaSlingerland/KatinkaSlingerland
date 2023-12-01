def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0
getallen={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9};

for x in contents:
    regel = x.strip()
    som=0
    beginInt = None
    eindInt = None

    gevondengetallen = {}

    print(regel)

    for getal in list(getallen.keys()):
        index = regel.find(getal)
        if index >-1:
            gevondengetallen[index] = getallen[getal]
            print(getal + ' gevonden in ' + regel + ': plek ' + str(index))

    for num, element in enumerate(regel, start=0):
        som=0
        try:
            int(element)
            print(element + ' gevonden in ' + regel + ': plek ' + str(num))
            gevondengetallen[num] = int(element)
        except:
            pass

    print(gevondengetallen)
    keysList = list(gevondengetallen.keys())
    keysList.sort()
    # print(keysList)
    # print('eerste')
    # print(gevondengetallen[keysList[0]])
    # print('laatste' + str(keysList[len(keysList)-1]))
    # print(gevondengetallen[keysList[len(keysList)-1]])
    som = str(gevondengetallen[keysList[0]]) + str(gevondengetallen[keysList[len(keysList)-1]])
    print(som)
    totaal += int(som)

    # if eindInt == None and beginInt != None:
    #     som = str(beginInt) + str(beginInt)
    #     print('if '+som)
    # else:
    #     som = str(beginInt) + str(eindInt)
    #     print('else ' +som)
    # totaal += int(som)
    #
    print(f'totaal{totaal}')
