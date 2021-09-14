import tkinter as tkt
import tkinter.messagebox as tkmb
import tkinter.scrolledtext as tkst
from random import *
from tkinter.ttk import *
from math import *
from tkinter.constants import RIGHT, LEFT, Y, BOTH, END
click=False
cal=tkt.Tk()
cal.title('Calculator')
cal.geometry('415x431+0+0')
cal.resizable(0,0)
cal.config(bg='#a3f1da')
a=tkt.StringVar()
x=0
X=0
Y=0
move=0
#Constants
ε=8.85E-12
μ=(4E-7)*pi
h=6.626E-34
G=6.67E-11
c=1/sqrt(ε*μ)
N=6.022e23
qe=1.602e-19
me=9.11e-31
mp=1.660e-27
Rh=1.097e7
k=1.3806e-23
R=8.314
F=96500
a0=5.29e-11
#Frames
btnframe=tkt.Frame(width=0,height=700,bg='#a3f1da')
btnframe.place(x=0,y=40)
txt_frame=tkt.Frame(cal,width=31,height=50,bg='black')
txt_frame.place(x=0,y=0)
#Main Program starts here
txt=tkt.Entry(txt_frame,textvariable=a,width=29,font='Arial 19',justify='right',bd='5')
txt.grid(row=0,column=0)
π=pi
E=e
d=[]
fg=open('History.dat',mode='w')
fg.close()
#Functions
def HELP():
   h=tkt.Tk()
   h.resizable(0,0)
   h.title('Help')
   h.geometry('845x645+0+0')
   Help="""HELP:
Note:The usage of the different functions is given below, for any assistance please refer to this.
_______________________________________________________________________________________________________
1. fn:
   This function returns the value of the function you entered for a particular value of x.
   Usage: fn('your function',a), which returns the value of the function when we substitute the
   variable with 'a'.
   The function must be in quotes and 'a' must be a number.
_______________________________________________________________________________________________________
2. nCr:
   This function returns the number of ways choosing 'r' different objects from a set of 'n' total
   objects.
   Usage: nCr(a,b), which returns number of ways of choosing 'b' different objects from 'a' total
   objects.
   'a' and 'b' must be whole numbers and a must be greater than b.
_______________________________________________________________________________________________________
3. nPr:
   This function returns the number of ways of arranging 'r' different objects from a set of 'n' total
   objects.
   Usage: nPr(a,b), which returns number of ways of arranging 'b' different objects from 'a' total
   objects.
   'a' and 'b' must be whole numbers and a must be greater than b.
_______________________________________________________________________________________________________
4. Fact:
   This function returns the factorial of the value given.
   Usage: factorial(a), which returns the factorial of a.
   'a' must be a whole number.
_______________________________________________________________________________________________________
5. nRoot:
   This function returns the 'n'th root of the number.
   Usage: nRoot(a,b), which returns the 'b'th root of 'a'
_______________________________________________________________________________________________________
6. log_x:
   This function returns the logarithm of the number with base 'x'.
   Usage: log(a,b), which returns the logarithm of 'b' with base 'a'.
   'b' must not be equal to 0 or 1 and 'a' must not be equal to 0.
_______________________________________________________________________________________________________
7. shift:
   This button alters a few functions. For eg: when switched on, the sin function changes to asin.
_______________________________________________________________________________________________________
8. const:
   This button opens a new window of tkinter which contains some of the Univeral Constants.
   Click on any one of them to insert it into the calculator textbox.
   In the constants:
   ε=permittivity of free space/vacuum
   μ=permeability of free space/vacuum
   h=Planck's constant
   G=Universal gravitational constant
   c=speed of light
   N=Avogadro constant/Avogadro's number
   qe=magnitude of charge on electron
   me=mass of electron
   mp=mass of proton
   Rh=Rydberg's constant
   k=Boltzmann constant
   R=Universal Gas constant
   F=Faraday's constant
   a0=Bohr radius
_______________________________________________________________________________________________________
9. eqn:
   This button helps to solve simultaneous equations in x and y.
   Usage: eqn(a1,b1,c1,a2,b2,c2)
   a1=coefficient of x in first equation
   b1=coefficient of y in first equation
   c1=constant in first equation
   a2=coefficient of x in second equation
   b2=coefficient of y in second equation
   c2=constant in second equation
_______________________________________________________________________________________________________
10. solve:
   This button helps to solve Quadratic equations ONLY.
   Usage: solve(a,b,c)
   a=coefficient of x^2
   b=coefficient of x
   c=constant
   Returns the roots of the quadratic equation ax^2+bx+c=0
_______________________________________________________________________________________________________
11. hyp:
   This button opens a new tkinter window which contains the hyperbolic functions.
   Click on any one of them to insert into the calculator textbox.
   The functions are:
   sinh: hyperbolic sine
   cosh: hyperbolic cosine
   tanh: hyperbolic tangent
   csch: hyperbolic cosecant
   sech: hyperbolic secant
   coth: hyperbolic cotangent
_______________________________________________________________________________________________________
12. random:
   This button generates a random decimal number between 0 and 1.
_______________________________________________________________________________________________________
13. randint:
   This button generates a random integer number between two given numbers.
   Usage: randint(a,b)
   Returns a number between 'a' and 'b' including both endpoints.
_______________________________________________________________________________________________________
14. randrng:
   This button generates a random integer number between two given numbers. Displays 'randrange' in
   the textbox.
   Usage: randrange(a,b)
   Returns a number between 'a' and 'b' excluding both endpoints.
_______________________________________________________________________________________________________
15. angle:
   This button opens a new tkinter window which contains functions to change the value of angles in the
   different units, degrees and radians.
   The functions are:
   deg: degrees(), converts radians to degrees, displays degrees in textbox.
   rad: radians(), converts degrees to radians, displays radians in textbox."""
   stxt=tkst.ScrolledText(h,bg='#eee6ff',width=103,height=40)
   stxt.insert(END,Help)
   stxt.place(x=0,y=0)
   stxt.focus_set()
   h.mainloop()
