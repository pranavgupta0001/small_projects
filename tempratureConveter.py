# %%
import tkinter as tk
from tkinter.constants import NSEW

window = tk.Tk()
window.title("Temprature Converter")
window.columnconfigure([0, 1], weight=1, minsize=120)
window.rowconfigure([0, 1, 2, 3, 4], weight=1, minsize=80)

inputText = tk.StringVar()
conversionIntoCelsius = True


def convert():
    #"\N{DEGREE SIGN}"
    output = ""

    try:
        temp = float(inputText.get())
        if conversionIntoCelsius:
            cTemp = (temp-32)*5/9
            output = "{:.2f} \N{DEGREE SIGN}C".format(cTemp)
        else:
            fTemp = (temp*9/5)+32
            output = "{:.2f} \N{DEGREE SIGN}F".format(fTemp)
    except:
        output = "Error: Input Valid Temparature"

    outputBox["text"] = output

# Reset everything


def reset():
    inputText.set("")
    outputBox["text"] = ""

# Reverse Button Function


def Reverse():
    global conversionIntoCelsius
    if conversionIntoCelsius:
        title["text"] = "Celsuis To Farenhite"
        ReverseButton["text"] = "Reverse F\N{RIGHTWARDS BLACK ARROW}C"
        conversionIntoCelsius = False
    else:
        title["text"] = "Farenhite to Celsuis"
        ReverseButton["text"] = "Reverse C\N{RIGHTWARDS BLACK ARROW}F"
        conversionIntoCelsius = True
    reset()

# exit the window


def exitLoop():
    window.destroy()


title = tk.Label(
    text="Farenhite to Celsuis",
    fg="white",
    bg="black"
)


# Input Box to enter temparture
inputBox = tk.Entry(width=22, textvariable=inputText)
outputBox = tk.Label(
    text=""
)


# Conwert Button
ConvertButton = tk.Button(
    text="Convert",
    command=convert
)
# reset Button
ResetButton = tk.Button(
    text="Reset",
    command=reset
)

# Reverse Button
ReverseButton = tk.Button(
    text="Reverse C-F",
    command=Reverse
)

# exit Button
exitButton = tk.Button(
    text="Exit",
    command=exitLoop
)


title.grid(row=0, column=0, sticky="nesw")
inputBox.grid(row=1, column=0, sticky="nesw")
inputBox.focus()
outputBox.grid(row=1, column=1, sticky="nesw")
ConvertButton.grid(row=2, column=0, sticky="nesw")
ResetButton.grid(row=3, column=1, sticky="nwse")
ReverseButton.grid(row=3, column=0, sticky="nesw")
exitButton.grid(row=4, column=0, sticky="snew")

window.mainloop()


# Start the script if its opened directly
if __name__ == '__main__':

    pass

"""



"""
