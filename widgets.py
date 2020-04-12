#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:05:41 2020

@author: pablo
"""

# instructions
# to execute this script you need to use an external terminal with the commands:
# << bokeh server widgets.py


#import libraries
from bokeh.io import output_file, show, curdoc
from bokeh.models.widgets import TextInput, Button, Paragraph
from bokeh.layouts import layout


#create widgets
text_input=TextInput(value='Pablo')
button=Button(label='Generate Text')
output=Paragraph()

def update():
    output.text='Hello,'+text_input.value
    
button.on_click(update)

lay_out=layout(([[button,text_input],[output]]))

curdoc().add_root(lay_out)