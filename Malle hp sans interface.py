# coding: utf-8


fournitures_scolaires = [{'Nom': 'Manuel scolaire', 'Poids': 0.55, 'Mana': 11},
                         {'Nom': 'Baguette magique', 'Poids': 0.085, 'Mana': 120},
                         {'Nom': 'Chaudron', 'Poids': 2.5, 'Mana': 2},
                         {'Nom': 'Boîte de fioles', 'Poids': 1.2, 'Mana': 4},
                         {'Nom': 'Téléscope', 'Poids': 1.9, 'Mana': 6},
                         {'Nom': 'Balance de cuivre', 'Poids': 1.3, 'Mana': 3},
                         {'Nom': 'Robe de travail', 'Poids': 0.5, 'Mana': 8},
                         {'Nom': 'Chapeau pointu', 'Poids': 0.7, 'Mana': 9},
                         {'Nom': 'Gants', 'Poids': 0.6, 'Mana': 25},
                         {'Nom': 'Cape', 'Poids': 1.1, 'Mana': 13}]

poids_maximal = 4


def tri_selection(tab):  # Méthode de trie par séléction
    for i in range(len(tab)):
        min = i
        for j in range(i + 1, len(tab)):
            if tab[min][1] < tab[j][1]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab


def remplir_malle(fournitures, poids_max: int) -> int:
    """
    La fonction remplir_malle ajoute le plus d'élément possible sans aucune opptimisation
    Entrée : les différentes informations à propos des objets (fournitures) et aussi le poids maximal de que la malle peut supporter(poids_max)
    Sortie : le poids et les éléments de la malle remplie
    """
    poids_max_lock = poids_max
    malle_pleine = []  # Liste finale du contenu de la malle
    for element in fournitures:  # boucle qui ajoute un objet et rajoute son poids si le poids restant est supérieur ou égale à celui de l'objet
        if element['Poids'] <= poids_max:
            poids_max -= element['Poids']
            malle_pleine.append(element['Nom'])
    return [round(poids_max_lock - poids_max, 3),malle_pleine]  # Renvoie des éléments dans la malle et du poids arrondie


def remplir_malle_max(fournitures, poids_max: int) -> int:
    """
    La fonction remplir_malle_max rempli donc la malle avec les plus gros poids en premier
    Entrée : les différentes informations à propos des objets (fournitures) et aussi le poids maximal de que la malle peut supporter(poids_max)
    Sortie : le poids et les éléments de la malle remplie
    """
    poids_max_lock = poids_max
    malle_pleine = []  # Liste final du contenu de la malle
    liste_poids_trier = []
    for element in fournitures:  # Création d'une liste par une boucle pour sortir les informations du dictionnaire et donc pouvoir les trier
        liste_poids_trier.append([element['Nom'], element['Poids']])
    tri_selection(liste_poids_trier)  # appelle de la fonction pour trier la nouvelle liste
    for i in range(len(liste_poids_trier)):  # boucle pour ajoute un objet et rajoute son poids si le poids restant est supérieur ou égale à celui de l'objet
        if liste_poids_trier[i][1] <= poids_max:
            poids_max -= liste_poids_trier[i][1]
            malle_pleine.append(liste_poids_trier[i][0])

    return [round(poids_max_lock - poids_max, 3), malle_pleine]  # Renvoie des valeurs poids et éléments dans la malle


def remplir_malle_max_mana(fournitures, poids_max: int) -> int:
    """
    la fonction remplir_malle_max_mana rempli la malle en ajoutant le plus de mana possible
    Entrée : les différentes informations à propos des objets (fournitures) et aussi le poids maximal de que la malle peut supporter(poids_max)
    Sortie : le mana, le poids et les éléments de la malle remplie
    """
    liste_mana_trier = []
    poids_max_lock = poids_max
    mana_malle = 0
    malle_pleine_avec_mana = []
    for element in fournitures:  # Création d'une liste par une boucle pour sortir les informations du dictionnaire et donc pouvoir les trier
        liste_mana_trier.append([element['Nom'], element['Mana'], element['Poids']])  # Ajout du mana en deuxème position dans la liste pour être adapter au trie
    tri_selection(liste_mana_trier)  # appelle de la fonction pour trier la nouvelle liste
    for i in range(len(liste_mana_trier)):  # ici la boucle rajoute l'élément avec le plus de mana et on calcule le poids comme pour les autres
        if liste_mana_trier[i][2] <= poids_max:
            poids_max -= liste_mana_trier[i][2]
            mana_malle += liste_mana_trier[i][1]
            malle_pleine_avec_mana.append(liste_mana_trier[i][0])

    return [round(poids_max_lock - poids_max, 3), mana_malle,malle_pleine_avec_mana]  # Renvoie du poids, du mana et des éléments de la malle


liste_malle = remplir_malle(fournitures_scolaires, poids_maximal)
liste_malle_max = remplir_malle_max(fournitures_scolaires, poids_maximal)
liste_malle_mana_max = remplir_malle_max_mana(fournitures_scolaires, poids_maximal)

print("A. Remplir la malle… n’importe comment !")
print(f"Le poids de la malle est {liste_malle[0]} et elle est composée des fournitures suivantes :", *liste_malle[1],
      sep='\n -')
print('B. Remplir la malle la plus lourde possible')
print(f"Le poids maximale remplie avec les objets les plus lourds est de {liste_malle_max[0]} et elle est composée"
      f" des fournitures suivantes :", *liste_malle_max[1], sep='\n -')
print('C. Remplir la malle avec le maximum de mana')
print(f"Le mana maximale est {liste_malle_mana_max[1]}, elle pèse {liste_malle_mana_max[0]} et"
      f" elle est composée des fournitures suivantes :", *liste_malle_mana_max[2], sep='\n -')
