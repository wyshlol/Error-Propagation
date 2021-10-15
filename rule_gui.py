from tkinter import *
from error_calc import Rules
from subscript import getSub

#Error Propagation GUI -----------------------------------------------------------------------------------------------------
#
#
#
#Pop-out Window for Rule 1 -------------------------------------------------------------------------------------------------
def rule1():
	rule1 = Toplevel()
	rule1.title('Rule 1')
	rule1.iconphoto(False, PhotoImage(file='icon.png'))
	root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
	win_x, win_y = root_x + 375, root_y - 31
	rule1.geometry(f'600x350+{win_x}+{win_y}')
	rule1.configure(bg='light gray')
	space = Label(rule1, text='   ', bg='light gray').grid(row=0, column=0)

	#Error Textbox
	errorLabel = Label(rule1, text='\u03B4A :', bg='light gray').grid(row=1, column=1, sticky='w')
	errorTextbox = Entry(rule1, width=10)
	errorTextbox.grid(row=2, column=1)
	space = Label(rule1, text='   ', bg='light gray').grid(row=0, column=2)

	#Constant Textbox
	cLabel = Label(rule1, text='c :', bg='light gray').grid(row=1, column=3, sticky='w')
	cTextbox = Entry(rule1, width=10)
	cTextbox.grid(row=2, column=3)
	space = Label(rule1, text='   ', bg='light gray').grid(row=0, column=4)

	#Run Error Propagation Function
	def calculate():
		try:
			error = float(errorTextbox.get())
			c = float(cTextbox.get())
			resultLabel = Label(rule1, text=f'Result: {Rules.rule1(error, c)}', bg='light gray').grid(row=2, column=7)
		except:
			resultLabel = Label(rule1, text=f'Result: {None}', bg='light gray').grid(row=2, column=7)

	#Calculate Button
	calculateButton = Button(rule1, text='Calculate', command=calculate).grid(row=2, column=5)
	space = Label(rule1, text='   ', bg='light gray').grid(row=0, column=6)

#---------------------------------------------------------------------------------------------------------------------------
#
#Pop-out Window for Rule 2 -------------------------------------------------------------------------------------------------
def rule2():
	rule2 = Toplevel()
	rule2.title('Rule 2')
	rule2.iconphoto(False, PhotoImage(file='icon.png'))
	root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
	win_x, win_y = root_x + 375, root_y - 31
	rule2.geometry(f'600x350+{win_x}+{win_y}')
	rule2.configure(bg='light gray')
	space = Label(rule2, text='   ', bg='light gray').grid(row=0, column=0)

	#Value Textbox
	valueLabel = Label(rule2, text='A :', bg='light gray').grid(row=1, column=1, sticky='w')
	valueTextbox = Entry(rule2, width=10)
	valueTextbox.grid(row=2, column=1)
	space = Label(rule2, text='   ', bg='light gray').grid(row=0, column=2)

	#Error Textbox
	errorLabel = Label(rule2, text='\u03B4A :', bg='light gray').grid(row=1, column=3, sticky='w')
	errorTextbox = Entry(rule2, width=10)
	errorTextbox.grid(row=2, column=3)
	space = Label(rule2, text='   ', bg='light gray').grid(row=0, column=4)

	#Exponent Textbox
	exponentLabel = Label(rule2, text='m :', bg='light gray').grid(row=1, column=5, sticky='w')
	exponentTextbox = Entry(rule2, width=10)
	exponentTextbox.grid(row=2, column=5)
	space = Label(rule2, text='   ', bg='light gray').grid(row=0, column=6)

	#Constant Textbox
	cLabel = Label(rule2, text='c :', bg='light gray').grid(row=1, column=7, sticky='w')
	cTextbox = Entry(rule2, width=10)
	cTextbox.grid(row=2, column=7)
	space = Label(rule2, text='   ', bg='light gray').grid(row=0, column=8)

	#Run Error Propagation Function
	def calculate():
		try:
			value = float(valueTextbox.get())
			error = float(errorTextbox.get())
			exponent = float(exponentTextbox.get())
			c = float(cTextbox.get())
			resultLabel = Label(rule2, text=f'Result: {Rules.rule2(value, error, exponent, c)}', bg='light gray').grid(row=2, column=11)
		except:
			resultLabel = Label(rule2, text=f'Result: {None}', bg='light gray').grid(row=2, column=11)

	#Calculate Button
	calculateButton = Button(rule2, text='Calculate', command=calculate).grid(row=2, column=9)
	space = Label(rule2, text='   ', bg='light gray').grid(row=0, column=10)