def clearh():
   fp=open('History.dat',mode='w')
   fp.write('')
def op(txt,b):
   global p
   p=txt.get()+b
   a.set(p)
def addn(txt,b=0):
   global p,a
   p=txt.get()+str(b)
   a.set(p)
def eq(s=0):
   fh=open('History.dat',mode='a')
   global p,a
   p=txt.get()
   try:
      C=eval(p)
      a.set(C)
      fh.write(str(C)+'\n')
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Division by zero')
   except TypeError:
      pass
   except ValueError:
      tkmb.showinfo('Math Error','Value Error: Not in Domain')
   fh.close()
def solve(a,b=0,c=0):
   D=b**2-4*a*c
   if D<0:
      tkmb.showinfo('Math Error','Complex Roots')
   else:
      x1=((-b+sqrt(D))/2)/a
      x2=((-b-sqrt(D))/2)/a
      return 'x='+str(x1)+','+str(x2)
def clear():
   a.set('')
def delete(txt):
   global p
   p=txt.get()
   s=p[0:len(p)-1]
   a.set(s)
def eqn(a1=0,b1=0,c1=0,a2=0,b2=0,c2=0):
   global X,Y
   try:
      X=(b1*c2-c1*b2)/((a1*b2)-(b1*a2))
      Y=(c1*a2-a1*c2)/((a1*b2)-(b1*a2))
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Division by Zero')
   return 'x='+str(X)+','+'y='+str(Y)
def hist():
   global a,move
   move=1
   fr=open('History.dat',mode='r')
   try:
      S=fr.readlines()
      d=S[len(S)-move][0:len(S[len(S)-move])-1]
      if txt.get()=='':
         s=d
      elif txt.get()!='' and txt.get()==d:
         s=d
      elif txt.get()!='':
         s=txt.get()+d
      a.set(s)
   except IndexError:
      pass
