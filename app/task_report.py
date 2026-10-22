from app.models.task import Task


def riepilogo(tasks: list[Task]) -> str:
    """Restituisce un riepilogo testuale, senza stampare direttamente."""
    totali = len(tasks)
    completati = sum(task.completato for task in tasks)
    return f"Task totali: {totali} | Completati: {completati} | Aperti: {totali - completati}"



# correggere o uniformare il testo di intestazione del riepilogo senza cambiare il comportamento dei conteggi. Aggiungere/aggiornare test se opportuno
def riepilogo_uniforme(tasks: list[Task]) -> str:
    """Restituisce un riepilogo testuale uniforme, senza stampare direttamente."""
    totali = len(tasks)
    completati = sum(task.completato for task in tasks)
    aperti = totali - completati
    return f"Totale Task: {totali} | Completati: {completati} | Aperti: {aperti}"
