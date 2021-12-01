from tkinter import*

newroot = Tk()
newroot.title("Menu")
newroot.geometry("350x250+390+50")
newroot.resizable(0,0)
newroot.configure(bg="light green")


def enter1():
	newroot.destroy()
	import restaurant_management_system


def enter2():
	newroot.destroy()
	import price	


label11 = Label(newroot, text="Bill",font = ('arial',10,'bold'),bg="light green")
label11.grid(row=3, sticky=E)

press_btn = Button(newroot, text="Press Here", command= enter1,bd=10)
press_btn.grid(row=3, column=4)

label21 = Label(newroot, text="Change Price",font = ('arial',10,'bold'),bg="light green")
label21.grid(row=4,sticky=E)

press1_btn = Button(newroot, text="Press Here", command= enter2,bd=10)
press1_btn.grid(row=4, column=4)

newroot.mainloop()