#---------------------------------------------------------------------------------------------------------------------------
#
#Pop-out Window for Rule 3 -------------------------------------------------------------------------------------------------
def rule3():
	rule3 = Toplevel()
	rule3.title('Rule 3')
	rule3.iconphoto(False, PhotoImage(file='icon.png'))
	root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
	win_x, win_y = root_x + 375, root_y - 31
	rule3.geometry(f'600x350+{win_x}+{win_y}')

	#Create Scrollbar
	mainFrame = Frame(rule3)
	mainFrame.pack(fill=BOTH, expand=1)

	mainCanvas = Canvas(mainFrame, bg='light gray', highlightthickness=0)
	mainCanvas.pack(side=LEFT, fill=BOTH, expand=1)

	scrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=mainCanvas.yview)
	scrollbar.pack(side=RIGHT, fill=Y)

	mainCanvas.configure(yscrollcommand=scrollbar.set)
	mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion=mainCanvas.bbox('all')))

	secondaryFrame = Frame(mainCanvas, bg='light gray')

	mainCanvas.create_window((0, 0), window=secondaryFrame, anchor='nw')

	#Update Scrollbar
	def updateScrollRegion():
		mainCanvas.update_idletasks()
		mainCanvas.config(scrollregion=secondaryFrame.bbox())


	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=0, column=0)

	#Number of Terms Textbox and Button
	termsLabel = Label(secondaryFrame, text='# Terms :', bg='light gray').grid(row=1, column=1, sticky='w')
	termsTextbox = Entry(secondaryFrame, width=10)
	termsTextbox.grid(row=2, column=1)
	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=3, column=1)

	#Run Error Propagation Function
	def calculate():
		try:
			errors = []
			for error in error_terms:
				errors.append(float(error.get()))
			resultLabel = Label(secondaryFrame, text=f'Result: {Rules.rule3(errors)}', bg='light gray').grid(row=5, column=7)
		except:
			resultLabel = Label(secondaryFrame, text=f'Result: {None}', bg='light gray').grid(row=5, column=7)

	def getTerms():
		try:
			terms = int(termsTextbox.get())
			termsLabel = Label(secondaryFrame, text='', bg='light gray', width=20).grid(row=2, column=7)

			errors = []
			#Error Textbox
			for i in range(terms):
				sub = getSub(str(i+1))
				errorLabel = Label(secondaryFrame, text=f'\u03B4A{sub} :', bg='light gray').grid(row=4+(3*i), column=1, sticky='w')
				errorTextbox = Entry(secondaryFrame, width=10)
				errorTextbox.grid(row=5+(3*i), column=1)
				errors.append(errorTextbox)
				space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=6+(3*i), column=1)
			global error_terms
			error_terms = errors
		except:
			termsLabel = Label(secondaryFrame, text='Insert a number of terms.', bg='light gray').grid(row=2, column=7)
		#Calculate Button
		calculateButton = Button(secondaryFrame, text='Calculate', command=calculate).grid(row=5, column=5)
		updateScrollRegion()
	termsButton = Button(secondaryFrame, text='Go',command=getTerms, width=7).grid(row=2, column=5)

	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=0, column=2)
	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=0, column=6)

