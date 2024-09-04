def perdida_de_casa():
    """Simula la situación de perder la casa y tomar una decisión."""
    
    print("Haz perdido tu casa. Ya llega la noche. ¿Qué vas a hacer?")
    decision = input("Escribe 'llamar a mamá' para llamar a tu mamá, 'buscar refugio' para encontrar un lugar donde dormir, o 'quedarte en la calle': ")

    if decision.lower() == "llamar a mamá":
        print("Llamas a tu mamá. Ella te ofrece quedarte en su casa por la noche.")
    elif decision.lower() == "buscar refugio":
        print("Decides buscar un refugio. Encuentras un lugar seguro donde pasar la noche.")
    elif decision.lower() == "quedarte en la calle":
        print("Decides quedarte en la calle. La noche es fría y te sientes vulnerable.")
    else:
        print("No has tomado una decisión válida. Debes actuar rápido.")

# Llama a la función para ejecutar el código
perdida_de_casa()