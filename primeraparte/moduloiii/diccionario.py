alumnos = {123: "Juan", 456: "Sofia", 789: "Pablo"}

print(alumnos[123])
print(alumnos[456])

del alumnos[456]
print(alumnos)

alumnos[321] = "Mariano"
print(alumnos)

print(len(alumnos))

alumno = {
    "nombre": "Juan",
    "dni": 1234,
    "cursos_actuales": ["Phyton", "Java", "PHP"],
    "cursos_previos": 2
}

print(alumno["cursos_previos"])
print(alumno["cursos_actuales"][-1])