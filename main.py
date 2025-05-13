from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.clock import Clock

from instructions import *
from ruffier import *

BG_COLOR = "#392e8f"
BTN_COLOR= "#f2f2f2"
Window.clearcolor = BG_COLOR

p1, p2, p3 = 0, 0, 0
age = 7
class MyButton(Button):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.background_color = BG_COLOR
      self.font_size = 20
      self.size_hint = (0.5, None)
      self.pos_hint = {"center_x": 0.5}
      self.height = "30sp"
      self.markup = True
   
class MyTextInput(TextInput):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.multiline=False
      self.size_hint=(0.5, None)
      self.pos_hint = {"center_x": 0.5}
      self.height="30sp"

class InsructionScreen(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)

      instr = Label(text = txt_instruction)

      lbl1 = Label(text = "Введіть [b] iм'я: [/b]", 
                  size_hint=(1, None),
                  height="30sp",
                  markup=True)
      lbl2 = Label(text = "Введіть [b] вiк: [/b]",
                  size_hint=(1, None),
                  height="30sp",
                  markup=True)
      self.name_input = MyTextInput()
      self.age_input = MyTextInput()
      start_button = MyButton(text="[b] Почати [/b]")
      start_button.on_press = self.next

      v_line = BoxLayout(orientation='vertical', 
                        size_hint=(0.9, 1), 
                        pos_hint={"center_x": 0.5},
                        spacing=10,
                        padding=10)
      v_line.add_widget(instr)
      v_line.add_widget(lbl1)
      v_line.add_widget(self.name_input)
      v_line.add_widget(lbl2)
      v_line.add_widget(self.age_input)
      v_line.add_widget(start_button)

      self.add_widget(v_line)

   def next(self):
      global age
      if self.name_input.text != "" and self.age_input.text.strip() != "":
         try:
            age = int(self.age_input.text.strip())
            if age >= 7:
               self.manager.transition.direction = 'left'
               self.manager.current = 'pulse'
            else:
               error = Popup(title="Вік має бути числом більше 7",
                              size_hint=(0.6, 0.2),
                              auto_dismiss=True)
               error.open()
         except:
            error = Popup(title="Вік має бути числом",
                           size_hint=(0.6, 0.2),
                           auto_dismiss=True)
            error.open()
      

class PulseScreen(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.time = 0
      self.timer_event = None
      self.timer_label = Label(text="Час: 0",
                                size_hint=(1, 0.1),
                                font_size=24)
      lbl1 = Label(text = txt_test1,
                     size_hint=(1, 0.2))
      lbl2 = Label(text = "Введіть [b] результат: [/b]",
                     size_hint=(1, None),
                     height="30sp",
                     markup=True)
      self.result_input = MyTextInput()
      self.btn = MyButton(text="[b] Почати [/b]")

      v_line = BoxLayout(orientation='vertical',
                        size_hint=(0.9, 1), 
                        pos_hint={"center_x": 0.5},
                        spacing=10,
                        padding=10)
      
      v_line.add_widget(lbl1)
      v_line.add_widget(lbl2)
      v_line.add_widget(self.timer_label)
      v_line.add_widget(self.result_input)
      v_line.add_widget(self.btn)
      self.btn.on_press = self.next
      self.add_widget(v_line)

   def on_enter(self):
      self.time = 0
      self.timer_label.text = "Час: 0"
      self.timer_event = Clock.schedule_interval(self.update_timer, 1)

   def on_leave(self):
      if self.timer_event:
         self.timer_event.cancel()

   def update_timer(self, dt):
      self.time += 1
      self.timer_label.text = f"Час: {self.time}"

   def next(self):
      anim = Animation(background_color = (2, 8, 2, 1), duration = 1)
      anim.start(self.btn)
      if self.result_input.text != "":
         try:
            global p1
            p1 = int(self.result_input.text.strip())
            self.manager.transition.direction = 'left'
            self.manager.current = 'sits'
         except:
            error = Popup(title="Результат має бути числом",
                          size_hint=(0.6, 0.2),
                          auto_dismiss=True)
            error.open()

class Sitscreen(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      lbl1 = Label(text = txt_sits,
                     size_hint=(1, 0.2))
      btn = MyButton(text="[b] Продовжити [/b]")
      btn.on_press = self.next
      v_line = BoxLayout(orientation='vertical',
                        size_hint=(0.9, 1), 
                        pos_hint={"center_x": 0.5},
                        spacing=10,
                        padding=10)
      v_line.add_widget(lbl1)
      v_line.add_widget(btn)
      self.add_widget(v_line)
   def next(self):
      self.manager.transition.direction = 'left'
      self.manager.current = 'task'

class TaskScreen(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      lbl1 = Label(text = txt_test3,
                     size_hint=(1, 0.2))
      lbl2 = Label(text = "Введіть [b] результат: [/b]",
                     size_hint=(1, None),
                     height="30sp",
                     markup=True)
      self.result_input = MyTextInput()
      lbl3 = Label(text = "Введіть [b] результат після відпочинку:[/b]",
                     size_hint=(1, None),
                     height="30sp",
                     markup=True)
      self.result_input2 = MyTextInput()
      btn = MyButton(text="[b] Почати [/b]")
      btn.on_press = self.next
      v_line = BoxLayout(orientation='vertical',
                        size_hint=(0.9, 1), 
                        pos_hint={"center_x": 0.5},
                        spacing=10,
                        padding=10)
      v_line.add_widget(lbl1)
      v_line.add_widget(lbl2)
      v_line.add_widget(self.result_input)
      v_line.add_widget(lbl3)
      v_line.add_widget(self.result_input2)
      v_line.add_widget(btn)
      self.add_widget(v_line)

   def next(self):
      if self.result_input.text != "":
         try:
            global p2
            p2 = int(self.result_input.text.strip())
            self.manager.transition.direction = 'left'
            self.manager.current = 'result'
         except:
            error = Popup(title="Результат має бути числом",
                          size_hint=(0.6, 0.2),
                          auto_dismiss=True)
            error.open()
      if self.result_input2.text != "":
         try:
            global p3
            p3 = int(self.result_input2.text.strip())
            self.manager.transition.direction = 'left'
            self.manager.current = 'result'
         except:
            error = Popup(title="Результат має бути числом",
                          size_hint=(0.6, 0.2),
                          auto_dismiss=True)
            error.open()

class ResultScreen(Screen):
   def __init__(self, **kwargs):
      super().__init__(**kwargs)
      self.result_label = Label(text = "")
      v_line = BoxLayout(orientation='vertical',
                        size_hint=(0.9, 1), 
                        pos_hint={"center_x": 0.5},
                        spacing=10,
                        padding=10)
      v_line.add_widget(self.result_label)
      self.on_press = self.before()
      self.add_widget(v_line)

   def before(self):
      result = test(p1, p2, p3, age)
      self.result_label.text = result

class HeartChech(App):
   def build(self):
      sm = ScreenManager()
      sm.add_widget(InsructionScreen(name='instruction'))
      sm.add_widget(PulseScreen(name='pulse'))
      sm.add_widget(Sitscreen(name='sits'))
      sm.add_widget(TaskScreen(name='task'))
      sm.add_widget(ResultScreen(name='result'))
      
      
      return sm

app = HeartChech()
app.run()