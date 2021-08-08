"""Run 'streamlit run app.py' in the terminal to start the app.
"""
import streamlit as st

# st.set_page_config(layout="wide")

"# leafmap streamlit demo"
st.markdown('Source code: <https://github.com/giswqs/leafmap-streamlit/blob/master/app.py>')

"## Create a heat map"
with st.echo():
    import streamlit as st
    from streamlit_folium import folium_static
    import leafmap.foliumap as leafmap

    # Create a heat map
    filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"

    m = leafmap.Map(tiles='stamentoner')
    m.add_heatmap(filepath, latitude="latitude", longitude='longitude', value="pop_max", name="Heat map", radius=20)

    folium_static(m)


"## Load a GeoJSON file"
with st.echo():


    m = leafmap.Map(center=[0, 0], zoom=2)
    in_geojson = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/cable-geo.geojson'
    m.add_geojson(in_geojson, layer_name="Cable lines")
    folium_static(m)


"## Add a colorbar"
with st.echo():

    m = leafmap.Map()
    m.add_basemap('USGS 3DEP Elevation')
    colors = ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']
    vmin = 0
    vmax = 4000
    m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax)
    folium_static(m)   


"## Change basemaps"
with st.echo():
    m = leafmap.Map()
    m.add_basemap("Esri.NatGeoWorldMap")
    folium_static(m)  