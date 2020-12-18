from datetime import datetime


# Variable permettant de récupérer et stocker les messages dans imagefilter.log
log_file = "imagefilter.log"

def log(msg):
    """
    Fonction permettant de répertorier les actions du code
    dans un fichier imagefilter.log.
    :param msg: Message apparaissant dnas le fichier .log avec la date et heure.
    """
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')
