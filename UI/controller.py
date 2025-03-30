import flet as ft
from UI.view import View
from model.model import Model
import datetime

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleIscritti(self, e):
        corso_selezionato = self._view._ddCorso.value
        if not corso_selezionato:
            self._view.Errore("Corso non selezionato")
            return
        studenti = self._model._corso.getStudentiByCorso(corso_selezionato)
        for i in studenti:
            self._view.txt_output.controls.append(ft.Text(f" {i['nome']} {i['cognome']} ({i['codins']})"))
        self._view.update()
        return studenti

    def handleStudente(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        matricola = self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.Errore("Matricola non inserita")
            return False
        studente = self._model._corso.getStudente(matricola)
        if studente is None:
            self._view.Errore("Studente non esistente")
            return False
        self._view.txt_nome.value = studente['nome']
        self._view.txt_cognome.value = studente['cognome']
        self._view.update()
        return True

    def handleCorsi(self, e):
        if not self.handleStudente(e):
            return
        corsi = self._model._corso.getCorsiByStudente(self._view.txt_matricola.value)
        if corsi is None:
            self._view.Errore("Studente ancora non iscritto a un corso")
            return
        for i in corsi:
            self._view.txt_output.controls.append(ft.Text(f"{i['nome']} ({i['codins']})"))
        self._view.update()

    def handleIscrizione(self, e):
        if not self._view._ddCorso.value and not (self._view.txt_matricola.value):
            self._view.Errore("Corso e Matricola non inseriti")
            return
        if not self._view._ddCorso.value:
            self._view.Errore("Corso non selezionato")
            return
        if not self.handleStudente(e):
            return
        if not self._model._corso.AddIscrizione(self._view.txt_matricola.value, self._view._ddCorso.value):
            self._view.Errore("Studente già iscritto al corso")
            return
        self._view.Successo(f"Dati iscrizione: \n {self._view.txt_nome.value} {self._view.txt_cognome.value} \n {self._view.txt_matricola.value} \n {self._view._ddCorso.value} \n {datetime.date.today()}")
        self._view.update()