import tkinter as tk
import subprocess

def handle_click(event):
    if username_entry.get() == "":
        username_entry.insert(0, 0)
    if username_entry1.get() == "":
        username_entry1.insert(0, 0)
    if username_entry2.get() == "":
        username_entry2.insert(0, 0)

    time = int(username_entry.get()) * 3600 + int(username_entry1.get()) * 60 + int(username_entry2.get())

    subprocess.call(["shutdown", "-s", "-t", str(time)], shell = True)

def quitar_apagado(event):
    subprocess.call(["shutdown", "-a"], shell = True)

if __name__ == '__main__':
    window = tk.Tk()
    window.geometry("300x200")
    window.title('Programado automático')

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    a = tk.Label(window, text="Programación de apagado")
    a.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

    username_label = tk.Label(window, text="Horas:")
    username_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

    username_entry = tk.Entry(window)
    username_entry.insert(0, 1)
    username_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)


    username_label1 = tk.Label(window, text="Minutos:")
    username_label1.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

    username_entry1 = tk.Entry(window)
    username_entry1.insert(0, 0)
    username_entry1.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)


    username_label2 = tk.Label(window, text="Segundos:")
    username_label2.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

    username_entry2 = tk.Entry(window)
    username_entry2.insert(0, 0)
    username_entry2.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

    button = tk.Button(text="Programar apagado")
    button.bind("<Button-1>", handle_click)
    button.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)

    button2 = tk.Button(text="Cancelar apagado automático")
    button2.bind("<Button-1>", quitar_apagado)
    button2.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)


    window.mainloop()

