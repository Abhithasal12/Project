# creating calculater 
# tkinter is a python library that allows you to create a graphical user interface (GUIs).
import tkinter as tk
import re


calculation = "" 
#addition(+,-,/,*,%)
def add_to_calculation(symbol):
    global calculation
    if symbol =="%":
        calculation += "%"
    else:
        calculation += str(symbol)

    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#Equal result (=)
def evaluate_calculation():
    global calculation
    try:
        # Convert percentages properly 
        calculation_with_percent = re.sub(
            r"(\d+(\.\d+)?)%", r"(\1/100)", calculation
        )

        # Handle cases like `183-15%` -> `183 - (183 × 15 / 100)`
        calculation_with_percent = re.sub(
            r"(\d+(\.\d+)?)\s*[-+*/]\s*\((\d+(\.\d+)?)/100\)",
            lambda m: f"({m.group(1)} {m.group(0)[len(m.group(1))]} ({m.group(1)} * {m.group(3)}/100))",
            calculation_with_percent
        )

        result = str(eval(calculation_with_percent))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)

    except Exception as e:
        clear_filed()
        text_result.insert(1.0, "Error")
        print(f"Error: {e}")

#clear button
def clear_filed():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Delete button 
def delete_filed():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)  


root = tk.Tk()
root.geometry("300x325")
root.title("calculator")

text_result = tk.Text(root, height=2, width=16, font=("Arial",24),background="Gray")
text_result.grid(columnspan=5)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font= ("arial",14),background="yellow")
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font= ("arial",14),background="yellow")
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font= ("arial",14),background="yellow")
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font= ("arial",14),background="yellow")
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font= ("arial",14),background="yellow")
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font= ("arial",14),background="yellow")
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font= ("arial",14),background="yellow")
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font= ("arial",14),background="yellow")
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font= ("arial",14),background="yellow")
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font= ("arial",14),background="yellow")
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font= ("arial",14),background="yellow")
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font= ("arial",14),background="yellow")
btn_minus.grid(row=3, column=4)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font= ("arial",14),background="yellow")
btn_mul.grid(row=4, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font= ("arial",14),background="yellow")
btn_div.grid(row=5, column=4)

btn_dot = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font= ("arial",14),background="yellow")
btn_dot.grid(row=5, column=3)

btn_zero = tk.Button(root, text="00", command=lambda: add_to_calculation("00"), width=5, font= ("arial",14),background="yellow")
btn_zero.grid(row=5, column=1)

btn_percent = tk.Button(root, text="%", command=lambda: add_to_calculation("%"), width=5, font= ("arial",14),background="yellow")
btn_percent.grid(row=6, column=1)

# This three button have spacific reasons 
btn_delete = tk.Button(root, text="DEL", command=delete_filed, width=11, font= ("arial",14),background="orange")
btn_delete.grid(row=6, column=3, columnspan=2) 

btn_clear = tk.Button(root, text="C", command=clear_filed , width=11, font= ("arial",14),background="orange")
btn_clear.grid(row=7, column=1, columnspan=2)

btn_eual = tk.Button(root, text="=", command=evaluate_calculation, width=11, font= ("arial",14),background="orange")
btn_eual.grid(row=7, column=3, columnspan=2)


root.mainloop()