import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):#Removes blank space in List
    with open('save.txt', 'r') as f:
        tempApps=f.read()
        apps = tempApps.split(',')
        print(apps)
        apps = [x for x in tempApps if x.strip()]

def addApp():

   filename = filedialog.askopenfilename(initialdir ="/", title = "Select File", filetypes = (("executables", "*.exe"),("all files", "*.*"))) # Lets user open up all file types ans execute exe files

   for widget in frame.winfo_children(): #Puts last executable file opened on top of previous executable
        widget.destroy()

   apps.append(filename)
   print(filename)
   for app in apps:
       label = tk.Label(frame, text = app, bg="green")
       label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D45")
canvas.pack()

frame = tk.Frame(root, bg = "white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1) #Places window frame and position

openFile = tk.Button(root, text = "Open File", padx=10, 
                     pady = 5, fg="white", bg ="#263D45", command=addApp)

openFile.pack()

runApps = tk.Button(root, text = "Run Apps", padx=10,
                   pady=5, fg="white", bg ="#263D45", command = runApps )
runApps.pack()



for app in apps:
    label = tk.Label (frame, text=app)
    label.pack()


root.mainloop()

#Saves a file for a user to be able to open up a previous set of apps
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')