def cosec(x):
   global p,a
   try:
      p=1/sin(x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Division by zero')
   return p
def acosec(x):
   global p,a
   try:
      p=asin(1/x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Division by zero')
   return p
def sec(x):
   global p,a
   try:
      p=1/cos(x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Value Error: Not in Domain')
   return p
def asec(x):
   global p,a
   try:
      p=acos(1/x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Value Error: Not in Domain')
   if abs(x)<1 and abs(x)>0:
      tkmb.showinfo('Math Error','Value Error: Not in Domain')
   return p
def cot(x):
   global p,a
   try:
      p=1/(round(tan(x),15))
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Division by zero')
   return p
def acot(x):
   global p,a
   try:
      p=(π/2)-atan(x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Division by zero')
   return p
def csch(x):
   global p,a
   try:
      p=1/sinh(x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Value Error: Not in Domain')     
   return p
def sech(x):
   global p,a
   try:
      p=1/cosh(x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Division by zero')
   return p
def coth(x):
   global p,a
   try:
      p=1/tanh(x)
   except ZeroDivisionError:
      tkmb.showinfo('Math Error','Value Error: Not in Domain')
   return p
def shift():
   global click
   if click==True:
      b_shift['bg']='#ee9451'
      b_sin['text']='sin'
      b_cos['text']='cos'
      b_tan['text']='tan'
      b_log['text']='log_e'
      b_cosec['text']='cosec'
      b_sec['text']='sec'
      b_cot['text']='cot'
      b_log10['text']='log10'
      click=False
   elif click==False:
      b_shift['bg']='green'
      b_sin['text']='asin'
      b_cos['text']='acos'
      b_tan['text']='atan'
      b_log['text']='e^'
      b_cosec['text']='acosec'
      b_sec['text']='asec'
      b_cot['text']='acot'
      b_log10['text']='10^'
      click=True
def trigfunc(txt,n=''):
   global click,p
   if click==True:
      p=txt.get()+'a'+n+'('
   elif click==False:
      p=txt.get()+n+'('
   a.set(p)
def up():
   global move
   fr=open('History.dat',mode='r')
   try:
      S=fr.readlines()
      if move==0 and txt.get()=='':
         move+=1
      elif move>0 and move<len(S) and txt.get()!='':
         move+=1
      elif move>0 and move<=len(S) and txt.get()=='':
         move=1
      s=S[len(S)-move][0:len(S[len(S)-move])-1]
      a.set(s)
   except IndexError:
      pass
def down():
   global move
   if move>1:
      move-=1
   else:
      move-=0
   fr=open('History.dat',mode='r')
   try:
      S=fr.readlines()
      s=S[len(S)-move][0:len(S[len(S)-move])-1]
      a.set(s)
   except IndexError:
      pass
def Addspl(txt,c=''):
   global p
   p=txt.get()+c
   a.set(p)
def logfunc(txt,n='',B='e'):
   global p,click
   if click==False:
      p=txt.get()+n+'('
   elif click==True:
      p=txt.get()+B+'**'
   a.set(p)
def P(A,B):
   global a
   try:
      k=factorial(A)/(factorial(A-B))
      return k
   except ValueError:
      tkmb.showinfo('Error','Math Error')
      return None
def C(A,B):
   global a
   try:
      k=factorial(A)/(factorial(A-B)*factorial(B))
      return k
   except ValueError:
      tkmb.showinfo('Error','Math Error')
      return None
def cbrt(A):
   global a
   s=round(A**(1/3),15)
   a.set(str(s))
   return s
def nRoot(A,B):
   global a
   s=round(A**(1/B),15)
   a.set(str(s))
   return s
def fn(t='',n=0):
   global a
   x=n
   y=n
   s=eval(t)
   return s
def addcons(txt,Const=''):
   global a
   p=txt.get()+Const
   a.set(p)
def const():
   Con=tkt.Tk()
   Con.title('Universal Constants')
   Con.resizable(0,0)
   Con.geometry('259x167+0+0')
   const=tkt.Frame(Con)
   const.place(x=0,y=0)
   btn_ε=tkt.Button(const,text='ε',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'ε'))
   btn_ε.grid(row=0,column=0)
   btn_μ=tkt.Button(const,text='μ',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'μ'))
   btn_μ.grid(row=0,column=1)
   btn_h=tkt.Button(const,text='h',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'h'))
   btn_h.grid(row=0,column=2)
   btn_G=tkt.Button(const,text='G',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'G'))
   btn_G.grid(row=0,column=3)
   btn_c=tkt.Button(const,text='c',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'c'))
   btn_c.grid(row=0,column=4)
   btn_N=tkt.Button(const,text='N',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'N'))
   btn_N.grid(row=1,column=0)
   btn_qe=tkt.Button(const,text='qe',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'qe'))
   btn_qe.grid(row=1,column=1)
   btn_me=tkt.Button(const,text='me',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'me'))
   btn_me.grid(row=1,column=2)
   btn_mp=tkt.Button(const,text='mp',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'mp'))
   btn_mp.grid(row=1,column=3)
   btn_Rh=tkt.Button(const,text='Rh',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'Rh'))
   btn_Rh.grid(row=1,column=4)
   btn_k=tkt.Button(const,text='k',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'k'))
   btn_k.grid(row=2,column=0)
   btn_R=tkt.Button(const,text='R',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'R'))
   btn_R.grid(row=2,column=1)
   btn_F=tkt.Button(const,text='F',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'F'))
   btn_F.grid(row=2,column=2)
   btn_a0=tkt.Button(const,text='a0',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'a0'))
   btn_a0.grid(row=2,column=3)
   btn_exit=tkt.Button(const,text='close',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:Con.destroy())
   btn_exit.grid(row=2,column=4)
   Con.mainloop()
