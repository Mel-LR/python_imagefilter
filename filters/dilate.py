import cv2
import numpy as np


def filter_dilate(image):
    """
    Fonction permettant d'appliquer un filtre de dilatation à l'image.
    Try except permet de gérer les erreurs et de ne pas arrêter le programme.
    :param image: Appliquer le filtre de dilatation sur l'image.
    :return: Renvoie l'image filtrée et la stock dans le dossier data/output.
    """
    try:
        kernel = np.ones((7, 7), 'uint8')

        dilate_image = cv2.dilate(image, kernel, iterations=2)
        #cv2.imshow('Dilated Image', dilate_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        return dilate_image
    except ValueError as e:
        print("Dimension non valide")