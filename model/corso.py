class Corso:
    def __init__(self, codins, crediti, nome):
        self._codins = codins
        self._crediti = crediti
        self._nome = nome

    def __str__(self):
        return f"Corso({self._codins}, {self._crediti}, {self._nome})"