def hyp():
   hyp=tkt.Tk()
   hyp.geometry('155x110+0+0')
   hyp.resizable(0,0)
   hyp.title('Hyp')
   hypf=tkt.Frame(hyp)
   hypf.place(x=0,y=0)
   btn_sinh=tkt.Button(hyp,text='sinh',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'sinh('))
   btn_sinh.grid(row=0,column=0)
   btn_cosh=tkt.Button(hyp,text='cosh',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'cosh('))
   btn_cosh.grid(row=0,column=1)
   btn_tanh=tkt.Button(hyp,text='tanh',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'tanh('))
   btn_tanh.grid(row=0,column=2)
   btn_csch=tkt.Button(hyp,text='csch',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'csch('))
   btn_csch.grid(row=1,column=0)
   btn_sech=tkt.Button(hyp,text='sech',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'sech('))
   btn_sech.grid(row=1,column=1)
   btn_coth=tkt.Button(hyp,text='coth',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'coth('))
   btn_coth.grid(row=1,column=2)
   hyp.mainloop()
def angle():
   ang=tkt.Tk()
   ang.title('Angle')
   ang.resizable(0,0)
   ang.geometry('155x55+0+0')
   angf=tkt.Frame(ang)
   angf.place(x=0,y=0)
   btn_deg=tkt.Button(ang,text='deg',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'degrees('))
   btn_deg.grid(row=0,column=0)
   btn_rad=tkt.Button(ang,text='rad',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addcons(txt,'radians('))
   btn_rad.grid(row=0,column=1)
   btn_close=tkt.Button(ang,text='close',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:ang.destroy())
   btn_close.grid(row=0,column=2)
   ang.mainloop()
