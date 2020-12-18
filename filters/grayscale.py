import cv2


def filter_grayscale(image):
    """
    Fonction permettant d'appliquer un filtre N&B à l'image.
    Try except permet de gérer les erreurs et de ne pas arrêter le programme.
    :param image: Appliquer le filtre N&B sur l'image.
    :return: Renvoie l'image filtrée et la stock dans le dossier data/output.
    """
    try:
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        return image_gray
    except cv2.error as e:
        print('Fichier inexsistant')