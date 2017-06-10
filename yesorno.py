import Tkinter
import random

class yesOrNo(Tkinter.Tk):
    responses = ['','','','']
    resultsFile = "data.csv"
    
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        self.columnconfigure(0,minsize=100)
        self.columnconfigure(1,minsize=100)
        self.rowconfigure(0,minsize=40)
        self.rowconfigure(1,minsize=40)
        self.rowconfigure(2,minsize=40)
        self.title("Yes or No?")

        title = Tkinter.Label(self,text="Yes...or No?")
        title.grid(column=0,row=0,columnspan=2,sticky='EW')
        
        self.labelVariable = Tkinter.StringVar()
        result = Tkinter.Label(self,textvariable=self.labelVariable)
        result.grid(column=0,row=1, columnspan=2)

        self.resizable(False, False)
        
        self.counter = 0
        
        yesBut = Tkinter.Button(self,text="Yes", command=self.onYesClick)
        noBut = Tkinter.Button(self,text="No", command=self.onNoClick)
        yesBut.grid(column=0, row=2)
        noBut.grid(column=1,row=2)

    def onYesClick(self):
        answer = rightAnswer()

        self.counter+=1
        self.responses[self.counter-1] = 'Y'
        if(answer == 1):
            self.labelVariable.set("Good job!")
            if(self.counter==3):
                self.end(1)
        else:
            self.labelVariable.set("Wrong!")
            self.end(0)

    def onNoClick(self):
        answer = rightAnswer()

        self.counter+=1
        self.responses[self.counter-1]='N'
        if(answer == 0):
            self.labelVariable.set("Good job!")
            if(self.counter == 3):
                self.end(1)
        else:
            self.labelVariable.set("Wrong!")
            self.end(0)

    def end(self,win):
        
        endWindow = Tkinter.Toplevel()
        endWindow.grid()
        endWindow.columnconfigure(0,minsize=75)
        endWindow.columnconfigure(1,minsize=75)
        endWindow.grab_set()
        
        endMessage = Tkinter.Label(endWindow,text="Game over!")
        endMessage.grid(column=0,row=0,columnspan=3)

        string = Tkinter.StringVar()
        winMessage = Tkinter.Label(endWindow,textvariable=string)
        winMessage.grid(column=0,row=1,columnspan=3)

        if(win == 1):
            string.set("You win!")
            self.responses[3] = 'W'
        else:
            string.set("You lose!")
            self.responses[3] = 'L'

        with open(self.resultsFile,'a') as f:
            f.write(self.responses[0]+','+self.responses[1]+','+self.responses[2]+','+self.responses[3]+'\n')
            f.close()

        endWindow.title(string.get())
        restartBut = Tkinter.Button(endWindow,text="Play Again?",command=self.restart)
        restartBut.grid(column=0,row=2)

        exitBut = Tkinter.Button(endWindow,text="Exit",command=self.destroy)
        exitBut.grid(column=2,row=2)

        statsBut = Tkinter.Button(endWindow,text="Statistics",command=self.stats)
        statsBut.grid(column=1,row=2)

    def restart(self):
        self.destroy()
        self.__init__(None)

    def stats(self):
        statsWindow = Tkinter.Toplevel()
        statsWindow.grid()
        statsWindow.grab_set()

        statsTitle = Tkinter.Label(statsWindow,text="Statistics")
        statsTitle.grid(column=0,row=0,columnspan=3)

        stats = calcStats(self.resultsFile)

        wins = Tkinter.Label(statsWindow,text="Wins: %d"%(stats[0]))
        wins.grid(column=0,row=1)
        losses = Tkinter.Label(statsWindow,text="Losses: %d"%(stats[1]))
        losses.grid(column=0,row=2)
        total = Tkinter.Label(statsWindow,text="Total: %d"%(stats[2]))
        total.grid(column=0,row=3)
        percent = stats[0]/float(stats[2]) * 100
        perc = Tkinter.Label(statsWindow,text="Win Percentage: %d"%(percent))
        perc.grid(column=0,row=4)
        ansyes = Tkinter.Label(statsWindow,text="Yes: %d"%(stats[3]))
        ansyes.grid(column=2,row=1)
        ansno = Tkinter.Label(statsWindow,text="No: %d"%(stats[4]))
        ansno.grid(column=2,row=2)
        chy = Tkinter.Label(statsWindow,text="Chose Yes: %d"%(stats[5]))
        chy.grid(column=2,row=3)
        chn = Tkinter.Label(statsWindow,text="Chose No: %d"%(stats[6]))
        chn.grid(column=2,row=4)
        curst = Tkinter.Label(statsWindow,text="Current Streak: ")
        curst.grid(column=0,row=5,columnspan=3)
        
        restartBut = Tkinter.Button(statsWindow,text="Play Again?",command=self.restart)
        restartBut.grid(column=0,row=6)

        fameBut = Tkinter.Button(statsWindow,text="Hall of Fame",command=self.fame)
        fameBut.grid(column=1, row=6)

        exitBut = Tkinter.Button(statsWindow,text="Exit",command=self.destroy)
        exitBut.grid(column=2,row=6)

    def fame(self):
        print("BLAH")

def rightAnswer():
    random.seed()
    return random.randint(0,1)

def calcStats(statsFile):
    f=open(statsFile,'r')
    lines = f.readlines()
    f.close
    
    win=0
    loss=0
    tot=0
    yes=0
    no=0
    ansy=0
    ansn=0

    for line in lines:
        chars = line.split(',')
        prev = ''
        for char in chars:
            if(char == 'Y'):
                ansy+=1
            elif (char=='N'):
                ansn+=1
            elif (char == 'W\n'):
                win+=1
                tot+=1
            elif (char == 'L\n'):
                loss+=1
                tot+=1
                if(prev == 'N'):
                    yes+=1
                elif (prev == 'Y'):
                    no+=1
            elif (char == ''):
                if(prev == 'Y'):
                    no +=1
                elif (prev == 'N'):
                    yes +=1
            prev = char
    return [win, loss, tot, yes, no, ansy, ansn]
                
    

if __name__ == "__main__":
    app = yesOrNo(None)
    app.mainloop()
