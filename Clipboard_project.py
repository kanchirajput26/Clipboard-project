from tkinter import *
from tkinter import messagebox
import pyperclip 
import os

root = Tk()

#check if the folder exists or not; else, create one
clip_folder = os.path.isdir("c:\\Clipboard_folder")

if not clip_folder:

	os.makedirs("c:\\Clipboard_folder")
	f=open("c:\\Clipboard_folder\\save1.txt","w")
	f.close()


## FUNCTIONALITY BUTTONS ##

# saving the copied text 
def save_copied_data():

	clipboard_text = pyperclip.paste()
	f = open("c:\\Clipboard_folder\\file1.txt","w")
	f = open("c:\\Clipboard_folder\\file1.txt","a")
	f.write("\n")
	f.write(clipboard_text)
	f.write("\n")
	f.close()
	
	# appending latest copied data on the top of text file
	with open("c:\\Clipboard_folder\\save1.txt","r") as c_f:
		save_data_1=c_f.read()
		
	with open("c:\\Clipboard_folder\\file1.txt","r") as c_f:
		save_data_2=c_f.read()
		
	with open("c:\\Clipboard_folder\\save1.txt","w") as c_f:
		c_f.write(save_data_2)
		
	with open("c:\\Clipboard_folder\\save1.txt","a") as c_f:
		c_f.write(save_data_1)

	
# viewing the previous saved clipboard data
def saved_file():

	os.startfile("c:\\Clipboard_folder\\save1.txt")	


# viewing the current copied data
def clip_text():

	clip_text = pyperclip.paste()
	f = open("c:\\Clipboard_folder\\file1.txt","w")
	f.write(clip_text)
	f.close()
	os.startfile("c:\\Clipboard_folder\\file1.txt")


# clearing the current copied text
def clear_clipboard():

	pyperclip.copy(" ")
	messagebox.showinfo(title="Clear Dialogue Box", message= "Clipboard has been cleared")



# creation of tkinter window
root.title("Clipboard")
root.geometry("300x200")
top = Frame(root)
top.pack(pady=25)

#creation of buttons
Button1 = Button(top,justify = CENTER, text ="View Current Text",
	        width = 13, bg= 'black',fg='white', command = clip_text)
Button1.pack(pady=5)

Button2 = Button(top,justify = CENTER, text ="Save Current Text",
	        width = 13, bg='black',fg='white', command = save_copied_data)
Button2.pack(pady=5)

Button3 = Button(top,justify = CENTER, text ="View History",
	       width = 13, bg= 'black', fg='white',command = saved_file)
Button3.pack(pady=5)

Button4 = Button(top,justify = CENTER, text ="Clear Current Text ",
	       width = 13,  bg= 'black',fg='white', command = clear_clipboard)
Button4.pack(pady=5)


# closing the mainloop
root.mainloop()