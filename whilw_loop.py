from winotify import Notification
nome= input("seu nome para cadastro: ")
toast = Notification(app_id="windows app",
                     title="Felipe Cortez Sousa",
                     msg=f"bem vindo ao sistema{nome}",
                     icon=r"C:\Users\felip\OneDrive\Imagens\IMG-20230620-WA0008.ico")
toast.show()