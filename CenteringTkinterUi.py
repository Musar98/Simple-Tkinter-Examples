import tkinter

root = tkinter.Tk()
title = root.title("Centered Ui")
config = root.configure(bg="black", )
x = int(root.winfo_screenwidth() / 2 - (root.winfo_reqwidth() / 2))
#to get it right in the middle change the /3 to /2
#i prefer it a bit higher than the exact middle
y = int(root.winfo_screenheight() / 3 - (root.winfo_reqheight() / 2))
geometry = root.geometry(f"+{x}+{y}")

root.mainloop()
