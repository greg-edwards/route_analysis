import streamlit as st
from folium.features import Marker, Popup
import pandas as pd
import numpy as np
import geopandas as gpd
import leafmap
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.sidebar.image('https://becagroup.sharepoint.com/sites/ClientsandMarkets/Images1/Market%20Profile%20&%20Brand/Beca%20Brand%20&%20Standards/Beca%20Logo%20Black%20PNG.png?csf=1&web=1&e=p6QEq9&cid=d89ac465-29af-4979-83d9-a76c21e84693', width=150, output_format="auto")
st.sidebar.title("About")
st.sidebar.info(
    """
    The Western Bay of Plenty PT Services and Infrastructure Business Case is investigating options to anble signficant mode shift to PT in the Western Bay. The business case will identify both service and infrastructure modifications/interventions.
    """
)

st.sidebar.title("Questions / Contact")
st.sidebar.info(
    """
    If you have any questions or general feedback on this app or notice any errors, please contact Greg Edwards (greg.edwards@beca.com)
    """
)

#import route geometry
route_c = gpd.read_file(r"C:\Users\GSE1\Beca\3813283 - PT Services and Infrastructure SSBC - Documents\Technical - Working Files\01 SSBC\05 Shortlist\01 Service options assessment\01 Route modifications\Route C\route_c.geojson")
route_ca = gpd.read_file(r"C:\Users\GSE1\Beca\3813283 - PT Services and Infrastructure SSBC - Documents\Technical - Working Files\01 SSBC\05 Shortlist\01 Service options assessment\01 Route modifications\Route C\route_ca.geojson")
route_cb = gpd.read_file(r"C:\Users\GSE1\Beca\3813283 - PT Services and Infrastructure SSBC - Documents\Technical - Working Files\01 SSBC\05 Shortlist\01 Service options assessment\01 Route modifications\Route C\route_cb.geojson")

#import stop geometry
route_stops = gpd.read_file(r'C:\Users\GSE1\Beca\3813283 - PT Services and Infrastructure SSBC - Documents\Technical - Working Files\01 SSBC\05 Shortlist\01 Service options assessment\01 Route modifications\Route C\stops_routes.geojson')

#import route data
route_data = pd.read_excel(r'C:\Users\GSE1\Beca\3813283 - PT Services and Infrastructure SSBC - Documents\Technical - Working Files\01 SSBC\05 Shortlist\01 Service options assessment\01 Route modifications\Route C\route_C_options.xlsx')

#select stops by route
route_c_stops = route_stops.loc[route_stops['lines'].str.contains("C - Existing"), "geometry"]                       
route_ca_stops = route_stops.loc[route_stops['lines'].str.contains("CA - via Pooles Rd"), "geometry"]  
route_cb_stops = route_stops.loc[route_stops['lines'].str.contains("CB - via Maleme St"), "geometry"]  

#title and intro
st.title("Route C - Analysis and Potential Options")
st.markdown("""
            This page displays potential alternative options for Route C (Pyes Pa - City - Papamoa). The page displays summary route statistics for each option. The options include:
            - Route C - Existing configuration
            - Route Ca - Diverting down Pooles and Mansels Rd
            - Route Cb - Diverting down Maleme Street
                        """)

#drop-down box
route_selection = st.selectbox('Please select a route in the drop down below.', ['Route C', 'Route Ca', 'Route Cb'])

#define columns
col1, col2 = st.columns([3, 1])

#show specific routes on selection
if route_selection == 'Route C':
        
    with col1:
        map = folium.Map(location=[-37.7317724847819, 176.13535800654518], 
                            zoom_start=15, 
                            tiles="CartoDB positron"
                            )
        folium.GeoJson(route_c,
                       zoom_on_click=True,
                       tooltip=route_c['line_name'],
                        style_function=lambda feature: {
                                                        "fillColor": "#ffff00",
                                                        "color": "grey",
                                                        "weight": 1.5,
                                                        "dashArray": "5, 5"}).add_to(map)
        
        folium.GeoJson(route_c_stops, tooltip="Bus stop",
                       marker=folium.Circle(radius=4, fill_color="orange", fill_opacity=0.4, color="black", weight=1),
                       ).add_to(map)
        
        tooltip = "Pyes Pa"
        folium.Marker([-37.77360, 176.11650], tooltip=tooltip, icon=folium.Icon(color="blue", icon="glyphicon-flag")).add_to(map)

        tooltip = "Papamoa"
        folium.Marker([-37.701462909595115, 176.2846907972899], tooltip=tooltip, icon=folium.Icon(color="blue", icon="glyphicon-flag")).add_to(map)
           
        out = st_folium(map, height=500, width=800)
        
        st.subheader("Comapre key route statistics")

        data_selection = st.selectbox('Please select a comparator in the drop down below to compare against the different options.', ['Route length', 'Operating cost per year', 'Layover hours per year', 'KMs per year', 'Average daily PT trips'])

        if data_selection == 'Route length':

            st.bar_chart(route_data, x="route_no", y="length(km)")

        if data_selection == 'Operating cost per year':

            st.bar_chart(route_data, x="route_no", y="cost_yr")

        if data_selection == 'Layover hours per year':

            st.bar_chart(route_data, x="route_no", y="layhrs_yr")

        if data_selection == 'KMs per year':

            st.bar_chart(route_data, x="route_no", y="km_yr")
                
        if data_selection == 'Average daily PT trips':

            st.bar_chart(route_data, x="route_no", y="dy_pt_demand_twoway")
        
        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(route_data)  
        
    with col2:
        st.subheader("Route Stats")
        
        st.metric(
            label="Length (kms)",
            value=(route_data.iloc[0, 2]))
                           
        st.metric(
            label="Operating cost per year ($)",
            value=(route_data.iloc[0, 3]))
        
        st.metric(
            label="Required layover hours per year",
            value=(route_data.iloc[0, 4]))
        
        st.metric(
            label="Vehicle kilometres per year",
            value=(route_data.iloc[0, 5]))
        
        st.metric(
            label="Average daily PT demand (2048)",
            value=(route_data.iloc[0, 6]))
    
