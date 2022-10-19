test = [["       \t"],["      \t"],["  ___ \t"], [" / \t"], [" \___\t"]]
lowerTemplate = [["       \t"],["      \t"],[""], [""], [""]]
# maximum 3 lines height
low = {"a": [["       \t"],["      \t"],["  ___ \t"], ["  ___\ \t"], [" \___/\t"]],"b": [["       \t"],["      \t"],[" |   \t"], [" |___ \t"], [" |___|\t"]],"c": [["       \t"],["      \t"],["  ___ \t"], [" / \t"], [" \___\t"]], "e": [["       \t"],["      \t"],["  ___ \t"], [" /___\ \t"], [" \___\t"]], "h": [["|     |\t"],["|     |\t"], ["|_____|\t"], ["|     |\t"], ["|     |\t"]]}
def add(fromn, n):
    for f in range(len(n)):
        fromn[f][0] += n[f][0]
    return fromn

word = input("what word ?")
first = True

for g in word:
    if first:
        test = low[g]
        first = False
    else:
        add(test, low[g])

for f in test:
    print(f[0])