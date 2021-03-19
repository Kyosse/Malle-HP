import pygame
from pygame.locals import *
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

#creer une class pour l'emplacement
class Emplacement(pygame.sprite.Sprite):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(r"images/rien.png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def set_image(self, image):
        self.image = image

rien = pygame.image.load(r"images/rien.png")


fournitures_scolaires = [{'Nom' : 'Manuel scolaire', 'Poids' : 0.55, 'Mana' : 11},
                        {'Nom' : 'Baguette magique', 'Poids' : 0.085, 'Mana' : 120},
                        {'Nom' : 'Chaudron', 'Poids' : 2.5, 'Mana' : 2},
                        {'Nom' : 'Boîte de fioles', 'Poids' : 1.2, 'Mana' : 4},
                        {'Nom' : 'Téléscope', 'Poids' : 1.9, 'Mana' : 6},
                        {'Nom' : 'Balance de cuivre', 'Poids' : 1.3, 'Mana' : 3},
                        {'Nom' : 'Robe de travail', 'Poids' : 0.5, 'Mana' : 8},
                        {'Nom' : 'Chapeau pointu', 'Poids' : 0.7, 'Mana' : 9},
                        {'Nom' : 'Gants', 'Poids' : 0.6, 'Mana' : 25},
                        {'Nom' : 'cape', 'Poids' : 1.1, 'Mana' : 13}
                        ]

poids_maximal = 4

def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min][1] < tab[j][1]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab

def remplir_malle(fournitures, poids_max):
    poids_malle = 0
    malle_pleine =[]
    for element in fournitures:
        poids_malle += element['Poids']
        malle_pleine.append(element['Nom'])
        if poids_malle > poids_max:
            poids_malle -= element['Poids']
            malle_pleine.pop()

    if len(malle_pleine) == 1:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])

    elif len(malle_pleine) == 2:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])

    elif len(malle_pleine) == 3:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])

    elif len(malle_pleine) == 4:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        

    elif len(malle_pleine) == 5:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])

    elif len(malle_pleine) == 6:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])

    elif len(malle_pleine) == 7:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])

    elif len(malle_pleine) == 8:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])
        emplacement8.set_image(fournitures_image[malle_pleine[7]])

    elif len(malle_pleine) == 9:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])
        emplacement8.set_image(fournitures_image[malle_pleine[7]])
        emplacement9.set_image(fournitures_image[malle_pleine[8]])
    
    else:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])
        emplacement8.set_image(fournitures_image[malle_pleine[7]])
        emplacement9.set_image(fournitures_image[malle_pleine[8]])
        emplacement10.set_image(fournitures_image[malle_pleine[9]])

    round(poids_malle ,3 )



    return round(poids_malle ,3 ), malle_pleine


def remplir_malle_max(fournitures, poids_max):
    poids_malle = 0 
    malle_pleine =[] 
    liste_poids_trier =[]
    for element in fournitures:
        liste_poids_trier.append([element['Nom'],element['Poids']])
    tri_selection(liste_poids_trier)
    for element in liste_poids_trier: 
        poids_malle += element[1]
        malle_pleine.append(element[0])
        if poids_malle > poids_max: 
            poids_malle -= element[1]
            malle_pleine.pop()

    if len(malle_pleine) == 1:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])

    elif len(malle_pleine) == 2:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])

    elif len(malle_pleine) == 3:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])

    elif len(malle_pleine) == 4:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        

    elif len(malle_pleine) == 5:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])

    elif len(malle_pleine) == 6:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])

    elif len(malle_pleine) == 7:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])

    elif len(malle_pleine) == 8:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])
        emplacement8.set_image(fournitures_image[malle_pleine[7]])

    elif len(malle_pleine) == 9:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])
        emplacement8.set_image(fournitures_image[malle_pleine[7]])
        emplacement9.set_image(fournitures_image[malle_pleine[8]])
    
    else:
        emplacement1.set_image(fournitures_image[malle_pleine[0]])
        emplacement2.set_image(fournitures_image[malle_pleine[1]])
        emplacement3.set_image(fournitures_image[malle_pleine[2]])
        emplacement4.set_image(fournitures_image[malle_pleine[3]])
        emplacement5.set_image(fournitures_image[malle_pleine[4]])
        emplacement6.set_image(fournitures_image[malle_pleine[5]])
        emplacement7.set_image(fournitures_image[malle_pleine[6]])
        emplacement8.set_image(fournitures_image[malle_pleine[7]])
        emplacement9.set_image(fournitures_image[malle_pleine[8]])
        emplacement10.set_image(fournitures_image[malle_pleine[9]])
            
    return round(poids_malle ,3 ), malle_pleine



