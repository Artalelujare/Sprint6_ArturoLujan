import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('./vehicles_us.csv')  # leer los datos
car_data['model'] = car_data['model'].str.replace('-', '')

st.header('Anuncios de venta de coches')
st.write('Elige la gráfica que desees:')

show_histogram = st.checkbox('Histograma_Condición del vehículo')
show_Hist_model = st.checkbox('Histograma_Tipos de vehículos')
show_scatter = st.checkbox('Diagrama de dispersión_Odómetro')


if show_histogram:
    fig_hist = px.histogram(car_data,
                            x='model_year',
                            color='condition',
                            opacity=0.6,
                            color_discrete_sequence=[
                                '#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'],
                            title="Histograma de la <span style='color:red'>condición del auto</span> vs <span style='color:red'>el año del modelo</span>")

    fig_hist.update_layout(
        xaxis_title='Año del Modelo',
        yaxis_title='Cantidad de Vehículos'
    )
    st.plotly_chart(fig_hist)

if show_Hist_model:

    tipo_auto = st.selectbox(
        'Selecciona el tipo de vehículo', car_data['type'].unique())

    # Filtrar los modelos según el tipo de vehículo seleccionado
    modelos_filtrados = car_data[car_data['type']
                                 == tipo_auto]['model'].unique()
    modelo_auto = st.selectbox('Selecciona el modelo', modelos_filtrados)

    data_filtrada = car_data[(car_data['type'] == tipo_auto) & (
        car_data['model'] == modelo_auto)]

    fig_model = px.histogram(data_filtrada,
                             x='odometer',
                             opacity=0.6,
                             color_discrete_sequence=['skyblue'],
                             title="Histograma del tipo de vehículo por año del modelo")

    fig_model.update_layout(
        xaxis_title='Odómetro',
        yaxis_title='Cantidad de Vehículos'
    )
    st.plotly_chart(fig_model)

if show_scatter:
    fig_scatter = px.scatter(car_data,
                             x='odometer',
                             y='price',
                             color_discrete_sequence=['skyblue'],
                             title='Diagrama de dispersión')
    fig_scatter.update_layout(
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )
    st.plotly_chart(fig_scatter)
