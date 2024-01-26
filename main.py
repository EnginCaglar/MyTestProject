import time

from plyer import notification

notification_title = 'NT_HL/LL Bildirim!'
notification_message = 'Bu gün haftanın Son günü HL/LL Bildirim girişlerini unutmayalım.İyi Çalışmalar.'

notification.notify(
    title=notification_title,
    message=notification_message,
    app_icon=None,
    timeout=10,
    toast=False
)
