#test desktop app

from tkinter import *
from error_calc import Rules

#
# Desktop App Gui
#

root = Tk()
root.title('Physics Rules')
root.iconphoto(False, PhotoImage(file='icon.png'))
root.geometry('500x300')

def rule():
	get_rule = Label(root, text=ruleTextbox.get())
	get_rule.pack()

ruleCheck = Label(root, text='Which rule are you using?')
ruleCheck.pack()

ruleTextbox = Entry(root, width=30)
ruleTextbox.pack()

myButton = Button(root, text='Go', command=rule)
myButton.pack()

root.mainloop()