import psutil
from tkinter import *
r = Tk() 
r.title('Monitor RAM Usage')
r['bg']='#90e0ef'
label=Label(r,bg='#90e0ef',font='bold')
label2=Label(r,bg='#90e0ef',font='bold',text='RAM remaining:')
label3=Label(r,bg='#90e0ef',font='bold')
flag=None
def ram():
	#label.config(text=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
	label.config(text="{:.2f} %".format(100-psutil.virtual_memory().percent))
	label3.config(text='Scanning started')
	global flag
	flag=r.after(2000,ram)
def cancel():
	label3.config(text='Scanning stopped')
	r.after_cancel(flag)
	
button1 = Button(r, text='start', width=15, command=ram,bg='#06d6a0')
button2=Button(r, text='stop', command=cancel,bg='#ef233c')
label3.grid(row = 1, column = 3, pady = 5, padx = 50)
label2.grid(row =2, column = 3, pady = 5, padx = 50)
label.grid(row = 3, column = 3, pady = 5, padx = 50)
button1.grid(row = 4, column = 3, pady = 10, padx = 50)
button2.grid(row = 5, column = 3, pady = 10, padx = 50)
flag=r.after(2000,ram)
r.mainloop()
 