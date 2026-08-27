import tkinter as tk

calculation = ""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except Exception:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title("XGalculator")
root.geometry("371x290")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

text_result = tk.Text(root, height=2, width=20, font=("Arial", 24, "bold"))
text_result.grid(columnspan=5, sticky="nsew")

buttonframe = tk.Frame(root)
for column in range(4):
    buttonframe.columnconfigure(column, weight=1)
for row in range(5):
    buttonframe.rowconfigure(row, weight=1)


btn_1 = tk.Button(buttonframe, text="1", font=("Arial", 18, "bold"), command=lambda: add_calculation(1), width=5)
btn_1.grid(row=0, column=0, sticky="nsew")

btn_2 = tk.Button(buttonframe, text="2", font=("Arial", 18, "bold"), command=lambda: add_calculation(2), width=5)
btn_2.grid(row=0, column=1, sticky="nsew")

btn_3 = tk.Button(buttonframe, text="3", font=("Arial", 18, "bold"), command=lambda: add_calculation(3), width=5)
btn_3.grid(row=0, column=2, sticky="nsew")

btn_4 = tk.Button(buttonframe, text="4", font=("Arial", 18, "bold"), command=lambda: add_calculation(4), width=5)
btn_4.grid(row=1, column=0, sticky="nsew")

btn_5 = tk.Button(buttonframe, text="5", font=("Arial", 18, "bold"), command=lambda: add_calculation(5), width=5)
btn_5.grid(row=1, column=1, sticky="nsew")

btn_6 = tk.Button(buttonframe, text="6", font=("Arial", 18, "bold"), command=lambda: add_calculation(6), width=5)
btn_6.grid(row=1, column=2, sticky="nsew")

btn_7 = tk.Button(buttonframe, text="7", font=("Arial", 18, "bold"), command=lambda: add_calculation(7), width=5)
btn_7.grid(row=2, column=0, sticky="nsew")

btn_8 = tk.Button(buttonframe, text="8", font=("Arial", 18, "bold"), command=lambda: add_calculation(8), width=5)
btn_8.grid(row=2, column=1, sticky="nsew")

btn_9 = tk.Button(buttonframe, text="9", font=("Arial", 18, "bold"), command=lambda: add_calculation(9), width=5)
btn_9.grid(row=2, column=2, sticky="nsew")

btn_0 = tk.Button(buttonframe, text="0", font=("Arial", 18, "bold"), command=lambda: add_calculation(0), width=5)
btn_0.grid(row=3, column=0, sticky="nsew")

btn_plus = tk.Button(buttonframe, text="+", font=("Arial", 18, "bold"), command=lambda: add_calculation("+"), width=5)
btn_plus.grid(row=0, column=3, sticky="nsew")

btn_minus = tk.Button(buttonframe, text="-", font=("Arial", 18, "bold"), command=lambda: add_calculation("-"), width=5)
btn_minus.grid(row=1, column=3, sticky="nsew")

btn_x = tk.Button(buttonframe, text="*", font=("Arial", 18, "bold"), command=lambda: add_calculation("*"), width=5)
btn_x.grid(row=2, column=3, sticky="nsew")

btn_divide = tk.Button(buttonframe, text="/", font=("Arial", 18, "bold"), command=lambda: add_calculation("/"), width=5)
btn_divide.grid(row=3, column=3, sticky="nsew")

btn_open = tk.Button(buttonframe, text="(", font=("Arial", 18, "bold"), command=lambda: add_calculation("("), width=5)
btn_open.grid(row=3, column=1, sticky="nsew")

btn_close = tk.Button(buttonframe, text=")", font=("Arial", 18, "bold"), command=lambda: add_calculation(")"), width=5)
btn_close.grid(row=3, column=2, sticky="nsew")

btn_equal = tk.Button(buttonframe, text="=", font=("Arial", 18, "bold"), command=evaluate_calculation, width=12)
btn_equal.grid(row=4, column=0, columnspan=2, sticky="nsew")

btn_clear = tk.Button(buttonframe, text="C", font=("Arial", 18, "bold"), command=clear_field, width=12)
btn_clear.grid(row=4, column=2, columnspan=2, sticky="nsew")

buttonframe.grid(
    row=1,
    column=0,
    sticky="nsew"
)


root.mainloop()
