import cv2
import logger

def filter_grayscale(image):
    """
    Fonction permettant d'appliquer un filtre N&B à l'image
    :param image: Appliquer le filtre N&B sur l'image
    :return: Renvoie une image filtrée
    """
    try:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #logger.log(f'Filter grayscale={image_gray}')
        return image_gray
    except cv2.error as e:
        print('Fichier inexsistant')

















#def apply_grayscale():
#    try:
#        # 1. Ouvrir le fichier => extraire l'image
#        image = cv2.imread("data/imgs/automne.jpg")
#
#        # 2. Appliquer le filtre N&B sur l'image
 #       image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#
 #       # 3. Enregister l'image filtrée dans le dossier
  #      cv2.imwrite("data/output/automne.jpg", image_gray)
   # except cv2.error as e:
    #   print('Fichier inexistant')