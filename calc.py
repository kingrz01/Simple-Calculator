#simple calculator

from tkinter import*
import math

cal = Tk() #create GUI
cal.title("CALC") #calculator Title
cal.geometry('250x500')
screen = "" #Empty screen
text_Input =StringVar() #temp input
bgc = '#E3E3E3'   #default beckground color
bgc2 = '#FDFDFD'   #beckground color
cal_font = ('calibri', 20) #default font
cal_font2 = ('calibri', 20 ,'bold')  

#function to update dispaly
def click(br):
    global screen
    screen = screen + str(br)
    text_Input.set(screen)

#function to clear display
def clear():
    global screen
    screen = ""
    text_Input.set("")

#function to evaluate display
def evaluate():
    global screen
    screen = str(eval(screen))
    text_Input.set(screen)

#function for square
def power2():
    global screen
    screen = str(eval(screen)**2)
    text_Input.set(screen)

#function for square root
def sqr():
    global screen
    screen = str(math.sqrt(eval(screen)))
    text_Input.set(screen)
    
#function for +/-
def change():
    global screen
    screen = str(eval(screen)*(-1))
    text_Input.set(screen)

display = Entry(cal, font=cal_font, textvariable = text_Input, bd=8, insertwidth=2,
                   bg=bgc, justify= 'right')
display.pack(expand=TRUE, fill=BOTH) #first object, with option to expand/shrink

btn_row1 = Frame(cal)
btn_row1.pack(expand=TRUE, fill=BOTH)
btn_sqr = Button(btn_row1, width=1, height=1, fg='black', font=cal_font, text="SQR", bg=bgc, command=sqr)
btn_X2 = Button(btn_row1, width=1, height=1, fg='black', font=cal_font, text="X2", bg=bgc, command=power2)
C = Button(btn_row1, width=1, height=1, fg='black', font=cal_font, text="CE", bg=bgc, command=clear)
devide = Button(btn_row1, width=1, height=1, fg='black', font=cal_font, text="/", bg=bgc, command=lambda:click("/"))
row1 = (btn_sqr,btn_X2,C,devide)

btn_row2 = Frame(cal)
btn_row2.pack(expand=TRUE, fill=BOTH)
btn_7 = Button(btn_row2, width=1, height=1, fg='black', font=cal_font2, text="7", bg=bgc2, command=lambda:click(7))
btn_8 = Button(btn_row2, width=1, height=1, fg='black', font=cal_font2, text="8", bg=bgc2, command=lambda:click(8))
btn_9 = Button(btn_row2, width=1, height=1, fg='black', font=cal_font2, text="9", bg=bgc2, command=lambda:click(9))
multiply = Button(btn_row2, width=1, height=1, fg='black', font=cal_font, text="*", bg=bgc, command=lambda:click("*"))
row2 = (btn_7,btn_8,btn_9,multiply)

btn_row3 = Frame(cal)
btn_row3.pack(expand=TRUE, fill=BOTH)
btn_4 = Button(btn_row3, width=1, height=1, fg='black', font=cal_font2, text="4", bg=bgc2, command=lambda:click(4))
btn_5 = Button(btn_row3, width=1, height=1, fg='black', font=cal_font2, text="5", bg=bgc2, command=lambda:click(5))
btn_6 = Button(btn_row3, width=1, height=1, fg='black', font=cal_font2, text="6", bg=bgc2, command=lambda:click(6))
minus = Button(btn_row3, width=1, height=1, fg='black', font=cal_font, text="-", bg=bgc, command=lambda:click("-"))
row3 = (btn_4,btn_5,btn_6,minus)

btn_row4 = Frame(cal)
btn_row4.pack(expand=TRUE, fill=BOTH)
btn_1 = Button(btn_row4, width=1, height=1, fg='black', font=cal_font2, text="1", bg=bgc2, command=lambda:click(1))
btn_2 = Button(btn_row4, width=1, height=1, fg='black', font=cal_font2, text="2", bg=bgc2, command=lambda:click(2))
btn_3 = Button(btn_row4, width=1, height=1, fg='black', font=cal_font2, text="3", bg=bgc2, command=lambda:click(3))
plus = Button(btn_row4, width=1, height=1, fg='black', font=cal_font, text="+", bg=bgc, command=lambda:click("+"))
row4 = (btn_1,btn_2,btn_3,plus)

btn_row5 = Frame(cal)
btn_row5.pack(expand=TRUE, fill=BOTH)
change = Button(btn_row5, width=1, height=1, fg='black', font=cal_font2, text="+/-", bg=bgc2, command=change)
btn_0 = Button(btn_row5, width=1, height=1, fg='black', font=cal_font2, text="0", bg=bgc2, command=lambda:click(0))
C = Button(btn_row5, width=1, height=1, fg='black', font=cal_font2, text=",", bg=bgc2, command=lambda:click(','))
evaluate = Button(btn_row5, width=1, height=1, fg='black', font=cal_font, text="=", bg=bgc, command=evaluate)
row5 = (change,btn_0,C,evaluate)

for ls in row1,row2,row3,row4,row5: #buttons of each frame, starting form left side with option with option to expand/shrink
    for row in ls:
        row.pack(side=LEFT, expand=TRUE, fill=BOTH)
        
cal.mainloop()
