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

#helper per formattare una riga del report, mantenendo l'output precedente. Anna dovrà riutilizzarla in una feature dipendente.
def formatta_riga_report(task: Task) -> str:
    """Restituisce una stringa formattata per una singola riga del report."""
    stato = "Completato" if task.completato else "Aperto"
    return f"ID: {task.id} | Titolo: {task.titolo} | Stato: {stato}"