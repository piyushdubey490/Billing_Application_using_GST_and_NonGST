from tkinter import*
import tkinter.messagebox
root1 = Tk()
root1.geometry("650x550+390+50")
root1.resizable(0,0)
root1.title("Login Page")
root1.configure(bg="light green")

name_inp = StringVar()
password_inp = StringVar()

def enter():
	if name_inp.get() == "piyush" and password_inp.get() == "1234":
		root1.destroy()
		import question
	else:
		tkinter.messagebox.showinfo('Error','Authentication Failed')
		name_inp.set("")
		password_inp.set("")	

def destroy():
	root1.destroy()	


label = Label(root1, font = ('arial',30,'bold'), text ="Login Page",bg="light green", fg = "Black", bd = 10, anchor = 'w')
label.grid(row = 0,column=1)


label1 = Label(root1, font = ('arial',20,'bold'),text="Name",bg="light green",fg="Black")
label2 = Label(root1, font =('arial',20,'bold'),text="Password(1234)",bg="light green",fg="Black")
	
entry1 = Entry(root1, textvariable = name_inp,bd=10,fg="blue")
entry2 = Entry(root1, textvariable = password_inp,bd=10,fg="blue")

label1.grid(row=1, sticky=E)
label2.grid(row=2,sticky=E)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)

enter_btn = Button(root1, text="Enter", command= enter,bd=5,bg="orange")
enter_btn.grid(row=4, column=1)

exit_btn = Button(root1, padx= 1, text="Exit", command= destroy,bd=5,bg="orange")
exit_btn.grid(row=5,column=1)

root1.mainloop()
