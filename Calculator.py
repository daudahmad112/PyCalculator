import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Calculator')
        self.master.geometry('600x600')
        self.master.resizable(False, False)

        # create the input field
        self.input_field = tk.Entry(master, width=30, font=('Arial', 16))
        self.input_field.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create the buttons
        self.create_button('1', 1, 0)
        self.create_button('2', 1, 1)
        self.create_button('3', 1, 2)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('7', 3, 0)
        self.create_button('8', 3, 1)
        self.create_button('9', 3, 2)
        self.create_button('0', 4, 1)
        self.create_button('.', 4, 2)
        self.create_button('C', 4, 0)
        self.create_button('/', 1, 3)
        self.create_button('*', 2, 3)
        self.create_button('-', 3, 3)
        self.create_button('+', 4, 3)
        self.create_button('=', 5, 3)
    

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)

    def button_click(self, text):
        if text == 'C':
            self.input_field.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(self.input_field.get())
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, result)
            except:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, 'Error')
        else:
            self.input_field.insert(tk.END, text)

# create the main window
root = tk.Tk()

# create the calculator
calc = Calculator(root)

# run the main loop
root.mainloop()
