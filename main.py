import yt_dlp
from os import startfile
from pywebio.input import input
from pywebio.output import put_text

def videoDownload():
    while True:
        videoLink = input("Informe o link do vídeo: ")

        if videoLink.startswith("https://"):
            put_text("Fazendo download do vídeo...").style('color: red; font-size: 50px')

            try:
                ydl_opts = {
                    'format': 'best',  # Melhor qualidade disponível
                    'outtmpl': r'C:\Users\Miamotinho\Downloads\%(title)s.%(ext)s',  # Salvar no diretório Downloads
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([videoLink])

                put_text("Vídeo baixado com sucesso!").style('color: blue; font-size: 50px')

                # Abrindo o vídeo baixado
                startfile(r"C:\Users\Miamotinho\Downloads")

            except Exception as e:
                put_text(f"Ocorreu um erro: {e}").style('color: red; font-size: 20px')
        else:
            put_text("Link inválido! Certifique-se de que começa com 'https://'.").style('color: red; font-size: 20px')

if __name__ == "__main__":
    videoDownload()
