with open('input.txt') as f:
    contents = f.readlines()
[print(line.strip()) for line in contents]

totaal = 0
map={}
mapnaam = ''
vantotranges=[]
seeds=[]
locs=[]

for x in contents:
    lokaal = x.strip()
    if "seeds:" in lokaal:
        seeds=lokaal.replace("seeds:","").strip().split(' ')
    if "map:" in lokaal:
        if vantotranges.__len__() >0 and str(mapnaam)!="":
            map[mapnaam]= vantotranges
        vantotranges=[]
        mapnaam = lokaal
    elif "" != lokaal:
        vantotrange = lokaal.strip().split(' ')
        vantotranges.append(vantotrange)

#de laatste wil er ook nog bij
map[mapnaam]= vantotranges

print(map)
print(seeds)


def getmatch(mapkind, tofind):
    for x in map[mapkind]:
        if(int(tofind)>=int(x[1]) and int(tofind)<=int(x[1])+int(x[2])):
            # for i in range(int(x[1]), int(x[1])+int(x[2])):
            #     if int(tofind)==i:
            difference = int(tofind)-int(x[1])
            print(mapkind)
            print(int(x[0])+difference)
            return int(x[0])+difference
                    # print(int(x[0])+i-int(x[1]))
                    # return int(x[0])+i-int(x[1])
    return tofind


for seed in seeds:
    print('seed '+seed)
    soil = getmatch('seed-to-soil map:', seed)
    fertilizer = getmatch('soil-to-fertilizer map:', soil)
    water = getmatch('fertilizer-to-water map:', fertilizer)
    light = getmatch('water-to-light map:', water)
    temperature = getmatch('light-to-temperature map:', light)
    humidity = getmatch('temperature-to-humidity map:', temperature)
    location = getmatch('humidity-to-location map:', humidity)
    locs.append(location)
    print('loc ' + str(location))

locs.sort()
print(locs[0])
