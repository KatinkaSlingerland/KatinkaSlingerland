with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0

T = [[]]
teller=0

for x in contents:
    lokaal = x.strip()
    T.insert(teller,list(lokaal))
    teller+=1


def getcharacterFromGrid(T, top, left):
    try:
        return T[top][left]
    except:
        return '.'


def checkNeighbourOnSpecialChars(T, numrow, numcharStart, numcharEind):
    specialChar = False
    print('coordinaten rij ' + str(numrow) + ' start ' + str(numcharStart) + ' eind ' +str(numcharEind))

    neighbours=[]

    neighbours.append(getcharacterFromGrid(T, numrow, numcharStart-1))

    for i in range(numcharStart-1, numcharEind+2):
        neighbours.append(getcharacterFromGrid(T, numrow-1, i))
        neighbours.append(getcharacterFromGrid(T, numrow+1, i))

    neighbours.append(getcharacterFromGrid(T, numrow, numcharEind+1))
    print(neighbours)

    for neighbour in neighbours :
        try:
            int(neighbour)
        except:
            if neighbour!='.':
                specialChar=True

    return specialChar


som = 0

for numrow, row in enumerate(T, start=0):
    specialNeighbour = False
    volledigGetal=''
    startPositie=-1
    eindPositie=-1
    for numchar, char in enumerate(row, start=0):
        try:
            int(char)
            if startPositie ==-1:
                startPositie = numchar
            if startPositie != -1:
                eindPositie = numchar
            volledigGetal+=char
            if eindPositie == len(row)-1 :
                print('YO ' + volledigGetal + ' ' + str(startPositie) + ' ' + str(eindPositie))
                specialNeighbour = checkNeighbourOnSpecialChars(T, numrow, startPositie, eindPositie)
                print('speciale buurman? ' + volledigGetal + str(specialNeighbour))
                if specialNeighbour:
                    totaal += int(volledigGetal)

                volledigGetal = ''
                startPositie = -1
        except:
            if startPositie != -1:
                print('YO ' + volledigGetal + ' ' + str(startPositie) + ' ' + str(eindPositie))
                specialNeighbour = checkNeighbourOnSpecialChars(T, numrow, startPositie, eindPositie)
                print('speciale buurman? '+ volledigGetal + str(specialNeighbour))
                if specialNeighbour:
                    totaal+=int(volledigGetal)

                volledigGetal=''
                startPositie=-1
print(totaal)