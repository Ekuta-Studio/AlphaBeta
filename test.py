from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

class MyApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical', padding=10)

        # 创建一个Label
        label = MDLabel(text='Hello, KivyMD!', halign='center')
        layout.add_widget(label)

        # 创建一个Entry
        entry = MDTextField(hint_text='Enter some text')
        layout.add_widget(entry)

        # 创建一个Button
        button = MDRaisedButton(text='Click Me', on_release=self.on_button_release)
        layout.add_widget(button)

        return layout

    def on_button_release(self, instance):
        # 当按钮被点击时，获取Entry的文本并打印
        text = instance.parent.children[1].text
        print('You entered:', text)

if __name__ == '__main__':
    MyApp().run()