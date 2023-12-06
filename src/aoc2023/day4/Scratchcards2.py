import re

with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0
cards={}

def vulKaartenWinstAan(gameNumber, winstaantal):
    for x in range(1, winstaantal+1):
        andereRonde = int(gameNumber)+x
        # print(str(x) + ' ' + str(andereRonde))
        if andereRonde <= len(contents):
            if str(andereRonde) not in cards:
                cards[str(andereRonde)]=1
            cards[str(andereRonde)] += 1

for x in contents:
    lokaal = x.strip()
    lokaal = re.sub(r'  ', ' ', lokaal)
    zonderGame = re.sub(r'Card ', '', lokaal)
    zonderGame = re.sub(r': ', '|', zonderGame)

    gesplit = zonderGame.split('|')
    print(gesplit)

    gameNumber = gesplit[0].strip()
    cardNumbers = gesplit[1].strip().split(' ')
    myNumbers = gesplit[2].strip().split(' ')

    print(cardNumbers)
    print(myNumbers)

    matches = list(set(cardNumbers).intersection(myNumbers))

    if str(gameNumber) not in cards:
        cards[str(gameNumber)] = 1

    print(gameNumber + ': aantal matches ' +str(len(matches)))
    if len(matches)>0:
        # print('aantal kaarten in dit spel:' + str(cards[gameNumber]))
        for x in range(0, cards[gameNumber]):
            vulKaartenWinstAan(gameNumber, len(matches))
    print(cards)
print(sum(cards.values()))
