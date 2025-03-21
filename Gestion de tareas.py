from collections import deque


class Tareas:
    def __init__(self):
        # CREAMOS DOS COLAS: UNA PARA LA ALTA PRIORIDAD Y OTRA PARA PRIORIDAD NORMAL
        self.high_priority_queue = deque()
        self.normal_priority_queue = deque()

    def add_task(self, task, priority="normal"):


        if priority == "high":
            self.high_priority_queue.append(task)
            print(f"Tarea agregada a la cola de alta prioridad: {task}")
        else:
            self.normal_priority_queue.append(task)
            print(f"Tarea agregada a la cola normal: {task}")


    def process_task(self):
        if self.high_priority_queue:
            task = self.high_priority_queue.popleft()
            print(f"Procesando tarea de alta prioridad: {task}")
        elif self.normal_priority_queue:
            task = self.normal_priority_queue.popleft()
            print(f"Procesando tarea normal: {task}")
        else:
            print("No hay tareas para procesar.")

    def show_queues(self):
        print()
        print("Tareas agregadas:")
        print("Tareas de alta prioridad:", list(self.high_priority_queue))
        print("Tareas normales:", list(self.normal_priority_queue))
        print()




if __name__ == "__main__":
    manager = Tareas()

    # AGREGA TAREAS
    print()
    manager.add_task("Revisar servidor", priority="high")
    manager.add_task("Actualizar software")
    manager.add_task("Responder correo urgente", priority="high")
    manager.add_task("Organizar documentos")

    # MUESTRA COLAS
    manager.show_queues()

    # PROCESA LAS TAREAS
    manager.process_task()
    manager.process_task()
    manager.process_task()
    manager.process_task()
    manager.process_task()  # NO DEBERIA HABER MAS TAREAS

    # MUESTRA LAS COLAS DESPUES DEL PROCESO
    manager.show_queues()
