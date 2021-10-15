from threading import Thread
from ttkbootstrap import Style
import matplotlib.pyplot as plt
# ----- TKINTER
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

usual_font = "Helvetica"


class Interface(tk.Tk, Thread):
    """
    Manages the interface of the program and attributes

    """

    def __init__(self):
        tk.Tk.__init__(self)
        Thread.__init__(self)

        # Window settings
        self.title("Compound Interest Calculator")
        self.geometry("500x400")
        #self.resizable(False, False)
        style = Style(theme='flatly')
        style.configure('custom.TFrame', foreground='blue',background='white')

        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=0, column=0, rowspan=3, pady=1, sticky="NSEW")
        self.main_frame_setup(self.main_frame)

    def main_frame_setup(self, frame):


        mf_label = ttk.Label(frame, text="Compound Interest Calculator", font=(usual_font, 18))
        mf_label.grid(row=0, column=0)

        # Initial Investment attributes
        self.initial_investment_input = tk.StringVar()
        initial_investment_label = ttk.Label(frame,text="Initial Investment", font=(usual_font, 14))
        initial_investment_desc = ttk.Label(frame,text="Amount of money that you wish to invest initially.", font=(usual_font, 12))
        self.initial_investment_entry = ttk.Entry(frame, width=10, textvariable=self.initial_investment_input)
        initial_investment_label.grid(row=1, column=0, sticky="W")
        initial_investment_desc.grid(row=2, column=0, sticky="W")
        self.initial_investment_entry.grid(row=1,column=1, rowspan=2, sticky="E")

        # Contribution attributes
        self.contribution_input = tk.StringVar()
        self.length_years_input = tk.StringVar()

        monthly_contribution_label = ttk.Label(frame,text="Monthly contribution", font=(usual_font, 14))
        monthly_contribution_desc = ttk.Label(frame, text="Amount of money that you wish to contribute monthly.", font=(usual_font, 12))
        self.monthly_contribution_entry = ttk.Entry(frame, width=10, textvariable=self.contribution_input)

        length_of_years_label = ttk.Label(frame, text="Length of time in years", font=(usual_font, 14))
        length_of_years_desc = ttk.Label(frame, text="The amount of years you plan to invest for", font=(usual_font, 12))
        self.length_years_entry = ttk.Entry(frame, width=10, textvariable=self.length_years_input)

        monthly_contribution_label.grid(row=3, column=0, sticky="W")
        monthly_contribution_desc.grid(row=4, column=0, sticky="W")
        self.monthly_contribution_entry.grid(row=3, column=1, rowspan=2, sticky="NE")

        length_of_years_label.grid(row=5, column=0, sticky="W")
        length_of_years_desc.grid(row=6, column=0, sticky="W")
        self.length_years_entry.grid(row=5, column=1, rowspan=2, sticky="NE")

        self.calculate_btn = ttk.Button(frame, text="Calculate")
        self.calculate_btn.grid(row=7, column=0, rowspan=2, sticky="E")
        self.reset_btn = ttk.Button(frame, text="Reset")
        self.reset_btn.grid(row=7, column=1, sticky="W")





root = Interface()
root.run()
root.mainloop()