from tkinter import * 
from PIL import Image, ImageTk
from calculator import evaluar


class mainWindowCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.resizable(False, False)
        self.root.geometry('300x150')
        self.root.attributes('-alpha', 0.7)
        self.createElements()
    
    def createElements(self):
        #Fondo
        self.pillImage = Image.open("cat.png")
        image = self.pillImage.resize((300,150))
        self.image = ImageTk.PhotoImage(image)
        backGround = Label(self.root, image=self.image)
        backGround.place(x=0, y=0)

        welcome = Label(self.root, text='Hi. Welcome to my Calculator.', font=('Arial 10 bold'), foreground='black')
        welcome.pack(pady=(20, 10))

        button_frame = Frame(self.root)
        button_frame.pack(pady=(20, 0), padx=10)

        closeWindowButton = Button(button_frame, text='Close window', font=('Arial 10 bold'), command=lambda: self.root.destroy())
        closeWindowButton.pack(padx=(0, 5), side=LEFT)

        goCalculator = Button(button_frame, text='Open calculator', font=('Arial 10 bold'), command=lambda: calculatorWindow(self))
        goCalculator.pack(padx=(5, 0), side=LEFT)

class calculatorWindow:
    def __init__(self, mainWindow):
        self.parent = Toplevel(mainWindow.root)
        self.parent.title(mainWindow.root.title())
        self.parent.resizable(False, False)
        self.parent.geometry('250x300')
        self.parent.attributes('-alpha', 0.7)
        self.ecuacion = ''
        self.results = ''

        self.createElements(mainWindow)

        self.label()
        self.buttonsGenerator()
        self.buttonSymbol()

        mainWindow.root.withdraw()

    def label(self):
        self.results = Label(self.parent, bd=5, relief="solid", font=('Arial 10 bold'))
        self.results.place(x=10, y=10, width=230, height=50)

    def ecuation(self, value):
        self.ecuacion += str(value)
        self.results.config(text=self.ecuacion)

    def calcular(self, arguments):
        self.ecuacion = evaluar(arguments)
        if self.ecuacion['ok'] == False:
            self.results.config(text=self.ecuacion['error'])
            self.parent.after(3000, lambda: self.results.config(text=''))
            self.ecuacion = ''
        else:
            self.ecuacion = str(self.ecuacion['result'])
            self.results.config(text=self.ecuacion)
            
    def createElements(self, mainWindow):

        #Fondo
        image = mainWindow.pillImage
        image = image.resize((250,300))
        self.image = ImageTk.PhotoImage(image)
        image = Label(self.parent, image=self.image)
        image.place(x=0, y=0)

        frameButton = Frame(self.parent)
        frameButton.pack(side=BOTTOM)

        goBackToMain = Button(frameButton, text='Close Window', font=('Arial 10 bold'), command=lambda: self.closeWindow(mainWindow))
        goBackToMain.pack(padx=(0,5), side=LEFT)

        closeSession = Button(frameButton, text='Close Calculator', font=('Arial 10 bold'), command=lambda: mainWindow.root.destroy())
        closeSession.pack(padx=(5, 0), side=LEFT)

        sendButton = Button(self.parent, text='=', font=('Arial 10 bold'), command=lambda: self.calcular(self.ecuacion))
        sendButton.place(x=110, y=220, width=40, height=40)

        delButton = Button(self.parent, text='AC', font=('Arial 10 bold'), command= lambda: self.ac())
        delButton.place(x=10, y=220, width=40, height=40)

    def buttonsGenerator(self):
        yPosition = 70
        xPosition = 10
        for button in range(9, -1, -1):
            if button % 3  == 0 and button != 9:
                xPosition = 10
                yPosition += 50
            if button == 0:
                xPosition += 50 
            buttonGen = Button(self.parent, text=f'{button}', font=('Arial 10 bold'), command=lambda b=button: self.ecuation(b))
            buttonGen.place(x=xPosition, y=yPosition, width=40, height=40)
            xPosition += 50
    
    def buttonSymbol(self): 
        yPosition = 70
        for symbol in ['+', '-', '/', '*']:
            buttonGen = Button(self.parent, text=f'{symbol}', font=('Arial 10 bold'), command=lambda b=symbol: self.ecuation(b))
            buttonGen.place(x=160, y=yPosition, width=80, height=40)
            yPosition += 50

    def closeWindow(self, mainWindow):
        self.parent.destroy()
        mainWindow.root.deiconify()


mainWindow = Tk()
logic = mainWindowCalculator(mainWindow)
mainWindow.mainloop()