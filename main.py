from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class SimpleKivyApp(App):
    def build(self):
        # Creating a BoxLayout as the root widget
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Creating a label
        self.label = Label(text="Hello, Kivy!")

        # Creating a button
        button = Button(text="Click me!", on_press=self.on_button_click)

        # Adding widgets to the layout
        layout.add_widget(self.label)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Change the label text when the button is clicked
        self.label.text = "Button clicked!"


if __name__ == '__main__':
    SimpleKivyApp().run()
