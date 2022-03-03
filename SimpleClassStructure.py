import tkinter

class RootConfig:
    def __init__(self,root):
        self.root = root
        self.title = root.title("Tkinter-Class")
        self.config = root.configure(bg="black", )
        self.x = int(root.winfo_screenwidth() / 2 - (root.winfo_reqwidth() / 2))
        self.y = int(root.winfo_screenheight() / 3 - (root.winfo_reqheight() / 2))
        self.geometry = root.geometry(f"+{self.x}+{self.y}")

if __name__ == "__main__":
    root = tkinter.Tk()
    RootConfig(root)
    root.mainloop()
