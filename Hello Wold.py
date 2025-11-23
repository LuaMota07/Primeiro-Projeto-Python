import tkinter as tk

janela = tk.Tk()
janela.title ("Hello World")

janela.geometry ("300x150")

label = tk.Label(janela, text="Hello World", font=("Arial", 20))
label.pack(pady=40)

janela.mainloop()