if route_selection == 'Route Ca':

    with col1:
        map = folium.Map(location=[-37.7317724847819, 176.13535800654518], 
                            zoom_start=15, 
                            tiles="CartoDB positron"
                            )
        folium.GeoJson(route_ca,
                       zoom_on_click=True,
                        style_function=lambda feature: {
                                                        "fillColor": "#ffff00",
                                                        "color": "blue",
                                                        "weight": 1,
                                                        "dashArray": "5, 5"}).add_to(map)
            
        folium.GeoJson(route_ca_stops, tooltip="Bus stop",
                       marker=folium.Circle(radius=4, fill_color="orange", fill_opacity=0.4, color="black", weight=1),
                       ).add_to(map)
        
        tooltip = "Pyes Pa"
        folium.Marker([-37.77360, 176.11650], tooltip=tooltip, icon=folium.Icon(color="blue", icon="glyphicon-flag")).add_to(map)

        tooltip = "Papamoa"
        folium.Marker([-37.701462909595115, 176.2846907972899], tooltip=tooltip, icon=folium.Icon(color="blue", icon="glyphicon-flag")).add_to(map)
        
        out = st_folium(map, height=500, width=800)
        
        st.subheader("Comapre key route statistics")

        data_selection = st.selectbox('Please select a comparator in the drop down below to compare against the different options.', ['Route length', 'Operating cost per year', 'Layover hours per year', 'KMs per year', 'Average daily PT trips'])

        if data_selection == 'Route length':

            st.bar_chart(route_data, x="route_no", y="length(km)")

        if data_selection == 'Operating cost per year':

            st.bar_chart(route_data, x="route_no", y="cost_yr")

        if data_selection == 'Layover hours per year':

            st.bar_chart(route_data, x="route_no", y="layhrs_yr")

        if data_selection == 'KMs per year':

            st.bar_chart(route_data, x="route_no", y="km_yr")
                
        if data_selection == 'Average daily PT trips':

            st.bar_chart(route_data, x="route_no", y="dy_pt_demand_twoway")
        
        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(route_data)
        
    with col2:
        st.subheader("Route Stats")
        
        st.metric(
            label="Length (kms)",
            value=(route_data.iloc[1, 2]))
                           
        st.metric(
            label="Operating cost per year ($)",
            value=(route_data.iloc[1, 3]))
        
        st.metric(
            label="Required layover hours per year",
            value=(route_data.iloc[1, 4]))
        
        st.metric(
            label="Vehicle kilometres per year",
            value=(route_data.iloc[1, 5]))
        
        st.metric(
            label="Average daily PT demand (2048)",
            value=(route_data.iloc[1, 6]))
    
if route_selection == 'Route Cb':

    with col1:
        map = folium.Map(location=[-37.7317724847819, 176.13535800654518], 
                            zoom_start=14, 
                            tiles="CartoDB positron"
                            )
        folium.GeoJson(route_cb,
                       zoom_on_click=True,
                        style_function=lambda feature: {
                                                        "fillColor": "#ffff00",
                                                        "color": "blue",
                                                        "weight": 1,
                                                        "dashArray": "5, 5"}).add_to(map)
            
        folium.GeoJson(route_cb_stops, tooltip="Bus stop",
                       marker=folium.Circle(radius=4, fill_color="orange", fill_opacity=0.4, color="black", weight=1),
                       ).add_to(map)
        
        tooltip = "Pyes Pa"
        folium.Marker([-37.77360, 176.11650], tooltip=tooltip, icon=folium.Icon(color="blue", icon="glyphicon-flag")).add_to(map)

        tooltip = "Papamoa"
        folium.Marker([-37.701462909595115, 176.2846907972899], tooltip=tooltip, icon=folium.Icon(color="blue", icon="glyphicon-flag")).add_to(map)
        
        out = st_folium(map, height=500, width=800)
        
        st.subheader("Comapre key route statistics")

        data_selection = st.selectbox('Please select a comparator in the drop down below to compare against the different options.', ['Route length', 'Operating cost per year', 'Layover hours per year', 'KMs per year', 'Average daily PT trips'])

        if data_selection == 'Route length':

            st.bar_chart(route_data, x="route_no", y="length(km)")

        if data_selection == 'Operating cost per year':

            st.bar_chart(route_data, x="route_no", y="cost_yr")

        if data_selection == 'Layover hours per year':

            st.bar_chart(route_data, x="route_no", y="layhrs_yr")

        if data_selection == 'KMs per year':

            st.bar_chart(route_data, x="route_no", y="km_yr")
                
        if data_selection == 'Average daily PT trips':

            st.bar_chart(route_data, x="route_no", y="dy_pt_demand_twoway")
        
        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(route_data) 
        
    with col2:
        st.subheader("Route Stats")
        
        st.metric(
            label="Length (kms)",
            value=(route_data.iloc[2, 2]))
                           
        st.metric(
            label="Operating cost per year ($)",
            value=(route_data.iloc[2, 3]))
        
        st.metric(
            label="Required layover hours per year",
            value=(route_data.iloc[2, 4]))
        
        st.metric(
            label="Vehicle kilometres per year",
            value=(route_data.iloc[2, 5]))
        
        st.metric(
            label="Average daily PT demand (2048)",
            value=(route_data.iloc[2, 6])) 
    
    









