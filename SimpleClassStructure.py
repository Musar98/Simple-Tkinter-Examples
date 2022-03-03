import tkinter

class RootConfig:
    def __init__(self,root):
        self.root = root
        self.title = self.root.title("Tkinter-Class")
        self.config = self.root.configure(bg="black", )
        self.x = int(self.root.winfo_screenwidth() / 2 - (self.root.winfo_reqwidth() / 2))
        self.y = int(self.root.winfo_screenheight() / 3 - (self.root.winfo_reqheight() / 2))
        self.geometry = self.root.geometry(f"+{self.x}+{self.y}")

if __name__ == "__main__":
    root = tkinter.Tk()
    RootConfig(root)
    root.mainloop()