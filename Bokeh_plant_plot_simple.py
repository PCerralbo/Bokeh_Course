#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:00:24 2020

@author: pablo
"""


# Bokeh plot examples

# Bokeh plot 1: plants example (Hoover tools, axes, legend, etc...)
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import gridplot
import pandas as pd
from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, ColumnDataSource,BoxZoomTool
from bokeh.models.annotations import Span, BoxAnnotation, Label, LabelSet

# preprocessing data
# create column with size that wll be used for the plot
flowers['size'] = flowers['sepal_width'] * 4
# prepare color column
colormap={'setosa':'red','versicolor':'green','virginica':'orange'}
flowers['color']=[colormap[x] for x in flowers['species']]

#create ColumnDataSource --> format used by Bokeh
setosa=ColumnDataSource(flowers[flowers['species']=='setosa'])
versicolor=ColumnDataSource(flowers[flowers['species']=='versicolor'])
virginica=ColumnDataSource(flowers[flowers['species']=='virginica'])


output_file('iris.html')

#create figure
f=figure()
f1 = figure(width=700, height=200,title='Triangles')
#adding glyphs
# all in one ...the problem here is for the legend....
#f.circle(x=flowers['petal_length'],y=flowers['petal_width'],
#         size=flowers['sepal_width']*3,fill_alpha=0.4,color=flowers['color'],line_width=0)

#if you want to have a legend for each atribute in different color..you need three lines
f.circle(x='petal_length',y='petal_width',
         size='size',
         fill_alpha=0.4,color='color',line_width=0,legend_label='Setosa',source=setosa)

f.circle(x='petal_length',y='petal_width',
         size='size',
         fill_alpha=0.4,color='color',line_width=0,legend_label='Versicolor',source=versicolor)


f.circle(x='petal_length',y='petal_width',
         size='size',
         fill_alpha=0.4,color='color',line_width=0,legend_label='Virginica',source=virginica)



f1.triangle(x='petal_length',y='petal_width',
         size='size',
         fill_alpha=0.4,color='color',line_width=0,legend_label='Virginica',source=virginica)


#Style de tools
f.tools=[PanTool(),ResetTool(),BoxZoomTool()]
hover=HoverTool(tooltips=[('Species','@species'),('Sepal Width','@sepal_width')])
f.add_tools(hover) # if you want to add tools (not standard ones)
f.toolbar_location='above'
f.toolbar.logo=None



#Stylize the plot area
f.plot_width=1100
f.plot_height=650
f.background_fill_color='gray'
#f.background_fill_color="#CD5C5C" #RGB hex values
#f.background_fill_color=(205,92,92) #RGB intensity

f.background_fill_alpha=0.3
#f.border_fill_color='gray'

# Style of the title
f.title.text='Iris Morphology'
f.title.text_color='gray'
f.title.text_font='times'
f.title.text_font_size='25px'
f.title.align='center'

# Style the axes
f.axis.minor_tick_line_color='gray' #f.xaxis.minor_tick_line_color='gray' for x axis
f.yaxis.major_label_orientation=45
f.xaxis.visible=True
#f.xaxis.minor_tick_line_color=None # no minor ticks
f.xaxis.minor_tick_in=-6 # move x minor ticks
f.xaxis.axis_label='Petal Length'
f.yaxis.axis_label='Petal Width'
f.axis.axis_label_text_color='red'

#Style th grid
f.xgrid.grid_line_color='gray'
f.xgrid.grid_line_alpha=0.5

#Axes geometry
#f.x_range=Range1d(start=0,end=10) # to define axes
#f.y_range=Range1d(start=0,end=5)
#f.xaxis.bounds=(2,8) # to restrict axis showed
f.xaxis[0].ticker.desired_num_ticks=6

#Styling legend
f.legend.location='top_left'
f.legend.background_fill_alpha=0
f.legend.border_line_color=None
f.legend.margin=60


#create a span annotation for f
span_4=Span(location=4,dimension='height',line_color='red',line_width=2)
f.add_layout(span_4)

#create a box annotation
box_2_6=BoxAnnotation(left=2,right=6,fill_color='firebrick',fill_alpha=0.2)
f.add_layout(box_2_6)

#create annotation
description=Label(x=6,y=0.25,text='This graph is for testing', render_mode='css', text_font_size='10px')
f.add_layout(description)

#create labeles for glyphs
labels=LabelSet(x='petal_length',y='petal_width',text='species', source=setosa, text_font_size='5px')
f.add_layout(labels)

#grid= gridplot([[f],[f1]])

show(f)