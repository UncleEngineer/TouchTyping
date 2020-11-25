from tkinter import *
from tkinter import ttk
import random
import wikipedia
import time

alltext = wikipedia.summary('python programming')

alltext = alltext.split()
print(alltext)

GUI = Tk()
GUI.geometry('700x500')

label = Label(GUI, font=("Courier", 30, 'bold'), bg="blue", fg="white", bd =30)
label.place(x=20,y=20)
count = 0
alltime = 10
first = True
waiting = True
newgame = False
reset = True
def digitalclock():
	global first
	global count
	global waiting
	global count
	global newgame
	global score
	global reset

	if newgame == False and first == False: 
		count += 1

	if first == False and waiting == True:
		global current
		global corrected
		select = random.choice(alltext)
		v_vocab.set(select)
		corrected = False
		current = select
		waiting = False

	text_input = count
	label.config(text=str(text_input))
	if first == True:
		print('5 second')
		label.after(5000, digitalclock)
		first = False
	elif newgame == True:
		count = 0
		score = 0
		print('10 second')
		newgame = False
		label.after(10000, digitalclock)
		#RandomVocab()
	else:
		if reset == True:
			E1.configure(state='enabled')
			E1.focus()
			reset = False
			v_text.set('')
			RandomVocab()

		print('1 second')
		newgame == False
		label.after(1000, digitalclock)
		if count == alltime:
			count = 0
			v_vocab.set('Game Over\nWaiting 10 second\nYou Got {}! '.format(score))
			score = 0
			v_score.set(score)
			newgame = True
			E1.configure(state='disabled')
			reset = True
	

FONT1 = ('Angsana New',30)

L1 = Label(GUI,text='ข้อความ',font=FONT1).pack()

v_vocab = StringVar()
L2 = Label(GUI,textvariable=v_vocab,font=FONT1).pack()

v_score = StringVar()
v_score.set(0)
L3 = Label(GUI,textvariable=v_score,font=FONT1).place(x=600,y=10)

v_text = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_text,font=FONT1,width=40)
E1.pack(pady=40)

E1.configure(state='disabled')
global current
current = ''
global corrected
global score
score = 0

def RandomVocab():
	global current
	global corrected
	select = random.choice(alltext)
	v_vocab.set(select)
	corrected = False
	current = select

def CheckTyping(sv):

	global current
	global corrected
	global score
	print('corrected? ',corrected)
	text = v_text.get()
	print(text)
	if corrected == True:
		select = random.choice(alltext)
		v_vocab.set(select)
		corrected = False
		current = select

	if corrected == False:
		if text == current:
			corrected = True
			score += 1
			print('You Got 1, All Score: ',score)
			RandomVocab()
			v_text.set('')
			v_score.set(score)

v_text.trace("w", lambda name, index, mode, sv=v_text: CheckTyping(sv))
digitalclock()
GUI.mainloop()