import random

# desarrollador junior 
# desarrollador intermedio 
# desarrollador avanzado  
# arquitecto

#SOLO si se ganan mas de 6 millones se aplica retencion en la fuente del 10%

empleados = []
for _ in range(2000):
    id = random.choice([0,2000])
    nombre = random.choice(['Andres', 'Ana', 'Isabel', 'Pablo'])
    apellido = random.choice(['Moreno', 'Murillo', 'Alzate', 'Correa'])
    cargo = random.choice(['Arquitecto', 'Avanzado', 'Junior', 'Medio'])
    deuda = random.randint(500000, 800000)
    salario = random.randint(1160000, 18000000)
    retefuente = random.randint(1,2)
    correo = random.randint(2,3)
    telefono = random.randint(3,4)
    empleado = [id, nombre, apellido, cargo, deuda, salario, retefuente, correo, telefono]
    empleados.append(empleado)

