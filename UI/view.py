import flet as ft

class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None
        self._errore_dialog = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(ft.Row([self._title], alignment=ft.MainAxisAlignment.CENTER))
        self._ddCorso = ft.Dropdown(label="Corso", hint_text="Selezionare un corso",
            expand=True)
        for i in self._controller._model._corso.getAllCorsi():
            print(i)
            corso_text = f"{i['nome']} ({i['codins']})"
            self._ddCorso.options.append(ft.dropdown.Option(text=corso_text, key=i['codins']))
        self._btnIscritti = ft.ElevatedButton("Cerca Iscritti",
                                         on_click=self._controller.handleIscritti)
        self._page.controls.append(ft.Row([self._ddCorso, self._btnIscritti], alignment=ft.MainAxisAlignment.CENTER))
        self.txt_matricola = ft.TextField(
            label="matricola",
            width=200,
            hint_text="Insertisci la tua matricola"
        )
        #TODO
        self.txt_nome = ft.TextField(
            label="nome",
            width=200,
            read_only=True,
            value=None
        )
        self.txt_cognome = ft.TextField(
            label="cognome",
            width=200,
            read_only=True,
            value=None
        )
        self._page.controls.append(ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome], alignment=ft.MainAxisAlignment.CENTER))
        self._btnStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handleStudente)
        self._btnCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handleCorsi)
        self._btnIscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handleIscrizione)
        self._page.controls.append(ft.Row([self._btnStudente, self._btnCorsi, self._btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER))
        self.txt_output = ft.ListView(expand=True, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_output)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()

    def Errore(self, messaggio):
        # Crea un AlertDialog per l'errore
        self._errore_dialog = ft.AlertDialog(title=ft.Text("Errore", color=ft.colors.RED),content=ft.Text(messaggio, color=ft.colors.RED), actions=[
            ft.TextButton("OK", on_click=self.chiudiDialogo)
        ],
        open=True)
        self._page.add(self._errore_dialog)
       # self._page.update()

    def Successo(self, messaggio):
        # Crea un AlertDialog per l'errore
        self._errore_dialog = ft.AlertDialog(title=ft.Text("Iscrizione avvenuta con successo", color=ft.colors.GREEN),content=ft.Text(messaggio, color=ft.colors.BLACK), actions=[
            ft.TextButton("OK", on_click=self.chiudiDialogo)
        ],
        open=True)
        self._page.add(self._errore_dialog)
       # self._page.update()

    def chiudiDialogo(self, e):
        self._errore_dialog.open = False
        self._page.update()



