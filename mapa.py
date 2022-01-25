import tkinter

canvas=tkinter.Canvas(width=1024,height=521)
canvas.pack()

mapa=tkinter.PhotoImage(file="mapaSR.gif")
canvas.create_image(512,260.5,image=mapa)

x=0
y=0
p=canvas.create_text(100,100,text="AHOJ")

def klik(e):

    global x,y
    x=e.x
    y=e.y

def hyb(e):
    global x,y
    canvas.itemconfig(p,text=str(((x-e.x)**2+(y-e.y)**2)**.5*0.56))
    canvas.delete("cara")
    canvas.create_line(x,y,e.x,e.y,tag="cara")

canvas.bind("<Button-1>",klik)
canvas.bind("<B1-Motion>",hyb)

tkinter.mainloop()

