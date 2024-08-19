import tkinter as tk
from tkinter import ttk
import Modes
import traceback

class BootLoader:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.initialize_frame()
        self.initialize_content()
        self.root.mainloop()

    def initialize_frame(self):
        # create the frame
        big_frame = ttk.Frame(self.root)
        big_frame.pack(fill="both", expand=True)

        # set the title and size of the window
        self.root.title("Select Focus Mode")
        self.root.geometry("920x480")

        # set the theme
        self.root.tk.call("source", "C:\\Users\\rayra\\Projects\\CustomBootManager\\azure.tcl")
        self.root.tk.call("set_theme", "dark")

    def initialize_content(self):
        label = ttk.Label(self.root, text="Select Focus Mode", font=("Arial", 16))
        label.pack()

        button_frame = ttk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ttk.Button(button_frame, text="Research Mode", style='Accent.TButton', command=lambda : self.start_mode("research")),
            ttk.Button(button_frame, text="Chi-Epsilon Work Mode", style='Accent.TButton', command= lambda : self.start_mode("chi_epsilon")),
            ttk.Button(button_frame, text="Note-Taking Mode", style='Accent.TButton', command= lambda : self.start_mode("note_taking")),
        ]

        for button in buttons:
            button.pack(side=tk.LEFT, padx=5)


    def start_mode(self, mode : str):
        try:
            m : Modes.Mode = None
            match mode:
                case "research":
                    m = Modes.ResearchMode()
                case "chi_epsilon":
                    m = Modes.ChiEpsilonMode()
                case "note_taking":
                    m = Modes.NoteTakingMode()

            m.run()
        except Exception as e:
            print(e)
        finally:
            self.cleanup_process()

    def cleanup_process(self):
        self.root.destroy()
BootLoader()