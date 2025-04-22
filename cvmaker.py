from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.clock import Clock
from  docx import Document
from docx import *

class Main(Screen):
    def generate(self):
        self.ids.cv.color = "#8D9A92FF"
        self.ids.cv.text = "generating..."
        
        Clock.schedule_once(self.generator, 2)    
    def expreience():
        ...
    def achievements():
        ...
    def references():
        ...
    def skills():
        ...          
    def information():
        ...

        
    def generator(self,*args):
        self.ids.cv.text = "generated :)"
        self.ids.cv.color = "#6AE394FF"
        
class CvMaker (MDApp):
    def build(self):
        Window.size = (600, 620)
        Window.clearcolor = "#22438646"
        #Window.borderless = True
        self.theme_cls.primary_palette = "White"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("C:\\Users\\AUTHENTIC PLUS STORE\\Desktop\\goals for the holidays\\sleepy panda\\cv maker\\cv.kv")
CvMaker().run()    