import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Construcción de gráficos con plotly-express')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
car_model_avg=car_data['model_year'].mean() 
car_data['model_year'].fillna(car_model_avg, inplace=True) #corregir datos de una columna
car_data['model_year']=car_data['model_year'].astype('int')

# crear una casilla de verificación
build_histogram_scattter = st.checkbox('Ver gráficos de precio y año de los coches')
if build_histogram_scattter:
    st.write('Histograma de los precios de venta de coches')
    hist_button1 = st.button('Construir histograma') # crear un botón
    if hist_button1:
        st.write('Creación de histograma')
        fig = px.histogram(car_data, x="price") # crear un histograma
        st.plotly_chart(fig, use_container_width=True) # mostrar gráfico interactivo
    hist_button2 = st.button('Construir gráfico de dispersión') # crear un botón
    if hist_button2:
        st.write('Creación de gráfico de dispersión con línea de correlación') # crear un gráfico de correlación
        fig = px.scatter(car_data, x='model_year', y='price', title='Precio vs Año', trendline='ols') # mostrar gráfico
        st.plotly_chart(fig, use_container_width=True) # mostrar gráfico interactivo

        
build_pie = st.checkbox('Ver gráfica de tipos de coches')
if build_pie: # al hacer clic en el botón
    st.write('Creación de un gráfico pastel de los tipos de coches')
    fig = px.pie(car_data, names='type', title='Tipos de coches')
    fig.show()