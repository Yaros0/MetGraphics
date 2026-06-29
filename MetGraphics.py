import tkinter as tk
import matplotlib.pyplot as plt
from numpy import *
from matplotlib.ticker import LinearLocator, MultipleLocator
import Parser

def get_dots(func: str, max, dot_num):
    """Функция для получения точек графика по функции, нужно задать макс значение и точность"""
    x_cords = linspace(-max, max, dot_num)
    y_cords = linspace(0,0, dot_num)
    for i in range(x_cords.size):
        calculator.user_expr = func.replace("x", str(x_cords[i]))
        calculator.simplify_user_expr()
        y_cords[i] = calculator.calculate_user_expr(False)
    return x_cords, y_cords

def plot_function():
    """Функция для получения ввода и построения графика по нему"""
    global gr1
    func_str = entry.get()
    try:
        x, y = get_dots(func_str, 20, 10000)
        gr1.set_data(x, y)
        errlabel.config(text="valid function", fg="#ffffff")
        plt.draw()
    except:
        errlabel.config(text="invalid function!", fg="#ff5555")


# Окно для редактирования функций
optwind = tk.Tk()
optwind.title("Функции")
optwind.geometry("400x300")
optwind.resizable(False, False)
optwind.configure(background="#222")
#Поле ввода функций
entry = tk.Entry(optwind, width=30, font=('Sans', 15), background="#222", fg="#ffffff", insertbackground="#ffffff")
entry.pack(pady=10)
entry.size()
#Сообщение о (не)валидности функции
errlabel = tk.Label(optwind, width=20, font=('Sans', 10))
errlabel.config(text="your function is empty", background="#222", fg="#ffffff")
errlabel.pack(pady=10)
#Кнопка построения
btn = tk.Button(optwind, text="Apply", command=plot_function, bg="#444", fg="white", font=('Sans', 10))
btn.pack(pady=5)
#Показатель версии
show_vers = tk.Label(optwind, width=10, font=('Sans', 10))
show_vers.config(text="v-0.05", background="#222", fg="#ffffff")
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
calculator = Parser.Parser("")

plt.show()
optwind.mainloop()