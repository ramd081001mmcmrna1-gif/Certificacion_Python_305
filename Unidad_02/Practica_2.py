dias_permitidos = ("lunes", "miercoles", "viernes")

print("Dias de atención para prestamos:")
for indice, dia in enumerate(dias_permitidos):
    print(f"[{indice}] {dia}")

dia_solicitado = input("\nIngresa el dia en que deseas solicitar el préstamo: ").strip().lower()

if dia_solicitado in dias_permitidos:
    print(f"Solicitud permitida: se atiende los {dia_solicitado}.")
else:
    print("No hay atención ese dia.") 