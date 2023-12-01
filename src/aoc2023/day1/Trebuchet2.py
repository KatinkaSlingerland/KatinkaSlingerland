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

for x in contents:
    lokaal = x.strip()
    som=0
    beginInt = None
    eindInt = None

    for element in lokaal:
        som=0
        try:
            int(element)
            print ('int ' + element)
            if beginInt==None :
                beginInt=element
                print ('begin ='+ beginInt)
            else :
                eindInt=element
                print('eind =' + eindInt)
        except:
            pass

    if eindInt == None and beginInt != None:
        som = str(beginInt) + str(beginInt)
        print('if '+som)
    else:
        som = str(beginInt) + str(eindInt)
        print('else ' +som)
    totaal += int(som)

    print(f'totaal{totaal}')
