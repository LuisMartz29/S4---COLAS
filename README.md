Crear una clase Queue sin utilizar estructuras predefinidas (list, deque, queue.Queue).

Funciones requeridas en la Cola:

- enqueue(element): Agregar un elemento a la cola.
- dequeue(): Eliminar y devolver el primer elemento.
- front(): Devolver el primer elemento sin eliminarlo.
- is_empty(): Retornar True si la cola está vacía.
- size(): Retornar el número de elementos en la cola.
  
Aplicación práctica:

Sistema de Gestión de Tareas:

- Implementar un gestor de tareas con prioridad donde las tareas urgentes sean atendidas antes de las tareas normales.
Se deben manejar dos colas:
- "1." Cola de alta prioridad (procesos críticos).
- "2." Cola normal (procesos estándar).
- El programa debe permitir agregar tareas con diferentes niveles de prioridad y procesarlas en orden correcto.

Simulación de un sistema de atención al cliente:
- Crear un programa donde los clientes sean atendidos en orden de llegada, pero si un cliente VIP entra en la cola, debe ser atendido antes que los clientes regulares.
- Debe permitir agregar clientes de tipo VIP y Regular.**
