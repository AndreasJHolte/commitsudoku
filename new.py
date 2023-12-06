


def recurse(body):
    level=body+1

    if level<10:
        level+=1
        print(recurse(level))
        level-=1
    print(level)
    return level

sap=[[1,[2]],[3,4]]

for it in range(2):
    for yt in range(2):
        if sap[it][yt] not in range(2,5):
            print(sap[it][yt])


print(recurse(1))