from tkinter import *
import NN_Algo
def main():
    GUI()


def GUI():
    top = Tk()
    top.geometry("500x500")
    var=StringVar()
    var.set("choose 2 features")
    featureLabel=Label(top,textvariable=var,anchor=NW)
    featureLabel.pack()


    featureListbox=Listbox(top)
    featureListbox.insert(1,"X1 & X2")
    featureListbox.insert(2, "X1 & X3")
    featureListbox.insert(3, "X1 & X4")
    featureListbox.insert(4, "X2 & X3")
    featureListbox.insert(5, "X2& X4")
    featureListbox.insert(6, "X3 & X4")

    featureListbox.pack()

    var = StringVar()
    var.set("choose 2 classes")
    classLabel = Label(top, textvariable=var, anchor=NW)
    classLabel.pack()
    ClassLb=Listbox(top)
    ClassLb.insert(1,"C1 & C2")
    ClassLb.insert(2,"C1 & C3")
    ClassLb.insert(3,"C2 & C3")

    ClassLb.pack()

    var = StringVar()
    var.set("select there is bias or not")
    bais = Label(top, textvariable=var, anchor=NW)
    bais.pack()
    baisLB = Listbox(top)
    baisLB.insert(1, "yes")
    baisLB.insert(2, "no")
    baisLB.pack()

    var = StringVar()
    var.set("epochs")
    epoch = Label(top, textvariable=var, anchor=NW)
    epoch.pack()

    epochTextbox=Text(top,height=3,width=10)
    epochTextbox.pack()

    var = StringVar()
    var.set("learning rate")
    learningRate = Label(top, textvariable=var, anchor=NW)
    learningRate.pack()

    LearningRateTextbox = Text(top, height=3, width=10)
    LearningRateTextbox.pack()

    B=Button(top,text="Run",command=Run())################################# function run call function main of neural file

    top.mainloop()

def Run(Feature1,Feature2,Class1,Class2,Bias,Epochs,LearningRate):
    NN_Algo.main(Feature1,Feature2,Class1,Class2,Bias,Epochs,LearningRate)


main()