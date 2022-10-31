from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Dark2')
layout = [
  [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
  [sg.Text('Senha'), sg.Input(key='senha',password_char='*', size=(20,1))],
  [sg.Checkbox('Salvar o login?')],
  [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os enventos
while True:
  eventos, valores = janela.read()
  if eventos == sg.WINDOW_CLOSED:
    break
  if eventos == 'Entrar':
    if valores['usuario'] == 'jhonne' and valores['senhas'] == '123456':
      print('Bem vindo!!')
