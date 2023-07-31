from datetime import datetime, time

class Cita:
    def __init__(self, paciente, fecha, hora, motivo):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo

class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horario_disponible = []
        self.citas_agendadas = []  # Lista para almacenar las citas agendadas

class Especialidad:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Paciente:
    def __init__(self, idPaciente, nombre, telefono, documento):
        self.idPaciente = idPaciente
        self.nombre = nombre
        self.telefono = telefono
        self.documento = documento

class Horario:
    def __init__(self, dia, hora, fecha):
        self.dia = dia
        self.hora = hora
        self.fecha = fecha

class Consultorio:
    def __init__(self, idConsultorio, nombre):
        self.idConsultorio = idConsultorio
        self.nombre = nombre

def mostrar_menu():
    print("---- Menú ----")
    print("1. Ingresar como doctor")
    print("2. Ingresar como paciente")
    print("3. Salir")

def consultar_citas_doctor(medico):
    print(f"Citas agendadas para el médico {medico.nombre} ({medico.especialidad}):")
    for cita in medico.citas_agendadas:
        print(f"Fecha: {cita.fecha}, Hora: {cita.hora}, Paciente: {cita.paciente.nombre}, Motivo: {cita.motivo}")

def verificar_horario_disponible(fecha_hora_str, horarios_disponibles):
    fecha_hora_paciente = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
    for horario in horarios_disponibles:
        fecha_hora_horario = datetime.combine(horario.fecha, time(*map(int, horario.hora.split(':'))))
        if fecha_hora_paciente == fecha_hora_horario:
            return True
    return False

def registrar_cita_paciente(paciente, medicos):
    print("---- Registro de cita ----")
    print("Especialidades disponibles:")
    for medico in medicos:
        print(medico.especialidad)

    especialidad = input("Ingrese la especialidad deseada: ")
    medico_disponible = None

    for medico in medicos:
        if medico.especialidad.nombre == especialidad:
            medico_disponible = medico
            break

    if not medico_disponible:
        print("Especialidad no encontrada.")
        return

    print("Horarios disponibles:")
    for horario in medico_disponible.horario_disponible:
        print(f"Día: {horario.dia}, Hora: {horario.hora}, Fecha: {horario.fecha}")

    fecha_hora_str = input("Ingrese la fecha y hora para la cita (formato: yyyy-mm-dd HH:MM): ")

    if not verificar_horario_disponible(fecha_hora_str, medico_disponible.horario_disponible):
        print("Horario no encontrado para la fecha y hora seleccionadas.")
        return

    fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
    motivo = input("Ingrese el motivo de la cita: ")
    cita = Cita(paciente, fecha_hora.date(), fecha_hora.time(), motivo)
    medico_disponible.citas_agendadas.append(cita)
    print("Cita registrada con éxito.")

def main():
    especialidad1 = Especialidad("Pediatra")
    especialidad2 = Especialidad("Dermatóloga")

    medico1 = Medico("Dr. Juan Perez", especialidad1)
    medico2 = Medico("Dra. Maria Garcia", especialidad2)

    horario1 = Horario("Lunes", "10:00", datetime(2023, 7, 24))
    horario2 = Horario("Miércoles", "15:00", datetime(2023, 7, 26))
    medico1.horario_disponible.extend([horario1, horario2])

    horario3 = Horario("Martes", "11:00", datetime(2023, 7, 25))
    horario4 = Horario("Viernes", "14:00", datetime(2023, 7, 28))
    medico2.horario_disponible.extend([horario3, horario4])

    paciente1 = Paciente(1, "Ana Martinez", "1234567890", "ABC123")
    paciente2 = Paciente(2, "Carlos Ramirez", "0987654321", "XYZ789")

    medicos = [medico1, medico2]

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            medico = None
            nombre_medico = input("Ingrese el nombre del médico: ")
            for m in medicos:
                if m.nombre == nombre_medico:
                    medico = m
                    break
            if medico:
                consultar_citas_doctor(medico)
            else:
                print("Médico no encontrado.")

        elif opcion == "2":
            paciente = None
            id_paciente = int(input("Ingrese su ID de paciente: "))
            for p in [paciente1, paciente2]:
                if p.idPaciente == id_paciente:
                    paciente = p
                    break
            if paciente:
                registrar_cita_paciente(paciente, medicos)
            else:
                print("Paciente no encontrado.")

        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

print(main())