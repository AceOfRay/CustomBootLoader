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
        self.root.geometry("820x280")

        # set the theme
        self.root.tk.call("source", "C:\\Users\\rayra\\Projects\\CustomBootManager\\azure.tcl")
        self.root.tk.call("set_theme", "dark")

    def initialize_content(self):
        label = ttk.Label(self.root, text="Select Focus Mode", font=("Arial", 16))
        label.pack(pady=50)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=50)


        buttons = [
            ttk.Button(button_frame, text="Virtual Home Development", style='Accent.TButton', command=lambda : self.start_mode("virtual_home")),
            ttk.Button(button_frame, text="Chi-Epsilon Work", style='Accent.TButton', command= lambda : self.start_mode("chi_epsilon")),
            ttk.Button(button_frame, text="Note-Taking", style='Accent.TButton', command= lambda : self.start_mode("note_taking")),
            ttk.Button(button_frame, text="Ultimate Guitar", style='Accent.TButton', command= lambda : self.start_mode("guitar")),
            #ttk.Button(button_frame, text="Research", style='Accent.TButton', command= lambda : self.start_mode("research")),

        ]

        for button in buttons:
            button.pack(side=tk.LEFT, padx=30)


    def start_mode(self, mode : str):
        try:
            m : Modes.Mode = None
            match mode:
                case "virtual_home":
                    m = Modes.VirtualHome()
                case "research":
                    m = Modes.ResearchMode()
                case "chi_epsilon":
                    m = Modes.ChiEpsilonMode()
                case "note_taking":
                    m = Modes.NoteTakingMode()
                case "guitar":
                    m = Modes.GuitarMode()

            m.run()
        except Exception as e:
            print(e)
        finally:
            self.cleanup_process()

    def cleanup_process(self):
        self.root.destroy()
BootLoader()