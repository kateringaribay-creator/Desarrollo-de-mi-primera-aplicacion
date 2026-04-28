import streamlit as st
import pandas as pd
import numpy as np

#Home 
st.title("Desarrollo de mi primera aplicación")
st.image("logo.png", width=150) 
st.subheader("Katerin Delfina Garibay Fernandez")
st.write("Especializacion en Python")          
st.markdown("2026")
st.write("Este proyecto consiste en el desarrollo de una aplicación interactiva utilizando Python y Streamlit. Permite ingresar datos mediante formularios y procesarlos con funciones y clases definidas en librerías externas. La aplicación muestra resultados en tiempo real y almacena registros en tablas dinámicas. Además, incorpora operaciones CRUD para gestionar la información ingresada.")
st.write("Tecnologias utilizadas",
         "1. Python",
         "2.Streamlit",
         "3. Pandas",
         "4. NumPy",
         "5. Librerías personalizadas") 


# Ejercicio 1
st.title("Ejercicio 1 – Flujo de caja con listas")
st.markdown("Módulo para registrar movimientos financieros en una lista vacía.")

Concepto = st.text_input("Ingrese el concepto")
Tipo = st.selectbox("Tipo de movimiento", ["Gasto", "Ingreso"]) 
Valor = st.number_input("Valor")

# Crear lista
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# Botón
if st.button("Agregar"):
    movimiento = [Concepto, Tipo, Valor]
    st.session_state.movimientos.append(movimiento)

# Mostrar lista
st.write(st.session_state.movimientos)

# Solo si hay datos
if st.session_state.movimientos:

    # Crear DataFrame
    df = pd.DataFrame(
        st.session_state.movimientos,
        columns=["Concepto", "Tipo", "Valor"]
    )

    st.dataframe(df)

    # Cálculos
    ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
    gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
    saldo = ingresos - gastos

    # Resultados
    st.metric("Ingresos", ingresos)
    st.metric("Gastos", gastos)
    st.metric("Saldo", saldo)

    # Estado
    if saldo > 0:
        st.success("Flujo de caja a favor")
    else:
        st.error("Flujo de caja en contra")

#Ejercicio 2 
import streamlit as st
import numpy as np
import pandas as pd


# Título y descripción
st.title("Ejercicio 2 – Registro de Productos")
st.markdown("Formulario para registrar productos usando NumPy y DataFrame")


nombre = st.text_input("Nombre del producto")
categoria = st.selectbox("Categoría", ["Alimentos", "Ropa", "Tecnología"])
precio = st.number_input("Precio", min_value=0.0)
cantidad = st.number_input("Cantidad", min_value=0)


# Inicializar arrays en memoria
if "nombres" not in st.session_state:
    st.session_state.nombres = np.array([])
    st.session_state.categorias = np.array([])
    st.session_state.precios = np.array([])
    st.session_state.cantidades = np.array([])
    st.session_state.totales = np.array([])

# Botón
if st.button("Agrega"):
    if nombre != "" and precio > 0 and cantidad > 0:
        
        total = precio * cantidad

        # Guardar en arrays (NumPy)
        st.session_state.nombres = np.append(st.session_state.nombres, nombre)
        st.session_state.categorias = np.append(st.session_state.categorias, categoria)
        st.session_state.precios = np.append(st.session_state.precios, precio)
        st.session_state.cantidades = np.append(st.session_state.cantidades, cantidad)
        st.session_state.totales = np.append(st.session_state.totales, total)

    else:
        st.warning("Completa todos los campos correctamente")


# Crear DataFrame
df = pd.DataFrame({
    "Producto": st.session_state.nombres,
    "Categoría": st.session_state.categorias,
    "Precio": st.session_state.precios,
    "Cantidad": st.session_state.cantidades,
    "Total": st.session_state.totales
})


# Mostrar tabla
st.subheader("Registros")
st.dataframe(df)

import streamlit as st
import pandas as pd
import libreria_funciones_proyecto1 as lf


# Ejercicio 3

st.title("Ejercicio 3 - Margen Neto")
st.markdown("Cálculo de utilidad y margen neto usando función externa")


ingresos = st.number_input("Ingresos", min_value=0.01)
costos = st.number_input("Costos", min_value=0.0)
gastos = st.number_input("Gastos operativos", min_value=0.0)
impuestos = st.number_input("Impuestos", min_value=0.0)

# Historial
if "historial" not in st.session_state:
    st.session_state.historial = []

# Botón
if st.button("Calcular", key="btn_margen"):

    try:
        resultado = lf.calcular_margen_neto(ingresos, costos, gastos, impuestos)

        # Mostrar resultados
        st.success("Resultado:")
        st.write(resultado)

        # Guardar en historial
        registro = {
            "Ingresos": ingresos,
            "Costos": costos,
            "Gastos": gastos,
            "Impuestos": impuestos,
            "Utilidad Neta": resultado["utilidad_neta"],
            "Margen Neto (%)": resultado["margen_neto_pct"]
        }

        st.session_state.historial.append(registro)

    except Exception as e:
        st.error(str(e))

# Tabla historial
df = pd.DataFrame(st.session_state.historial)

st.subheader("Historial de resultados")
st.dataframe(df)

#Ejercicio 4

import streamlit as st
import pandas as pd
import libreria_clases_proyecto1 as lc

st.title("Ejercicio 4 - CRUD Empleados")

# Memoria
if "empleados" not in st.session_state:
    st.session_state.empleados = []

# Tablas
tab1, tab2, tab3 = st.tabs(["Crear", "Actualizar", "Eliminar"])

# CREAR
with tab1:
    st.subheader("Registrar empleado")

    nombre = st.text_input("Nombre")
    salario = st.number_input("Salario base", min_value=0.01)
    bono = st.number_input("Bono (%)", min_value=0.0)
    descuento = st.number_input("Descuento (%)", min_value=0.0)

    if st.button("Agregar", key="crear_emp"):

        try:
            emp = lc.Empleado(nombre, salario, bono, descuento)
            resumen = emp.resumen()

            st.session_state.empleados.append(resumen)

            st.success("Empleado registrado")

        except Exception as e:
            st.error(str(e))


#MOSTRAR
df = pd.DataFrame(st.session_state.empleados)

st.subheader("Lista de empleados")
st.dataframe(df)

#ACTUALIZAR
with tab2:
    st.subheader("Actualizar empleado")

    if not df.empty:
        index = st.selectbox("Selecciona empleado", df.index)

        nombre_u = st.text_input("Nuevo nombre")
        salario_u = st.number_input("Nuevo salario", min_value=0.01)
        bono_u = st.number_input("Nuevo bono (%)", min_value=0.0)
        descuento_u = st.number_input("Nuevo descuento (%)", min_value=0.0)

        if st.button("Actualizar", key="update_emp"):

            try:
                emp = lc.Empleado(nombre_u, salario_u, bono_u, descuento_u)
                st.session_state.empleados[index] = emp.resumen()

                st.success("Empleado actualizado")

            except Exception as e:
                st.error(str(e))

#ELIMINAR
with tab3:
    st.subheader("Eliminar empleado")

    if not df.empty:
        index_del = st.selectbox("Selecciona empleado a eliminar", df.index)

        if st.button("Eliminar", key="delete_emp"):
            st.session_state.empleados.pop(index_del)
            st.success("Empleado eliminado")