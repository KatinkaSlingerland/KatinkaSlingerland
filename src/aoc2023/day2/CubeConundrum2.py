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

    totaalRonde = 0
    redMin = 0
    blueMin = 0
    greenMin = 0

    for num, ronde in enumerate(gesplit, start=1):

        print(ronde)

        kleuren = ronde.split(',')
        for kleur in kleuren:
            getal = re.search(r'\d+', kleur).group()
            print('gevonden nummer in kleur '+ kleur + ': '+getal)
            num = re.search(r'\d+', kleur).group()
            if kleur.find('red')>-1 :
                print('het is rood')
                if(int(num) > redMin) :
                    redMin=int(num)
            elif kleur.find('blue')>-1 :
                print('het is blauw')
                if (int(num) > blueMin):
                    blueMin= int(num)
            elif kleur.find('green')>-1:
                print('het is groen')
                if (int(num) > greenMin):
                    greenMin=int(num)

        print ('ronde ' + gesplit[0] + ' rood ' + str(redMin) + ' blauw ' + str(blueMin) + ' groen ' + str(greenMin))

        totaalRonde=redMin*blueMin*greenMin
    totaal+=totaalRonde
print(totaal)