#Buttons
b7=tkt.Button(btnframe,text='7',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,7))
b7.grid(row=1,column=0)
b8=tkt.Button(btnframe,text='8',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,8))
b8.grid(row=1,column=1)
b9=tkt.Button(btnframe,text='9',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,9))
b9.grid(row=1,column=2)
b6=tkt.Button(btnframe,text='6',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,6))
b6.grid(row=2,column=2)
b5=tkt.Button(btnframe,text='5',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,5))
b5.grid(row=2,column=1)
b4=tkt.Button(btnframe,text='4',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,4))
b4.grid(row=2,column=0)
b3=tkt.Button(btnframe,text='3',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,3))
b3.grid(row=3,column=2)
b2=tkt.Button(btnframe,text='2',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,2))
b2.grid(row=3,column=1)
b1=tkt.Button(btnframe,text='1',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,1))
b1.grid(row=3,column=0)
b0=tkt.Button(btnframe,text='0',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:addn(txt,0))
b0.grid(row=4,column=1)
b_pi=tkt.Button(btnframe,text='π',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:Addspl(txt,'π'))
b_pi.grid(row=4,column=0)
b_e=tkt.Button(btnframe,text='e',width=6,height=3,bg='#9368d9',cursor='hand2',command=lambda:Addspl(txt,'e'))
b_e.grid(row=4,column=2)
b_shift=tkt.Button(btnframe,text='shift',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:shift())
b_shift.grid(row=0,column=2)
b_sin=tkt.Button(btnframe,text='sin',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:trigfunc(txt,'sin'))
b_sin.grid(row=1,column=5)
b_cos=tkt.Button(btnframe,text='cos',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:trigfunc(txt,'cos'))
b_cos.grid(row=1,column=6)
b_tan=tkt.Button(btnframe,text='tan',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:trigfunc(txt,'tan'))
b_tan.grid(row=1,column=7)
b_cosec=tkt.Button(btnframe,text='cosec',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:trigfunc(txt,'cosec'))
b_cosec.grid(row=2,column=5)
b_sec=tkt.Button(btnframe,text='sec',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:trigfunc(txt,'sec'))
b_sec.grid(row=2,column=6)
b_cot=tkt.Button(btnframe,text='cot',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:trigfunc(txt,'cot'))
b_cot.grid(row=2,column=7)
b_lbk=tkt.Button(btnframe,text='(',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'('))
b_lbk.grid(row=5,column=1)
b_rbk=tkt.Button(btnframe,text=')',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,')'))
b_rbk.grid(row=5,column=2)
b_dec=tkt.Button(btnframe,text='.',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'.'))
b_dec.grid(row=5,column=0)
b_add=tkt.Button(btnframe,text='+',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'+'))
b_add.grid(row=1,column=3)
b_sub=tkt.Button(btnframe,text='-',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'-'))
b_sub.grid(row=2,column=3)
b_mul=tkt.Button(btnframe,text='*',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'*'))
b_mul.grid(row=3,column=3)
b_div=tkt.Button(btnframe,text='/',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'/'))
b_div.grid(row=4,column=3)
b_pow=tkt.Button(btnframe,text='^',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'**'))
b_pow.grid(row=6,column=0)
b_eq=tkt.Button(btnframe,text='=',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:eq())
b_eq.grid(row=5,column=3)
b_clr=tkt.Button(btnframe,text='C',width=6,height=3,bg='#5858f1',cursor='hand2',command=lambda:clear())
b_clr.grid(row=0,column=0)
b_del=tkt.Button(btnframe,text='D',width=6,height=3,bg='#5858f1',cursor='hand2',command=lambda:delete(txt))
b_del.grid(row=0,column=1)
b_ans=tkt.Button(btnframe,text='Ans',width=6,height=3,bg='#5858f1',cursor='hand2',command=lambda:hist())
b_ans.grid(row=0,column=5)
b_clrh=tkt.Button(btnframe,text='CH',width=6,height=3,bg='#5858f1',cursor='hand2',command=lambda:clearh())
b_clrh.grid(row=0,column=6)
b_log=tkt.Button(btnframe,text='log_e',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:logfunc(txt,'log'))
b_log.grid(row=3,column=5)
b_log10=tkt.Button(btnframe,text='log_10',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:logfunc(txt,'log10','10'))
b_log10.grid(row=3,column=6)
b_logx=tkt.Button(btnframe,text='log_x',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'log('))
b_logx.grid(row=3,column=7)
b_comma=tkt.Button(btnframe,text=',',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,','))
b_comma.grid(row=6,column=1)
b_P=tkt.Button(btnframe,text='nPr',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'P('))
b_P.grid(row=4,column=5)
b_C=tkt.Button(btnframe,text='nCr',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'C('))
b_C.grid(row=4,column=6)
b_fact=tkt.Button(btnframe,text='Fact',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'factorial('))
b_fact.grid(row=4,column=7)
b_sqrt=tkt.Button(btnframe,text='SqRt',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'sqrt('))
b_sqrt.grid(row=5,column=5)
b_cbrt=tkt.Button(btnframe,text='CbRt',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'cbrt('))
b_cbrt.grid(row=5,column=6)
b_nrt=tkt.Button(btnframe,text='nRoot',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'nRoot('))
b_nrt.grid(row=5,column=7)
b_fd=tkt.Button(btnframe,text="f'",width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,"f'("))
b_fd.grid(row=1,column=8)
b_x=tkt.Button(btnframe,text="x",width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,"x"))
b_x.grid(row=6,column=2)
b_fn=tkt.Button(btnframe,text='fn',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'fn('))
b_fn.grid(row=1,column=8)
b_aps=tkt.Button(btnframe,text="'",width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,"'"))
b_aps.grid(row=6,column=3)
b_help=tkt.Button(btnframe,text="?",width=6,height=3,bg='#5858f1',cursor='hand2',command=lambda:HELP())
b_help.grid(row=0,column=7)
b_const=tkt.Button(btnframe,text="Const",width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:const())
b_const.grid(row=2,column=8)
b_up=tkt.Button(btnframe,text="↑",width=6,height=1,bg='#ee9451',cursor='hand2',command=lambda:up())
b_up.place(x=156,y=0)
b_down=tkt.Button(btnframe,text="↓",width=6,height=1,bg='#ee9451',cursor='hand2',command=lambda:down())
b_down.place(x=156,y=30)
b_eqn=tkt.Button(btnframe,text='eqn',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'eqn('))
b_eqn.grid(row=3,column=8)
b_solve=tkt.Button(btnframe,text='solve',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'solve('))
b_solve.grid(row=4,column=8)
b_off=tkt.Button(btnframe,text='off',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:cal.destroy())
b_off.grid(row=0,column=8)
b_hyp=tkt.Button(btnframe,text='hyp',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:hyp())
b_hyp.grid(row=5,column=8)
b_random=tkt.Button(btnframe,text='random',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'random()'))
b_random.grid(row=6,column=5)
b_randint=tkt.Button(btnframe,text='randint',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'randint('))
b_randint.grid(row=6,column=6)
b_randrange=tkt.Button(btnframe,text='randrng',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:op(txt,'randrange('))
b_randrange.grid(row=6,column=7)
b_ang=tkt.Button(btnframe,text='angle',width=6,height=3,bg='#ee9451',cursor='hand2',command=lambda:angle())
b_ang.grid(row=6,column=8)
txt.mainloop()
