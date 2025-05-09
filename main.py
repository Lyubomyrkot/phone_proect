from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


from instructions import *
from ruffier import *

class InsructionScreen(Screen):
   def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text = txt_instruction)

        lbl1 = Label(text = "Ввеліть iм'я")
        lbl2 = Label(text = "Ввеліть вiк")
        name_input = TextInput(multiline=False)
        age_input = TextInput(multiline=False)
        start_button = Button(text="Почати")

        v_line = BoxLayout(orientation='vertical')
        v_line.add_widget(instr)
        v_line.add_widget(lbl1)
        v_line.add_widget(name_input)
        v_line.add_widget(lbl2)
        v_line.add_widget(age_input)
        v_line.add_widget(start_button)

        self.add_widget(v_line)

class ResultScreen(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)

class HeartChech(App):
   def build(self):
      sm = ScreenManager()
      sm.add_widget(InsructionScreen(name='instruction'))
      sm.add_widget(ResultScreen(name='result'))
      
      return sm

app = HeartChech()
app.run()