import random
import tkinter as tk

def lanzar_dado():
    return random.randint(1, 6)

def jugar():
    oportunidades = 3
    resultado_total = 0
    resultado_text.set("")

    for i in range(oportunidades):
        resultado = lanzar_dado()
        resultado_total += resultado
        resultado_text.set(f"Lanzamiento {i + 1}: Has obtenido un {resultado}\n")
        ventana.update()
        ventana.after(1000)

    resultado_text.set(f"Resultado total: {resultado_total}\n")
    if resultado_total > 10:
        resultado_text.set(resultado_text.get() + "¡Felicidades! Ganaste.")
    else:
        resultado_text.set(resultado_text.get() + "Lo siento, no ganaste. ¡Mejor suerte la próxima!")

ventana = tk.Tk()
ventana.title("Juego de Dados")

titulo = tk.Label(ventana, text="¡Bienvenido al juego de azar de dados!")
titulo.pack()

boton = tk.Button(ventana, text="Lanzar Dados", command=jugar)
boton.pack()

resultado_text = tk.StringVar()
resultado_label = tk.Label(ventana, textvariable=resultado_text)
resultado_label.pack()

ventana.mainloop()
