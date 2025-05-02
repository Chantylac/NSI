
# Créé par :
# Timothé Sauvage
# Arthur Da Silva Fernandes

import time

import keyboard

import random

import shutil

import pygame

import tqdm

# Temps d'attente entre les lignes
to_sleep = 0.3
to_sleep2 = 1

# La classe initiale du joueur est "None"
class_player = "None"

# Points de vie du joueur
pv_player = 5

# Argent du joueur
po_player = 8

# Stats du joueur
stats = {"force": 0, "agilite": 0, "eloquence": 0, "arcane": 0, "endurance": 0}

# Choix basique, à répéter pour limiter l'espace de stockage
choix_base1 = "None"

# Niveau de l'amulette de lumière (Nb tentative juste prix)
lvl_amulette = 2

# Valeur pour tests
val_test = 0

# Obtenir la longueur de la console
largeur_console = shutil.get_terminal_size().columns

# Nom du chien
name_chien = "None"


def intro():
    print("\n\033[1;3;34m") # Texte stylisé Intro
    print("━" * largeur_console)  # \033[1;3;34m --> Changer couleur texte
    print("Les chroniques de l'Amulette de Lumière")  # \n --> sauter une ligne
    print("Chapitre 1 : Où tout à Commencé")
    print("━" * largeur_console), time.sleep(2)
    print("\n\033[0m")
    print(  # Dialogues Intro
        "Narrateur : \033[3mVous incarnez Elias, un jeune aventurier cherchant à se faire une place parmi \nles plus "
        "grand guerriers du royaume d'Elderia.\033[0m\n"
    ), time.sleep(to_sleep2)
    print("Système : [Appuyez sur [MAJ] pour passer au dialogue suivant]\n"), keyboard.wait("shift")
    print(
        "\033[3mAlors que vous voyagez vers le village de Yharnam en quête d'aventure, \nvous décidez de passer la nuit"
        "dans la taverne du Soleil Levant.\033[0m\n"
    ), keyboard.wait("shift")
    print(
        "\033[3mVous vous endormez vite sans ranger vos affaires.\nA votre réveil vous remarquez une épée rouillée,"
        " un livre ancien et une carte du Royaume d'Elderia, posés sur un petit bureau, en face de votre lit\033[0m"
    ), keyboard.wait("shift")


def competence():
    global class_player, stats
    retour, retour1 = True, True

    def enonciation_stats():  # Affichage stats par classe
        print(stats["force"], "de \033[0;36mforce\033[0;0m,", end=" "), time.sleep(to_sleep)
        print(stats["agilite"], "d'\033[0;36magilité\033[0;0m,", end=" "), time.sleep(to_sleep)
        print(stats["eloquence"], "d'\033[0;36méloquence\033[0;0m et", end=" "), time.sleep(to_sleep)
        print(stats["arcane"], "d'\033[0;36marcane\033[0;0m\n", end=" "), time.sleep(to_sleep)

    while retour:  # Choix classe
        try:
            print("\n\033[3mInteragir avec l'épée et deviens \033[3;35mRodeur\033[0m [1]")
            choix_class = int(input("\033[3mInteragir avec le livre et deviens \033[3;35mMage\033[0m [2]\n⮚ \033[0m"))
            if choix_class == 1:  # Rodeur
                print("\n\033[3mTu deviens \033[3;35mRodeur\033[0m avec :"), time.sleep(to_sleep)
                stats = {"force": 7, "agilite": 6, "eloquence": 3, "arcane": 2, "endurance": 3}
                enonciation_stats()
                while retour1:
                    retour_class = int(input(  # Possibilité retour en arrière
                        "\n\033[3mVeux-tu retourner en arrière ? Oui [1] Non [2]\n⮚ \033[0m"))
                    if retour_class == 1:
                        break
                    elif retour_class == 2:
                        class_player = "\033[0;35mRodeur\033[0m"
                        retour, retour1 = False, False
            elif choix_class == 2:  # Mage
                print("\n\033[3mTu deviens \033[3;35mMage\033[0m, avec :"), time.sleep(to_sleep)
                stats = {"force": 3, "agilite": 2, "eloquence": 6, "arcane": 7, "endurance": 3}
                enonciation_stats()
                while retour1:
                    retour_class = int(input("\n\033[3mVeux-tu retourner en arrière ? Oui [1] Non [2]\n⮚ \033[0m"))
                    if retour_class == 1:
                        break
                    elif retour_class == 2:
                        class_player = "\033[0;35mMage\033[0m"
                        retour, retour1 = False, False

        except ValueError:
            print("Système : [Veuillez entrer [1] ou [2] !]")
            continue

    time.sleep(to_sleep)  # Affichage classe finale
    print("\nVous êtes désormais", class_player, "!\n"), time.sleep(to_sleep2)
    return stats, class_player


def choix1():
    global choix_base1
    print("\n\033[3mVous voyez une carte, enroulée sur le côté de la petite table.\033[0m")
    time.sleep(to_sleep)

    while True:
        choix_base1 = input("\033[3mInteragir avec la carte [CARTE]\033[0m\n⮚ ")
        if choix_base1.lower() == "carte":  # Quelque façon que soit écrit "carte", il sera transformé en minuscule
            time.sleep(to_sleep)
            print("\n\033[3mVous remarquez des annotations runiques à un endroit précis de la carte.\033[0m")
            break
        else:
            print("\nVeuillez écrire [CARTE] pour interagir avec la carte.\n")

    keyboard.wait("shift")


def intro_invoc():  # Intro invocation (excplications)
    print("\033[3mVous pensez que Sélène, l'esprit qui vous accompagne, saurait lire ces runes.\033[0m")
    keyboard.wait("shift")
    print("\nTest d'invocation :"), time.sleep(to_sleep)
    print("Système : [Ce test repose sur la mécanique du juste prix.]\n"), time.sleep(to_sleep2)
    print(
        "\033[3mSélène est un être de lumière, il faut trouver dans quelle constellation elle se trouve afin de "
        "l'invoquer;\033[0m\n"), time.sleep(to_sleep2)
    print(
        "\033[3mVous devrez trouver le chiffre correspondant à la constellation où Sélène est présente, en plusieurs "
        "essais;\033[0m\n"), time.sleep(to_sleep2)
    print(
        "\033[3mVous savez que ce chiffre est compris entre 1 et 10, et à chaque erreur s'affichera une indication "
        "'Plus' ou 'Moins';\033[0m\n"), time.sleep(to_sleep2)
    print(
        "\033[3mVotre nombre de tentatives correspond au niveau de votre Amulette de Lumière. (Niveau 2)\033[0m\n")
    time.sleep(to_sleep2), keyboard.wait("shift")


def test_invoc():
    global lvl_amulette, largeur_console
    choix_justeprix, amulette_i = 0, 0
    nb_justeprix = random.randint(1, 10)

    print("━" * largeur_console)
    print("\033[1mTest d'Invocation\033[0m")
    print("━" * largeur_console), time.sleep(to_sleep2)

    justeprix = True
    while justeprix:
        try:  # Choix nombre
            choix_justeprix = int(input("\033[3mQuelle constellation ? (1...10) \033[0m\n⮚ "))
            if choix_justeprix > 10 or choix_justeprix < 0:
                print("Système : [Veuillez entrer une valeur comprise entre 1 et 10]")  # Si nombre ne fonctionne pas
                continue
            else:
                while justeprix:
                    if choix_justeprix == nb_justeprix:
                        print(
                            "\n\033[3mVous avez trouvé la constellation dans laquelle se trouve Sélène !\033[0m")  # Si réussite
                        print("\033[3mSélène est invoquée.\033[0m", end=" "), time.sleep(to_sleep)
                        print("[MAJ]"), keyboard.wait("shift")
                        justeprix = False
                    elif choix_justeprix < nb_justeprix:
                        amulette_i += 1
                        print("\033[1;33mPlus haut;\033[0m", lvl_amulette - amulette_i, "Tentatives restantes\n")
                        if amulette_i == lvl_amulette:
                            print("\033[3mSélène n'a pas remarqué votre invocation\033[0m", end=" "), time.sleep(
                                # Si défaite
                                to_sleep)
                            print("[MAJ]\n"), keyboard.wait("shift")
                            print(
                                "\033[3mIl semblerait que la chance soit de votre côté, puisque malgré votre tentative\n"  # Si défaite
                                "ratée de contacter, Sélène vous remarque et vient à vous\033[0m."
                            ), keyboard.wait("shift")
                            justeprix = False
                        else:
                            break
                    else:
                        amulette_i += 1
                        print("\033[1;33mPlus bas;\033[0m", lvl_amulette - amulette_i, "Tentative restantes\n")
                        if amulette_i == lvl_amulette:
                            print("\033[3mSélène n'a pas remarqué votre invocation\033[0m", end=" "), time.sleep(
                                # Si défaite
                                to_sleep)
                            print("[MAJ]"), keyboard.wait("shift")
                            print(
                                "\033[3mIl semblerait que la chance soit de votre côté,puisque malgré votre tentative\n"
                                "ratée de contacter, Sélène vous remarque et vient à vous.\033[0m"
                            ), keyboard.wait("shift")
                            justeprix = False
                        else:
                            break

        except ValueError:
            print("Système : [Veuillez entrer une valeur comprise entre 1 et 10]")  # Si nombre non fonctionnel
            continue


def suite_invoc1():
    print(
        "\n\033[1;3;33mCe sont des runes du Culte du soleil indiquant la présence d'une\n"
        # \033[1;3;33m = code pour colorer + couleur en question (jaune) + italique + gras
        "forte concentration de mana dans une zone plus au sud : La Forêt Brumeuse.\n"
        # \033[0m = code pour colorer + couleur en question (0 = couleur base)
    ), keyboard.wait("shift")
    print(
        "Sachant que ce Culte du Soleil est l'un des plus néfastes, il serait juste d'aller\n"
        "détruire la source de mana dans cette forêt avant qu'ils ne s'en emparent,\n"
        "même si vous les savez bien plus puissants que vous.\033[0m\n"
    ), keyboard.wait("shift")
    while True:
        try:
            print('"Pas de temps à perdre, allons-y !" [1]')
            choix_base1 = int(input('"Je trouverai bien un plan en chemin !" [2]\n⮚ '))
            if choix_base1 == 1:
                print("\n\033[1;34mPas de temps à perdre, allons-y!\033[0m [MAJ]\n"), time.sleep(to_sleep)
                break
            elif choix_base1 == 2:
                print("\n\033[1;34mJe trouverai bien un plan en chemin !\033[0m [MAJ]\n"), time.sleep(to_sleep)
                break
        except ValueError:
            print("\nSystème : [Veuillez entrer [1] ou [2] !]\n")
            continue
    keyboard.wait("shift")
    print(
        "\033[3mDans la précipitation, vous oubliez de payer le tavernier en quittant la chambre.\n"
        "Vous tentez de vous enfuir, avant que celui-ci vous rattrape\033[0m", end=" "
    )
    for i in range(0, 3):
        time.sleep(to_sleep2 * 0.80)
        print(".", end="")
    print(" "), keyboard.wait("shift")


