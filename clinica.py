import flet as ft

def main(page: ft.Page):

    page.add(ft.Text('Sistema de Cadastro de Pacientes', color = '#F1F1F1', size = 40))
    page.add(ft.Text('Feito com Flet 0.32.0', color = '#FFFFFF', size = 20))
    
    page.title = 'Sistema Clinica'
    page.window_width = 500
    page.window_heigth = 500

    page.bgcolor = "#77DF9C"

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    #configurando posicionamento 
    #da tela inicial a frente das demais telas
    page.window_always_on_top = True
    page.window_title_bar_windows = False

    #abrir em modo tela cheia
    page.window_frameless = True
    page.window_full_screen = True

    page.update()

ft.app(target=main)
