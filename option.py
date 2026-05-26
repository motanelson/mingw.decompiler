import tkinter as tk




class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("option")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.label=tk.Label(background="black",foreground="white",text="click me")
        self.label.pack(padx=10,pady=10)
        self.canvas=tk.Canvas(background="black",width=40,height=40)
        self.canvas.pack(padx=10,pady=10)
        self.c1=self.canvas.create_oval(10,10,40-10,40-10,fill="white")
        self.canvas.bind("<Button-1>",self.clicks)
    def clicks(self,event):
        if self.c1!=None:
            self.canvas.delete(self.c1)
            self.c1=None
        else: 
            self.c1=self.canvas.create_oval(10,10,40-10,40-10,fill="white")



root=tk.Tk()
apps=myapps(root)
root.mainloop()
