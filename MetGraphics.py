#import matplotlib
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, MultipleLocator

# Функция для получения точек графика по функции, нужно задать макс значение и точность
def get_dots(func, max, dot_num):
    x_cords = np.linspace(-max, max, dot_num)
    y_cords = func(x_cords)
    return x_cords, y_cords

# Функция для получения ввода и построения графика по нему
def plot_function():
    global gr1
    func_str = entry.get()
    try:
        user_func = lambda x: eval(func_str)
        x, y = get_dots(user_func, 20, 100000)
        gr1.set_data(x, y)
        errlabel.config(text="valid function", fg="#ffffff")
        plt.draw()
    except:
        errlabel.config(text="invalid function!", fg="#ff5555")

# Окно для редактирования функций
optwind = tk.Tk()
optwind.title("Функции")
optwind.geometry("300x300")
optwind.resizable(False, False)
optwind.configure(background="#222")
entry = tk.Entry(optwind, width=20, font=('Sans', 15))
entry.configure(background="#222", fg="#ffffff", insertbackground="#ffffff")
entry.pack(pady=10)
entry.size()
errlabel = tk.Label(optwind, width=20, font=('Sans', 10))
errlabel.config(text="your function is empty", background="#222", fg="#ffffff")
errlabel.pack(pady=10)
btn = tk.Button(optwind, text="Применить", command=plot_function, bg="#444", fg="white", font=('Sans', 10))
btn.pack(pady=5)


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