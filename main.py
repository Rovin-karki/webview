import webview
from android.permissions import Permission, request_permissions

request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

webview.create_window('Hello world', 'https://pywebview.flowrl.com/')
webview.start()
