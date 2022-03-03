import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title = parent.title("Tkinter-Class-With-Frame")
        self.config = parent.configure(bg="black", )
        self.x = int(parent.winfo_screenwidth() / 2 - (parent.winfo_reqwidth() / 2))
        self.y = int(parent.winfo_screenheight() / 3 - (parent.winfo_reqheight() / 2))
        self.geometry = parent.geometry(f"+{self.x}+{self.y}")

        #<create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root)
    root.mainloop()