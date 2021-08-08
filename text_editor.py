import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filetypes=(("text files","*.txt"),
                ("all files","*.*"))
    filepath=askopenfilename(title="OPEN_FILE", initialdir="d:/test_files", filetypes=filetypes)
    if not filepath:
        return

    #print(filepath)
    txt_edit.delete("1.0",tk.END)

    with open(filepath,"r") as input_file:
        #print(input_file)
        text=input_file.read()
        txt_edit.insert(tk.END,text)

    window.title(f"Simple Text Editor - {filepath}")


def save_file():
    filetypes=(("text files","*.txt"),
                ("all files","*.*"))

    filepath=asksaveasfilename(defaultextension="txt",title="SAVE_FILE", initialdir="d:/test_files", filetypes=filetypes)
    if not filepath:
        return

    with open(filepath,"w") as output_file:
        text=txt_edit.get("1.0",tk.END)
        output_file.write(text)

    window.title(f"Simple Text Editor - {filepath}")





window=tk.Tk()
#print(dir(window))
window.title("Simple Text Editor")

window.rowconfigure(0,minsize=400,weight=1)
#window.columnconfigure(0,minsize=50,weight=1)
window.columnconfigure(1,minsize=600,weight=1)


fr_buttons=tk.Frame(window)
txt_edit=tk.Text(window)

btn_open=tk.Button(fr_buttons,text="Open",command=open_file)
btn_save=tk.Button(fr_buttons,text="Save as",command=save_file)

btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
txt_edit.grid(row=0,column=1,sticky="nsew")


window.mainloop()