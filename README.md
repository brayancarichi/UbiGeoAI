# UbiGeoAI


Serie de funciones que permiten al usuario ubicar espacialmente los Bounding Boxes a partir de archivos georreferenciados (ráster) generando de esta manera, archivos en formato shapefile. Lo que permite hacer análisis en Sistemas de Información Geográfica (SIG).

Si quieres conocer mas de nuestro trabajo visita los siguientes enlaces de LinkedIn:

- https://mx.linkedin.com/in/brayan-murillo-guti%C3%A9rrez-76a2a7281?original_referer=https%3A%2F%2Fwww.google.com%2F

- https://mx.linkedin.com/in/hugo-luis-rojas-villalobos-5918661a4?original_referer=https%3A%2F%2Fwww.google.com%2F

## Instalación

## Creación de carpetas dentro de la ruta donde se implemente la librería  

De manera automática, la librería creará carpetas esenciales para su funcionamiento. Estas carpetas se encontrarán en la dirección del código donde se ejecute la librería. NOTA IMPORTANTE: cada vez que se ejecute la librería se deben de respaldar los resultados ya que estos serán borrados de manera permanente. Las carpetas que se crearán serán las siguientes:

- Predict

- Predict_jpg

- Resultados

- runs  

## Parámetros esenciales de la librería  

- path_raster = ruta del archivo ráster donde se harán las detecciones    

- path_model = ruta del archivo PyTorch generado obtenido mediante Yolo OBB 

- confidence = el valor de confidencia

- output_name = el nombre que se les asignará a los resultados obtenidos

- img_div = tamaño de las matrices generadas a partir de la división del ráster de entrada



