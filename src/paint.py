from random import random
import math

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window

from clickLogger import ClickLogger
from clickPlayer import ClickPlayer


class RootWidget(Widget):
    def __init__(self,**kwargs):
        super(RootWidget,self).__init__(**kwargs)
        self.painter = MyPaintWidget(size_hint=(.5, 1))
        self.painter.update(0)
        self.slider = Slider(min=0,max=10,value=0,size_hint=(.5, 1))
        self.slider.bind(value=self.update_canvas)
        self.add_widget(self.painter)
        self.add_widget(self.slider)

    def get_layout(self):
        self.layout = BoxLayout(padding=10,orientation='vertical')
        self.layout.add_widget(self.painter)
        self.layout.add_widget(self.slider)
        return self.layout

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
    def update_canvas(self,obj,value):
        self.painter.update(value)


class MyPaintWidget(Widget):
    def update(self,sliderTime):
        with self.canvas:
            eventQueue = self.mockEventList()
            for event in eventQueue:
                time = event[0]
                x = event[1]
                y = event[2]
                print "time, sliderTime: "+str(time)+", "+str(sliderTime)
                if(time == math.floor(sliderTime)):
                    Color(1,0,0)
                    d=30
                    Ellipse(pos=((x*50+100) -d /2, (y*50+100) - d / 2), size=(d, d))
                elif(time < sliderTime):
                    Color(0,1,0)
                    d=30
                    Ellipse(pos=((x*50+100) -d /2, (y*50+100) - d / 2), size=(d, d))
                else:
                    Color(0,0,1)
                    d=30
                    Ellipse(pos=((x*50+100) -d /2, (y*50+100) - d / 2), size=(d, d))

    def mockEventList(self):
        eventQueue = []
        for num in range(1,10):
            eventQueue.append([num,num,num])
        return eventQueue

class MyPaintApp(App):
    def build(self):
        root = RootWidget()
        return root

if __name__ == '__main__':
    MyPaintApp().run()
