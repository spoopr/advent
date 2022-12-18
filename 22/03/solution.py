input = repr(open("input.txt", "r+").read()).replace("'","").split(r"\n")
check = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

doubles_total = sum([check.index(z) for z in [list(set(x[:int(len(x)/2)])&set(x[int(len(x)/2):]))[0] for x in input]])

triples_total = sum([check.index(letter) for letter in [list(set(x)&set(y)&set(z))[0] for x,y,z in list(zip(input,input[1:],input[2:]))[::3]]])

print(doubles_total, triples_total)
