from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import webview

class BoxLayoutApp(App):
    def build(self):
        # Create a BoxLayout with vertical orientation
        box_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a button to open the webview window
        webview_button = Button(text='Open Webview')
        webview_button.bind(on_press=self.open_webview)

        # Add the button to the BoxLayout
        box_layout.add_widget(webview_button)

        return box_layout

    def open_webview(self, instance):
        # Code to create and start the webview window
        webview.create_window('Hello world', 'https://pywebview.flowrl.com/')
        webview.start()

if __name__ == '__main__':
    BoxLayoutApp().run()