def remplir_malle_max_mana(fournitures, poids_max):
    liste_mana =[]
    poids_malle_mana = 0
    mana_malle = 0
    malle_pleine_avec_mana = []
    for element in fournitures:
        liste_mana.append([element['Nom'],element['Mana'], element['Poids']])
    tri_selection(liste_mana)
    for i in range(len(liste_mana) - 1):
        mana_malle += liste_mana[i][1]
        poids_malle_mana += liste_mana[i][2]
        malle_pleine_avec_mana.append(liste_mana[i][0])
        if poids_malle_mana >= poids_max:
            poids_malle_mana -= liste_mana[i][2]
            mana_malle -= liste_mana[i][1]
            malle_pleine_avec_mana.pop()

    if len(malle_pleine_avec_mana) == 1:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])

    elif len(malle_pleine_avec_mana) == 2:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])

    elif len(malle_pleine_avec_mana) == 3:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])

    elif len(malle_pleine_avec_mana) == 4:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])
        emplacement4.set_image(fournitures_image[malle_pleine_avec_mana[3]])
        

    elif len(malle_pleine_avec_mana) == 5:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])
        emplacement4.set_image(fournitures_image[malle_pleine_avec_mana[3]])
        emplacement5.set_image(fournitures_image[malle_pleine_avec_mana[4]])

    elif len(malle_pleine_avec_mana) == 6:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])
        emplacement4.set_image(fournitures_image[malle_pleine_avec_mana[3]])
        emplacement5.set_image(fournitures_image[malle_pleine_avec_mana[4]])
        emplacement6.set_image(fournitures_image[malle_pleine_avec_mana[5]])

    elif len(malle_pleine_avec_mana) == 7:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])
        emplacement4.set_image(fournitures_image[malle_pleine_avec_mana[3]])
        emplacement5.set_image(fournitures_image[malle_pleine_avec_mana[4]])
        emplacement6.set_image(fournitures_image[malle_pleine_avec_mana[5]])
        emplacement7.set_image(fournitures_image[malle_pleine_avec_mana[6]])

    elif len(malle_pleine_avec_mana) == 8:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])
        emplacement4.set_image(fournitures_image[malle_pleine_avec_mana[3]])
        emplacement5.set_image(fournitures_image[malle_pleine_avec_mana[4]])
        emplacement6.set_image(fournitures_image[malle_pleine_avec_mana[5]])
        emplacement7.set_image(fournitures_image[malle_pleine_avec_mana[6]])
        emplacement8.set_image(fournitures_image[malle_pleine_avec_mana[7]])

    elif len(malle_pleine_avec_mana) == 9:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])
        emplacement4.set_image(fournitures_image[malle_pleine_avec_mana[3]])
        emplacement5.set_image(fournitures_image[malle_pleine_avec_mana[4]])
        emplacement6.set_image(fournitures_image[malle_pleine_avec_mana[5]])
        emplacement7.set_image(fournitures_image[malle_pleine_avec_mana[6]])
        emplacement8.set_image(fournitures_image[malle_pleine_avec_mana[7]])
        emplacement9.set_image(fournitures_image[malle_pleine_avec_mana[8]])
    
    else:
        emplacement1.set_image(fournitures_image[malle_pleine_avec_mana[0]])
        emplacement2.set_image(fournitures_image[malle_pleine_avec_mana[1]])
        emplacement3.set_image(fournitures_image[malle_pleine_avec_mana[2]])
        emplacement4.set_image(fournitures_image[malle_pleine_avec_mana[3]])
        emplacement5.set_image(fournitures_image[malle_pleine_avec_mana[4]])
        emplacement6.set_image(fournitures_image[malle_pleine_avec_mana[5]])
        emplacement7.set_image(fournitures_image[malle_pleine_avec_mana[6]])
        emplacement8.set_image(fournitures_image[malle_pleine_avec_mana[7]])
        emplacement9.set_image(fournitures_image[malle_pleine_avec_mana[8]])
        emplacement10.set_image(fournitures_image[malle_pleine_avec_mana[9]])

    return round(poids_malle_mana, 2), mana_malle, malle_pleine_avec_mana




# création de la fenetre

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Remplir malle")

#font d'écran

background = pygame.image.load(r"images/fond.jpg")
malle = pygame.image.load(r"images/Malle_HP.png")
malle.fill((255, 255, 255, 190), special_flags=BLEND_RGBA_MULT)

# dictionnaire fourniture image

