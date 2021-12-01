# Python program to create a Calculator to calculate Bill with GST or without GST.
import tkinter
from tkinter import *
# globally declare the expression variable
expression = ""
# Function to update expression in the text entry box
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
# Function to evaluate the final expression
def equalpress():
	# Try and except statement is used for handling the errors like zero division error etc.
	try:

		global expression

		# eval function evaluate the expression
		# and str function convert the result
		# into string
		total = str(eval(expression))

		equation.set(total)

		# initialize the expression variable
		# by empty string
		expression = ""

	# if error is generate then handle
	# by the except block
	except:

		equation.set(" error ")
		expression = ""


# Function to clear the contents
# of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")


# Driver code
if __name__ == "__main__":
	# create a GUI window
	gui = tkinter.Tk()

	# set the background colour of GUI window
	gui.configure(background="silver")

	# set the title of GUI window
	gui.title("GST Calculator")

	# set the configuration of GUI window
	gui.geometry("600x550")
	gui.resizable(height=700,width=700)
	# StringVar() is the variable class
	# we create an instance of this class
	equation = StringVar()

# create the text entry box for
# showing the expression .
	#expression_field = Entry(gui, textvariable=equation,fg='red')
	expression_field = Entry(gui, textvariable=equation, font=("Verdana", 15),bg='light green', bd=14,insertwidth=5, width=36, justify=CENTER,fg='black')
	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	expression_field.grid(columnspan=10, ipadx=50)

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(gui, font=('futura', 15, 'bold'),padx=16, pady=16,
					 text='1',command=lambda: press (1),
					 height=2, width=9)
	button1.grid(row=4, column=0)


	button2 =Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='2',
           command=lambda: press (2),
           height=2, width=9)
	button2.grid(row=4, column=1)

	button3 = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='3',
           command=lambda: press (3),
           height=2, width=9)
	button3.grid(row=4, column=2)

	button4 = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='4',
           command=lambda: press (4),
           height=2, width=9)
	button4.grid(row=5, column=0)

	button5 = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='5',
           command=lambda: press (5),
           height=2, width=9)
	button5.grid(row=5, column=1)

	button6 =Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='6',
           command=lambda: press (6),
           height=2, width=9)
	button6.grid(row=5, column=2)

	button7 = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='7',
           command=lambda: press (7),
           height=2, width=9)
	button7.grid(row=6, column=0)

	button8 = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='8',
           command=lambda: press (8),
           height=2, width=9)
	button8.grid(row=6, column=1)

	button9 = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='9',
           command=lambda: press (9),
           height=2, width=9)
	button9.grid(row=6, column=2)

	button0 = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='0',
           command=lambda: press (0),
           height=2, width=9)
	button0.grid(row=7, column=0)

	plus = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='+',
           command=lambda: press ("+"),
           height=2, width=9,fg='red')
	plus.grid(row=4, column=3)

	minus = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='-',
           command=lambda: press ("-"),
           height=2, width=9,fg='red')
	minus.grid(row=5, column=3)

	multiply = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='*',
           command=lambda: press ("*"),
           height=2, width=9,fg='red')
	multiply.grid(row=6, column=3)

	divide = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='/',
           command=lambda: press ("/"),
           height=2, width=9,fg='red')
	divide.grid(row=7, column=3)

	equal =Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='= ''(Equals)',
           command=equalpress,
           height=2, width=9,fg='red')
	equal.grid(row=7, column=2)

	clear = Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='AC',
           command=clear,
           height=2, width=9,fg='red')
	clear.grid(row=3, column=0,columnspan=2,sticky='nsew')
	mod= Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='Mod(%)',
           command=lambda: press ("%"),
           height=2, width=9,fg='red')
	mod.grid(row=3,column=2)

	Decimal= Button(gui, font=('futura', 15, 'bold'),
           padx=16, pady=16, text='.',
           command=lambda: press ("."),
           height=2, width=9,fg='red')
	Decimal.grid(row=7, column=1)


	def iExit():
		gui.destroy()


	exit= Button(gui, font=('futura', 15, 'bold'),
					 padx=16, pady=16, text='Exit',
					 command=iExit,
					 height=2, width=9)
	exit.grid(row=3, column=3)



	# start the GUI
	gui.mainloop()
