'''
Created on May 26, 2019

@author: jpeuker
'''

import tkinter

class AppFrame:
    def __init__(self, mover, speed):
        self.mover = mover
        self.speed = speed
        self.run = False
        
        self.initRoot()
        self.initButton()
        
    def initRoot(self):
        self.root = tkinter.Tk()
        self.root.title('El raton bailando')
        w = 260
        h = 50
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/5) - (w/2)
        y = (hs/5) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.root.configure(bg='blue')
        
    def initButton(self):
        self.button = tkinter.Button(self.root, 
                text="bailando", 
                bg="yellow",
                activebackground="DeepPink2",
                relief="raised", 
                command=self.bailando)
        self.button.config(highlightbackground="DeepPink3")
        self.button.place(relx=.5, rely=.5, anchor="c")

    def bailando(self):
        if self.button.config('relief')[-1] == 'raised':
            self.button.config(relief="sunken")
            self.button.config(text="duerme")
            self.run = True
            self.moveLoop()
        else:
            self.run = False
            self.button.config(relief="raised")
            self.button.config(text="bailando")
    
    def moveLoop(self):
        if self.run:
            self.mover.move()
            self.root.after(self.speed, self.moveLoop)
    
    def runApp(self):
        self.root.mainloop()