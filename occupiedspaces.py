def occupied():
    x = 0
    n = 5
    y = "CCC.."
    t = ".CCCC"
    y = list(y)
    t = list(t)
    for i in range(n):
        if (y[i] == "C" and t[i] == "C"):
            x = x + 1
    print(x)
occupied()