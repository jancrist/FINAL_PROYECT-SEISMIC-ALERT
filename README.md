# FINAL


## PROYECTO GRUPAL ALERTAS SISMICAS

Propuesta de trabajo
Para este proyecto ustedes harán parte del equipo de atención de desastres del país latinoamericano de su preferencia. En este momento se encuentran trabajando en un proyecto tri-nacional en conjunto con el Estados unidos (USGS) y Japón (JMA) llamado “Working towards global standardization of seismological networks and effective communication to the civilian community.”  
Los objetivos de esta alianza son:  
1. Crear una base de datos depurada que contemple los datos de las tres naciones de forma estandarizada:  
A las autoridades les interesa tener la información estándar de todos los países para poder crear un mecanismo de clasificación. La definición de un evento sísmico y los criterios de alerta adecuados deben tener en cuenta la calidad de los datos.  
Spoiler: Tendran "problemas" de outliers, y en este caso no son errores 👀  
2. Implementar mecanismos de comunicación y alerta a la comunidad civil en un lenguaje intuitivamente interpretable a través de Internet o cellBroadCast:  
Al público le interesa saber si se produjeron daños en los edificios o si la salud y la seguridad están en peligro.  
¿Que quiere decir esto? Enfoquense en generar analisis valiosos para su comunidad! Piensen en como ustedes les gustaria ser informados cada vez que un sismo ocurre:  Entienden que significa Magnitud? Profundidad? La diferencia entre hipocentro o epicentro? Por que podria importar? Traducir esto al lenguaje cotidiano es su reto!  
¿Como lo hacemos?
*Para grupos de 5 personas, los dos enfoques son obligatorios  
Enfoque 1 [Data Analysis focus]  
Analizando profundamente la relacion de los sismos con otra u otras particularidades de su pais latinoamericano escogido.  

Ejemplos de lineas de investigacion (Solo para que se inspiren. Pueden divagar y escoger lo que se les ocurra, su mente es el limite!):  
Sismicidad secundaria (después de un gran sismo) ¿cómo afecta? ¿Qué ha pasado? Se pueden anticipar medidas si es que hay algo sistemáticamente mal?  
Es aconsejable que haya una reubicación de habitantes en zonas como CDMX que es sabido esta construida en una zona geológicamente inestable y con alta actividad sísmica?  
Derribando (o acentuando) mitos: Tiene que ver el clima con la propensión a sismos de mayor “magnitud” y los cambios estacionales?  
Efectos secundarios no deseables: Sismos y Tsunamis, Problemas en redes eléctricas, incendios…  
Entregables tangibles minimos: Mapa de geolocalizacion de los sismos escogidos que contemple la actualizacion cada hora. La informacion que debe tener DEBE ser la escogida en su analisis. NO debe ir informacion cientifica como: Magnitud, Profundidad si esta no esta explicada o se indica por que es relevante.  

Enfoque 2 [Machine Learning Focus]  
Aplicar un modelo de clasificacion no supervisada. La idea aqui NO sera predecir un sismo, sino, dadas las caracteristicas que tienen los sismos, clasificarlos segun patrones como Peligrosidad Media/Alta/Baja o cualquier enfoque que quieran aplicar.  
Entregables tangibles minimos: Presentacion de las etiquetas de clasificacion y performancia del modelo.  
Deploy del modelo de ML - puesta en produccion (plataforma a elección)  

Datasets y fuentes complementarias  
Fuentes de datos obligatorias:  

Estados Unidos https://earthquake.usgs.gov/fdsnws/event/1/  
Japon https://www.fdsn.org/networks/detail/JP/  
Observatorio Latinoamericano de su preferencia ***********  
Nota: El producto final debe tener en su etapa de extraccion los datos en formato JSON o GeoJSON. Formatos de texto como CSV podrian usarse en los pasos intermedios para hacer sus test respectivos de ser necesario, pero no seran admitidos en la entrega final.  

