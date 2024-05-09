from collections import defaultdict
def boatsToSave(people,limit):
    ensPeople = set(people)
    combinaison = defaultdict(lambda: set())
    occurrences = {}
    longueur = len(people)
    resultat = []
    nbBoats = 0
    if 1 >= longueur >= 5 * 10 ** 4 : return nbBoats

    for element in people:
        if element in occurrences:
            occurrences[element] += 1
        else:
            occurrences[element] = 1

    tmp = list(ensPeople)

    for i in range(len(tmp)):
        tmpi = tmp[i]
        if 1<= tmpi <= limit <= 3 * 10**4 :combinaison[tmpi].add(tmpi)
        if tmpi <= limit : combinaison[tmpi].add(tmpi)
        for j in range(i+1,len(tmp)):
            tmpj = tmp[j]
            if tmpi+tmpj <= limit :
                combinaison[tmpi].add(tmpj)
                combinaison[tmpj].add(tmpi)

    tmp = sorted(tmp)
    k = -1
    while len(tmp) > 0:
        current = tmp[k]
        if occurrences[current] == 0 :
            tmp.pop()
            continue
        tmpens = combinaison[current]
        longueur = len(tmpens)
        tmpcompteur = set()
        while len(combinaison[current]) != 0 and len(tmpcompteur) < longueur:
            minimum = min(tmpens)
            if occurrences[minimum] > 0 :
                if current == minimum :
                    a = 0
                    if current + minimum <= limit :
                        occurrences[minimum] -= 1
                        occurrences[current] -= 1
                        resultat.append((current, minimum))
                        nbBoats += 1
                    elif  current <= limit :
                        occurrences[minimum] -= 1
                        resultat.append((current))
                        nbBoats += 1

                    else :
                        a = 0
                        tmpens.remove(minimum)
                else :
                    occurrences[minimum] -= 1
                    occurrences[current] -= 1
                    resultat.append((current,minimum))
                    nbBoats += 1
                if occurrences[minimum] == 0 :
                    combinaison[current].remove(minimum)
                    tmpcompteur.add(minimum)
            else : tmpcompteur.add(minimum)
        tmp.pop()
    print(resultat)
    print(nbBoats)
    return nbBoats

boatsToSave([5,1,4,2],6)