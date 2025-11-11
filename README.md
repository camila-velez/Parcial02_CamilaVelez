# Microservicio Factorial – Parcial 01

Autor: Tu Nombre  
Curso: Arquitectura de Microservicios

## Descripción
Microservicio en Flask que recibe un número por URL y devuelve un JSON con:
- `numero_recibido`
- `factorial`
- `etiqueta` ("par" o "impar", según el factorial)

### Endpoint
- `GET /factorial/<n>` — `n` entero **no negativo**
- Ejemplo de respuesta:
```json
{
  "numero_recibido": 5,
  "factorial": 120,
  "etiqueta": "par"
}
