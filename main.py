import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    ft.Text()

    titulo1 = ft.Text('Cadastro Paciente')
    titulo2 = ft.Text(value = 'Cadastrode Paciente',
                      color = 'blue',
                      size = 18,
                      weight = 'bold',
                      font_family = 'Open Sans')
        
    page.add(titulo1, titulo2)

ft.app(target = main)



