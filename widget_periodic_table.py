#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:07:40 2020

@author: pablo
"""


from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.periodic_table import elements
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Select
from bokeh.layouts import layout
from bokeh.models.annotations import Span
 
#Remove rows with NaN values and then map standard states to colors
elements.dropna(inplace=True) #if inplace is not set to True the changes are not written to the dataframe
colormap = {'gas':'yellow', 'liquid':'orange', 'solid':'red'}
elements['color'] = [colormap[x] for x in elements['standard state']]
elements['size'] = elements['van der Waals radius'] / 10
 
#Create three ColumnDataSources for elements of unique standard states
gas = ColumnDataSource(elements[elements['standard state']=='gas'])
liquid = ColumnDataSource(elements[elements['standard state']=='liquid'])
solid = ColumnDataSource(elements[elements['standard state']=='solid'])
 
#Define the output file path
output_file("elements_annotations.html")
 
#Create the figure object
f=figure()
 
#adding glyphs
f.circle(x="atomic radius", y="boiling point", size='size',
         fill_alpha=0.2, color="color", legend='Gas', source=gas)
 
f.circle(x="atomic radius", y="boiling point", size='size',
         fill_alpha=0.2, color="color", legend='Liquid', source=liquid)
 
f.circle(x="atomic radius", y="boiling point", size='size',
         fill_alpha=0.2,color="color",legend='Solid',source=solid)
 
#Add axis labels 
f.xaxis.axis_label = "Atomic radius"
f.yaxis.axis_label = "Boiling point"
 
#Calculate the average boiling point for all three groups by dividing the sum by the number of values
gas_average_boil = sum(gas.data['boiling point']) / len(gas.data['boiling point'])
liquid_average_boil = sum(liquid.data['boiling point']) / len(liquid.data['boiling point'])
solid_average_boil = sum(solid.data['boiling point']) / len(solid.data['boiling point'])

solid_max_boil = max(solid.data['boiling point'])
solid_min_boil = min(solid.data['boiling point'])
 
#Create three spans
span_gas_average_boil = Span(location=gas_average_boil, dimension='width', line_color='yellow', line_width=2)
span_liquid_average_boil = Span(location=liquid_average_boil, dimension='width', line_color='orange', line_width=2)
span_solid_average_boil = Span(location=solid_average_boil, dimension='width', line_color='red', line_width=2)
 
#Add spans to the figure
f.add_layout(span_gas_average_boil)
f.add_layout(span_liquid_average_boil)
f.add_layout(span_solid_average_boil)


#create function
def update_span_solid(attr,old,new):
    span_solid_average_boil.location=float(select.value)

#create select widget
options=[(str(min(solid.data['boiling point'])),"Minimum Solid Boiling Point"),
         (str(max(solid.data['boiling point'])),"Maximum Solid Boiling Point"),
         (str(solid_average_boil),"Average Solid Boiling Point")]
         
select=Select(title="span value",options=options) #options has to be a list
select.on_change("value",update_span_solid)

#create layout and add to curdoc
lay_out=layout([[select]])
curdoc().add_root(f)
curdoc().add_root(lay_out)


 
#Save and show the figure
show(f)