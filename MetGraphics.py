import tkinter as tk
import matplotlib.pyplot as plt
from numpy import *
from matplotlib.ticker import LinearLocator, MultipleLocator

def get_dots(func, max, dot_num):
    """Функция для получения точек графика по функции, нужно задать макс значение и точность"""
    x_cords = linspace(-max, max, dot_num)
    y_cords = func(x_cords)
    return x_cords, y_cords

def plot_function():
    """Функция для получения ввода и построения графика по нему"""
    global gr1
    func_str = entry.get()
    try:
        if check_chars(func_str) or allow_danger.get():
            user_func = lambda x: eval(func_str)
            x, y = get_dots(user_func, 20, 100000)
            gr1.set_data(x, y)
            errlabel.config(text="valid function", fg="#ffffff")
            plt.draw()
        else:
            errlabel.config(text="DANGER FUNCTION!", fg="#ffa500")
    except:
        errlabel.config(text="invalid function!", fg="#ff5555")

def check_chars(string):
    """Функция для проверки разрешенных символов"""
    for char in string:
        if char not in ",. x+-*/1234567890":
            return False
    return True

# Окно для редактирования функций
optwind = tk.Tk()
optwind.title("Функции")
optwind.geometry("400x300")
optwind.resizable(False, False)
optwind.configure(background="#222")
entry = tk.Entry(optwind, width=30, font=('Sans', 15))
entry.configure(background="#222", fg="#ffffff", insertbackground="#ffffff")
entry.pack(pady=10)
entry.size()
allow_danger = tk.BooleanVar()
switch_danger = tk.Checkbutton(optwind, text="Danger functions", variable=allow_danger)
switch_danger.configure(background="#222", fg="#ffffff", activebackground="#222", selectcolor="#222", activeforeground="#ffffff")
switch_danger.place(relx=0.15, rely=0.9, anchor="center")
errlabel = tk.Label(optwind, width=20, font=('Sans', 10))
errlabel.config(text="your function is empty", background="#222", fg="#ffffff")
errlabel.pack(pady=10)
btn = tk.Button(optwind, text="Применить", command=plot_function, bg="#444", fg="white", font=('Sans', 10))
btn.pack(pady=5)
show_vers = tk.Label(optwind, width=10, font=('Sans', 10))
show_vers.config(text="test-v0.04", background="#222", fg="#ffffff")
show_vers.place(relx=0.90, rely=0.9, anchor="center")

# Окно отображения функций
graph_wind = plt.figure(figsize = (8, 5))
ax = graph_wind.add_subplot(1, 1, 1);
ax.set_aspect('equal')
ax.set_ylim(-20, 20)
ax.set_xlim(-20, 20)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.axhline(0, color='black', lw=1.5)
ax.axvline(0, color='black', lw=1.5)
gr1, = ax.plot([],[], ls = ' ', marker = 'o', ms = 0.06);
plt.grid(True)

plt.show()
optwind.mainloop()
