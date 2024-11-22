import pandas as pd
import json
import dash
from dash import dcc, html
import plotly.express as px
#import os

# Datos de incidencia de pobreza
Incidencia = {
    'Departamento': ['ASUNCION', 'CONCEPCION', 'SAN PEDRO', 'CORDILLERA', 'GUAIRA', 'CAAGUAZU', 'CAAZAPA',
                     'ITAPUA', 'MISIONES', 'PARAGUARI', 'ALTO PARANA', 'CENTRAL', 'NEEMBUCU', 'AMAMBAY',
                     'CANINDEYU', 'PRESIDENTE HAYES','BOQUERON', 'ALTO PARAGUAY'],
    'Indice': [3.06, 35.78, 35.79, 23.88, 29.83, 29.24, 37.51, 27.65, 18.50, 28.80, 18.72, 9.30, 22.91, 23.63,
               30.74, 23.77, 36, 33]
}
df = pd.DataFrame(Incidencia)

# Cargar el archivo GeoJSON
geojson_path = 'DEPARTAMENTOS_PY_CNPV2022.geojson'
with open(geojson_path, 'r') as f:
    geojson_data = json.load(f)

# Crear la app Dash
#app = dash.Dash(__name__, requests_pathname_prefix='/')

# Crear el mapa
fig = px.choropleth_mapbox(
    df,
    geojson=geojson_data,
    locations='Departamento',  # Columna del DataFrame
    featureidkey='properties.DPTO_DESC',  # Clave del GeoJSON
    color='Indice',  # Columna para color
    color_continuous_scale='Plasma',
    mapbox_style='carto-positron',
    zoom=5,
    center={'lat': -23.4, 'lon': -58.4},
    title='Incidencia pobreza en Paraguay'
)
fig.update_geos(fitbounds="locations", visible=False)
# Ajustar diseño
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Configurar el diseño de la app
#app.layout = html.Div([
#    dcc.Graph(figure=fig)
#])

# Ejecutar el servidor
#if __name__ == "__main__":
#    app.run_server(debug=True)

fig.show()
