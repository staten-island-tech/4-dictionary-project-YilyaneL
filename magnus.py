def mango():
    HONI = 0
    honeel = ["H","O","N","I"]
    letters = list(input("put your honi letters here "))
    x = 0
    for i in letters:
        if i == honeel[x]:
            x +=1
        if x >= 4:
            x = 0
            HONI += 1
    print(HONI)
mango()