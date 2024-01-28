from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class SimpleApp(App):
    def build(self):
        # Create a layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create a button
        button = Button(text="Click me!", on_press=self.on_button_press)

        # Add the button to the layout
        layout.add_widget(button)

        # Return the layout as the root widget
        return layout

    def on_button_press(self, instance):
        # Define the button press behavior
        print("Button pressed!")


if __name__ == '__main__':
    SimpleApp().run()
