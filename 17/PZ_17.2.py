"""
Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 2 - 9.
PZ 2
"""
import tkinter as tk


def convert_bytes():
    try:
        bytes_value = int(entry.get())
        kilobytes = bytes_value / 1024
        result_label.config(text=f'Результат в килобайтах: {kilobytes:.2f}', fg='black')
    except ValueError:
        result_label.config(text="Ошибка: введите целое число", fg='red')


root = tk.Tk()
root.title("PZ_17_2")
root.geometry("400x200")

label = tk.Label(root, text="Введите размер файла в байтах:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

convert_button = tk.Button(root, text="Конвертировать", command=convert_bytes)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Результат в килобайтах: ", fg='black')
result_label.pack(pady=10)

root.mainloop()
