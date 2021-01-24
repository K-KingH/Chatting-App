from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.recyclelayout import RecycleLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class Grid(BoxLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.c = BoxLayout(orientation ='vertical') 
        
        self.value = TextInput(multiline=True, font_size=25)
        self.add_widget(self.value)
        
        self.submit = Button(text="send", font_size=30)
        self.submit.bind(on_press=self.upload)
        self.add_widget(self.submit)
              
        
    def upload(self, instance):
        print(self.value.text)
        self.value.text = ""
        
class SampleApp(App):     
    def build(self):        
        return Grid()
    

SampleApp().run() 