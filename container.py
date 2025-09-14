import flet as ft

def main(page: ft.Page):
    page.title = 'Container'
    page.bgcolor = 'white'

    bloco1 = ft.Container(
        content= ft.Text('Ficha Cadastral',
                         color = 'black',
                         size = 10,
                         weight = 'bold'),
        bgcolor= "#502DEA",
        border_radius= ft.border_radius.all(25),
        padding= 5)
    
    bloco2 = ft.Container(
        content= ft.TextField(label= 'Digite o Nome: ',
                              color= '#000000',
                              value= 'Nome Completo'),
        bgcolor= '#FFBF00',
        border_radius= ft.border_radius.only(bottom_left= 5,
                                             bottom_right= 25),
        padding= 5)
    
    page.add(bloco1, bloco2)

ft.app(target= main)

    