with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0
stars={}
T = [[]]
teller=0
completeSums=[]

for x in contents:
    lokaal = x.strip()
    T.insert(teller,list(lokaal))
    teller+=1


def getcharacterFromGrid(T, top, left):
    try:
        character = T[top][left]
        return character
    except:
        return '.'


def addToDictionary(key, value):
    if key in stars:
        stars[key].append(int(value))
        completeSums.append(key)
    else:
        stars[key] = [int(value)]

def checkNeighbourOnSpecialChars(T, numrow, numcharStart, numcharEind):
    specialChar = False
    print('coordinaten rij ' + str(numrow) + ' start ' + str(numcharStart) + ' eind ' +str(numcharEind))

    neighbours=[]

    # karakterlinks
    char = getcharacterFromGrid(T, numrow, numcharStart - 1)
    neighbours.append(char)
    if char == '*':
        addToDictionary(str(numrow) + 'k' + str(numcharStart - 1), int(volledigGetal))

    # karakters boven en onder
    for i in range(numcharStart-1, numcharEind+2):
        # boven
        char = getcharacterFromGrid(T, numrow - 1, i)
        neighbours.append(char)
        if char == '*':
            addToDictionary(str(numrow-1) + 'k' + str(i), int(volledigGetal))
        # onder
        char = getcharacterFromGrid(T, numrow + 1, i)
        neighbours.append(char)
        if char == '*':
            addToDictionary(str(numrow+1) + 'k' + str(i), int(volledigGetal))

    # karakterrechts
    char = getcharacterFromGrid(T, numrow, numcharEind+1)
    neighbours.append(char)
    if char == '*':
        addToDictionary(str(numrow)+'k'+str(numcharEind+1), int(volledigGetal))
    print(neighbours)

    for neighbour in neighbours :
        try:
            int(neighbour)
        except:
            if neighbour=='*':
                specialChar=True

    return specialChar

for numrow, row in enumerate(T, start=0):
    volledigGetal=''
    startPositie=-1
    eindPositie=-1
    # loop door alle karakters heen in een rij
    for numchar, char in enumerate(row, start=0):
        # is het een getal? zet dat dan in een object, plak evt aan de vorige vast
        try:
            int(char)
            if startPositie ==-1:
                startPositie = numchar
            if startPositie != -1:
                eindPositie = numchar
            volledigGetal+=char
            # komt ie op het eind van de regel uit, moet hij ook stoppen met verder zoeken
            if eindPositie == len(row)-1 :
                raise Exception("Einde van de regel bereikt, buren zoeken aub")
        # is het geen getal, dan is het getal compleet en kan je de buurkarakters gaan opvragen, rondom
        except:
            if startPositie != -1:
                print('Getal gevonden: ' + volledigGetal)
                specialNeighbour = checkNeighbourOnSpecialChars(T, numrow, startPositie, eindPositie)
                print('sterretje als buurman? ' + str(specialNeighbour))

                volledigGetal=''
                startPositie=-1

for complete in completeSums:
    sum=stars[complete][0]*stars[complete][1]
    totaal+=sum
print(completeSums)
print(stars)
print(totaal)