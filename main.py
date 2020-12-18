import cv2
import os
import sys
import logger
from filters import grayscale, blur, dilate


# Variable permettant de récupérer et stocker les images originales.
input_dir = "data/imgs"


# Permets de récupérer et d'afficher les arguments grâce à la CLI.
args = sys.argv
print(f"args={args}")
for i in range(0, len(args)):
    print(args[i])
    if args[i] == '-h':
        print('Aide de mon programme :')
        print("-i : Le dossier d'images originales à filtrer")
        print("-o : Le dossier d'images filtrées et enregistrées.")
        sys.exit()

    if args[i] == '-i' and len(args) >= i + 1:
        print("Dossier d'images originales à filtrer :")
        print("Ce dossier contient les images originales qui doivent être filtrées.")
        print("Plusieurs filtres sont disponibles :")
        print("- Grayscale permet d'appliquer un flitre noir et blanc,")
        print("- Blur permet d'appliquer un filtre flou,")
        print("- Dilate permet de dilater l'image.")
        print("Une fois le filtre appliqué, l'image filtré est automatiquement enregistrer dans le dossier data/output.")
        i = 0

    if args[i] == '-o' and len(args) >= i + 1:
        print("Dossier d'images filtrées et enregistrées :")
        print("Ce dossier contient les images filtrées et enregistrées.")
        print("Une fois le filtre appliqué, l'image filtré est automatiquement enregistrer dans ce dossier (data/output).")
        i = 0


# Parcours la liste et ajoute chaque filtres à chaques images.
files = os.listdir(input_dir)
print(files)
for f in files:
    file_path = f"{input_dir}/{f}"

    # 1. Ouvrir le fichier => extraire l'image
    # image => image originale
    image = cv2.imread(file_path)
    logger.log(f'Ouverture du fichier {file_path}')

    # 2. Appliquer le filtre sur l'image
    # image => maintenant l'image est filtrée
    image = grayscale.filter_grayscale(image)
    image = blur.filter_blur(image)
    image = dilate.filter_dilate(image)
    logger.log(f'Application du filtre {file_path}')

    # 3. Enregister l'image filtrée dans le dossier
    cv2.imwrite(f"data/output/{f}",image)
    logger.log(f"Enregistrement de l'image {file_path}")