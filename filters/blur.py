import cv2
import logger

def filter_blur(image):
    """
    Fonction permettant d'appliquer un filtre flou à l'image
    :param image: Appliquer le filtre N&B sur l'image
    :return: Renvoie une image filtrée
    """
    try:
        gaussian_blur = cv2.GaussianBlur(image, (77, 13), 0)

        #logger.log(f'Filter blur={gaussian_blur}')

        return gaussian_blur
    except cv2.error as e:
        print("Le fichier n'est pas une image")


















#def apply_blur():
 #   try:
 #       # 1. Ouvrir le fichier => extraire l'image
  #      image = cv2.imread("data/imgs/automne.jpg")
#
 #       # 2. Appliquer le filtre flou sur l'image
  #      gaussian_blur = cv2.GaussianBlur(image,(15,5),0)
#
 #       # 3. Enregister l'image filtrée dans le dossier
  #      cv2.imwrite("data/output/automne.jpg", gaussian_blur)
   # except cv2.error as e:
    #    print("Le fichier n'est pas un image")
