class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    # ESTA CLASE AGG UNA COLA USANDO NODOS ENLAZADOS.
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0

    def enqueue(self, element):
        # AGREGA ELEMENTO
        new_node = Node(element)
        if self.rear_node is None:
            self.front_node = new_node
            self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self._size += 1

    def dequeue(self):
        # ELIMINA Y DEVUELVE EL PRIMERO
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        value = self.front_node.value
        self.front_node = self.front_node.next
        if self.front_node is None:
            self.rear_node = None
        self._size -= 1
        return value

    def front(self):
        # REGRESA EL PRIMER ELEMENTO SIN ELIMINRLO.
        if self.is_empty():
            raise IndexError("front from an empty queue")
        return self.front_node.value

    def is_empty(self):
        # VERIFICA SI ESTA VACIA
        return self.front_node is None

    def size(self):
        # DEVUELVE LOS ELEMENTOS DE LA COLA
        return self._size

class CustomerService:
    # CLASE QUE GESTIONA AL CLIENTE VIP
    def __init__(self):
        self.vip_queue = Queue()
        self.regular_queue = Queue()

    def add_customer(self, customer_name, customer_type="regular"):
        # AGREGA UN CLIENTE A DONDE CORRESPONDE.
        if customer_type.lower() == "vip":
            self.vip_queue.enqueue(customer_name)
            print(f"Cliente VIP agregado: {customer_name}")
        else:
            self.regular_queue.enqueue(customer_name)
            print(f"Cliente regular agregado: {customer_name}")

    def serve_customer(self):
        # ATIENDE AL CLIENTE SEGUN LA PRIORIDAD
        if not self.vip_queue.is_empty():
            customer = self.vip_queue.dequeue()
            print(f"Atendiendo cliente VIP: {customer}")
        elif not self.regular_queue.is_empty():
            customer = self.regular_queue.dequeue()
            print(f"Atendiendo cliente regular: {customer}")
        else:
            print("No hay clientes para atender.")

    def show_queues(self):
        # MUESTRA EL ESTADO DE LAS COLAS
        print()
        print("Clientes VIP:", end=" ")
        self._print_queue(self.vip_queue)
        print("Clientes regulares:", end=" ")
        self._print_queue(self.regular_queue)

    def _print_queue(self, queue):
        # IMPRIME ELEMENTOS
        current = queue.front_node
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print(elements)



if __name__ == "__main__":
    service = CustomerService()

    # AGREGAR CILENTES
    print()
    service.add_customer("Carlos", customer_type="regular")
    service.add_customer("Ana", customer_type="vip")
    service.add_customer("Luis", customer_type="regular")
    service.add_customer("María", customer_type="vip")

    # MUESTRA COLAS
    service.show_queues()

    # ATIENDE OS CLIENTES
    print()
    service.serve_customer()
    service.serve_customer()
    service.serve_customer()
    service.serve_customer()
    service.serve_customer()  # No debería haber más clientes

    # MUESTRA LAS COLAS DESPUES DE ATENDER
    service.show_queues()
