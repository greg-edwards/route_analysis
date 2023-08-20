import folium
import streamlit as st
from folium.features import Marker, Popup
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "plotly_mimetype+notebook"
import osmnx as ox
import leafmap
import folium

from streamlit_folium import st_folium

current_services = gpd.read_file(r"C:\Users\GSE1\Beca\3813283 - PT Services and Infrastructure SSBC - Documents\Technical - Working Files\01 SSBC\04 Longlist\Accessibility analysis\Jupyter\current_services.geojson")
current_to_cbd = gpd.read_file(r"C:\Users\GSE1\Beca\3813283 - PT Services and Infrastructure SSBC - Documents\Technical - Working Files\01 SSBC\04 Longlist\Accessibility analysis\Jupyter\current_to_cbd.geojson")

st.write("Route Modifications for the Western Bay of Plenty")

return_on_hover = st.checkbox("Return on hover?")

m_current_cbd = folium.Map(location=[-37.68897481760735, 176.20297734800462], zoom_start=12,  tiles="CartoDB positron")

tooltip = "Tauranga CBD"
folium.Marker([-37.68393165612077, 176.16731368437846], tooltip=tooltip).add_to(m_current_cbd)


travel_time = folium.Choropleth(
    geo_data=current_to_cbd,
    name='Bus travel time to Tauranga CBD',
    data=current_to_cbd,
    columns=['geoid', 'minutes'],
    key_on='feature.id',
    fill_color='YlOrRd',
    fill_opacity=0.4,
    line_opacity=0.2,
    line_color='white', 
    line_weight=0,
    highlight=True, 
    smooth_factor=1.0,
    #threshold_scale=[100, 250, 500, 1000, 2000],
    legend_name= 'Bus travel time to Tauranga CBD - Current network 2048').add_to(m_current_cbd)

folium.features.GeoJsonTooltip(fields=['minutes']).add_to(travel_time.geojson)

routes = folium.Choropleth(geo_data=current_services,
    data=current_services,
    columns=['line_id', 'line_name'],
    line_color="#98bad4",
    line_weight=2,
    line_opacity=0.4).add_to(m_current_cbd)

folium.features.GeoJsonTooltip(fields=['line_name']).add_to(routes.geojson)

   

out = st_folium(m_current_cbd, height=600, width=600, return_on_hover=return_on_hover)

st.write("Minutes:", current_to_cbd['minutes'])
