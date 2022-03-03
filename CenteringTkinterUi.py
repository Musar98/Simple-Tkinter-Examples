import tkinter

root = tkinter.Tk()
title = root.title("FOI-Smart Money")
config = root.configure(bg="black", )
x = int(root.winfo_screenwidth() / 2 - (root.winfo_reqwidth() / 2))
y = int(root.winfo_screenheight() / 3 - (root.winfo_reqheight() / 2))
geometry = root.geometry(f"+{x}+{y}")



root.mainloop()