def test_tavernier():
    global stats, val_test, po_player, pv_player, choix_base1
    while True:
        try:
            print("[\033[0;36mEloquence\033[0m :", stats["eloquence"],
                  "] Convaincre le tavernier de vous laisser partir [1]")
            print("[\033[0;36mAgilité\033[0m :", stats["agilite"],
                  "] Tenter de vous cachez dans la foule devant la taverne [2]")
            choix_base1 = int(input("⮚ "))
            if choix_base1 not in [1, 2]: # Si les résultat n'est pas dans la liste :
                print("\nSystème : [Veuillez entrer [1] ou [2] !]\n")
        except ValueError:
            print("\nSystème : [Veuillez entrer [1] ou [2] !]\n")
        try:
            if choix_base1 == 1:
                print(
                    "\nVous allez réaliser un test d'\033[0;36mEloquence\033[0m\n"), time.sleep(to_sleep2)
                print(
                    "Votre but est d'avoir un score d'\033[0;36mEloquence\033[0m supérieur ou égal à celui de votre "
                    "adversaire.\n"
                ), time.sleep(to_sleep2)
                print(
                    "Pour cela vous pouvez transformer un nombre de vos\n"
                    '\033[0;32mPE\033[0m (Points \033[0;32mEndurance\033[0m) en "points \033[0;36mEloquence\033[0m" '
                ), time.sleep(to_sleep2)
                print(
                    "afin d'avoir une \033[0;36mEloquence\033[0m supérieur ou égal à celle de votre adversaire,\n"
                ), time.sleep(to_sleep)
                print(
                    "- S'il surpasse le score adverse de 2pts minimum, un bonus vous sera décerné."
                ), time.sleep(to_sleep)
                print(
                    "- Au contraire, si vous n'avez pas assez de points \033[0;32mEndurance\033[0m pour égaler "
                    "l'adversaire, vous perdez 2 \033[0;31mPV\033[0m"
                ), time.sleep(to_sleep)
                print(
                    "- Les points \033[0;32mEndurance\033[0m ne se récupèrent que lors des repos.\n[MAJ]\n"
                ), keyboard.wait("shift")

                print("━" * largeur_console, )
                print("Test d'\033[0;36mEloquence\033[0m")
                print("━" * largeur_console, ), time.sleep(to_sleep2)

                print("\nVous :", stats["eloquence"], "stat d'\033[0;36mEloquence\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 5 stat d'\033[0;36mEloquence\033[0m")
                elo_adverse = 5

                while True:
                    val_test = int(input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !\n")
                        continue
                    else:
                        print("Vous avez désormais", stats["eloquence"] + val_test, "stat d'\033[0;36mEloquence\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["eloquence"] + val_test >= 7:
                    print("Après lui avoir raconté votre difficile enfance, que vous venez d'inventer,\nle tavernier"
                          " vous tends une bourse de pièce d'or, apitoyé par votre sort.\nElle est maintenant vôtre !"
                          "[ +4 \033[0;3;33mPO\033[0m][",
                          po_player + 4, "\033[0;3;33mPO\033[0m]")
                    po_player += 4

                    break
                elif stats["eloquence"] + val_test < elo_adverse:
                    pv_player -= 2
                    print("Le tavernier ne semble pas convaincu par vos excuses, et vous saute dessus.\n[ -2 \033["
                          "0;31mPV\033[0m][",
                          pv_player, "\033[0;31mPV\033[0m restants]")
                    if pv_player <= 1:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                elif 7 > stats["eloquence"] + val_test >= elo_adverse:
                    print("Vous réussissez à convaincre le tavernier de vous épargner.")
                    break
                break

            elif choix_base1 == 2:
                print(
                    "\nVous allez réaliser un test d'\033[0;36mAgilité\033[0m\n"), time.sleep(to_sleep2)
                print(
                    "Votre but est d'avoir un score d'\033[0;36mAgilité\033[0m supérieur ou égal à celui de votre "
                    "adversaire.\n"
                ), time.sleep(to_sleep2)
                print(
                    "Pour cela vous pouvez transformer un nombre de vos\n"
                    '\033[0;32mPE\033[0m (Points \033[0;32mEndurance\033[0m) en "points \033[0;36mAgilité\033[0m" '
                ), time.sleep(to_sleep2)
                print(
                    "afin d'avoir une \033[0;36mAgilité\033[0m supérieur ou égal à celle de votre adversaire,\n"
                ), time.sleep(to_sleep)
                print(
                    "- S'il surpasse le score adverse de 2pts minimum, un bonus vous sera décerné."
                ), time.sleep(to_sleep)
                print(
                    "- Au contraire, si vous n'avez pas assez de points \033[0;32mEndurance\033[0m pour égaler "
                    "l'adversaire, vous perdez 2 \033[0;31mPV\033[0m"
                ), time.sleep(to_sleep)
                print(
                    "- Les points \033[0;32mEndurance\033[0m ne se récupèrent que lors des repos.\n[MAJ]\n"
                ), keyboard.wait("shift")

                print("━" * largeur_console)
                print("Test d'\033[0;36mAgilité\033[0m")
                print("━" * largeur_console), time.sleep(to_sleep2)

                print("\nVous :", stats["agilite"], "stat d'\033[0;36mAgilité\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 5 stat d'\033[0;36mAgilité\033[0m")
                while True:
                    val_test = int(input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !\n")
                        continue
                    else:
                        print("Vous avez désormais", stats["agilite"] + val_test, "stat d'\033[0;36mAgilité\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["agilite"] + val_test >= 7:
                    print("Vous échappez au tavernier avec une aisance déconcertante.\nPendant votre course vous"
                          "trébuchez sur une bourse pleine de \033[0;3;33mpièce d'or\033[0m.\nElle est maintenant "
                          "vôtre [ +4 \033[0;3;33mPO\033[0m][",
                          po_player + 4, "\033[0;3;33mPO\033[0m]")
                    po_player += 4
                    break
                elif stats["agilite"] + val_test < 5:
                    pv_player -= 2
                    print("Le tavernier vous rattrape et vous passe à tabac\n[ -2 \033[0;31mPV\033[0m][", pv_player,
                          "\033[0;31mPV\033[0m restants]")
                    if pv_player <= 0:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                elif 7 > stats["agilite"] + val_test >= 5:
                    print("Vous échappez au tavernier sans trop de mal.")
                    break
                break

        except ValueError:
            print("Système : [Veuillez entrer une valeur]")
            continue
    return stats, po_player, pv_player


def yharnam():
    global choix_base1, po_player
    keyboard.wait("shift")
    print("\n\033[3mVous êtes maintenant prêt à quitter le village.\n"), keyboard.wait("shift")
    print("Enfin... Plus ou moins.\n"), keyboard.wait("shift")
    print("Vous ne connaissez pas le village dans lequel vous vous trouvez.")
    print("Vous décidez alors de sortir votre carte afin de vous repérer.\033[0m\n"), time.sleep(to_sleep2)

    print("Système : [Une fenêtre a dû s'ouvrir en arrière plan] [MAJ]")

    pygame.init()  # init de pygame

    info_ecran = pygame.display.Info()  # Récup les dims de l'écran et les attribuer à des variables
    screen_width, screen_height = info_ecran.current_w, info_ecran.current_h

    max_width = screen_width - 250  # Faire de la place pour les bordures
    max_height = screen_height - 250  # Pour pouvoir déplacer la fenêtre

    image_path = "yharnam.png"  # chemins d'accès des images
    logo_path = "logo.png"

    try:  # Si la carte et le logo ne se loadent pas, on ne crash pas.
        carte = pygame.image.load(image_path)
        logo = pygame.image.load(logo_path)
    except pygame.error as e:
        print(f"Erreur lors du chargement de la carte : {e}")
        pygame.quit()
        raise SystemExit

    carte_width, carte_height = carte.get_size()  # Récupérer la taille de la carte

    new_width = carte_width
    new_height = carte_height

    if carte_width > max_width or carte_height > max_height:  # Redimensionnement

        scale_width = max_width / carte_width
        scale_height = max_height / carte_height

        scale_factor = min(scale_width, scale_height)

        new_width = int(carte_width * scale_factor)
        new_height = int(carte_height * scale_factor)

        carte = pygame.transform.scale(carte, (new_width, new_height))

        carte_width, carte_height = new_width, new_height

    screen = pygame.display.set_mode((carte_width, carte_height))

    pygame.display.set_caption("Carte d'Yharnam")
    pygame.display.set_icon(logo)

    original_zones = [
        ("Iron Bridge",
         pygame.Rect(new_width * 31 / 100, new_height * 23 / 100, new_width * 27 / 100, new_height * 21 / 100)),
        ("Dunwall",
         pygame.Rect(new_width * 25.5 / 100, new_height * 53 / 100, new_width * 33 / 100, new_height * 14 / 100)),
        ("Rapeture",
         pygame.Rect(new_width * 68 / 100, new_height * 37 / 100, new_width * 9 / 100, new_height * 32 / 100)),
    ]  # pygame.Rect( x , y , width , height) Ici les valeurs sont des % de la fenêtre

    # scale_z devient racine de la profondeur si elle est <= max_profondeur sinon scale_x devient scale_factor
    scale_x = carte_width / carte_width if carte_width <= max_width else scale_factor
    scale_y = carte_height / carte_height if carte_height <= max_height else scale_factor

    zones = [
        (name, pygame.Rect(
            int(rect.x * scale_x),
            int(rect.y * scale_y),
            int(rect.width * scale_x),
            int(rect.height * scale_y)
        ))
        for name, rect in original_zones  # On associe pour chaque nom son rectangle
    ]

    running = True
    running2 = True

    while running:
        for event in pygame.event.get():  # test clic gauche
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for name, rect in zones:  # si clic gauche alors
                    if rect.collidepoint(mouse_pos):  # on check si c'est dans l'un des rectangles
                        choix_base1 = name
                        print(f"\033[3m\nVous vous dirigez dans le quartier de \033[3;35m{name}\033[0m,")
                        running = False

        screen.blit(carte, (0, 0))  # Poser l'image sur la fenêtre

        # Dessiner les zones interactives avec une couleur blanche transparente
        for _, rect in zones:
            # Créer une surface avec transparence
            transparent_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            # Remplir la surface avec une couleur blanche semi-transparente
            transparent_surface.fill((255, 255, 255, 30))  # RGBA
            # Blitter la surface semi-transparente sur l'écran
            screen.blit(transparent_surface, rect.topleft)

        pygame.display.flip()  # Apparemment sans cette fonction la fenêtre est pitch black ?

        if running2 == True:
            keyboard.wait("shift")
            print("\nVous relevez plusieurs points sur votre Carte."), time.sleep(to_sleep)
            print("Le quartier de \033[3;35mDunwall\033[0m, de \033[3;35mRapeture\033[0m, de \033[3;35mIron Bridge\033[0m et trois chemins,"), time.sleep(to_sleep)
            print("un vers le Sud, un vers le Nord, et un vers l'Ouest\n"), time.sleep(to_sleep2)
            print("Système : [Afficher la carte, et cliquez sur le nom d'un quartier pour vous y diriger]")
            running2 = False

    pygame.quit()

    if choix_base1 == "Dunwall":
        print("\033[3mVous êtes au sein du quartier principal du village.\n"), keyboard.wait("shift")
        print("Mais quelque chose cloche :")
        print("Les rues, habituellement animées, sont étrangement désertes.\n"), keyboard.wait("shift")
        print("Vous progressez à travers plusieurs ruelles silencieuses, jusqu'à apercevoir une silhouette.\n"), keyboard.wait("shift")
        print("Au bout de l'impasse où vous vous trouvez, un homme se tient là, immobile.\n")
        print("Une longue cape enveloppe son corps, masquant ses intentions.\n"), keyboard.wait("shift")
        print("Il attend."), keyboard.wait("shift")
        print("Seul.\n"), keyboard.wait("shift")
        print("Son murmure brise le silence, ses paroles étranges résonnent dans un dialecte inconnu\033[0m\n"), keyboard.wait("shift")
        print("\033[1;31m.slı-ʇuǝıos sʇıpnɐɯ‘sli-tneios stiduam‘slı-ʇuǝıos sʇıpnɐɯ\033[0m\n"), keyboard.wait("shift")
        print("\033[3mQuand il se retourne, son regard s'accroche au votre.\n")
        print("Son oeil perçant vous fixe, et une terreur glaciale vous paralyse.\nVos jambes refusent de bouger.\n"), keyboard.wait("shift")
        print("Il s'avance, lentement.\nVous êtes cloué sur place.\033[0m\n"), keyboard.wait("shift")
        print("\033[1;31m.slı-ʇuǝıos sʇıpnɐɯ‘sli-tneios stiduam‘slı-ʇuǝıos sʇıpnɐɯ\033[0m\n"), keyboard.wait("shift")
        print("\033[3mL'homme est désormais tout proche. Une force invisible semble emprisonner votre corps.\n"), keyboard.wait("shift")
        print("Soudain, il tire une dague de sous sa cape. L'éclat de la lame est la dernière chose que vous voyez\navant qu'il ne vous la plante dans le ventre\n"), keyboard.wait("shift")
        print("Une douleur fulgurante envahit tout votre être.\n"), keyboard.wait("shift")
        print("Il murmure d'une voix grave :\033[0m\n"), keyboard.wait("shift")
        print("\033[1;31mSachez que Dieu peut vous juger,\nmais ses péchés sont plus nombreux que les vôtres.\033[0m\n"), keyboard.wait("shift")
        print("\033[1;34mQue... Quoi ?\033[0m\n"), keyboard.wait("shift")
        print("\033[1;31mDieu... m'a piégé.\n"), keyboard.wait("shift")
        print("\033[1;31mIl n'est plus.\nDepuis des millénaires. Et personne ne le sait !\n"), keyboard.wait("shift")
        print("Mais moi... Moi je le sais. Il ne tromperont plus personne !\n")
        print("Je révèlerai leur secret au monde !\033[0m\n"), keyboard.wait("shift")
        for i in range(3):
            print("\033[1;34m.\033[0m", end=""), time.sleep(to_sleep2)
        keyboard.wait("shift")
        print("\n\n\033[3mL'homme s'éloigne, vous abandonnant à votre sort. Son discours vous échappe.\n"), time.sleep(to_sleep2)
        print("Peu importe, vous sentez que tout est fini.\n"), keyboard.wait("shift")
        print("Votre vision se brouille. Les ténèbres envahissent votre esprit.")
        print("Vos membres s'engourdissent puis disparaissent, comme si votre corps se dissolvait.\033[0m\n"), keyboard.wait("shift")
        for i in range(3):
            print(".", end=""), time.sleep(to_sleep2)
        keyboard.wait("shift")
        print("\n\n\033[3mLorsque vous rouvrez les yeux, vous êtes étendu sur le sol, dans la ruelle.\nEn vie.\n"), keyboard.wait(
            "shift")
        print("Vous cherchez sur votre corps, mais aucune trace de blessure n'est visible.\n")
        print("Un rêve ? Etait-ce seulement un rêve ?\n"), keyboard.wait("shift")
        print("En sortant de l'impasse, vous découvrez une rue grouillante de vie.\nUn contraste saisissant.\n"), keyboard.wait("shift")
        print("Les paroles de l'inconnu hantent encore votre esprit. Pourquoi avoir rêvé de cela ?\n"), keyboard.wait("shift")
        print("N'obtenant aucune réponse, vous décidez de reprendre votre chemin.\033[0m")

    elif choix_base1 == "Iron Bridge":
        print("\033[3mUn lieu si petit, qu'il ne se résume qu'à une unique rue menant à un vieux pont de pierre.\n"), keyboard.wait("shift")
        print("Alors que vous approchez du pont, vous remarquez un mendiant assis à même le sol.\033[0m\n"), keyboard.wait("shift")
        print("\033[1;31mUne p'tite pièce m'sieur ?\033[0m\n"), keyboard.wait("shift")
        print(f"\033[3mSans trop réfléchir, vous lui donnez {po_player} pièces d'or.\033[0m\n"), time.sleep(to_sleep2)
        print("\033[1;31mJe vous suis redevable, gardez ces deux pièces d'or, vous en aurez besoin.\033[0m\n"), keyboard.wait("shift")
        po_player = 2
        print("Vous vous arrêtez net et vous tournez vers lui.\n"), keyboard.wait("shift")
        print("\033[1;31mMais... Pourquoi m'avoir donné de l'argent ?\033[0m\n"), keyboard.wait("shift")
        while True:
            print('"Parce que vous en avez besoin." [1]')
            print('"Vous voulez que je le reprenne ?" [2]')
            try:
                choix_base1 = int(input("⮚ "))
                print(" ")
                if choix_base1 == 1:
                    print("\033[1;34mParce que vous en avez besoin.\033[0m\n")
                    break
                elif choix_base1 == 2:
                    print("\033[1;34mVous voulez que je le reprenne ?\033[0m\n")
                    break
                break
            except ValueError:
                continue
        print("\033[1;31mApprochez.\033[0m\n"), keyboard.wait("shift")
        print("\033[3mVous obéissez presque instinctivement, comme si une force invisible vous poussait vers lui.\n\033[0m"), keyboard.wait("shift")
        print("\033[1;31mVous croyez vraiment avoir choisi de me donner cet argent ?\033[0m\n"), keyboard.wait("shift")
        print("\033[1;34mComment ça ?\nBien sûr que oui, j'aurais très bien pû passer mon chemin.\n"), keyboard.wait("shift")
        print("\033[1;31mC'est ce qu'on veut vous faire croire.\nVous pensez être maitre de vos choix, mais des forces bien au-dessus de nous\nmanipulent notre futur.\n"), keyboard.wait("shift")
        print("Nous faisons tous des choix, mais en réalité, ce sont ces choix qui nous façonnent.\n"), keyboard.wait("shift")
        print("Votre destin est déjà scellé.\033[0m\n"), keyboard.wait("shift")
        print("\033[3mUn frisson vous parcourt.\n\033[0m"), keyboard.wait("shift")
        print("\033[1;34mPourquoi devrai-je vous croire ?\033[0m\n"), keyboard.wait("shift")
        print("\033[1;31mFaites comme bon vous semble, personne ne vous force à me croire.\033[0m\n"), keyboard.wait("shift")
        print("\033[3mIl se penche légèrement vers vous, son murmure glacial résonne dans vos oreilles :\n\033[0m"), keyboard.wait("shift")
        print("\033[1;31mMais souvenez vous de mes paroles : un jour, vous comprenderez que j'avais raison.\n"), keyboard.wait("shift")
        print("Vous êtes déjà mort !\033[0m\n"), keyboard.wait("shift")
        print("\033[3mLe poids de ses mots vous oppresse, et une angoisse viscérale s'emparre de vous.\nIncapable de supporter plus longtemps cette conversation, vous tournez les talons\net vous éloignez à grandes enjambées.\n"), keyboard.wait("shift")
        print("Derrière vous, le rire rauque du vieillard résonne dans la rue déserte, s'accrochant à vos pensées\ncomme une ombre persistante.\n"), keyboard.wait("shift")
        print("Arrivé à la sortie du village, vous ralentissez enfin votre course.\nLes paroles du vieil homme tournent en boucle dans votre esprit.\n"), keyboard.wait("shift")
        print("Et s'il avait raison ?\n"), keyboard.wait("shift")
        print("Perdu dans vos pensées, vous reprenez votre chemin, troublé et incapable de donner un sens à cette\nrencontre.\033[0m")

    elif choix_base1 == "Rapeture":
        print("\033[3mDe l'autre coté de la rivière.")
        keyboard.wait("shift")
        print(" ")
        print("Vous marchez dans l'allée principale, à la recherche du chemin vers la Forêt Brumeuse,\navant d'apercevoir quelque chose de brillant, posé au sol.")
        keyboard.wait("shift")
        print(" ")
        po_player += 2
        print("Vous vous approchez et ramassez l'objet.\nIl s'agit de deux pièces d'or.\033[0m [+ 2 \033[0;3;33mPO\033[0m], [",po_player,"\033[0;3;33mPO\033[0m]")


def esprit_farceur():
    print(" ")
    keyboard.wait("shift")
    print("\033[3mVous êtes maintenant en route vers La Forêt Brumeuse\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;3;34m━" * largeur_console)
    print("Chapitre 2 : Le Chemin vers la Forêt")
    print("━" * largeur_console)
    print(" \033[0m")
    keyboard.wait("shift")
    print("\033[3mPeu après avoir quitté le village, votre attention est attirée par une étrange lueur verte scintillante\nau bord de la route.\n"), keyboard.wait("shift")
    print("En vous approchant prudemment, vous distinguez un vieux tronc d’arbre d’où émane cette\nmystérieuse lumière. L’envie de comprendre l’origine de ce phénomène l’emporte sur votre\nméfiance, et vous avancez lentement, le cœur battant.\n"), keyboard.wait("shift")
    print("Vous êtes désormais à moins d’un mètre du tronc lorsqu’une petite boule lumineuse en surgit\nsoudainement.\n"), keyboard.wait("shift")
    print("La sphère flottante, baignée de cette lumière verte envoûtante, commence à tourner autour de vous\ndans des mouvements lents et hypnotiques. Elle évoque les Esprits des contes de fées que vous avez\nentendus dans votre enfance.\n"), keyboard.wait("shift")
    print("En observant de plus près, vous réalisez qu’il s’agit bien d’un Esprit, et plus précisément d’un Esprit\nFarceur, ces créatures légendaires connues pour leur penchant à dérober et à se moquer des\nvoyageurs imprudents.\n"), keyboard.wait("shift")
    print("Avant que vous ne puissiez esquisser le moindre geste, l’Esprit s’immobilise brusquement face à\nvous, flottant à hauteur de vos yeux.\n"), keyboard.wait("shift")
    print("Une voix étrange, à la fois douce et espiègle, résonne dans votre esprit :\n"), keyboard.wait("shift")
    print("\033[1;32mJ’ai une proposition pour toi.\nJe pense à un chiffre entre 1 et 3.\nTu le trouves, je double ton argent !\n"), keyboard.wait("shift")
    print("par contre, si tu perds, je garde la moitié\nde ta fortune.\n"), keyboard.wait("shift")
    print("Partant ?\033[0m\n"), keyboard.wait("shift")
    global choix_base1, val_test, po_player

    while True:
        print('"Pourquoi vous ferais-je confiance ?" [1]')
        print("Attaquer la créature [2]")
        print("Accepter l'offre [3]")
        try:
            choix_base1 = int(input("⮚ "))
            print()
            if choix_base1 == 1:
                print("\033[1;34mPourquoi vous ferais-je confiance ?\033[0m")
                keyboard.wait("shift")
                print(" ")
                print(
                    "\033[1;32mTu n'as pas le choix.\nJ'ai déjà la moitié de ton or, refuse mon offre,\net je garde "
                    "tout pour moi !\033[0m")
                keyboard.wait("shift")
                print(" ")
                while True:
                    print("Accepter l'offre [1]")
                    print("Attaquer la créature [2]")
                    choix_base1 = int(input("⮚"))
                    print(" ")
                    try:
                        if choix_base1 == 1:
                            print("\033[1;32mAlors, choisis un nombre entre 1 et 3\033[0m")
                            choix_base1 = int(input("⮚"))
                            val_test = random.randint(1, 3)
                            if choix_base1 != val_test:
                                print(" ")
                                print("\033[1;32mDommage, tu as tort.\nAllez, à la prochaine.\033[0m")
                                po_player = po_player / 2
                                print("\033[3mVous perdez la moitié de votre or [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            else:
                                print("\033[1;32mMmmh...\033[0m")
                                time.sleep(to_sleep)
                                print("\033[1;32mTu m'as eu... Tiens, ton argent.\033[0m")
                                po_player = po_player * 2
                                print("\033[3mVous doublez votre argent ! [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            break
                        elif choix_base1 == 2:
                            print(
                                "Au moment où vous tentez de mettre fin aux jours de l'Esprit,\nCe dernier s'envole "
                                "et vous esquive.")
                            keyboard.wait("shift")
                            print(" ")
                            print(
                                "\033[1;32mAh ! tu pensais vraiment pouvoir m'atteindre,\nje suis bien trop rapide "
                                "pour toi !\033[0m")
                            keyboard.wait("shift")
                            print(" ")
                            print("\033[1;32mAlors, choisis un nombre entre 1 et 3\033[0m")
                            choix_base1 = int(input("⮚"))
                            val_test = random.randint(1, 3)
                            if choix_base1 != val_test:
                                print(" ")
                                print("\033[1;32mDommage, tu as tort.\nAllez, à la prochaine.\033[0m")
                                po_player = po_player / 2
                                print("Vous perdez la moitié de votre or [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            else:
                                print("\033[1;32mMmmh...\033[0m")
                                time.sleep(to_sleep)
                                print("\033[1;32mTu m'as eu... Tiens, ton argent.\033[0m")
                                po_player = po_player * 2
                                print("Vous doublez votre argent ! [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            break
                    except ValueError:
                        continue
                    break
                break

            elif choix_base1 == 2:
                print(
                    "Au moment où vous tentez de mettre fin aux jours de l'Esprit,\nCe dernier s'envole et vous "
                    "esquive.")
                keyboard.wait("shift")
                print(" ")
                print(
                    "\033[1;32mAh ! tu pensais vraiment pouvoir m'atteindre,\nje suis bien trop rapide pour toi "
                    "!\033[0m")
                keyboard.wait("shift")
                print(" ")
                while True:
                    print("Accepter l'offre [1]")
                    print('"Pourquoi vous ferais-je confiance" [2]')
                    choix_base1 = int(input("⮚"))
                    print(" ")
                    try:
                        if choix_base1 == 1:
                            print("\033[1;32mAlors, choisis un nombre entre 1 et 3\033[0m")
                            choix_base1 = int(input("⮚"))
                            val_test = random.randint(1, 3)
                            if choix_base1 != val_test:
                                print(" ")
                                print("\033[1;32mDommage, tu as tort.\nAllez, à la prochaine.\033[0m")
                                po_player = po_player / 2
                                print("Vous perdez la moitié de votre or [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            else:
                                print("\033[1;32mMmmh...\033[0m")
                                time.sleep(to_sleep)
                                print("\033[1;32mTu m'as eu... Tiens, ton argent.\033[0m")
                                po_player = po_player * 2
                                print("Vous doublez votre argent ! [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            break
                        elif choix_base1 == 2:
                            print("\033[1;34mPourquoi vous ferais-je confiance ?\033[0m")
                            keyboard.wait("shift")
                            print(" ")
                            print(
                                "\033[1;32mTu n'as pas le choix.\nJ'ai déjà la moitié de ton or, refuse mon offre,"
                                "\net je garde tout pour moi !\033[0m")
                            keyboard.wait("shift")
                            print(" ")
                            print("\033[1;32mAlors, choisis un nombre entre 1 et 3\033[0m")
                            choix_base1 = int(input("⮚"))
                            val_test = random.randint(1, 3)
                            if choix_base1 != val_test:
                                print(" ")
                                print("\033[1;32mDommage, tu as tort.\nAllez, à la prochaine.\033[0m")
                                po_player = po_player / 2
                                print("Vous perdez la moitié de votre or [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            else:
                                print("\033[1;32mMmmh...\033[0m")
                                time.sleep(to_sleep)
                                print("\033[1;32mTu m'as eu... Tiens, ton argent.\033[0m")
                                po_player = po_player * 2
                                print("Vous doublez votre argent ! [", po_player, "\033[0;3;33mPO\033[0m]")
                                break
                            break
                    except ValueError:
                        continue
                    break
                break

            elif choix_base1 == 3:
                print("\033[1;32mAlors, choisis un nombre entre 1 et 3\033[0m")
                choix_base1 = int(input("⮚ "))
                val_test = random.randint(1, 3)
                if choix_base1 != val_test:
                    print(" ")
                    print("\033[1;32mDommage, tu as tort.\nAllez, à la prochaine.\033[0m")
                    po_player = po_player / 2
                    print("Vous perdez la moitié de votre or, vous avez maintenant [", po_player, "\033[0;3;33mPO\033[0m]")
                    break
                else:
                    print("\033[1;32mMmmh...\033[0m")
                    time.sleep(to_sleep)
                    print("\033[1;32mTu m'as eu... Tiens, ton argent.\033[0m")
                    po_player = po_player * 2
                    time.sleep(to_sleep)
                    print(" ")
                    print("Vous doublez votre argent ! [", po_player, "\033[0;3;33mPO\033[0m]")
                    break
                break
            else:
                print("Système : [Veuillez entrer une valeur comprise entre 1 et 3 !]\n")
        except ValueError:
            print("Système : [Veuillez entrer une valeur comprise entre 1 et 3 !]\n")
            continue
    print(" ")
    return po_player


def suite_esprit():
    keyboard.wait("shift")
    print("\033[3mAprès cette étrange rencontre, vous décidez que faire une pause est nécessaire.")
    keyboard.wait("shift")
    print(" ")
    print("Vous montez votre campement sur le bord du chemin que vous suivez depuis plus d'une heure.")
    keyboard.wait("shift")
    print(" ")
    print(
        "Vous êtes dans un campement.\n"
        "Vous pouvez y faire plusieurs actions afin de faire progresser votre personnage :\033[0m\n"
        "- Acheter des objets (Potions, Sort...)\n"
        "- Miser vos \033[0;3;33mPO\033[0m\n"
        "- Récupérer vos \033[0;31mPV\033[0m et \033[0;32mPE\033[0m\n"
    )
    keyboard.wait("shift")

    global po_player, pv_player, stats, choix_base1, val_test, lvl_amulette
    print("━" * largeur_console)
    print("\033[1mCampement\033[0m")
    print("━" * largeur_console), time.sleep(to_sleep2)

    while True:
        print(" ")
        print("Vous avez", pv_player, "\033[0;31mPV\033[0m,", stats["endurance"], "\033[0;32mPE\033[0m, et", po_player,
              "\033[0;3;33mPO\033[0m")
        time.sleep(to_sleep2)
        print(" ")
        print("Acheter des objets [1]")
        print("Miser vos \033[0;3;33mPO\033[0m, [", po_player, "\033[0;3;33mPO\033[0m] [2]")
        print("Vous reposer (Met fin au campement) [3]")

        try:
            choix_base1 = int(input("⮚ "))

            if choix_base1 == 1:
                print(" ")
                print("Vous avez", po_player, "\033[0;3;33mPO\033[0m")
                time.sleep(to_sleep2)
                print(" ")
                print("Potion de Vie (+2\033[0;31mPV\033[0m)(3\033[0;3;33mPO\033[0m) [1]")
                print("Fiole d'Endurance (+2\033[0;32mPE\033[0m)(3\033[0;3;33mPO\033[0m) [2]")
                print("Jeton de Lumière (+1 lvl d'Amulette)(5\033[0;3;33mPO\033[0m) [3]")
                print("Sort de Cupidité (+2...8\033[0;3;33mPO\033[0m)(5\033[0;3;33mPO\033[0m) [4]")
                print("Parchemin de Stat (+1 \033[0;36mstat\033[0m)(5\033[0;3;33mPO\033[0m) [5]")
                choix_base1 = int(input("⮚"))
                if choix_base1 == 1 and po_player >= 3:
                    pv_player += 2
                    po_player -= 3
                    print(" ")
                    print("Vous regagnez 2 \033[0;31mPV\033[0m, [", pv_player, "\033[0;31mPV\033[0m]")
                    time.sleep(to_sleep2)
                elif choix_base1 == 2 and po_player >= 3:
                    stats["endurance"] += 2
                    po_player -= 3
                    print("Vous regagnez 2 \033[0;32mPE\033[0m, [", stats["endurance"], "\033[0;32mPE\033[0m]")
                    time.sleep(to_sleep2)
                elif choix_base1 == 3 and po_player >= 5:
                    lvl_amulette += 1
                    po_player -= 5
                    print("Votre amulette de Lumière gagne 1 niveau, [niveau", lvl_amulette, "]")
                    time.sleep(to_sleep2)
                elif choix_base1 == 4 and po_player >= 5:
                    val_test = random.randint(2, 8)
                    po_player += val_test
                    po_player -= 5
                    print("Vous gagnez", val_test, "\033[0;3;33mPO\033[0m")
                    time.sleep(to_sleep2)
                elif choix_base1 == 5 and po_player >= 5:
                    print("Quelle \033[0;36mstat\033[0m améliorer ?")
                    time.sleep(to_sleep2)
                    print(" ")
                    print("Tu as", stats["force"], "de \033[0;36mForce\033[0m [1]"), time.sleep(to_sleep)
                    print("Tu as", stats["agilite"], "d'\033[0;36mAgilité\033[0m [2]"), time.sleep(to_sleep)
                    print("Tu as", stats["eloquence"], "d'\033[0;36mEloquence\033[0m [3]"), time.sleep(to_sleep)
                    print("Tu as", stats["arcane"], "d'\033[0;36mArcane\033[0m [4]"), time.sleep(to_sleep)
                    choix_base1 = int(input("⮚"))
                    try:
                        if choix_base1 == 1:
                            stats["force"] += 1
                            po_player -= 5
                            print("Vous avez +1 en \033[0;36mForce\033[0m [", stats["force"], "\033[0;36mForce\033[0m]")
                            time.sleep(to_sleep2)
                        elif choix_base1 == 2:
                            stats["agilite"] += 1
                            po_player -= 5
                            print("Vous avez +1 en \033[0;36mAgilité\033[0m [", stats["agilite"],
                                  "\033[0;36mAgilité\033[0m]")
                            time.sleep(to_sleep2)
                        elif choix_base1 == 3:
                            stats["eloquence"] += 1
                            po_player -= 5
                            print("Vous avez +1 en \033[0;36mEloquence\033[0m [", stats["eloquence"],
                                  "\033[0;36mEloquence\033[0m]")
                            time.sleep(to_sleep2)
                        elif choix_base1 == 4:
                            stats["arcane"] += 1
                            po_player -= 5
                            print("Vous avez +1 en \033[0;36mArcane\033[0m [", stats["arcane"], "\033[0;36mArcane\033[0m]")
                            time.sleep(to_sleep2)
                    except ValueError:
                        continue
            elif choix_base1 == 2:
                print(" ")
                print("Vous avez", po_player, "\033[0;3;33mPO\033[0m")
                print("Choisissez une somme à miser :")
                print(
                    "2\033[0;3;33mPO\033[0m[1], 4\033[0;3;33mPO\033[0m[2], 7\033[0;3;33mPO\033[0m[3],"
                    "10\033[0;3;33mPO\033[0m[4]")
                choix_base1 = int(input("⮚ "))
                if choix_base1 == 1 and po_player >= 2:
                    print("Vous misez 2\033[0;3;33mPO\033[0m")
                    val_test = random.randint(1, 2)
                    if val_test == 1:
                        print("Vous perdez votre argent [-2\033[0;3;33mPO\033[0m]")
                        po_player -= 2
                    elif val_test == 2:
                        print("Vous doublez votre argent[+2\033[0;3;33mPO\033[0m]")
                        po_player += 2
                elif choix_base1 == 2 and po_player >= 4:
                    print("Vous misez 4\033[0;3;33mPO\033[0m")
                    val_test = random.randint(1, 2)
                    if val_test == 1:
                        print("Vous perdez votre argent [-4\033[0;3;33mPO\033[0m]")
                        po_player -= 4
                    elif val_test == 2:
                        print("Vous doublez votre argent[+4\033[0;3;33mPO\033[0m]")
                        po_player += 4
                elif choix_base1 == 3 and po_player >= 7:
                    print("Vous misez 7\033[0;3;33mPO\033[0m")
                    val_test = random.randint(1, 2)
                    if val_test == 1:
                        print("Vous perdez votre argent [-7\033[0;3;33mPO\033[0m]")
                        po_player -= 7
                    if val_test == 2:
                        print("Vous doublez votre argent[+7\033[0;3;33mPO\033[0m]")
                        po_player += 7
                if choix_base1 == 4 and po_player >= 10:
                    print("Vous misez 10\033[0;3;33mPO\033[0m")
                    val_test = random.randint(1, 2)
                    if val_test == 1:
                        print("Vous perdez votre argent [-10\033[0;3;33mPO\033[0m]")
                        po_player -= 10
                    if val_test == 2:
                        print("Vous doublez votre argent[+10\033[0;3;33mPO\033[0m]")
                        po_player += 10
            elif choix_base1 == 3:
                print(" ")
                print("\033[3mVous vous endormez et récupérez vos \033[0;31mPV\033[0m et \033[0;32mPE\033[0m")
                pv_player += 2
                stats["endurance"] += 2
                print("[", pv_player, "\033[0;31mPO\033[0m], [", stats["endurance"], "\033[0;32mPE\033[0m], [", po_player,
                      "\033[0;3;33mPO\033[0m]")
                keyboard.wait("shift")
                print(" ")
                break
            else:
                print("Système : [Veuillez entrer une valeur comprise entre 1 et 3 !]")
        except ValueError:
            print("Système : [Veuillez entrer une valeur comprise entre 1 et 3 !]")
    return po_player, pv_player, stats, lvl_amulette


def bandits():
    global val_test, choix_base1, stats, pv_player, po_player
    print("\033[3mVous reprenez la route dès le lendemain matin, après une bonne nuit de sommeil.")
    keyboard.wait("shift")
    print(" ")
    print(
        "Après quelques minutes de marche sur un étroit chemin de terre,\nvous remarquez quelque chose de bizarre, "
        "vous ne pouvez pas deviner quoi, mais vous avez un mauvais pressentiment.")
    keyboard.wait("shift")
    print(" ")
    print("Vous allez lancer un sort afin d'analyser la zone autour de vous.")
    keyboard.wait("shift")
    print(" ")
    print("Vous allez tester votre score d'\033[0;36mArcane\033[0m")
    time.sleep(to_sleep)
    print(
        "Le résultat de ce test est aléatoire, plus votre score de la stat correspondante (ici \033[0;36mArcane\033["
        "0m)\nest haute, plus votre chance de remporter le test est haute.")
    keyboard.wait("shift")
    print(" ")
    print("Vous lancez votre Sort de Repérage :")
    print("[N'appuyez sur aucune touche pendant le lancement d'un sort !]")
    print(" ")
    for i in tqdm.tqdm(range(30)):
        # pause de 0.1 sec.
        time.sleep(0.1)
    print(" ")
    val_test = random.randint(1, 10)
    print("\033[3mSoudain, trois ombres surgissent de derrière les arbres et vous attaquent par surprise.")
    if val_test > stats["arcane"]:
        print("Dans la panique, votre concentration vacille et votre sort échoue.")
        keyboard.wait("shift")
        print(" ")
        time.sleep(to_sleep)
        print("un coup rapide vous atteint.\033[0m")
        pv_player -= 1
        print("Vous perdez 1 \033[0;31mPV\033[0m [", pv_player, "\033[0;31mPV\033[0m]")
    keyboard.wait("shift")
    if pv_player <= 0:
        print("\033[0;31mVous êtes mort\033[0m")
    print(" ")
    print("\033[3mVous reculez légèrement, essayant de reprendre vos esprits, alors que les trois silhouettes se\ndressent maintenant devant vous.\033[0m\n"), keyboard.wait("shift")
    print("\033[1;31mMmmh... Intéressant.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mCelui là ne semble pas vouloir se rendre facilement\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mAlors, on va lui montrer ce que ça fait de mourir !\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[3mSans attendre, les trois hommes, dissimulés derrière leurs longues capes et masquès par leurs\ncapuches, se précipitent vers vous, tête baissée, prêts à en découdre.\n"), keyboard.wait("shift")
    while True:
        try:
            print("[\033[0;36mArcane\033[0m :", stats["arcane"],
                  "] Lancer un sort assez vite pour les stopper [1]")
            print("[\033[0;36mForce\033[0m :", stats["force"],
                  "] Engager le combat [2]")
            choix_base1 = int(input("⮚ "))
            if choix_base1 == 1:
                print(" ")
                print("━" * largeur_console, )
                print("Test d'\033[0;36mArcane\033[0m")
                print("━" * largeur_console, ), time.sleep(to_sleep2)
                print(" ")

                print("Vous :", stats["arcane"], "stat d'\033[0;36mArcane\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 6 stat d'\033[0;36mArcane\033[0m")
                elo_adverse = 6

                while True:
                    val_test = int(
                        input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !")
                        continue
                    else:
                        print("Vous avez désormais", stats["arcane"] + val_test, "stat d'\033[0;36mArcane\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["arcane"] + val_test >= 8:
                    print("Vous lancez votre sort si vite que vos ennemis n'ont pas le temps de vous atteindre.\n"
                            "Les trois hommes se retrouvent allongés par terre, assommés. En fouillant l'un d'entre"
                            "eux,\nvous trouvez une bourse pleine d'or ![ +3 \033[0;3;33mPO\033[0m][",
                            po_player + 3, "\033[0;3;33mPO\033[0m]")
                    po_player += 3
                    break
                elif stats["arcane"] + val_test < elo_adverse:
                    pv_player -= 3
                    print(
                        "Votre sort ne se lance pas assez vite. L'un des trois hommes sort une dague et vous la "
                        "plante dans l'avant-bras, avant de prendre la fuite.\n[ -3 \033[0;31mPV\033[0m][",
                        pv_player, "\033[0;31mPV\033[0m]")
                    if pv_player <= 0:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                elif 8 > stats["arcane"] + val_test >= elo_adverse:
                    print(
                        "Votre sort n'atteint pas vos cibles, mais, pris de peur, vous les voyez fuir le plus "
                        "vite possible.")
                    break
                break

            elif choix_base1 == 2:

                print("━" * largeur_console)
                print("- Test de \033[0;36mForce\033[0m -")
                print("━" * largeur_console), time.sleep(to_sleep2)

                print("Vous :", stats["force"], "stat de \033[0;36mForce\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 5 stat de \033[0;36mForce\033[0m")
                while True:
                    val_test = int(
                        input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !")
                        continue
                    else:
                        print("Vous avez désormais", stats["force"] + val_test, "stat de \033[0;36mForce\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["force"] + val_test >= 7:
                    print(
                        "Vous sortez votre épée, et tranchez le bras de deux de vos adversaires.\n Le troisième "
                        "reste debout, vous implorant de l'épargner. Dans sa fuite,\n"
                        "il fait tomber une bourse pleine de pièce d'or [ +3 \n\033[0;3;33mPO\n\033[0m][",
                        po_player + 3, "\033[0;3;33mPO\033[0m]")
                    po_player += 3
                    break
                elif stats["force"] + val_test < 5:
                    pv_player -= 3
                    print(
                        "Pendant que vous vous occupez de deux d'entre eux, le troisième sort\nune dague, "
                        "et vous la plante dans le dos, avant de partir en courant.\n[ -3 \033[0;31mPV\033[0m][",
                        pv_player,
                        "\033[0;31mPV\033[0m]")
                    if pv_player <= 0:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                elif 7 > stats["force"] + val_test >= 5:
                    print(
                        "Vous battez le premier se présentant à vous. Sous l'effet de la peur,\nles deux autres "
                        "partent en courant.")
                    break
                break
            else:
                print("Système : [Veuillez entrer [1] ou [2] !]\n")
        except ValueError:
            print("Système : [Veuillez entrer [1] ou [2] !]\n")
            continue


def suite_bandits():
    global choix_base1
    keyboard.wait("shift")
    print(" ")
    for i in range(0, 3):
        print(".", end=""), time.sleep(to_sleep2)
    print(" ")
    print("Un étrange malaise vous envahit.\n"), keyboard.wait("shift")
    print("Votre tête tourne, votre vision s'obscurcit, et soudain..."), keyboard.wait("shift")
    print("Plus rien.\n"), keyboard.wait("shift")
    print("Il n’y a plus autour de vous que du vide, une étendue sans fin, et votre corps semble avoir disparu,\ncomme si vous n'existiez plus.\n"), keyboard.wait("shift")
    print("Puis, une lumière pâle émerge dans l'obscurité, venant de derrière vous.\nEn vous retournant, vous apercevez Sélène.\n"), keyboard.wait("shift")
    print("Elle flotte, légère, juste au-dessus du sol, ses yeux rivés sur vous avec une intensité presque palpable.\n"), keyboard.wait("shift")
    print("\033[1;3;33mTe voila. Je te vois enfin.\033[0m\n"), keyboard.wait("shift")

    print('"Mais... Comment est-ce possible ?" [1]')
    print('"Où suis-je ?" [2]')
    choix_base1 = int(input("⮚ "))
    while True:
        try:
            if choix_base1 == 1:
                print("\n\033[1;34mMais... Comment est-ce possible ?\n\033[0m")
                break
            elif choix_base1 == 2:
                print("\n\033[1;34mOù suis-je ?\n\033[0m")
                break
            break
        except ValueError:
            continue
    keyboard.wait("shift")

    print("\033[1;3;33mtu es chez moi.\nEnfin, ton corps astral, est chez moi."), keyboard.wait("shift")
    print("Ne t'inquiète pas, tu es toujours en vie, tu es juste...\nDisons, dans le coma.\n"), keyboard.wait("shift")
    print("Ces trois hommes, ceux de tout à l'heure, ce sont des membres du Culte du Soleil.\nL'un d'eux t'a lancé un sort avant même que tu ne les voies.\n"), keyboard.wait("shift")
    print("C’est pour cela que tu es ici. Pour contrer ce sort, je devais te voir face à face. J’ai profité d’un\nmoment de faiblesse de ta part pour t’amener ici.\n\033[0m\n"), keyboard.wait("shift")
    print("Vous jetez un coup d'oeil autour de vous, pris de confusion.\n"), keyboard.wait("shift")

    print("'C'est si vide... Tu ne vis pas pas parmi les autres êtres de Lumières ?' [1]")
    print("'Il n'y a que toi ici ?' [2]")
    choix_base1 = int(input("⮚ "))
    while True:
        try:
            if choix_base1 == 1:
                print("\n\033[1;34mC'est si vide... Tu ne vis pas pas parmi les autres êtres de Lumières ?\n\033[0m")
                break
            elif choix_base1 == 2:
                print("\n\033[1;34mIl n'y a que toi ici ?\n\033[0m")
                break
            break
        except ValueError:
            continue
    keyboard.wait("shift")

    print("\033[1;3;33mLes êtres de Lumières ne sont plus qu'une poignée, tous répartis dans l'infini Univers\033[0m\n"), keyboard.wait("shift")
    print("Elle laisse échapper un soupir.\n"), keyboard.wait("shift")
    print("\033[1;3;33mAutrefois, nous étions des milliers, mais cette époque est révolue.\nDepuis la mort des Dieux anciens, les êtres Astraux sont livrés à leur sort,\net sont devenus... mortels.\033[0m\n"), keyboard.wait("shift")
    print("Elle fixe l'horizon, comme perdue dans un souvenir lointain.\n"), keyboard.wait("shift")
    print("\033[1;3;33mNous vivons comme les hommes maintenant.\nDans l'attente de l'ultime tâche.\n"), keyboard.wait("shift")

    for i in range(0, 3):
        print(".", end=""), time.sleep(to_sleep2)
    print(" "), keyboard.wait("shift")
    print(" ")

    print("\033[1;34mLa... La mort des Dieux ?\033[0m\n"), keyboard.wait("shift")
    print("\033[1;3;33mOui, ils sont tous morts il y a bien longtemps maintenant.\nPersonne ne sait pourquoi. De toute manière nous ne sommes plus qu'une dizaine, cela fait plusieurs siècle que je n'ai vu aucun ""être\npar ici, je suis peut-être même la dernière.\n"), keyboard.wait("shift")
    print("Les derniers êtres Astraux à ma connaissance se sont rangés du coté du Culte du Soleil\033[0m\n"), keyboard.wait("shift")
    print("Elle vous fixe alors intensément, comme si elle voulait vous transmettre toute la gravité de ses paroles.\n")
    print("\033[1;3;33mTu dois être prudent. Ils sont nombreux, et très puissants.\nJe t'offrirai mon aide pour les vaincre,\ncar sans moi, tu n'auras aucune chance.\n"), keyboard.wait("shift")
    print("Sache une dernière chose.\nCe voyage.. sera ton dernier.\n"), keyboard.wait("shift")
    print("Tu ne survivras pas à un combat contre des êtres Astraux.\033[0m\n"), keyboard.wait("shift")
    print("\033[1;34mAlors pourquoi je devrai m'en occuper ?\033[0m\n"), keyboard.wait("shift")
    print("\033[1;3;33mIl est trop tard pour faire demi-tour.\nIls savent que tu arrives.\033[0m\n"), keyboard.wait("shift")
    print("Elle se rapproche de vous, la lumière autour d'elle vacillant.\n")
    print("\033[1;3;33mTon jugement commence maintenant, et ton sang brillera devant les temples de l'Homme !\033[0m\n"), keyboard.wait("shift")

    for i in range(0, 3):
        print(".", end=""), time.sleep(to_sleep2)
    print(" ")

    print("\nSoudain, vous êtes projeté de retour dans votre corps, allongé sur le sol, le souffle court\n"), keyboard.wait("shift")
    print("Une pensée obsède votre esprit : pourquoi vous ?\n"), keyboard.wait("shift")
    print("Pourquoi vous avoir choisi plutôt qu'un autre ?\nEt dire que tout partait d'une simple aventure...\n"), keyboard.wait("shift")

    print("\033[1;34mPourquoi moi ?...\033[0m\n"), keyboard.wait("shift")
    print("\033[1;3;33mCertains arbres s’épanouissent, d'autres meurent.\nCertaines vaches grandissent, d'autres sont "
          "dévorées par les loups.\nCertains hommes naissent assez riches et stupides pour profiter de la vie.\nRien "
          "n’est juste. Tu le sais très bien.\033[0m\n"), keyboard.wait("shift")
    print("\033[1;34m...\033[0m\n"), keyboard.wait("shift")

    print("\033[1;3;34m")
    print("━" * largeur_console)
    print("Chapitre 3 : La Forêt Brumeuse")
    print("━" * largeur_console)
    print(" \033[0m")


def foret():
    global choix_base1, val_test, name_chien, stats, pv_player, po_player
    keyboard.wait("shift")
    print("Environ 1 heure plus tard, vous arrivez à une intersection, au bord de la Forêt Brumeuse\n"), keyboard.wait(
        "shift")
    print(
        "En cherchant sur la carte quel chemin emprunter,\nvous remarquez que cette intersection n'y est pas indiquée.")
    keyboard.wait("shift")
    print(" ")
    print("On dirait que vous allez devoir choisir un chemin à l'aveugle.")
    keyboard.wait("shift")

    while True:
        print(" ")
        print("Emprunter le chemin de Gauche [1]")
        print("Aller tout droit [2]")
        print("Emprunter le chemin de droite [3]")
        choix_base1 = int(input("⮚ "))
        try:

            if choix_base1 == 1:
                print(" ")
                print("Vous vous engagez sur un chemin longeant la forêt")
                keyboard.wait("shift")
                print(" ")
                print("Après avoir fait quelques pas, vous entendez des gémissements venant\nde derrière des buissons")
                keyboard.wait("shift")
                print(" ")
                print("Vous vous approchez, arme à la main.")
                keyboard.wait("shift")
                print(" ")
                print(
                    "Vous poussez les buissons, et découvrez un chien.\nun chien au pelage blanc est allongé, au pied d'un homme, mort.\nSûrement son ancien propriétaire.")
                keyboard.wait("shift")
                print(" ")
                print("Vous vous décidez à reprendre votre chemin, alors que le chien viens se frotter à vos pieds.")
                keyboard.wait("shift")
                print(" ")
                print(
                    "Il semblerait que le chien veuille rester à vos côtés.\nVous ne voyez pas le problème, après tout,\nun peu de compagnie ne peut pas faire de mal.")
                keyboard.wait("shift")
                print(" ")
                print("Comment voulez-vous appeler le chien ?")
                name_chien = input("⮚ ")
                print(name_chien, "Rejoint votre groupe, et fait gagner +1 \033[0;36mForce\033[0m au groupe")
                stats["force"] += 1
                print("[", stats["force"], "de \033[0;36mForce\033[0m ]")
                break
            elif choix_base1 == 2:
                print(" ")
                print("Vous vous engagez sur le chemin menant droit à la Forêt")
                keyboard.wait("shift")
                print(" ")
                print("Alors que vous avancez sur ce chemin, vous entendez des bruits dans les arbres.\nEncore une embuscade ?")
                keyboard.wait("shift")
                print(" ")
                print("Vous dégainez votre arme, alors qu'un homme saute depuis les arbres,\net atterrit sur le chemin, derrière vous.\nVous lui foncez dessus tête baissée.")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;32mAttends !")
                keyboard.wait("shift")
                print(" ")
                print("Tu es bien en route vers le Sanctuaire ?\033[0m")
                keyboard.wait("shift")
                print(" ")
                print("Vous vous arrêtez devant l'homme, qui ne semble vous vouloir aucun mal.")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;34mle Sanctuaire ? \033[0m")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;32mOui, cet endroit dans la Forêt où la fin est censée commencer.\033[0m")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;34mDe quoi parle-tu donc ?\033[0m")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;32mTu ne sais donc pas ça ?\nTu te dirige vers ta fin, jeune Elias.")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;34mTu connais mon nom ?\033[0m")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;32mJe te suis depuis plusieurs jours déjà. Je me dirige au même endroit que toi.\nAu sanctuaire, pour arrêter le Culte du Soleil.")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;34mAlors... Je ne suis pas le seul à le savoir ?\033[0m")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;32mNous ne sommmes que deux. faisons équipe, seul tu n'arriveras à rien.\033[0m")
                keyboard.wait("shift")
                print(" ")
                print("Vous le connaissez à peine, et ne lui faites pas confiance.\nMais Sélène vous l'a dit, seul, vous n'ariverez à rien.")
                keyboard.wait("shift")
                print(" ")
                print("\033[1;34mPourquoi pas, de toute façon, nous n'en revienderons pas vivant.\033[0m")
                keyboard.wait("shift")
                print(" ")
                print("L'homme rejoint votre groupe, et fait gagner +1 \033[0;36mAgilité\033[0m au groupe")
                stats["agilite"] += 1
                print("[", stats["agilite"], "d'\033[0;36mAgilité\033[0m ]")
                break
            elif choix_base1 == 3:
                print(" ")
                print("Vous vous engagez sur un petit chemin sinueux.")
                keyboard.wait("shift")
                print(" ")
                print("Un petit sac est posé à l'entrée du chemin.")
                keyboard.wait("shift")
                print(" ")
                print("Vous décidez de le fouiller et y trouvez un Parchemin impregné de Magie.\nVous le lisez, ce qui vous donne un immense mal de tête.")
                keyboard.wait("shift")
                print(" ")
                print("Vous gagnez +1 \033[0;36mEloquence\033[0m, et +1 \033[0;36mArcane\033[0m")
                stats["eloquence"] += 1
                stats["arcane"] += 1
                print("[", stats["eloquence"], "d'\033[0;36mEloquence\033[0m ], [", stats["arcane"], "d'\033[0;36mArcane\033[0m ]")
                break
        except ValueError:
            continue
    keyboard.wait("shift")
    print(" ")
    print("Vous vous enfoncez maintenant dans la Forêt Brumeuse.")
    keyboard.wait("shift")
    print(" ")
    print("Vous êtes épuisé de votre aventure. Vous repensez à votre chez-vous.\nVous savez que vous n'y retournerez plus jamais.")
    keyboard.wait("shift")
    print(" ")
    print("alors que vous êtes perdu dans vos pensées, vous voyez au loin une créature, plus précisément un Troll.")
    keyboard.wait("shift")
    print(" ")
    print("Il est immense, jamais vous ne réussirez à le battre.\nAlors que vous vous faites cette remarque, vous remarquez une clé en or accrochée à sa ceinture.")
    keyboard.wait("shift")
    print(" ")
    print("Vous remarquez également quelque chose de plus interessant. Il n'a pas d'yeux, ou du moins il n'en a plus.")
    keyboard.wait("shift")
    print(" ")
    print("peut-être que vous pourrez le vaincre malgré sa force et sa taille.\nDe toute manière, vous ne pouvez pas faire demi-tour.")
    keyboard.wait("shift")
    print(" ")
    while True:
        try:
            print("[\033[0;36mAgilité\033[0m :", stats["agilite"],
                  "] Vous faufiler entre les arbre et éviter le combat [1]")
            print("[\033[0;36mForce\033[0m :", stats["force"],
                  "] Affronter le Troll face-à-face [Pas de récompense pour +2 stats] [2]")
            choix_base1 = int(input("⮚ "))
        except ValueError:
            print("Système : [Veuillez entrer une valeur proposée ci-dessous]")
        try:
            if choix_base1 == 1:
                print(" ")
                print("━" * largeur_console, )
                print("Test d'\033[0;36mAgilité\033[0m")
                print("━" * largeur_console, ), time.sleep(to_sleep2)
                print(" ")

                print("Vous :", stats["agilite"], "stat d'\033[0;36mAgilité\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 4 stat d'\033[0;36mAgilité\033[0m")
                elo_adverse = 4

                while True:
                    val_test = int(input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !")
                        continue
                    else:
                        print("Vous avez désormais", stats["agilite"] + val_test, "stat d'\033[0;36mAgilité\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["agilite"] + val_test >= 6:
                    print("Vous réussissez sans aucun mal à esquiver le monstre.\n[Aucune récompense n'est attribuée pour ce test dû à se simplicité !]")
                    break
                elif stats["agilite"] + val_test < elo_adverse:
                    pv_player -= 3
                    print("Le Troll vous entend et vous massacre.\n[ -3 \033["
                          "0;31mPV\033[0m][",
                          pv_player, "\033[0;31mPV\033[0m]")
                    if pv_player <= 0:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                elif 6 > stats["agilite"] + val_test >= elo_adverse:
                    print("Vous esquivez de justesse la créature.")
                    break
                break

            elif choix_base1 == 2:
                print("━" * largeur_console)
                print("- Test de \033[0;36mForce\033[0m -")
                print("━" * largeur_console), time.sleep(to_sleep2)

                print("Vous :", stats["force"], "stat de \033[0;36mForce\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 10 stat de\033[0;36mForce\033[0m")
                while True:
                    val_test = int(input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !")
                        continue
                    else:
                        print("Vous avez désormais", stats["force"] + val_test, "stat de \033[0;36mForce\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["force"] + val_test >= 10:
                    print("Vous réussissez à mettre la créature à terre, et à récupérer sa clé.\n Vous chercher aux alentour et trouvez un coffre. Vous essayez de l'ouvrir et découvrez un coffre plein de pièces d'or !\n"
                          "[ +4 \033[0;3;33mPO\033[0m][",
                          po_player + 7, "\033[0;3;33mPO\033[0m]")
                    po_player += 7

                    break
                elif stats["force"] + val_test < 9:
                    pv_player -= 5
                    print("Le Troll vous attrape par les jambes, et vous fracasse par Terre.\n[ -5 \033[0;31mPV\033[0m][", pv_player,
                          "\033[0;31mPV\033[0m]")
                    if pv_player <= 0:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                break

        except ValueError:
            print("Système : [Veuillez entrer une valeur valide]")
            continue
    return stats, po_player, pv_player


def gobelins():
    def rencontre_gobelins():
        global stats, pv_player, po_player

        print("\nVous continuez votre marche dans la Forêt.")
        keyboard.wait("shift")
        print(
            "\nLes arbres, aux troncs torsadés, forment des ombres inquiétantes, et une épaisse brume semble danser autour de vous.")
        keyboard.wait("shift")
        print("\nAlors que vous avancez prudemment, vous entendez un bruissement parmi les buissons...")
        keyboard.wait("shift")
        print(
            "\nSoudain, trois gobelins surgissent, armés de couteaux rouillés et vous fixant avec un sourire malveillant !")
        keyboard.wait("shift")

        print("Vous vous préparez à réagir rapidement !\n")
        while True:
            print("[\033[0;36mArcane\033[0m :", stats["arcane"],
                  "] Lancer un sort pour intimider ou attaquer les gobelins [1]")
            print("[\033[0;36mForce\033[0m :", stats["force"], "] Engager un combat physique [2]")

            try:
                choix = int(input("⮚ "))

                if choix == 1:
                    print(" ")
                    print("━" * largeur_console)
                    print("- Test d'\033[0;36mArcane\033[0m -")
                    print("━" * largeur_console)
                    time.sleep(to_sleep2)
                    print(" ")
                    print("Vous :", stats["arcane"], "stat d'\033[0;36mArcane\033[0m")
                    print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                    print("Adversaire : 6 stat d'\033[0;36mArcane\033[0m")
                    while True:
                        val_test = int(
                            input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                        if val_test > stats["endurance"]:
                            print(
                                "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                                "0;32mEndurance\033[0m !")
                            continue
                        else:
                            print("Vous avez désormais", stats["arcane"] + val_test, "stat d'\033[0;36mArcane\033[0m")
                            break
                    if val_test + stats["arcane"] >= 8:
                        print("\nVotre sort crée une explosion lumineuse qui éblouit les gobelins !")
                        print("Ils fuient dans la forêt en criant de peur.")
                        po_gagne = 5
                        po_player += po_gagne
                        print(
                            f"En fouillant les environs, vous trouvez \033[0;33m{po_gagne}\033[0m pièces d'or ! [\033[0;33m+{po_gagne} PO\033[0m]")
                        break
                    elif val_test + stats["arcane"] >= 6 :
                        print("\nVotre sort crée une explosion lumineuse qui éblouit les gobelins !")
                        print("Ils fuient dans la forêt en criant de peur.")
                    else :
                        print("\nVotre sort échoue et les gobelins se jettent sur vous !")
                        pv_player -= 2
                        print(
                            f"Vous recevez plusieurs coups ! [ -2 \033[0;31mPV\033[0m][{pv_player} \033[0;31mPV\033[0m]")
                        if pv_player <= 0:
                            print("\033[1;31mVous êtes mort.\033[0m")
                            exit()
                        break

                elif choix == 2:
                    print(" ")
                    print("━" * largeur_console)
                    print("- Test de \033[0;36mForce\033[0m -")
                    print("━" * largeur_console)
                    time.sleep(to_sleep2)
                    print(" ")
                    print("Vous :", stats["force"], "stat de \033[0;36mForce\033[0m")
                    print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                    print("Adversaire : 6 stat de\033[0;36mForce\033[0m")
                    while True:
                        val_test = int(
                            input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                        if val_test > stats["endurance"]:
                            print(
                                "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                                "0;32mEndurance\033[0m !")
                            continue
                        else:
                            print("Vous avez désormais ", stats["force"] + val_test, "stat de\033[0;36mForce\033[0m")
                            break
                    if val_test + stats["force"] >= 8:
                        print(
                            "\nVous terrassez les gobelins avec votre épée. Leur chef tente de fuir, mais vous le stoppez !")
                        po_gagne = 5
                        po_player += po_gagne
                        print(
                            f"En fouillant leurs affaires, vous trouvez {po_gagne} pièces d'or ! [\033[0;33m+{po_gagne} PO\033[0m]")
                        break
                    elif val_test + stats["force"] >= 6:
                        print("\nVous terrassez les gobelins avec votre épée. Leur chef tente de fuir, mais vous le stoppez !")
                    else:
                        print("\nLes gobelins sont plus rapides que prévu et vous blessent lors du combat.")
                        degats = 4
                        pv_player -= degats
                        print(
                            f"Vous perdez des points de vie ! [ -{degats} \033[0;31mPV\033[0m][{pv_player} \033[0;31mPV\033[0m]")
                        if pv_player <= 0:
                            print("\033[1;31mVous êtes mort.\033[0m")
                            exit()
                        break

                else:
                    print("\nVeuillez choisir une option valide [1 ou 2].")

            except ValueError:
                print("\nEntrée invalide. Veuillez entrer un chiffre (1 ou 2).")
    rencontre_gobelins()


def fin():
    global choix_base1, val_test, po_player, pv_player, stats
    keyboard.wait("shift")
    print(" ")
    print("Vous arrivez à l'entrée de ruines. Une énergie étrange et écrasante s'en dégage :\nle Mana est presque palpable.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;3;33mC'est ici Elias.\ntu es à la dernière étape... ton ultime combat.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Vous inspirez profondément. Jamais vous ne vous êtes senti aussi prêt.")
    keyboard.wait("shift")
    print(" ")
    print("Avec une détermination inébranlable, vous entrez dans les ruines.\nElles ressemblent à un ancien sanctuaire, chargé d'une histoire oubliée.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mEnfin.\nJe t'attends depuis des heures.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("La voix résonne dans l'église délabrée. À l’autre bout de la salle, un homme se tient derrière un pupitre.\nIl porte une cape semblable à celle des hommes que vous avez affrontés plus tôt.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mTu viens sauver le monde hein ?\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("L'homme attend une réponse, son regard perçant posé sur vous.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mtu es muet ? Je t'ai posé une question me semble-il.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("'Exact, comment t'as deviné ?' [1]")
    print("'...' [2]")
    choix_base1 = int(input("⮚ "))
    while True:
        try:
            if choix_base1 == 1:
                print("\n\033[1;34mExact, comment t'as deviné ?\n\033[0m")
                keyboard.wait("shift")
                print("\033[1;31mMmmh... insolent hein ? un vrai héros, c'est ça ?")
                break
            elif choix_base1 == 2:
                print("\n\033[1;34m...\n\033[0m")
                keyboard.wait("shift")
                print("\033[1;31mTu ne veux pas parler ? Un vrai héros alors ?")
                break
            break
        except ValueError:
            continue
    keyboard.wait("shift")
    print(" ")
    print("\033[1;34mJe ne suis pas un héro, jamais je ne l'ai été, et je ne le serai jamais.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mMais oui, tu n'est pas un héro, tu n'es rien, et tu le sais.\nmalgré cela, tu oses venir ici ? Espères-tu accomplir quelque chose ?")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;34m...\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mPourquoi donc est-tu venu ici ? parce que tu n'avais pas le choix ?\nDu moins c'est ce qu'on a voulu te faire croire.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;34mNon ! je suis venu pour vous arrêter.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mOh... Alors, tu es venu de ton propre gré ? Tu es venu te suicider par pur héroïsme ?\nJe n’y crois pas. Je sais qui t’a forcé.\nEn vérité, tu pouvais faire demi-tour. Elle t’a menti.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;34mNon, je...\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mSélène ne t'as pas dit la vérité. Tu sais que j'ai raison.\nMais qu'importe. Maintenant que tu es là, finissons-en.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Cinq hommes surgissent devant vous, armés et déterminés à en finir.")
    keyboard.wait("shift")
    print(" ")
    print("Vous n'avez plus qu'une option.")
    keyboard.wait("shift")
    print("Combattre. Jusqu'au bout.")
    keyboard.wait("shift")
    print(" ")
    print("Vous lancez votre sort de Flamme Sacrée.")
    keyboard.wait("shift")
    print("[N'appuyez sur aucune touche pendant le lancement d'un sort !]")
    print(" ")
    for i in tqdm.tqdm(range(45)):
        # pause de 0.1 sec.
        time.sleep(0.1)
    print(" ")
    val_test = random.randint(1, 10)
    if val_test > stats["arcane"]:
        print("Vous ratez votre sort.\n[ -1 \033[1;31mPV\033[0m], [",pv_player,"\033[1;31mPV\033[0m]")
        keyboard.wait("shift")
        print(" ")
        print("Vous réussissez tout de même à repousser les hommes dans un ultime effort.")
    elif val_test <= stats["arcane"]:
        print("Votre sort les touche et brûle trois d'entre eux.\n"), keyboard.wait("shift")
    print("Sélène vous aurait-elle menti ?\nVous êtes désormais seul.\n"), keyboard.wait("shift")
    print("\033[1;31mPas mal, il semblerait que je vais devoir faire appel aux Dieux Anciens.\033[0m\n"), keyboard.wait("shift")
    print("\033[1;34mQuels Dieux ?"), keyboard.wait("shift")
    print("J'ai vu le trône des Dieux, et il est vide. Vous êtes tout aussi seul que moi.\n\033[0m"), keyboard.wait("shift")
    print("\033[1;31mDécidément, tu ne sais donc rien.\nNotre Magie ne repose pas sur l'invocation de Dieux, mais sur leur connaissances.\nVivants ou non, les Dieux sont avec nous.\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Alors que l'homme se met à prononcer des paroles incompréhensibles. Le ciel s'assombrit au-dessus des ruines.\nLes cinq hommes qui vous entouraient s'enfuient, pris de panique")
    keyboard.wait("shift")
    print("")
    print("L’énergie devient insupportable. Vous devez agir. Vous vous élancez vers lui.")
    keyboard.wait("shift")
    print(" ")
    print("Soudain, un cri glacial perce l’air depuis l’extérieur. Vous vous arrêtez, votre cœur battant à tout\nrompre.")
    keyboard.wait("shift")
    print(" ")
    print("Vous levez les yeux et, à travers les fissures du plafond, apercevez une silhouette gigantesque flotter dans les airs.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mUn Dieu... L'apparition d'un Dieu ! Le début de la fin !\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Vous ne pouvez pas gagner contre cette... chose.")
    keyboard.wait("shift")
    print(" ")
    print("Vous pensiez avoir une fin plus glorieuse que celle d'être englouti par un Dieu.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;3;33mElias, je le retient.\nTue le !\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Des lueurs dorées s’embrasent dans les airs, affrontant la créature divine. Sélène ne vous a donc pas abandonné.")
    keyboard.wait("shift")
    print(" ")
    print("L’homme derrière le pupitre, enragé, hurle :")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;31mJe vais m'occuper de toi moi-même !\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Son corps commence à fondre. Ce n’est plus qu’une flaque rougeâtre qui, soudain, s’élève dans les\nairs et prend forme.")
    keyboard.wait("shift")
    print(" ")
    print("Une créature ailée aux yeux rouges et à la chair carbonisée se dresse devant vous.")
    keyboard.wait("shift")
    print(" ")
    print("Elle s’élève avant de frapper violemment le sol, vous projetant face contre terre.")
    keyboard.wait("shift")
    print(" ")
    print("Le Démon vous agrippe par le cou.")
    keyboard.wait("shift")
    print(" ")
    while True:
        print("[\033[0;36mArcane\033[0m :", stats["arcane"],
                "] Lancer votre sort le plus puissant [1]")
        print("[\033[0;36mForce\033[0m :", stats["force"],
                "] Dégainer votre épée, et vous battre [2]")
        choix_base1 = int(input("⮚ "))
        try:

            if choix_base1 == 1:
                print(" ")
                print("━" * largeur_console, )
                print("Test d'\033[0;36mArcane\033[0m")
                print("━" * largeur_console, ), time.sleep(to_sleep2)
                print(" ")

                print("Vous :", stats["arcane"], "stat d'\033[0;36mArcane\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 8 stat d'\033[0;36mArcane\033[0m")
                elo_adverse = 8

                while True:
                    val_test = int(
                        input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !")
                        continue
                    else:
                        print("Vous avez désormais", stats["arcane"] + val_test, "stat d'\033[0;36mArcane\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["arcane"] + val_test >= 8:
                    print("Vous lancez un sort d'Explosion Majeure.\nVous vous faites projeter vous et votre adversaire contre un mur de l'église, et y laissez un bras.")
                    break
                elif stats["arcane"] + val_test < elo_adverse:
                    pv_player -= 4
                    print("Votre sort ne fait pas assez de dégats pour vaincre la créature, elle vous arrache un bras d'un coup sec."
                        "\n[ -3 \033[0;31mPV\033[0m][",
                        pv_player, "\033[0;31mPV\033[0m]")
                    if pv_player <= 0:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                break

            elif choix_base1 == 2:

                print("━" * largeur_console)
                print("- Test de \033[0;36mForce\033[0m -")
                print("━" * largeur_console), time.sleep(to_sleep2)

                print("Vous :", stats["force"], "stat de \033[0;36mForce\033[0m")
                print("Vous :", stats["endurance"], "pts d'\033[0;32mEndurance\033[0m")

                print("Adversaire : 8 stat de \033[0;36mForce\033[0m")
                while True:
                    val_test = int(
                        input("Combien de pts d'\033[0;32mEndurance\033[0m voulez-vous dépenser ? \n ⮚ "))
                    if val_test > stats["endurance"]:
                        print(
                            "Votre dépense d'\033[0;32mEndurance\033[0m ne peut excéder votre stat d'\033["
                            "0;32mEndurance\033[0m !")
                        continue
                    else:
                        print("Vous avez désormais", stats["force"] + val_test, "stat de \033[0;36mForce\033[0m")
                        break
                time.sleep(to_sleep)
                print(" ")
                if stats["force"] + val_test >= 8:
                    print("Vous plantez votre épée dans le buste du Démon, malgré cela, il vous tranche le bras avant de vous lacher.")
                    break
                elif stats["force"] + val_test < 8:
                    pv_player -= 4
                    print("Vous tranchez une main au Démon, avant qu'il ne vous arrache le bras et vous projette au sol."
                          "\n[ -3 \033[0;31mPV\033[0m][",pv_player,"\033[0;31mPV\033[0m]")
                    if pv_player <= 0:
                        print("\033[1;31mVous êtes Mort\033[0m")
                        exit()
                    break
                break
        except ValueError:
            continue
    keyboard.wait("shift")
    print(" ")
    print("Malgré la douleur atroce, vous vous relevez.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;34mSélène !\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;3;33mVite... Je... Je ne peux plus tenir... Il va s'écraser au sol !\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Vous voyez la silhouette divine descendre rapidement. Vous devez agir.")
    keyboard.wait("shift")
    print(" ")
    print("Le Démon, gravement blessé, avance lentement vers vous.")
    keyboard.wait("shift")
    print(" ")
    print("Dans un ultime effort, vous rassemblez votre énergie et lancez un dernier sort.")
    print(" ")
    keyboard.wait("shift")
    for i in tqdm.tqdm(range(75)):
        time.sleep(0.1)
    print(" ")
    for i in range(0, 3):
        print(".", end=""), time.sleep(to_sleep2)
    print("\n")
    print("Vous ouvrez les yeux. Le Démon gît au sol, inerte, baignant dans une mare de sang.")
    keyboard.wait("shift")
    print(" ")
    for i in range(0, 3):
        print(".", end=""), time.sleep(to_sleep2)
    print(" ")
    print("\n\033[1;3;33mElias, au dessus !\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Vous levez la tête. Le Dieu, en chute libre, se rapproche dangereusement.")
    keyboard.wait("shift")
    print(" ")
    print("\033[1;34mComme quoi... La bonne personne au mauvais endroit peut faire toute la différence...\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("Vos dernières pensées s’imposent :")
    keyboard.wait("shift")
    print(" ")
    print("Votre victoire..."), keyboard.wait("shift")
    print("Et la douleur."), keyboard.wait("shift")
    print(" ")
    print("\033[1;34mCette douleur...", end = " ")
    keyboard.wait("shift")
    print("Mes doigts picotent...", end = " ")
    keyboard.wait("shift")
    print("Ma bouche est sèche...", end = " ")
    keyboard.wait("shift")
    print("Mes yeux brûlent...\033[0m")
    keyboard.wait("shift")
    print(" ")
    print("malgré ces paroles, un timide sourire ne peut quitter votre visage.")
    print(" ")
    for i in range(0, 2):
        print(".", end=""), time.sleep(to_sleep2)
    time.sleep(3)




#S'il y a les deux prénoms (ex : Codé par Arthur / Timothé) le premier est celui à la base du programme (ici Arthur)

intro()    # Codé par Timothé
competence()    #Codé par Timothé
choix1()    #Codé par Timothé
intro_invoc()    #Codé par Timothé / Arthur
test_invoc()    #Codé par Arthur
suite_invoc1()    #Codé par Arthur
test_tavernier()    #Codé par Timothé / Arthur
yharnam() #Codé par Timothé / Arthur
esprit_farceur()   #Codé par Arthur
suite_esprit()   #Codé par Timothé
bandits()   #Codé par Arthur
suite_bandits()   #Codé par Timothé
foret()   #Codé par Arthur
gobelins() #Codé par Arthur
fin()  #Codé par Arthur


# --- Crédits ---
#Programmeurs : Arthur, Timothé
#Auteur : Arthur
#Bugs Fixer : Timothé
#Bêta-Testeurs : Léo Marseille, Neal Dautremont