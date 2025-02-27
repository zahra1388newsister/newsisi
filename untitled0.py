#======imports==========
from tkinter import *
from tkinter import messagebox
import random
#======values=======
win=Tk()
win.title('random colors')
win.geometry('400x300')
time=30
score=0
state=False
#==========function===========
def start_game(event=None):
    global time
    if time == 30:
        rcr()

def rcr():  
   color=['blue','red','green','pink','yellow','black','gray','gold']
   global score
   global state
   c=random.choice(color)
   t=random.choice(color)
   lbl_c.config(text=t,fg=c)
   if c.lower()==ent_c.get().lower():
      score+1
      lbl_scor.config(text=f'score:{score}')
   clear()    
   if state==False:
      timer()
      state=True
 
def clear():
   ent_c.delete(0,END)

def timer():
   global time
   time-=1
   lbl_time.config(text=f'time:{time}') 
   if time==0:
      messagebox.showinfo('timeup','your time finished')
      time=30  
      lbl_time.config(text=f'time:{time}')
   else:
      lbl_time.after(1000,timer)
#===============================================
discreeption=Label(win,font='calibri 12 bold',text='اگر"رنگ داخل نوشته"را بنویسید امتیاز کسب میکنید')
discreeption.pack()
lbl_c=Label(win,font='calibri 22 bold')
lbl_c.place(x=160,y=110)
lbl_time=Label(win,text='time:30',font='calibri 12 bold')
lbl_time.place(x=10,y=40)
lbl_scor=Label(win,text='score:0',font='calibri 12 bold')
lbl_scor.place(x=280,y=40)
ent_c=Entry(win)
ent_c.place(x=130,y=185)
win.bind('<Return>', lambda event: (start_game() if time == 30 else rcr()))
win.mainloop()