fournitures_image = {
    'Manuel scolaire' : pygame.image.load(r"images/livres.png"),
    'Baguette magique' : pygame.image.load(r"images/baguettes.png"),
    'Chaudron' : pygame.image.load(r"images/chaudron.png"),
    'boite a fioles' : pygame.image.load(r"images/fiole.png"),
    'Téléscope' : pygame.image.load(r"images/telescope.png"),
    'Balance de cuivre' : pygame.image.load(r"images/balance.png"),
    'Robe de travail' : pygame.image.load(r"images/robe.png"),
    'Chapeau pointu' : pygame.image.load(r"images/chapeau.png"),
    'Gants' : pygame.image.load(r"images/gant.png"),
    'cape' : pygame.image.load(r"images/cape.png")
}

#chargement des emplacements

emplacements = pygame.sprite.Group()
emplacement1 = Emplacement(400, 280)
emplacement2 = Emplacement(500, 280)
emplacement3 = Emplacement(600, 280)
emplacement4 = Emplacement(700, 280)
emplacement5 = Emplacement(800, 280)
emplacement6 = Emplacement(400, 400)
emplacement7 = Emplacement(500, 400)
emplacement8 = Emplacement(600, 400)
emplacement9 = Emplacement(700, 400)
emplacement10 = Emplacement(800, 400)

# rangement des emplacements dans le groupe

emplacements.add(emplacement1)
emplacements.add(emplacement2)
emplacements.add(emplacement3)
emplacements.add(emplacement4)
emplacements.add(emplacement5)
emplacements.add(emplacement6)
emplacements.add(emplacement7)
emplacements.add(emplacement8)
emplacements.add(emplacement9)
emplacements.add(emplacement10)



arial_font = pygame.font.SysFont( "arial", 40, bold=True, italic=False)
arial_font2 = pygame.font.SysFont( "arial", 32, bold=False, italic=False)
Titre = arial_font.render("Bienvenue dans la partie 2", True, white)
Titre2 = arial_font.render(" Appuyer sur les touches a, b ou c de votre clavier",True, white)



affichage = 0


running = True

#boucle tant que cette condition est vrai

while running: 

    # arrière plan 
    window.blit(background, (0, 0))
    window.blit(malle, (300, -50))
    window.blit(Titre, [50, 20])
    window.blit(Titre2, [35, 60])
    if affichage == 1:
        poids_1 = arial_font2.render(f"Poids: {str(remplir_malle(fournitures_scolaires , poids_maximal)[0])}", True, black)
        window.blit(poids_1, [575, 120])
    elif affichage == 2:
        poids_2 = arial_font2.render(f"Poids: {str(remplir_malle_max(fournitures_scolaires , poids_maximal)[0])}", True, black)
        window.blit(poids_2, [575, 120])
    elif affichage == 3:
        poids_3 = arial_font2.render(f"Poids: {str(remplir_malle_max_mana(fournitures_scolaires , poids_maximal)[0])}", True, black)
        poids_4 = arial_font2.render(f"Mana: {str(remplir_malle_max_mana(fournitures_scolaires , poids_maximal)[1])}", True, black)
        window.blit(poids_3, [575, 100])
        window.blit(poids_4, [575, 140])
    

    #fourniture image

    emplacements.draw(window)

    #mettre a jour l'écran

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print(emplacement1.set_image(rien),
                        emplacement2.set_image(rien),
                        emplacement3.set_image(rien),
                        emplacement4.set_image(rien),
                        emplacement5.set_image(rien),
                        emplacement6.set_image(rien),
                        emplacement7.set_image(rien),
                        emplacement8.set_image(rien),
                        emplacement9.set_image(rien),
                        emplacement10.set_image(rien))
                print(remplir_malle(fournitures_scolaires , poids_maximal))
                affichage = 1
                

            if event.key == pygame.K_b:
                print(emplacement1.set_image(rien),
                        emplacement2.set_image(rien),
                        emplacement3.set_image(rien),
                        emplacement4.set_image(rien),
                        emplacement5.set_image(rien),
                        emplacement6.set_image(rien),
                        emplacement7.set_image(rien),
                        emplacement8.set_image(rien),
                        emplacement9.set_image(rien),
                        emplacement10.set_image(rien))
                print(remplir_malle_max(fournitures_scolaires , poids_maximal))
                affichage = 2
                
            if event.key == pygame.K_c:
                print(emplacement1.set_image(rien),
                        emplacement2.set_image(rien),
                        emplacement3.set_image(rien),
                        emplacement4.set_image(rien),
                        emplacement5.set_image(rien),
                        emplacement6.set_image(rien),
                        emplacement7.set_image(rien),
                        emplacement8.set_image(rien),
                        emplacement9.set_image(rien),
                        emplacement10.set_image(rien))
                print(remplir_malle_max_mana(fournitures_scolaires , poids_maximal))
                affichage = 3



 