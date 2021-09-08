#Import modules
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root= tk.Tk()

#Draw the Canvas's size and style
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'white', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Convert Image to PDF', bg = 'white')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

#function to browse the file 
def getFile ():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    image1 = Image.open(import_file_path)
    im1 = image1.convert('RGB')

browseButton = tk.Button(text="     Select File     ", command=getFile, fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(150, 130, window=browseButton)

#function to convert the selected file
def convertToPdf ():
    global im1
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    im1.save(export_file_path)

saveAsButton = tk.Button(text='Convert to PDF', command=convertToPdf, fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton)

#To exit the app
def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='Exit Application',command=exitApplication, fg='black', font=('helvetica', 11, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()
