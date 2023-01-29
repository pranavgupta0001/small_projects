

import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import base64

window = tk.Tk()

private_key = tk.StringVar(window, name = "str")
Result = tk.StringVar()


#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def encode_mode():
   
    codedText = Encode(private_key.get(), txt_editor.get("1.0", tk.END))
    txt_editor.delete("1.0", tk.END)
    txt_editor.insert(tk.END, codedText)
    Result.set("Text Encoded Successfully")
   

def decode_mode():
    
    codedText = Decode(private_key.get(), txt_editor.get("1.0", tk.END))
    txt_editor.delete("1.0", tk.END)
    txt_editor.insert(tk.END, codedText)
    Result.set("Text Decoded Successfully")

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_editor.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_editor.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    """Save the current file as a new file."""
    messagebox.showwarning("Encode","Don't forget to encode the file before saving.")
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_editor.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


def exitLoop():
    window.destroy()

def messageForCoding():
    messagebox.askquestion("eueu", "aoeuu")

#######################################################################



window.title("Text Editor")
window.columnconfigure(0, weight=1, minsize=800)
window.rowconfigure(0, minsize=800, weight=1)

#creates tabs
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text= "Notepad")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text= "Coder")


#create menu 
menu = tk.Menu(window)

#create file folder
file_folder = tk.Menu(menu, tearoff=0)

file_folder.add_command(label="Open", command=open_file)

file_folder.add_command(label="Save As", command=save_file)

file_folder.add_separator()

file_folder.add_command(label="Close", command=exitLoop)

#add file folder to menu
menu.add_cascade(label="File", menu=file_folder)

#add menu to window
window.config(menu=menu)


fr_buttons = tk.Frame(master=window, width=100)

btn_encode = tk.Button(
    text="Encode",
    master=tab2,
    command=encode_mode
)

btn_decode = tk.Button(
    text="Decode",
    master=tab2,
    command=decode_mode
)


txt_editor = tk.Text(tab1)

#key
tk.Label(tab2, font = 'arial 12 bold', text ='KEY').grid(row=1, column=0)
tk.Entry(tab2, font = 'arial 10', textvariable = private_key , bg ='ghost white').grid(row=1, column=1)


#mode
btn_decode.grid(row=2, column=0)
btn_encode.grid(row=2, column=1)


#result
tk.Label(tab2, font = 'arial 12 bold', text ='Result').grid(row=3, column=0)
tk.Entry(tab2, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').grid(row=3, column=1)



#label

tk.Label(tab2, text ='ENCODE DECODE', font = 'arial 20 bold').grid(row=0, padx=5, pady=5)
tk.Label(tab2, text ='0001', font = 'arial 20 bold').grid(row=7, padx=5, pady=55)




#fr_buttons.grid(row=0, column=0, sticky="ns")
#btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#btn_save.grid(row=1, column=0, sticky="ew", padx=5)
#txt_editor.grid(row=0, column=0, sticky="nsew")
tab_control.grid(row=0, column=0, sticky="nsew")
txt_editor.pack(expand=1, fill="both")
window.mainloop()
