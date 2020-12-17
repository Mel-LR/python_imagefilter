import cv2
import numpy as np
import logger

def filter_dilate(image):
    try:
        kernel = np.ones((7, 7), 'uint8')

        dilate_image = cv2.dilate(image, kernel, iterations=2)
        #cv2.imshow('Dilated Image', dilate_image)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        #logger.log(f'Filter blur={dilate_image}')

        return dilate_image
    except ValueError as e:
        print("Dimension non valide")


















#def apply_dilate():
 #   try:
 #       # 1. Ouvrir le fichier => extraire l'image
 #       image = cv2.imread("data/imgs/automne.jpg")
  #      cv2.imshow('Original', image)
#
 #       # 2. Appliquer le filtre de dilatation sur l'image
#
 #       kernel = np.ones((7,7), 'uint8')
#
 #       dilate_image = cv2.dilate(image, kernel, iterations=2)
 #       cv2.imshow('Dilated Image', dilate_image)
#        cv2.waitKey(0)
 #       cv2.destroyAllWindows()
#
 #       # 3. Enregister l'image filtrée dans le dossier
 #       cv2.imwrite("data/output/automne.jpg", dilate_image)
 #   except ValueError as e:
 #       print("Dimension non valide")
