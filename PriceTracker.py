import tkinter
w=tkinter.Tk(className="Stock & Option Price Tracker")
w.geometry('600x200')
priceFrame=tkinter.Frame(w,borderwidth=2,height=150,width=130,bg='#ccffcc')
priceFrame.pack()
alertFrame=tkinter.Frame(w,borderwidth=2,height=50,width=30)
w.mainloop()
