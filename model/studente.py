class Studente:
    def __init__(self, matricola, cds):
        self._matricola = matricola
        self._cds = cds

    def __str__(self):
        return f"Studente({self._matricola}, {self._cds})"
