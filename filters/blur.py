import cv2


def filter_blur(image):
    """
    Fonction permettant d'appliquer un filtre flou à l'image.
    Try except permet de gérer les erreurs et de ne pas arrêter le programme.
    :param image: Appliquer le filtre flou sur l'image.
    :return: Renvoie l'image filtrée et l'enregistre dans le dossier data/output.
    """
    try:
        gaussian_blur = cv2.GaussianBlur(image, (77, 13), 0)

        return gaussian_blur
    except cv2.error as e:
        print("Le fichier n'est pas une image")