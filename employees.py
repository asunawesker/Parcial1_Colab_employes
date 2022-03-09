
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import re

DATA_URL = 'https://raw.githubusercontent.com/maldonadojudith18/Parcial1_Colab_employes/main/Employees.csv'

st.title('Parcial 1 - Empleados')

sidebar = st.sidebar

st.header('Integrantes')
st.text('Irais Aguirre Valente   ')
st.text('Judith Maldonado Garcia  ')
st.text('ISW 602')

st.markdown("___")

@st.cache
def cargar_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

data = cargar_data(500) 

checkbox_datos = sidebar.checkbox("Mostrar todos los datos", key ="Dataframe")
if checkbox_datos:
  estado = st.text('Cargando...')
  data = cargar_data(500)  
  estado.text("¡Cargado! (usando st.cache)")
  st.dataframe(data)
  
sidebar.markdown("___")

@st.cache
def cargar_data_empleados_id(id):  
  filtrar = data[data['Employee_ID'].str.contains(id,flags=re.IGNORECASE)]  
  return filtrar

@st.cache
def cargar_data_ciudad(hometown):  
  filtrar = data[data['Hometown'].str.contains(hometown,flags=re.IGNORECASE)]  
  return filtrar

@st.cache
def cargar_data_unidad(unit):  
  filtrar = data[data['Unit'].str.contains(unit, flags=re.IGNORECASE)]
  return filtrar

sidebar.subheader("Buscador empleados")

inputID = st.sidebar.text_input('Ingrese el ID: ')
btnFiltrarId = sidebar.button('Buscar ID')

inputCiudadNatal = st.sidebar.text_input('Ingrese la ciudad: ')
btnFiltrarCiudadNatal = sidebar.button('Buscar ciudad')

inputTrabajo = st.sidebar.text_input('Ingrese la unidad de trabajo: ')
btnFiltrarTrabajo = sidebar.button('Buscar unidad')

if (btnFiltrarId):
  st.write ("ID buscado: "+ inputID)
  filtrar = cargar_data_empleados_id(inputID)
  count_row = filtrar.shape[0]
  st.write(f'Total: {count_row}')
  st.dataframe(filtrar)

if (btnFiltrarCiudadNatal):
  st.write ("Ciudad buscada: "+ inputCiudadNatal)
  filtrar = cargar_data_ciudad(inputCiudadNatal)
  count_row = filtrar.shape[0]
  st.write(f'Total: {count_row}')

  st.dataframe(filtrar)

if (btnFiltrarTrabajo):
  st.write ("Trabajo buscado: "+ inputTrabajo)
  filtrar = cargar_data_unidad(inputTrabajo)
  count_row = filtrar.shape[0]
  st.write(f'Total: {count_row}')

  st.dataframe(filtrar)

sidebar.markdown("___")

sidebar.subheader("Buscador empleados por nivel academico")

@st.cache
def cargar_data_nivel(level):
  filtrar_data_nivel = data[data['Education_Level'] == level]
  return filtrar_data_nivel

selected = sidebar.selectbox("Selecciona el Nivel academico", data['Education_Level'].unique())
btnFilternivel = sidebar.button('Filtrar por Nivel academico')

if (btnFilternivel): 
  st.write("Empleados con nivel academico "+ str(selected))
  filternivel = cargar_data_nivel(selected)
  count_row = filternivel.shape[0]
  st.write(f'Total: {count_row}')

  st.dataframe(filternivel)
sidebar.markdown("___")

sidebar.subheader("Buscador empleados por ciudad natal")

@st.cache
def cargar_data_ciudad(home):
  filtrar_data_ciudad = data[data['Hometown'] == home]
  return filtrar_data_ciudad

selectedHome = sidebar.selectbox("Selecciona la ciudad natal", data['Hometown'].unique())
btnFilterciudad = sidebar.button('Filtrar por Ciudad')

if (btnFilterciudad): 
  st.write("Empleados con Ciudad natal "+ str(selectedHome))
  filterciudad = cargar_data_ciudad(selectedHome)
  count_row = filterciudad.shape[0]
  st.write(f'Total: {count_row}')

  st.dataframe(filterciudad)
sidebar.markdown("___")

@st.cache
def cargar_data_unidad(unit):
  filtrar_data_unidad = data[data['Unit'] == unit]
  return filtrar_data_unidad

selectedUnit = sidebar.selectbox("Selecciona el trabajo", data['Unit'].unique())
btnFilterunidad = sidebar.button('Filtrar por Trabajo')

if (btnFilterunidad): 
  st.write("Empleados con el trabajo "+ str(selectedUnit))
  filterunidad = cargar_data_unidad(selectedUnit)
  count_row = filterunidad.shape[0]
  st.write(f'Total: {count_row}')

  st.dataframe(filterunidad)
  
sidebar.markdown("___")

sidebar.subheader("Graficas")


checkboxHis = sidebar.checkbox("Histograma de empleados por edades ",key = "edades")
if checkboxHis:
  fig, ax = plt.subplots()

  ax.hist(data['Age'], color='#F2AB6D', rwidth=0.85)
  ax.set_xlabel("Edad")
  ax.set_ylabel("Numero de empleados")
  st.header("Histograma de empleados por edad")

  st.pyplot(fig)

  st.markdown("___")

 
checkbox_frecuencia = sidebar.checkbox("Empleados por unidad de trabajo ",key = "frecuencia")
if checkbox_frecuencia:
  fig, ax = plt.subplots()

  ax.hist(data['Unit'],color =  "#c39bd3", rwidth=0.85)
  ax.set_xlabel("Trabajo")
  ax.set_ylabel("Numero de empleados")
  st.header('Gráfica de frecuencia de empleados por unidad de trabajo')
  plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
  st.pyplot(fig)
  
  st.markdown("___")


checkbox_desercion = sidebar.checkbox("Indice de deserción por ciudad ",key = "desercion")
if checkbox_desercion:
  fig, ax = plt.subplots()

  y_pos = data['Attrition_rate']
  x_pos = data['Hometown']

  ax.bar(x_pos, y_pos,color = "#76448A")
  ax.set_ylabel("Desercion")
  ax.set_xlabel("Ciudad natal")
  ax.set_title('Cuidades que tienen el mayor indice de desercion')

  st.header("Indice de deserción por ciudad")

  st.pyplot(fig)

  st.markdown("___")



checkbox_edad = sidebar.checkbox("Indice de deserción por edad ", key = "desEdad")
if checkbox_edad:
  fig, ax = plt.subplots()

  y_pos = data['Attrition_rate']
  x_pos = data['Age']

  ax.barh(x_pos, y_pos, color = "#229954")
  ax.set_xlabel("Desercion")
  ax.set_ylabel("Edad")
  ax.set_title('Edad y tasa de desercion de los empleados')

  st.header("Indice de deserción por edad")

  st.pyplot(fig)

  st.markdown("___")


checkbox_servicio = sidebar.checkbox("Indice de deserción por Tiempo de servicio ",key = "service")
if checkbox_servicio:
  fig, ax = plt.subplots()

  y_pos = data['Attrition_rate']
  x_pos = data['Time_of_service']

  ax.bar(x_pos, y_pos, color = "#DF39DD")
  ax.set_ylabel("Desercion")
  ax.set_xlabel("Tiempo de servicio")
  ax.set_title('Empleados desertaron por tiempo de servicio')

  st.header("Indice de deserción por tiempo de servicio")

  st.pyplot(fig)

  st.markdown("___")
