def engofre():
    sentence = (input("sentence here"))
    t = 0
    s = 0
    sentence = list(sentence)
    for i in sentence:
        if i == "t" or i == "T":
            t += 1
        elif i == "s" or i == "S":
            s += 1
    if t > s:
        print("english")
    elif s > t:
        print("french")
    elif t == s:
        print("french")
engofre()