#---------------------------------------------------------------------------------------------------------------------------
#
#Pop-out Window for Rule 4 -------------------------------------------------------------------------------------------------
def rule4():
	rule4 = Toplevel()
	rule4.title('Rule 4')
	rule4.iconphoto(False, PhotoImage(file='icon.png'))
	root_x, root_y = root.winfo_rootx(), root.winfo_rooty()
	win_x, win_y = root_x + 375, root_y - 31
	rule4.geometry(f'600x350+{win_x}+{win_y}')

	#Create Scrollbar
	mainFrame = Frame(rule4)
	mainFrame.pack(fill=BOTH, expand=1)

	mainCanvas = Canvas(mainFrame, bg='light gray', highlightthickness=0)
	mainCanvas.pack(side=LEFT, fill=BOTH, expand=1)

	scrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=mainCanvas.yview)
	scrollbar.pack(side=RIGHT, fill=Y)

	mainCanvas.configure(yscrollcommand=scrollbar.set)
	mainCanvas.bind('<Configure>', lambda e: mainCanvas.configure(scrollregion=mainCanvas.bbox('all')))

	secondaryFrame = Frame(mainCanvas, bg='light gray')

	mainCanvas.create_window((0, 0), window=secondaryFrame, anchor='nw')

	#Update Scrollbar
	def updateScrollRegion():
		mainCanvas.update_idletasks()
		mainCanvas.config(scrollregion=secondaryFrame.bbox())


	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=0, column=0)

	#Number of Terms Textbox and Button
	termsLabel = Label(secondaryFrame, text='# Terms :', bg='light gray').grid(row=1, column=1, sticky='w')
	termsTextbox = Entry(secondaryFrame, width=10)
	termsTextbox.grid(row=2, column=1)
	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=3, column=1)

	#Run Error Propagation Function
	def calculate():
		try:
			values = []
			for value in value_terms:
				values.append(float(value.get()))
			errors = []
			for error in error_terms:
				errors.append(float(error.get()))
			exponents = []
			for exponent in exponent_terms:
				exponents.append(float(exponent.get()))
			Q = float(q_get.get())
			resultLabel = Label(secondaryFrame, text=f'Result: {Rules.rule4(values, errors, exponents, Q)}', bg='light gray').grid(row=5, column=13)
		except:
			resultLabel = Label(secondaryFrame, text=f'Result: {None}', bg='light gray').grid(row=5, column=13)

	def getTerms():
		try:
			terms = int(termsTextbox.get())
			termsLabel = Label(secondaryFrame, text='', bg='light gray', width=20).grid(row=2, column=11)

			#Value Textbox
			values = []
			for i in range(terms):
				sub = getSub(str(i+1))
				valueLabel = Label(secondaryFrame, text=f'A{sub} :', bg='light gray').grid(row=4+(3*i), column=1, sticky='w')
				valueTextbox = Entry(secondaryFrame, width=10)
				valueTextbox.grid(row=5+(3*i), column=1, sticky='w')
				values.append(valueTextbox)
				space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=6+(3*i), column=1)
			global value_terms
			value_terms = values

			#Error Textbox
			errors = []
			for j in range(terms):
				sub = getSub(str(j+1))
				errorLabel = Label(secondaryFrame, text=f'\u03B4A{sub} :', bg='light gray').grid(row=4+(3*j), column=5, sticky='w')
				errorTextbox = Entry(secondaryFrame, width=10)
				errorTextbox.grid(row=5+(3*j), column=5, sticky='w')
				errors.append(errorTextbox)
				space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=6+(3*j), column=5)
			global error_terms
			error_terms = errors

			#Exponent Textbox
			exponents = []
			for k in range(terms):
				sub = getSub(str(k+1))
				exponentLabel = Label(secondaryFrame, text=f'm{sub} :', bg='light gray').grid(row=4+(3*k), column=7, sticky='w')
				exponentTextbox = Entry(secondaryFrame, width=10)
				exponentTextbox.grid(row=5+(3*k), column=7, sticky='w')
				exponents.append(exponentTextbox)
				space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=6+(3*k), column=7)
			global exponent_terms
			exponent_terms = exponents

			#Q Textbox
			qLabel = Label(secondaryFrame, text='Q :', bg='light gray').grid(row=4, column=9, sticky='w')
			qTextbox = Entry(secondaryFrame, width=10)
			qTextbox.grid(row=5, column=9, sticky='w')
			global q_get
			q_get = qTextbox
		except:
			termsLabel = Label(secondaryFrame, text='Insert a number of terms.', bg='light gray').grid(row=2, column=11)


		#Calculate Button
		calculateButton = Button(secondaryFrame, text='Calculate', command=calculate).grid(row=5, column=11)
		updateScrollRegion()
	termsButton = Button(secondaryFrame, text='Go',command=getTerms, width=7).grid(row=2, column=5)

	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=0, column=2)
	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=0, column=6)
	space = Label(secondaryFrame, text='   ', bg='light gray').grid(row=0, column=8)

#---------------------------------------------------------------------------------------------------------------------------
#
#Main Window ---------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	root = Tk()
	root.title('Physics Rules')
	root.iconphoto(False, PhotoImage(file='icon.png'))
	x_size, y_size = 350, 210
	root.geometry(f'{x_size}x{y_size}+500+300')
	root.minsize(x_size, y_size)
	root.maxsize(x_size, y_size)
	root.configure(bg='light gray')
	space = Label(root, text='       ', bg='light gray').grid(row=0, column=0)
	space = Label(root, text='   ', bg='light gray').grid(row=2, column=2)

	#Rule Buttons
	rule1Button = Button(root, text='Rule 1', command=rule1).grid(row=1, column=1)
	rule2Button = Button(root, text='Rule 2', command=rule2).grid(row=3, column=1)
	rule3Button = Button(root, text='Rule 3', command=rule3).grid(row=5, column=1)
	rule4Button = Button(root, text='Rule 4', command=rule4).grid(row=7, column=1)

	#Rules
	rule1Equation = Label(text='\u03B4Q=|c|\u03B4A', font='15', width=25).grid(row=1, column=3)
	space = Label(root, text='   ', bg='light gray').grid(row=2, column=0)

	rule2Equation = Label(text='\u03B4Q=|cmAᵐ⁻¹|\u03B4A', font='15', width=25).grid(row=3, column=3)
	space = Label(root, text='   ', bg='light gray').grid(row=4, column=0)

	rule3Equation = Label(text='\u03B4Q=\u221A((\u03B4A)²+(\u03B4B)²)', font='15', width=25).grid(row=5, column=3)
	space = Label(root, text='   ', bg='light gray').grid(row=6, column=0)

	rule4Equation = Label(text='\u03B4Q=|Q|\u221A((m\u03B4A/A)²+(n\u03B4B/B)²', font='15', width=25).grid(row=7, column=3)


	root.mainloop()
#---------------------------------------------------------------------------------------------------------------------------