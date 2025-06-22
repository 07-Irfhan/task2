import tkinter as tk
from tkinter import messagebox
def calculate_bmi():
    try:
        height=float(entry_height.get())
        weight=float(entry_weight.get())
        bmi=weight/(height ** 2)
        label_result.config(text=("Your BMI is:",bmi))    
    except ValueError:
        messagebox.showerror("Invalid Input")
    
root=tk.Tk()
root.title("BMI Calculator")

tk.Label(root,text="Height(m):").grid(row=0,column=0,pady=5,padx=5,sticky='e')
entry_height=tk.Entry(root)
entry_height.grid(row=0,column=1,pady=5)

tk.Label(root,text="Weight(kg):").grid(row=1,column=0,pady=5,padx=5,sticky='e')
entry_weight=tk.Entry(root)
entry_weight.grid(row=1,column=1,pady=5)

tk.Button(root,text="Calculate BMI",command=calculate_bmi).grid(row=2,column=0,columnspan=2,pady=10)

label_result=tk.Label(root,text="",fg="blue")
label_result.grid(row=3,column=0,columnspan=2)
root.mainloop()
