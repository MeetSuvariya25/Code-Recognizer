
import tkinter as x
from tkinter import *
import tkinter.filedialog as tk
import datetime

#textarea------------------------------------------------------>
root =Tk(" TEXT EDITOR")
text = Text(root)
text.pack()
topFrame = Frame(root)
topFrame.pack()

thisTextArea = Text(root)
lis = []

#functions--------------------------------------------------------->
def saveas():
        global text
        global ext
        t=text.get("1.0","end-1c")
        lis.append(t)
        st = ''.join(lis)
        #res=st.__contains__('#include<stdio.h>',";","{","}")
        
        #keywords="#include<stdio"
        if(st.find("#include<stdio.h>")!=-1):
                   ext = ".c"
        elif (st.find("#include<iostream>")!=-1):
                      ext = ".cpp"
        elif(st.find("import java"or"public static void main")!=-1):
            ext = ".java"
        else:
            ext = ".py"
            
            
            
        

        saveLocation =tk.asksaveasfilename(defaultextension=ext)
        
        #saveLocation =tk.asksaveasfile(ext)
        save()
       # tk.askopenfilename()
        file1 = open(saveLocation,"w+")
        file1.write(t)
        #print(df)
        #print(ext)
        print(lis)
        
        file1.close()
        
def opn():

   text.delete(1.0 , END)
   

   if file != '':
       txt = file.read()
       text.insert(INSERT,txt)

   else:
       pass

def save():
        pass



                                
    



#menu-------------------------------------------------------------->
menu = Menu(root)
filemenu = Menu(root)
root.config(menu = menu)
menubar = Menu(root)  
file = Menu(menubar, tearoff=0)    
file.add_command(label="Save",command=saveas)   
file.add_command(label="Close")  
file.add_separator()    
file.add_command(label="Exit", command=quit)
menu.add_cascade(label="File", menu=file)



edit = Menu(menubar, tearoff=0)  
edit.add_command(label="Undo")  
edit.add_separator()  
edit.add_command(label="Cut")  
edit.add_command(label="Copy")  
edit.add_command(label="Paste")  
edit.add_command(label="Delete")  
edit.add_command(label="Select All")
menu.add_cascade(label="Edit", menu=edit)



Help = Menu(menubar, tearoff=0)  
Help.add_command(label="About developers")  
menu.add_cascade(label="Help", menu=Help)

        



#mainloop----------------------------------------------------------------->
root.mainloop()
