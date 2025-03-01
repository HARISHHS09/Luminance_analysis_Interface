from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
import random

def generate_random_data():
    used_values = set()  # Set to keep track of used values
    matrix_data = []

    for _ in range(10):
        row = []
        for _ in range(10):
            unique_value = random.randint(1, 1000)
            while unique_value in used_values:
                unique_value = random.randint(1, 1000)
            row.append(unique_value)
            used_values.add(unique_value)
        matrix_data.append(row)

    return matrix_data

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI")
        self.root.geometry("1200x500")
        image_path = "ADVIpng1.png"
        self.pho = PhotoImage(file=image_path)
        photo = PhotoImage(file='ADVIpng1.png')
        self.root.iconphoto(True, photo)
        self.root.config(background="#002B4D")

        title_label = Label(root, text="Luminance Analysis Interface",
                            font=('Calibri', 30),
                            background="#002B4D",
                            fg="white",
                            image=self.pho,
                            compound='left',
                            padx=15,
                            pady=15)
        title_label.pack(anchor="nw")
        des_label=Label(root,text="It analyzes the intensity of light emitted from a surface",font=('Calibri', 15),
                            background="#002B4D",
                            fg="white",)
        des_label.place(x=180,y=130)
        matrix_label = tk.Label(root,
                                text="MATRIX",
                                font=('Calibri', 30),
                                background="#002B4D",
                                fg="white")
        matrix_label.place(x=1000,y=140)

        self.matrix_app = MatrixAppWidget(root)

        self.timer_running = False

        def start_timer():
            self.timer_running = True
            countdown(10)

        def stop_timer():
            self.timer_running = False
            label.config(text="Timer Stopped")

        def countdown(seconds):
            if self.timer_running:
                label.config(text=f"Time Left: {seconds}s")
                if seconds > 0:
                    root.after(1000, countdown, seconds - 1)
                else:
                    self.matrix_app.generate_new_matrix()
                    countdown(10)

        start_button = tk.Button(root,
                                 text="Start Timer",
                                 font=('Calibri', 15),
                                 command=start_timer,
                                 bg="blue",
                                 fg="white",
                                 activebackground="blue",
                                 activeforeground="white")
        start_button.place(x=850, y=680)

        stop_button = tk.Button(root,
                                text="Stop Timer",
                                font=('Calibri', 15),
                                command=stop_timer,
                                bg="red",
                                fg="white",
                                activebackground="red",
                                activeforeground="white")
        stop_button.place(x=970, y=680)

        label = tk.Label(root, text="", bg="#002B4D", fg="white")
        label.place(x=980, y=650)

class MatrixAppWidget:
    def __init__(self, root):
        self.root = root
        self.matrix_data = generate_random_data()

        self.table = tk.Frame(root, bg="white")
        self.table.place(x=850, y=200)
        self.side_frame = tk.Frame(root, bg="skyblue", width=400, height=800)
        self.side_frame.place(x=1300, y=0)
        self.label_max_value = tk.Label(self.side_frame, text="Max Value", font=('Calibri', 15), bg="skyblue")
        self.label_max_value.place(x=70, y=50)
        self.entry_max_value_var = tk.StringVar()
        self.entry_max_value = tk.Entry(self.side_frame, textvariable=self.entry_max_value_var, font=('Calibri', 15), justify='center')
        self.entry_max_value.place(x=20, y=80)

        self.label_location = tk.Label(self.side_frame, text="Location", font=('Calibri', 15), bg="skyblue")
        self.label_location.place(x=80, y=130)
        self.label_row = tk.Label(self.side_frame, text="Row", font=('Calibri', 15), bg="skyblue")
        self.label_row.place(x=20, y=170)
        self.entry_row_var = tk.StringVar()
        self.entry_row = tk.Entry(self.side_frame, textvariable=self.entry_row_var, font=('Calibri', 15), justify='center')
        self.entry_row.place(x=20, y=200)
        self.label_column = tk.Label(self.side_frame, text="Column", font=('Calibri', 15), bg="skyblue")
        self.label_column.place(x=20, y=230)
        self.entry_column_var = tk.StringVar()
        self.entry_column = tk.Entry(self.side_frame, textvariable=self.entry_column_var, font=('Calibri', 15), justify='center')
        self.entry_column.place(x=20, y=260)
        self.update_table()

    def update_table(self):
        max_value = max(max(row) for row in self.matrix_data)
        max_value_location = [(i, row.index(max_value)) for i, row in enumerate(self.matrix_data) if max_value in row]
        row, column = max_value_location[0]

        # Update the entry boxes
        self.entry_max_value_var.set(max_value)
        self.entry_row_var.set(row+1)
        self.entry_column_var.set(column+1)

        # Display the matrix in the table
        for i in range(10):
            for j in range(10):
                cell_value = self.matrix_data[i][j]
                cell_label = tk.Label(self.table, text=str(cell_value), width=5, height=2, font=("Calibri", 10),
                                      relief="solid")
                cell_label.grid(row=i, column=j, padx=1, pady=1)
                if cell_value == max_value:
                    cell_label.config(bg="blue", fg="white")
                else:
                    cell_label.config(bg="darkred", fg="white")

    def generate_new_matrix(self):
        self.matrix_data = generate_random_data()
        self.update_table()


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()
