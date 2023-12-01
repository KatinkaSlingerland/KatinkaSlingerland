with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0
getallen={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9};


def findgetal(zoekindex):
    global index
    index = regel.find(getal,zoekindex)
    if index > -1:
        print(getal + ' gevonden in ' + regel + ': plek ' + str(index))
        gevondengetallen[index] = getallen[getal]
        findgetal(index+1)

for regelunformatted in contents:
    regel = regelunformatted.strip()
    som=0
    gevondengetallen = {}
    print(regel)

    for getal in list(getallen.keys()):
        findgetal(0)

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
    print(keysList)
    som = str(gevondengetallen[keysList[0]]) + str(gevondengetallen[keysList[-1]])
    print(som)
    totaal += int(som)

    print(f'totaal {totaal}')
