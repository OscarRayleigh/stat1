# une fonction permettant à l'utilisateur d'implémenter une valeur numérique
# entière n strictement positive et de la renvoyer : impln()

def impln():
    user_input = float(input("Entrez une valeur numérique strictement entière : "))
    if ((user_input % 1) == 0) and user_input > 0:
        return int(user_input)
    else:
        print("Ce n'est pas une valeur numérique strictement entière !")

# écrire une fonction permettant de renvoyer un tableau à une entrée à n composantes
# où chaque composantes est initialisée à une valeur nulle : vecn

def vecn(par):
    return [0 for i in range(par)]

# écrire une fonction permettant d'implémenter n valeurs numériques dans un tableau
# à une entrée et de renvoyer ce tableau : implvecn

def implvecn():
    tab = []
    while True:
        user_input = input("Entrez n'importe quel lettre pour signalez que vous avez fini d'entrer des valeurs.\nEntrez des valeurs numériques :  ")
        try:
            tab.append(float(user_input))
        except:
            print("Liste enregistrée ! ")
            return tab
            break

# une méthode permettant d'affiher les n valeurs numériques d'une tableau à une entrée : affichvecn(par)

def affichvecn(par):
    for i in range(dimn(par)):
        print(par[i])

# une fonction permettant de renvoyer la valeur de la dimension n d'un tableau à une entrée : dimn(par)

def dimn(par):
    compteur = 0
    for i in par:
        compteur += 1
    return compteur

# une fonction permettant de renvoyer un tableau n valeurs
# numériques classées par ordre croissant : vecncrois(par)

def vecncrois(par):
    liste = par
    liste_finale = []
    while liste:
        min = liste[0]
        for x in liste:
            if x < min:
                min = x
        liste_finale.append(min)
        liste.remove(min)
    return liste_finale

# une fonction permettant de renvoyer un tableau n valeurs
# numériques classées par ordre décroissante : vecndecrois(par)

def vecndecrois(par):
    # liste_croissante = vecncrois(par)
    # liste_finale = []
    # while liste_croissante:
    #     liste_finale.append(liste_croissante[-1])
    #     del liste_croissante[-1]
    # return liste_finale
    liste = par
    liste_finale = []
    while liste:
        max = liste[0]
        for x in liste:
            if x > max:
                max = x
        liste_finale.append(max)
        liste.remove(max)
    return liste_finale

# écrire une fonction permettant de renvoyer la valeur maximale d'un
# tableau à une entrée de n valeurs numériques

def vmax(par):
    while liste:
        max = liste[0]
        for x in liste:
            if x > max:
                max = x
        return max

# écrire une fonction permettant de renvoyer la valeur minimale d'un
# tableau à une entrée de n valeurs numériques

def vmin(par):
    while liste:
        min = liste[0]
        for x in liste:
            if x < min:
                min = x
        return min

# écrire une fonction permettant de renvoyer l'étendue d'un
# tableau à une entrée de n valeurs numériques

def vetend(par):
    return (max(par) - min(par))

# écrire une fonction permettant de renvoyer la somme d'un
# tableau à une entrée de n valeurs numériques

def vsom(par):
    somme = 0
    for i in par:
        somme = i + somme
    return somme

# écrire une fonction permettant de renvoyer la moyenne d'un
# tableau à une entrée de n valeurs numériques

def vmoy(par):
    return vsom(par)/dimn(par)

# écrire une fonction permettant de renvoyer l'écart absolu moyen d'un
# tableau à une entrée de n valeurs numériques

def vecma(par):
    eca_abs_moy = 0
    for i in par:
        eca_abs_moy += ((i - vmoy(par)))/dimn(par)
    return eca_abs_moy

# écrire une fonction permettant de renvoyer la variance d'un
# tableau à une entrée de n valeurs numériques

def vvar(par):
    var = 0
    for i in par:
        var += ((i - vmoy(par))**2)/dimn(par)
    return var

# écrire une fonction permettant de renvoyer l'écart-type d'un
# tableau à une entrée de n valeurs numériques

def vect(par):
    return (vvar(par)**(1/2))

# écrire une fonction permettant de renvoyer la valeur de S d'un
# tableau à une entrée de n valeurs numériques

def vs(par):
    vs = 0
    for i in par:
        vs += (((i - vmoy(par))**2)/(dimn(par)-1))
    vs **=(1/2)
    return vs

# écrire une fonction permettant de renvoyer la valeur de S^2 d'un
# tableau à une entrée de n valeurs numériques

def vss(par):
    return (vs(par) ** 2)

# une fonction permettant de renvoyer la valeur du premier quartile q1 d'un tableau
# à une entrée de n valeurs numériques : vqu(par)

def vqu(par):
    temp = list.copy(par)
    q1 = float((vsom(temp))*(25/100))
    sum = 0
    liste = vecncrois(temp)
    for i in liste:
        sum += i
        if sum >= q1:
            return i

# une fonction permettant de renvoyer la valeur de la médiane q2 d'un tableau
# à une entrée de n valeurs numériques : vqu(par)

def vqd(par):
    temp = list.copy(par)
    q2 = float(vsom(temp))*(50/100)
    sum = 0
    liste = vecncrois(temp)
    for i in liste:
        sum += i
        print(sum)
        print(q3)
        if sum >= q2:
            return i

# une fonction permettant de renvoyer la valeur du 3e quartile q3 d'un tableau
# à une entrée de n valeurs numériques : vqu(par)

def vqt(par):
    temp = list.copy(par)
    q3 = float((vsom(temp))*(75/100))
    sum = 0
    liste = vecncrois(temp)
    for i in liste:
        sum += i
        if sum >= q3:
            return i

# une fonction permettant de renvoyer la valeur de l'intervalle interquatile d'un tableau
# à une entrée de n valeurs numériques : vqu(par)

def viq(par):
    return (vqt(par) - vqu(par))

# une méthode permettant d'afficher les p valeurs numériques consécutives d'une sous suite
# d'un tableau à une entrée de n valeurs numériques : affichvecsn(par1,par2,par3)

def affichvecsn(tableau, index_debut, index_fin):
    sous_liste = []
    try:
        for i in tableau:
            while index_fin >= index_debut:
                sous_liste.append(tableau[index_debut])
                index_debut +=1
        for i in sous_liste:
            print(i)
    except:
        print("Erreur: les index donné les arguments dépassent la taille de la liste")

# une fonction permettant de renvoyer un tableau à une entrée des p valeurs numériques
# consécutives d'un tableau à une entrée de n valeurs numériques : vecextp(par1,par2,par3)

def vecextp(tableau, index_debut, index_fin):
    sous_liste = []
    try:
        for i in tableau:
            while index_fin >= index_debut:
                sous_liste.append(tableau[index_debut])
                index_debut +=1
        return sous_liste
    except:
        print("Erreur: les index donné les arguments dépassent la taille de la liste")

# une fonction permettant de renvoyer la valeur de la somme d'une sous suite p de valeurs
# numériques consécutives d'un tableau à une entrée de n valeurs numériques : vssom(par1,par2,par3)

def vssom(tableau, index_debut, index_fin):
    sous_liste = affichvecsn(tableau, index_debut, index_fin)
    return vsom(sous_liste)

# une méthode permettant de renvoyer la valeur de la moyenne d'une sous suite de p
# valeurs consécutives d'un tableau à une entrée de n vlauers numériques : vssom(par1,par2,par3)

def vssmoy(tableau, index_debut, index_fin):
    sous_liste = affichvecsn(tableau, index_debut, index_fin)
    return vsom(sous_liste)/dimn(sous_liste)
