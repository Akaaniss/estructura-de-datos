estudiantes = {}

for i in range(3):
    print(f"Ingresando información del estudiante {i+1}:")
    nombre = input("Nombre del estudiante: \n")
    asignatura = input("Nombre de la asignatura: \n")
    nota_lab1 = float(input("Nota del Laboratorio N°1: \n"))
    nota_lab2 = float(input("Nota del Laboratorio N°2: \n"))
    
    while True:
        nota_lab1 = float(input("Nota del Laboratorio N°1 (máximo 70): "))
        if nota_lab1 <= 70:
            break
        else:
            print("Error: La nota debe ser igual o menor a 70.")

    while True:
        nota_lab2 = float(input("Nota del Laboratorio N°2 (máximo 70): "))
        if nota_lab2 <= 70:
            break
        else:
            print("Error: La nota debe ser igual o menor a 70.")
            
    promedio = nota_lab1 * 0.3 + nota_lab2 * 0.7
    
    estudiantes[nombre] = {
        "Asignatura": asignatura,
        "Laboratorio N°1": nota_lab1,
        "Laboratorio N°2": nota_lab2,
        "Promedio final": round(promedio, 1)  
    }

print("Información de los estudiantes:\n")
for nombre, info in estudiantes.items():
    print(f"Nombre: {nombre}")
    for clave, valor in info.items():
        print(f"{clave}: {valor}")
    print()
