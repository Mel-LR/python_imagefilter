import cv2
import os
import sys
import logger
from filters import grayscale, blur, dilate

input_dir = "data/imgs"

#args = sys.argv
#print(f'args={args}')

#first_arg = args[1]

#f first_arg == "--i":
   # phone = args[1]
   # print("Dossier d'entré=" + phone)
#elif first_arg == "-o":
#    print('Dossier de sortie')
#elif first_arg == "-h":
#    print('Aide de mon programme')

args = sys.argv
print(f"args={args}")
for i in range(0, len(args)):
    print(args[i])
    if args == '-h':
        print('Aide de mon programme')
        print("-i Le dossier d'image à filtrées")
        sys.exit()

    if args[i] == '-i' and len(args) >= i + 1:
        print("Dossier d'entré")
        #input_dir = args[i + 1]
        print("Argument suivant")
    i = 0

    if args[i] == '-o' and len(args) >= i + 1:
        print("Dossier de sortir")
        print("Argument suivant")
        #input_dir = args[i + 1]
    i = 0

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