## COMO FUIMOS TRABAJANDO  
Division de Tareas:  
Data Engineer:  
Jan  Rivarola  
Sebastian Burella  
Data Scientist:  
Rodrigo Alegre  
Data Analyst:  
Agustina Ccastillo  
Lucas Rodriguez  

Para este trabajo nos fuimos dividiendo las tareas, si bien en este proceso todos realizamos practicamente todo y nos ayudamos entre si los puestos estan establecidos asi no solo por una division de tareas sino tambien de responsabilidad.  

## PLANIFICACION  
Para este proceso decidimos realizar todo el proceso en Google Cloud para asi este estar atomatizado y en caso de que en la API de la cual se descargan los datos correspondientes se vayan subiendo nuevos datos de sismos, estos automaticamente se vayan incorporando a nuestro modelo y realizando todo el proceso correspondiente de manera automatizada.   

## ARQUITECTURA:  
Si bien para este proceso al inicio no teniamos bien decidido como ibamos a ir trabajando, esta fue la arquitectura que nos decidimos por usar. Antes de realizar el proceso posteriormente nombrado, al inicio lo realizamos simplemente de forma local, descargando los datos en Visual Studio usando Python y con una base de datos local usando MySQL.  

## DIAGRAMA DE FLUJO:  

![image](https://user-images.githubusercontent.com/105827215/207708238-1ad77346-a386-4a6d-a2e2-d4ca4ee5ca75.png)

	
Si bien trabajando de forma local como nombramos anteriormente el proceso se ejecutaba correctamente, este no estaba automatizado por lo cual en caso de que se suban nuevos datos a la API de la cual se descagan los archivos, estos se iban a ver ignorados, por esta razon tuvimos que pasar todo el ambiente de produccion a una fase de desarrollo en la cual estos procesos estan todos automatizados en la nube de tal forma que en caso de subirse nuevos datos, estos automaticamente se iran actualizando y realizando el proceso de manera automatizada.  
Explicacion De la Arquitectura Final:  
Para este trabajo como decidimos trabajar, asi como esta explicado en la imagen del diagrama de flujo la cual esta encima, los siguientes son los proceso realizados.  

## ETL:  

Primero los datos son descargados de una API la cual es la siguiente: https://earthquake.usgs.gov/. Esta API es una API en la que se suben todo tipo de datos de catastrofes naturales en general pero en este caso lo unico que utilizamos son los datos de los sismos correspondientes.  

Segundo estos datos los toma el motor de Vertex AI el cual es un motor el cual abre Python desde la nube con jupyter notebooks, manera muy parecida a la trabajada de manera local con Visual Studio pero en este caso de manera automatizada y on cloud.  

Luego mediante la herramienta anteriormente nombrada se realiza todo el proceso de ETL del modelo, para esto se buscan aquellos valores los cuales no vamos a utilizar como aquellos sismos los cuales no son orignados por condiciones naturales sino por condiciones humanas como explosion de bombas, misiles, etc.  

Ademas se realiza un borrado de aquellos valores faltantes, y se toman solo aquellos sismos los cuales tengan mas una magnitud superior a 2 ya que aquellas las cuales son inferiores a dicho numero son practicamente imperceptibles.  

Tambien para este proceso se analizo muy bien los datos de cada columna ya que no teniamos mucho conocimiento sobre sismos por lo cual no sabiamos muy bien que realizar con estos datos.  

## Los Datos de estas son los siguientes:  

-Gap: O brecha sísmica: zona geológica en la que no ha ocurrido un sismo fuerte durante un periodo prolongado de tiempo.  
-Nst : El número total de estaciones sísmicas utilizadas para determinar la ubicación del terremoto.  
-Depth: La profundidad donde el terremoto comienza a romperse. Esta profundidad puede ser relativa al geoide WGS84, el nivel medio del mar o la elevación promedio de las estaciones sísmicas que proporcionaron datos de tiempo de llegada para la ubicación del terremoto. La elección de la profundidad de referencia depende del método utilizado para localizar el terremoto, que varía según la red sísmica. Dado que ComCat incluye datos de muchas redes sísmicas diferentes, el proceso para determinar la profundidad es diferente para diferentes eventos. La profundidad es el parámetro menos restringido en la ubicación del terremoto y las barras de error son generalmente más grandes que la variación debido a los diferentes métodos de determinación de la profundidad.  
-dmin : Distancia horizontal desde el epicentro hasta la estación más cercana (en grados). 1 grado son aproximadamente 111,2 kilómetros. En general, cuanto menor sea este número, más confiable es la profundidad calculada del terremoto.  
-rms : Valor Cuadratico Medio.  
-net : El ID de un contribuyente de datos. Identifica la red considerada como la fuente de información preferida para este evento.  
MagType: “Md”, “Ml”, “Ms”, “Mw”, “Me”, “Mi”, “Mb”, “MLg”.  
ML: Magnitud Local/Magnitud Richter.  
MW: Magnitud de Momento.  
MS: Magnitud de Ondas superficiales.  
MB: Magnitud de ondas de cuerpo.  

## Las columnas borradas en este proceso son las siguientes:  
-Status: estado si revisado/ manual u automático. No nos sirve para nuestro modelo.  
-Location source: misma información en latitud/longitud.  
-Mag source: misma razón que la anterior.  
-Updated: no nos interesa cuando se actualizaron los datos.  
-Id: no nos sirve para nuestro modelo, se puede volver a generar una id en el futuro pero siguiendo algún orden especifico.  
-magNst:no aporta datos a nuestro modelo.  
-horizontalError: no necesitamos conocer el error en nuestro modelo, no aporta en nada este tipo de error en la obtención de los datos, ya que con esta información no podemos hacer nada.  
-depthError: Misma razón anterior.  
-magError: misma razón anterior.  
-net: información confusa.  

## MACHINE LEARNING:  
Para este proceso se realizo un modelo predictivbo de clasificacion no supervisado, especificamente el modelo K-Mens para predecir la peligrosidad de los sismos. En este se predice el tipo de magnitud que puede llegar a tener el mismo. Considerando los diferentes tipos de magnitudes Ritcher que se ejemplifican a continuacion. En las magnitudes Ritcher se utilizan magnitudes logaritmicas, esto quiere decir que cada escala que va subiendo se multiplica por 30 el valor anterior, Esto quiere decir que por ejemplo: un sismo de magnitud 2 en la logica matematica nos diria que es el doble que un sismo de magnitud 1, pero en este caso no es asi ya uqe un sismo magnitud 2 es 30 veces superior a un sismo magnitud 1, un sismo magnitud 3 es 30 vewces superior a un sismo nivel 2 y asi cada escala que va subiendo en las magnitudes se va multiplicando por 30 la energia que libera dicho sismo.  


![image](https://user-images.githubusercontent.com/105827215/207708518-ab169271-6fa9-402d-af13-c5b739f39fbf.png)


Grafico de el modelo de codo de la prediccion correspondiente.  

![image](https://user-images.githubusercontent.com/105827215/207708752-60ceef03-e0b6-40dc-be4b-b82b4231f955.png)

Grafico del agrupamiento de los datos por clusters.  

![image](https://user-images.githubusercontent.com/105827215/207709107-cd5e1597-94c0-438a-954f-ed29c62aaef2.png)

## DATA ANALYST:  
Para este proceso se utilizo Power BI para realizar los dashboards. En estos realizamos multiples dashboards ya que no simplemente trabajabamos con datos de Sismos sino tambien de catastrofes naturales en general. 
Entre los datos mas destacados que pudimos sacar con la utilizacion y presentacion de estos dashboards fueron:
1)Pais con mayor cantidad de desastres naturales es Estados Unidos.
2)La catastrofe natural con mas numero de ocurrencias es la de inundaciones. 
3)Tipo de sismo con mas ocurrencia es "Eartquake"
4)Magnitud promedio de los sismos 2,11
![image](https://user-images.githubusercontent.com/106763237/207767555-d4a2983b-652c-4fa4-8109-8a31e703f0f9.png)



