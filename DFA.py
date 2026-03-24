with open("DFA.in", 'r') as f:
    nrStari=int(f.readline())
    Q=set(f.readline().split())
    sigma = set(f.readline().split())
    nrTranzitii=int(f.readline())
    delta={}
    for _ in range(nrTranzitii):
        tranzitie=f.readline().split()
        cheie1=tranzitie[0]
        val=tranzitie[1]
        cheie2=tranzitie[2]
        if cheie1 not in delta:
            delta[cheie1]={}
        delta[cheie1][cheie2]=val
    print(delta)
    q0 = f.readline().strip()
    nrStariFinale=f.readline()
    F = set(f.readline().split())
    nrCuvinte=int(f.readline())
    cuvinte=f.readlines()
    for i in range(len(cuvinte)):
        cuvinte[i]=cuvinte[i].strip()

def verif(cuvant):
    stareCurenta = q0
    for simbol in cuvant:
        if simbol in delta[stareCurenta]:
            stareCurenta = delta[stareCurenta][simbol]
    if stareCurenta in F:
        return "DA"
    else:
        return "NU"

with open("DFA.out", 'w') as g:
    for cuvant in cuvinte:
        g.write(cuvant+" "+verif(cuvant)+"\n")