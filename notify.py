from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast(
    "notificação",
    "Oi vagaba!",
    threaded=True,
    icon_path=None,
    duration=3
)