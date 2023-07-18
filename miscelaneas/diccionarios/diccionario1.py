empleados = {
    "id_001": {
        "nombre": "Juan Perez",
        "puesto": "Analista de Datos",
        "edad": 30,
        "salario": 45000.00
    },
    "id_002": {
        "nombre": "María Lopez",
        "puesto": "Ingeniera de Software",
        "edad": 28,
        "salario": 55000.00
    },
    "id_003": {
        "nombre": "Carlos Ramirez",
        "puesto": "Diseñador Gráfico",
        "edad": 25,
        "salario": 38000.00
    }
}

# Paso 2: Acceder y mostrar información de un empleado específico
id_empleado = "id_002"
if id_empleado in empleados:
    empleado = empleados[id_empleado]
    print("Información del empleado con ID", id_empleado)
    print("Nombre:", empleado["nombre"])
    print("Puesto:", empleado["puesto"])
    print("Edad:", empleado["edad"])
    print("Salario:", empleado["salario"])
else:
    print("Empleado con ID", id_empleado, "no encontrado.")