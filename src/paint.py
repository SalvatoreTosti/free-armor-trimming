from random import random
import math

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.graphics import InstructionGroup

from clickLogger import ClickLogger
from clickPlayer import ClickPlayer


class RootWidget(Widget):
    def __init__(self,**kwargs):
        super(RootWidget,self).__init__(**kwargs)
        self.size = Window.size
        with self.canvas:
            Color(0,0,0)
            Rectangle(pos = self.pos,size = self.size)

        # self.painter_proprtion_h = 1
        # self.painter_proprtion_v = .7
        # self.slider_proprtion_h = 1
        # self.slider_proprtion_v = .7

        self.painter = MyPaintWidget(size_hint=(1,.7))
        self.bind(on_size=self.painter.paint_background)
        #self.painter.size = Window.size
        self.painter.update(0)
        #self.painter.bind(size=self.painter.paint_background())

        #self.painter = BackgroundWrapper(painter,size_hint=(1,.7))
        #self.painter.widget.update(0)

        self.slider = SliderBG(min=0,max=10,value=0,size_hint=(1,.3)) #Slider(min=0,max=10,value=0,size_hint=(1,.3))
        #self.slider.size = Window.size

        #self.slider = BackgroundWrapper(slider,size_hint=(1,.15))

        # self.painter = MyPaintWidget(size_hint=(1,.7))
        # self.painter.update(0)
        # self.slider = MySliderWidget(min=0,max=10,value=0,size_hint=(1,.3))
        self.slider.bind(value=self.update_canvas)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.size = self.size
        self.layout.add_widget(self.painter)
        self.layout.add_widget(self.slider)

        self.add_widget(self.layout)


    def get_layout(self):
        return self.layout

    def clear_canvas(self, obj):
        self.painter.canvas.clear()
    def update_canvas(self,obj,value):
        self.painter.update(value)


    def get_painter(self):
        return self.painter
    def get_slider(self):
        return self.slider

class SliderBG(Slider):
    def __init__(self,**kwargs):
        super(SliderBG,self).__init__(**kwargs)
        with self.canvas.before:
            Color(.5,.5,.2)
            self.rect = Rectangle(size=self.size,pos=self.pos)
        self.bind(pos=self.update_rect,size=self.update_rect)

    def update_rect(self,instance,value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyPaintWidget(Widget):
    def __init__(self,**kwargs):
        super(MyPaintWidget,self).__init__(**kwargs)
        with self.canvas.before:
            Color(.1,.1,.1)
            self.rect = Rectangle(size=self.size,pos=self.pos)
        self.bind(pos=self.update_rect,size=self.update_rect)

    def update_rect(self,instance,value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def paint_background(self):
        with self.canvas:
            Color(0,1,0)
            Rectangle(pos = self.pos,size = self.size)

    def update(self,sliderTime):
        with self.canvas:
            print self.size
            print self.pos

            eventQueue = self.mockEventList()
            for event in eventQueue:
                time = event[0]
                x = event[1]
                y = event[2]
                #print "time, sliderTime: "+str(time)+", "+str(sliderTime)
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
