import flet as ft
import yt_dlp

def main(page: ft.Page):

    page.window.icon = "icon.ico"
    page.window.width = 600
    page.window.height = 700
    page.window.center()

    page.title = "Youtube videos doawnloader"

    page.bgcolor = ft.colors.BLACK
    page.window.bgcolor = ft.colors.BLACK

    text_field = ft.TextField(label="Enter url of the video")

    message = ft.Text("Wait ..." , visible=False, size=24)


    def download_video(url):
        try:
            message.visible = True
            
            page.update()
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'C:/Users/medme/Downloads/Vidoes' + '/%(title)s.%(ext)s',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            message.value = "Downloaded Completed !"
            page.update()

        except Exception :
            page.add(ft.Text("Please enter a valid video URL"))


    page.add(
    


        ft.Row(
            [
                text_field,
                ft.ElevatedButton(text="Download" , bgcolor=ft.colors.RED_500 , on_click=lambda e:download_video(text_field.value)),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=300
            ),

        ft.Row(
            [
                message,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            height=100
        ),

        


    )

    page.update()


    

ft.app(target=main)