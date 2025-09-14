import flet as ft
import requests
from io import BytesIO

def main(page: ft.Page):
    # Usar uma imagem online para teste
    try:
        # Imagem de exemplo da web
        image = ft.Image(
            src='../assets/imagens/perfume.jpg',  # Imagem aleatória para teste
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("Não foi possível carregar a imagem")
        )
        page.add(image)
        page.add(ft.Text("Imagem de teste carregada!"))
        
    except Exception as e:
        page.add(ft.Text(f"Erro: {str(e)}"))

ft.app(target=main)