from fastapi import FastAPI
import uvicorn
import json
import pandas as pd

app =FastAPI()

agrupacionF1 = pd.read_csv('agrupacionF1.csv')
agrupacionF2 = pd.read_csv('agrupacionF2.csv')
agrupacionF3 = pd.read_csv('agrupacionF3.csv')
agrupacionF4 = pd.read_csv('agrupacionF4.csv')
agrupacionF5 = pd.read_csv('agrupacionF5.csv')

@app.get("/")
def read_root():
    return {"Hola": "Mi Proyecto"}


## Funcion 1
@app.get("/TiempoJugado/genero")
def funcion1(genero):
    if genero in agrupacionF1['genres'].values :

        # Extrae el valor maximo de la columnas playtime_forever
        valorMaximoF1 = agrupacionF1.loc[agrupacionF1['genres'] == genero, 'playtime_forever'].max()
        añoBuscadoF1 = agrupacionF1.loc[agrupacionF1['playtime_forever'] == valorMaximoF1, 'years'].values[0]
        textoF1 = { f"Año de lanzamiento con más horas jugadas para Género {genero}": str(añoBuscadoF1) }
    else:
        textoF1 ="Ingrese un genero correcto"    
    return textoF1

# Funcion 2
@app.get("/UsoPorGeneroAcumulado/valorF2") 
def funcion2(valorF2):
    if valorF2 in agrupacionF2['genres'].values :
        # Solo sacar los valores para ese genero asociado
        generoBuscadoF2 = agrupacionF2[agrupacionF2['genres'] == valorF2]

        # Suma del total de horas jugadas por usuario
        horasPorUsuario = generoBuscadoF2.groupby('user_id')['playtime_forever'].sum().reset_index()

        # Encontrar el usuario que tiene más horas jugadas para el género dado
        usuario_max_horas = horasPorUsuario.loc[horasPorUsuario['playtime_forever'].idxmax(), 'user_id']
        #Horas Maximas
        horas_maximas = horasPorUsuario['playtime_forever'].max()
        # Con el usuario con mas horas 
        añosUsuarioMasHoras = generoBuscadoF2[generoBuscadoF2['user_id'] == usuario_max_horas]
        # Encontrar la acumlacion de horas por año
        acumulacion_horas_por_anio = añosUsuarioMasHoras.groupby('yearsReviews')['playtime_forever'].sum().reset_index()
        # Renombras los indicies del filtro
        acumulacion_horas_por_anio= acumulacion_horas_por_anio.rename(columns={'yearsReviews': 'anio', 'playtime_forever': 'horas Jugadas'})
        # Diccionario para impresion
        lista_diccionarios = acumulacion_horas_por_anio.to_dict(orient='records') 
        #Impresion del resultado de la funcion 
        #textoF2 = "{Usuario con más horas jugadas para Género "+valorF2,":",usuario_max_horas,",",horas_maximas,"\n", lista_diccionarios
        
                
        
        textoF2 = {f"Usuario con más horas jugadas para Género{valorF2}": str(usuario_max_horas),"HorasJugadas" :list(lista_diccionarios)}
    else:
        textoF2 = "Ingrese Genero Correcto"
    return textoF2

#FUncion 3
@app.get("/año3/valorF3") 
def funcion3(valorF3):
    valorF3 = int(valorF3)
    # Condicional si exite el numero de año
    if valorF3 in agrupacionF3['yearsReviews'].values :
    #Filtro de año
        # Igualar un filtro de año, solo al año a tomar
        añoFiltroF3 = agrupacionF3[agrupacionF3['yearsReviews'] == valorF3]
        # Ordenar los valores de mayor a menor
        top3F3 = añoFiltroF3.sort_values(by='sentimiento', ascending=False).head(3)
        # Reiniciar el indice
        top3F3 = top3F3.reset_index(drop=True)
        # Crear la columnas puero 
        
        # Tomar solo dos columnas relevantes para el diccionario de salida
        top3F3Ordenado = top3F3['item_name'].to_dict()
        
        # Hacer lista de diccionarios 
        lista_diccionarios = [{"Puesto " + str(indice + 1): valor} for indice, valor in enumerate(top3F3Ordenado.values())]
        # Reproducir texto
        textoF3 = lista_diccionarios
    #Caso contrario 
    else:
        textoF3 = "Ingrese fecha Correcta"
    return textoF3

#Funcion 4
@app.get("/año4/valorF4")
def funcion4(valorF4):
    valorF4 = int(valorF4)
    # Condicional si exite el numero de año
    if valorF4 in agrupacionF4['yearsReviews'].values :
    #Filtro de año
        # Igualar un filtro de año, solo al año a tomar
        añoFiltroF4 = agrupacionF4[agrupacionF4['yearsReviews'] == valorF4]
        # Ordenar los valores de menor a mayor
        top3F4 = añoFiltroF4.sort_values(by='sentimiento', ascending=True).head(3)
        # Reiniciar el indice
        top3F4 = top3F4.reset_index(drop=True)
        top3F4Ordenado = top3F4['item_name'].to_dict()
        
        lista_diccionarios = [{"Puesto " + str(indice + 1): valor} for indice, valor in enumerate(top3F4Ordenado.values())]

        # Reproducir texto
        textoF4 = lista_diccionarios
    #Caso contrario 
    else:
        textoF4 = "Ingrese fecha Correcta"
    return textoF4

@app.get("/analisis de sentimiento/año")
def funcion5(valorF5):
    valorF5 = int(valorF5)
    # Condicional si exite el numero de año
    if int(valorF5) in agrupacionF5['yearsReviews'].values :
    #Filtro de año
        # Igualar un filtro de año, solo al año a tomar
        añoFiltroF5 = agrupacionF5[agrupacionF5['yearsReviews'] == valorF5]
           
        # Texto de salida funcion
        textoF5 = {(f"Negativo: {añoFiltroF5['Negativo'].values[0]}"),
            (f"Neutral: {añoFiltroF5['Neutral'].values[0]}"),
            (f"Positivo: {añoFiltroF5['Positivo'].values[0]}")}
        
    #Caso contrario 
    else:
        textoF5 = "Ingrese fecha Correcta"
    return textoF5