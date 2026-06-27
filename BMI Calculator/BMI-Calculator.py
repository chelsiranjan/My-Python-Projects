import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('BMI Calculator')
window.geometry('350x400')
window.resizable(False, False)
window.configure(bg='#f0f4f8')

heading = tk.Label(window,text='⚖ BMI Calculator',font=('Helvetica', 18, 'bold'),bg='#f0f4f8',fg='#2d3748')
heading.pack(pady=20)

height_label = tk.Label(window,text='Enter your Height (in feet):',font=('Helvetica', 11),bg='#f0f4f8',fg='#4a5568')
height_label.pack(pady=(10, 2))

height_var = tk.StringVar()

height_entry = tk.Entry(window,textvariable=height_var,font=('Helvetica', 13),width=15,justify='center',relief='flat',bg='white',fg='#2d3748')
height_entry.pack(ipady=6)

weight_label = tk.Label(window,text='Enter your Weight (in kg):',font=('Helvetica', 11),bg='#f0f4f8',fg='#4a5568')
weight_label.pack(pady=(16, 2))

weight_var = tk.StringVar()

weight_entry = tk.Entry(window,textvariable=weight_var,font=('Helvetica', 13),width=15,justify='center',relief='flat',bg='white',fg='#2d3748')
weight_entry.pack(ipady=6)


def calculate_bmi():
    height_text = height_var.get()
    weight_text = weight_var.get()

    if height_text == '' or weight_text == '':
        messagebox.showerror('Missing Input','Please fill in both Height and Weight.')
        return

    try:
        height_feet = float(height_text)
        weight_kg = float(weight_text)
    except ValueError:
        messagebox.showerror('Invalid Input','Please enter numbers only (e.g. 5.8, 65).')
        return

    if height_feet <= 0 or weight_kg <= 0:
        messagebox.showerror('Invalid Input','Height and Weight must be greater than 0.')
        return

    ht_m = height_feet * 0.3048
    bmi = weight_kg / (ht_m ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = 'Underweight'
        colour = '#5fadda'
    elif bmi < 25:
        category = 'Normal weight'
        colour = '#3dbd6c'
    elif bmi < 30:
        category = 'Overweight'
        colour = '#f8b365'
    else:
        category = 'Obese'
        colour = '#c94040'

    result_value_label.config(text=f'Your BMI: {bmi}',fg=colour)

    result_category_label.config(text=category,fg=colour)


calc_button = tk.Button(window,text='Calculate',font=('Helvetica', 12, 'bold'),bg='#3b82f6',fg='white',activebackground='#2563eb',activeforeground='white',relief='flat',padx=20,pady=6,command=calculate_bmi)
calc_button.pack(pady=24)

result_value_label = tk.Label(window,text='',font=('Helvetica', 12, 'bold'),bg='#f0f4f8')
result_value_label.pack()

result_category_label = tk.Label(window,text='',font=('Helvetica', 12, 'bold'),bg='#f0f4f8')
result_category_label.pack()

window.mainloop()