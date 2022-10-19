h = [["|     |\t"],["|     |\t"], ["|_____|\t"], ["|     |\t"], ["|     |\t"]]
e = [["       \t"],["      \t"],["  ___ \t"], [" /___\ \t"], [" \___\t"]]
def add(fromn, n):
    for f in range(len(n)):
        fromn[f][0] += n[f][0]
    return fromn
e = add(h, e)
e = add(e, e)
for f in e:
    print(f[0])