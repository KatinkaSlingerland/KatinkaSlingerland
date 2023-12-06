import re

with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0

for x in contents:
    lokaal = x.strip()
    lokaal = re.sub(r'  ', ' ', lokaal)
    zonderGame = re.sub(r'Card ', '', lokaal)
    zonderGame = re.sub(r':', '|', zonderGame)

    gesplit = zonderGame.split('|')
    print(gesplit)

    cardNumbers = gesplit[1].strip().split(' ')
    myNumbers = gesplit[2].strip().split(' ')

    print(cardNumbers)
    print(myNumbers)

    matches = list(set(cardNumbers).intersection(myNumbers))

    print(len(matches))
    if len(matches)>0:
        totaal += 2 ** (len(matches)-1)

print(totaal)
