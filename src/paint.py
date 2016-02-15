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
        self.size = Window.size
        # self.painter_proprtion_h = 1
        # self.painter_proprtion_v = .7
        # self.slider_proprtion_h = 1
        # self.slider_proprtion_v = .7

        painter = MyPaintWidget()
        painter.size = Window.size

        #painter.update(0)
        self.painter = BackgroundWrapper(painter,size_hint=(1,.7))
        self.painter.widget.update(0)

        # self.painter = MyPaintWidget(size_hint=(1,.7))
        # self.painter.update(0)
        # self.slider = MySliderWidget(min=0,max=10,value=0,size_hint=(1,.3))
        # self.slider.bind(value=self.update_canvas)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.size = self.size
        # self.layout.size = self.size
        self.layout.add_widget(self.painter)

        self.layout.add_widget(Button(text="kk",size_hint=(1,.3)))
        #print self.painter.width
        #print self.painter.height
        # self.layout.add_widget(self.slider)
        #
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

class BackgroundWrapper(Widget):
    def __init__(self,widget,**kwargs):
        super(BackgroundWrapper,self).__init__(**kwargs)
        self.widget = widget
        size_x = self.size_hint[0]
        size_y = self.size_hint[1]
        window_x = Window.size[0]
        window_y = Window.size[1]

        self.background = BackgroundWidget(
            height=widget.height*size_y,
            width=widget.width*size_x,
            pos_x=window_x*(1-size_x),
            pos_y=window_y*(1-size_y))

        self.background.width = widget.width
        self.background.height = widget.height
        self.add_widget(self.background)
        self.add_widget(self.widget)


class BackgroundWidget(Widget):
    def __init__(self,pos_x,pos_y,**kwargs):
        super(BackgroundWidget,self).__init__(**kwargs)
        with self.canvas:
            Color(1, .5, .2, 1)  # set the colour to orange
            self.rect = Rectangle(
                size=(self.width,self.height),
                pos=(pos_x,pos_y))

class MyPaintApp(App):
    def build(self):

        root = RootWidget()
        return root

if __name__ == '__main__':
    MyPaintApp().run()
