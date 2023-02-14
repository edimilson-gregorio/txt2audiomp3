import tkinter as tk
from tkinter import filedialog

def save_text():
    text = text_area.get("1.0", "end")
    with open("texto.txt", "w") as f:
        f.write(text)
    message_label.config(text="Texto salvo com sucesso")

def run_script():
    message_label.config(text="Convertendo o texto salvo... Aguarde...")
    # run the script here
    message_label.config(text="Seu arquivo foi convertido com sucesso")



root = tk.Tk()
root.title("TXT2MP3")

text_area = tk.Text(root, height=20, width=100)
text_area.pack(pady=50)

message_label = tk.Label(root, text="Insira o texto que vai ser convertido em MP3")
message_label.pack()

save_button = tk.Button(root, text="Salvar o texto", command=save_text)
save_button.pack()

run_button = tk.Button(root, text="Converter texto para mp3", command=run_script)
run_button.pack()

root.mainloop()
