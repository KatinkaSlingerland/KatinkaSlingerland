import re

with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0

for x in contents:
    lokaal = x.strip()
    zonderGame = re.sub(r'Game ', '', lokaal)
    zonderGame = re.sub(r':', ';', zonderGame)

    gesplit = zonderGame.split(';')
    print(gesplit)

    mogelijk= False

    for num, ronde in enumerate(gesplit, start=1):

        red = 0
        blue = 0
        green = 0
        print(ronde)

        kleuren = ronde.split(',')
        for kleur in kleuren:
            getal = re.search(r'\d+', kleur).group()
            print('gevonden nummer in kleur '+ kleur + ': '+getal)
            num = re.search(r'\d+', kleur).group()
            if kleur.find('red')>-1 :
                print('het is rood')
                red+=int(num)
            elif kleur.find('blue')>-1 :
                print('het is blauw')
                blue+= int(num)
            elif kleur.find('green')>-1:
                print('het is groen')
                green +=int(num)

        print ('ronde '+ gesplit[0] + ' rood '+ str(red)+ ' blauw ' +str(blue) + ' groen ' +str(green))

        if red<=12 and green <=13 and blue <=14 :
            mogelijk = True
        else :
            mogelijk = False
            break

    print(mogelijk)
    if mogelijk :
        totaal+=int(gesplit[0])

print(totaal)