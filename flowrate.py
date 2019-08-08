
from tkinter import *
import tkinter as tk
from functools import partial

# the title of the program
root=tk.Tk()
root.title('FLOW RATE CALCULATOR')
root.geometry('700x500')

labeltitle=tk.Label(root, text="FLOW RATE CALCULATOR", fg= 'purple', font=('Arial black',18, 'bold'))
labeltitle.grid(row=1, sticky='news')

# below are different function used for calculating the needed resultdef hydraulic_diameter(labelresult,l,b,p,f,g,j,k,m,o,q):
  
def reynold (labelresult2,l,b,p,f):
    width=(l.get())
    height=(b.get())
    density=(p.get())
    flowrate=(f.get())
    
    lenght=(g.get())
    K=(j.get())
    roughness=(k.get())
    viscocity=(m.get())
    g=(o.get())
    Cp=(q.get())
    
    mean_velocity=float(flowrate)/(float(width)*float(height))
    hydraulic_diameter=(2*float(width)*float(height))/(float(width)+float(height))
    Reynolds_number=float(mean_velocity)*float(hydraulic_diameter)*float(density)/viscocity
    labelresult2.config(text="THE REYNOLDS NUMBER IS %f" % Reynolds_number)

    return
# calculating the throat area
def ThroatArea(labelresult3,a):
    throatdiameter=a.get()
    Throatarea=3.142*throatdiameter**2/4
    labelresult3.configure(text="%f" %Throatarea)
    return
def PipeArea(labelresult4,b):
    pipediameter=b.get()
    PipeArea=3.142*(pipediameter**2)/4
    labelresult4.config(text="%f" % PipeArea)
    return
def flowrate(labelresult5,a,b,c,d,e):
    throatdiamter=a.get()
    pipediameter=b.get()
    P1=c.get()
    P2=d.get()
    den=e.get()
    if den==1:
        DENSITY=1000
    elif den==2:
        DENSITY=748.9
    elif den==3:
        DENSITY=1295
    elif den==4:
        DENSITY=872.5
    PipeArea=3.142*(throatdiamter**2)/4
    Throatarea=3.142*(pipediameter**2)/4
    h=  (P1-P2)/(DENSITY*9.81)
    K=PipeArea/Throatarea
    g=2*9.81*h
    f=(K**2)-1
    m=(g/f)**1/2
    Flowrate=PipeArea*m
    labelresult5.configure(text="%f" % Flowrate)

# label values for the parameter    
W=tk.Label(root,text='PRESSURE OF FLUID, P1 (IN Pa)', fg='dark green', font=('Arial black',10, 'bold'))
H=tk.Label(root,text='PESSURE OF THROAT, P2(IN Pa)', fg='dark green', font=('Arial black',10, 'bold'))
P=tk.Label(root,text='PIPE DIAMETER, D1(IN METRES)', fg='dark green', font=('Arial black',10, 'bold'))
F=tk.Label(root,text='THROAT DIAMETER, D2 (IN METRES)', fg='dark green', font=('Arial black',10, 'bold'))

# variables for assigning the entry value inputed by the user
num1=tk.DoubleVar()
num2=tk.DoubleVar()
num3=tk.DoubleVar()
num4=tk.DoubleVar()
num1.set(150000.0)
num2.set(-53328.95)
num3.set(0.3)
num4.set(0.1)


# Labelling Entry value for each input
entry1=tk.Entry(root, textvariable=num1)
entry2=tk.Entry(root, textvariable=num2)
entry3=tk.Entry(root, textvariable=num3)
entry4=tk.Entry(root, textvariable=num4)


# arranging the label
W.grid(row=4, sticky=N)
H.grid(row=6, sticky=N)
P.grid(row=8, sticky=N)
F.grid(row=10, sticky=N)



# arranging the entry
entry1.grid(row=4, column=1)
entry2.grid(row=6, column=1)
entry3.grid(row=8, column=1)
entry4.grid(row=10, column=1)

#creating radio button
v=tk.IntVar()
v.set(1)
# label for the radio button
tk.Label(root, text="choose type of fluid passing through the pipe", justify=tk.LEFT, padx=20).grid(row=2, column=34)
# radio button
tk.Radiobutton(root, text='Air', padx=20, variable=v, value=1).grid(row=4, column=34)
tk.Radiobutton(root, text='Petrol', padx=20, variable=v, value=2).grid(row=6, column=34)
tk.Radiobutton(root, text='R134a', padx=20, variable=v, value=3).grid(row=8, column=34)
tk.Radiobutton(root, text='Engine', padx=20, variable=v, value=4).grid(row=10, column=34)



labelresult3=tk.Label(root,fg='blue', font=('Arial black',10, 'bold'))
labelresult3.grid(row=62,column=10 )
labelresult4=tk.Label(root,fg='blue',font=('Arial black',10, 'bold'))
labelresult4.grid(row=64, column=10)
labelresult5=tk.Label(root,fg='blue', font=('Arial black',10, 'bold'))
labelresult5.grid(row=66,column=10 )

# reset button
def reset():
    num1.set(0.0)
    num2.set(0.0)
    num3.set(0.0)
    num4.set(0.0)
    v.set(1)
    labelresult3.config(text='')
    labelresult4.config(text='')
    labelresult5.config(text='')


    
    

reset1=Button(text='RESET ALL!', command=reset,fg='blue', bg='yellow', font=('Arial black',10, 'bold') )
reset1.grid(row=200, sticky=N)

#for hydraulic diameter


#for reynolds calculation
call_result2=partial(ThroatArea,labelresult3,num3)
call_result3=partial(PipeArea,labelresult4,num4)
call_result4=partial(flowrate,labelresult5,num3, num4, num1,num2,v)
tk.Label(root).grid(row=61,sticky=N)
Rbutton=tk.Button(root, text='AREA OF THROAT DIAMETER', command=call_result2,bg= 'dark green', fg='gold',font=('Arial black',10, 'bold', 'underline'), height=1, width=25, )
Rbutton.grid(row=62, sticky=N)
tk.Label(root).grid(row=63,sticky=N)
ebutton=tk.Button(root, text='AREA OF PIPE DIAMETER', command=call_result3,bg= 'dark green', fg='gold',font=('Arial black',10, 'bold', 'underline'), height=1, width=25, )
ebutton.grid(row=64, sticky=N)
tk.Label(root).grid(row=65,sticky=N)
ebutton=tk.Button(root, text='FLOW RATE ', command=call_result4,bg= 'dark green', fg='gold',font=('Arial black',10, 'bold', 'underline'), height=1, width=20, )
ebutton.grid(row=66, sticky=N)
tk.Label(root).grid(row=67,sticky=N)



                   

root.mainloop()
