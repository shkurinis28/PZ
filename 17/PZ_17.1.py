"""
Вариант 31
В соответствии с номером варианта перейти по ссылке на прототии.
Реализовать ег в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу (см.таблицу 1)
"""

import tkinter as tk
from tkinter import ttk, messagebox

class RemotePCSettingsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Удаленная настройка ПК")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
      
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TEntry', font=('Arial', 10))
        self.style.configure('TCombobox', font=('Arial', 10))
        
     
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
     
        self.header = ttk.Label(self.main_frame, text="Удаленная настройка ПК", style='Header.TLabel')
        self.header.pack(pady=(0, 20))
        
      
        self.info_frame = ttk.Frame(self.main_frame)
        self.info_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.info_text = tk.Text(self.info_frame, height=8, wrap=tk.WORD, font=('Arial', 10), 
                                padx=10, pady=10, bg='white', bd=1, relief=tk.SOLID)
        self.info_text.pack(fill=tk.X)
        self.info_text.insert(tk.END, 
                            "Наша услуга 'Удаленная настройка ПК' позволяет профессионально настроить ваш компьютер "
                            "без необходимости выезда специалиста. Наши эксперты удаленно подключатся к вашему ПК, "
                            "проведут диагностику, оптимизируют систему, установят необходимое программное обеспечение "
                            "и настроят его для максимальной производительности.\n\n"
                            "Для заказа услуги заполните форму ниже и нажмите кнопку 'Заказать настройку'.")
        self.info_text.config(state=tk.DISABLED)
        
       
        self.form_frame = ttk.Frame(self.main_frame)
        self.form_frame.pack(fill=tk.X)
        
       
        self.create_form_field("Имя:", 0)
        self.create_form_field("Телефон:", 1)
        self.create_form_field("Email:", 2)
        self.create_form_field("Тип ОС:", 3, is_combobox=True, values=["Windows 10", "Windows 11", "Linux", "macOS"])
        self.create_form_field("Описание проблемы:", 4, is_textarea=True)
        
 
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.order_btn = ttk.Button(self.button_frame, text="Заказать настройку", command=self.place_order)
        self.order_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_btn = ttk.Button(self.button_frame, text="Очистить форму", command=self.clear_form)
        self.clear_btn.pack(side=tk.LEFT)
        
     
        self.status_bar = ttk.Label(self.main_frame, text="Готово к работе", relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(fill=tk.X, pady=(20, 0))
    
    def create_form_field(self, label_text, row, is_combobox=False, values=None, is_textarea=False):
        frame = ttk.Frame(self.form_frame)
        frame.pack(fill=tk.X, pady=5)
        
        label = ttk.Label(frame, text=label_text, width=15)
        label.pack(side=tk.LEFT)
        
        if is_textarea:
            entry = tk.Text(frame, height=4, wrap=tk.WORD, font=('Arial', 10), 
                          padx=5, pady=5, bd=1, relief=tk.SOLID)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            setattr(self, f"entry_{row}", entry)
        elif is_combobox:
            entry = ttk.Combobox(frame, values=values, font=('Arial', 10))
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            setattr(self, f"entry_{row}", entry)
        else:
            entry = ttk.Entry(frame, font=('Arial', 10))
            entry.
          pack(side=tk.LEFT, fill=tk.X, expand=True)
            setattr(self, f"entry_{row}", entry)
    
    def place_order(self):
        name = self.entry_0.get()
        phone = self.entry_1.get()
        email = self.entry_2.get()
        os_type = self.entry_3.get()
        problem = self.entry_4.get("1.0", tk.END).strip()
        
        if not all([name, phone, email, os_type, problem]):
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля формы")
            return
        
        messagebox.showinfo("Успех", "Ваш заказ на удаленную настройку ПК принят!\nНаш специалист свяжется с вами в ближайшее время.")
        self.status_bar.config(text="Заказ успешно отправлен")
    
    def clear_form(self):
        for i in range(5):
            entry = getattr(self, f"entry_{i}")
            if isinstance(entry, tk.Text):
                entry.delete("1.0", tk.END)
            else:
                entry.delete(0, tk.END)
        self.status_bar.config(text="Форма очищена")

if name == "__main__":
    root = tk.Tk()
    app = RemotePCSettingsApp(root)
    root.mainloop()
