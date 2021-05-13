# Source code credit Yash Sanghvi (https://medium.com/tech-carnot/interactive-map-based-visualization-using-plotly-44e8ad419b97)

from os import environ
import os
import sys

import json

import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
plotly.io.orca.config.executable = r"C:\Users\username\AppData\Local\Programs\orca\orca.exe" # application server specific
import datetime as d

def map(self):
    df = pd.read_csv('CNMI_Data.csv')
    with open('rota_saipan_tinian.json') as f: cnmi = json.load(f)
    #with open('cnmi.json') as f: cnmi = json.load(f) #northern islands unpopulated based on best information available to me at time of publication
    
    cnmi["features"][0]['properties']
    #max_value = 1.0 # Default setting is 1.0 as max value
    max_value = df["Value"].max()
    fig = px.choropleth(df, geojson=cnmi, locations='NAMELSAD', color='Value', #change 'Value' to the name of the column describing color temperature
                color_continuous_scale="Viridis",range_color=(0, max_value),
                featureidkey="properties.NAMELSAD", projection="mercator")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(autosize=True, width=1900, height=750,)
    for i in range(0, len(cnmi["features"])): 
        print(cnmi["features"][i]["properties"]["NAMELSAD"])
    fig.write_html(r'.\cnmichoropleth.html')
    fig.update_layout(autosize=True, width=3500, height=2500,)
    pio.write_image(fig, 'cnmichoropleth.pdf', width=3500, height=2500)

if __name__ == '__main__':
    map()
