import PySimpleGUI as sg
from back.Calcular import Operacao

class Tela_Calculadora:
    def __init__(self):
        # themes
        sg.theme('Dark')
        # layout
        layout = [
            [sg.Output(size=(31,2),
                       font='Calculator',
                       text_color='green2',
                       tooltip=True)],
            [sg.Input(default_text='',
                      text_color='green2',
                      font='Calculator',
                      size=(25,0),
                      do_not_clear=False,
                      key='calculo'),
             sg.Button("calc",
                       font='Calculator',
                       size=(6,2),
                       button_color="grey")],
            [sg.Text()]
        ]
        # window
        self.window = sg.Window("Calculadora").layout(layout)
                
    def executar(self):
        while True:
            self.button, self.values = self.window.read()
            self.Calculo = str(self.values['calculo'])
            self.resultado = Operacao(self.Calculo)
            print (self.resultado)
