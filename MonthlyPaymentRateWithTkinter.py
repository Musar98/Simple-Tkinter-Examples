import tkinter as tk

root = tk.Tk()

def calculateCostPerMonth():
    totalCost = inputTotalCost.get()
    totalTime = inputTotalTime.get()
    if len(totalCost) == 0:
        result = "Please enter the total cost"
    elif len(totalTime) == 0:
        result = "Please enter the total time"
    else:
        result = f"The monthly payment is: {round(float(totalCost)/float(totalTime),2)}"
    
    resultLabel = tk.Label(root,text=f"{result}")
    
    return resultLabel.place(relx=0.5,rely=0.82,anchor="center")


labelTotalCost = tk.Label(root,text="Enter total cost: ")
inputTotalCost = tk.Entry(root,name="inputTotalCost")
labelTotalTime = tk.Label(root,text="Enter payment duration: \n (in months) ")
inputTotalTime = tk.Entry(root,name="inputTotalName")
submitButton = tk.Button(root,name="submitCostTime",text="Submit",command=calculateCostPerMonth)


placementLabelTotalCost = labelTotalCost.place(relx=0.18,rely=0.1)
placementInputTotalCost = inputTotalCost.place(relx=0.20,rely=0.2)
placementLabelTotalTime = labelTotalTime.place(relx=0.18,rely=0.3)
placementInputTotalTime = inputTotalTime.place(relx=0.20,rely=0.5)
placementSubmitButton = submitButton.place(relx=0.5,rely=0.7,anchor="center")


root.mainloop()