#  Microservicio Factorial – Parcial 02

**Autor:** Camila Vélez  
**Curso:** Arquitectura de Microservicios  

---

##  Descripción del proyecto

Este microservicio desarrollado con **Python y Flask** recibe un número entero por URL y devuelve una respuesta en formato **JSON** con la siguiente información:

- El número recibido.  
- Su factorial.  
- Una etiqueta que indica si el factorial es **par** o **impar**.  

El objetivo del ejercicio es aplicar los principios básicos de los **microservicios**, como la independencia, escalabilidad y simplicidad, además de la **contenedorización con Docker**.

---

##  Requisitos previos

- Python 3.10 o superior  
- pip (administrador de paquetes de Python)  
- (Opcional) Docker y Docker Hub  

---

##  Ejecución local

1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar la aplicación:
   ```bash
   python app.py
   ```

3. Probar en el navegador o Postman:
   ```
   http://localhost:5000/factorial/5
   ```

 **Ejemplo de respuesta JSON:**
```json
{
  "numero_recibido": 5,
  "factorial": 120,
  "etiqueta": "par"
}
```

---

##  Ejecución con Docker

1. Construir la imagen:
   ```bash
   docker build -t camilavelez/microservicio-factorial:latest .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -p 5000:5000 camilavelez/microservicio-factorial:latest
   ```

3. Acceder desde el navegador:
   ```
   http://localhost:5000/factorial/7
   ```

---

##  Análisis – Comunicación con otro servicio

Si este microservicio tuviera que comunicarse con otro servicio que almacene el historial de cálculos en una base de datos externa, **modificaría su diseño aplicando los principios de arquitectura de microservicios** para mantener la independencia y la escalabilidad.

En lugar de incluir la lógica de almacenamiento dentro del mismo servicio, se crearía **un segundo microservicio** encargado exclusivamente de recibir y guardar los registros en la base de datos.  
El microservicio actual (factorial) seguiría calculando el resultado y luego **enviaría una solicitud HTTP (por ejemplo, un POST en formato JSON)** al servicio de historial, transmitiendo los datos del cálculo (número, factorial y etiqueta).

Ambos servicios se comunicarían mediante **APIs REST** dentro de la misma red de Docker (usando *Docker Compose* o *Docker Swarm*), lo que permite aislarlos y escalarlos de forma independiente.  
Además, se podrían definir **variables de entorno** para configurar la dirección del servicio de historial, mejorando la portabilidad y la configuración del sistema.

De esta forma:
- Se mantiene el **desacoplamiento** entre componentes.  
- Cada servicio puede **evolucionar o escalar** sin afectar al otro.  
- Se asegura la **persistencia y registro de operaciones** sin alterar la lógica principal del cálculo.  

---


##  Tecnologías utilizadas

- **Python 3.11**
- **Flask**
- **Docker**
- **JSON**
