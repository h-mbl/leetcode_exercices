def boatsToSave(people,limit):
    people = sorted(people)
    i = 0
    longueur = len(people)
    j = -1
    nbBoats = 0
    boat = {}
    if 1 <= longueur <= 5 * 10**4 :
        while len(people) > 0 and i < longueur:
            tmp = people[j]
            if 1 <= tmp <= limit <= 3 * 10**4:
                reste = limit - tmp
                if reste > 0  :
                    found = False
                    for k in range(len(people)-2, -1, -1):
                        tmp2 = people[k]
                        if tmp + tmp2 <= limit:
                            boat[nbBoats] = (tmp, tmp2)
                            people.pop(j)
                            people.pop(k)
                            nbBoats += 1
                            found = True
                            break
                    if found == False:
                        boat[nbBoats] = tmp
                        people.pop(j)
                        nbBoats += 1

                else :
                    boat[nbBoats] = tmp
                    people.pop(j)
                    nbBoats += 1
            # le cas ou il y a une personne depassant la limite
            else : return 0
            i += 1
        print(boat)
        print(len(boat))
        return len(boat)
    else : return 0
boatsToSave([3,5,3,4],5)