from tkinter import *
import tkinter.ttk as ttk
import NN_Algo
top = Tk()
top.title("Single layer")
top.geometry("400x400")

# def Run(Feature1,Feature2,Class1,Class2,Bias,Epochs,LearningRate):
#     NN_Algo.main(Feature1,Feature2,Class1,Class2,Bias,Epochs,LearningRate)

def get_entries():
    # feature1_input=Feature1listbox.get(Feature1listbox.curselection())
    feature1_input=box.get()
    feature2_input=box2.get()
    class1_input=box3.get()
    class2_input=box4.get()
    print (feature1_input,feature2_input,class1_input,class2_input)
    eta_input=float(eta_textfield.get('1.0',END))

    epoch_input=int(epoch_textfield.get('1.0',END))
    if (var1.get()==1):
        baisboolen=True
    elif(var2.get()==1):
        baisboolen=False
    #print (baisboolen)
    # print (feature1_input,feature2_input,class1_input,class2_input,baisboolen,epoch_input,eta_input)
    # return feature1_input,feature2_input,class1_input,class2_input,baisboolen,epoch_input,eta_input
    NN_Algo.main(feature1_input,feature2_input,class1_input,class2_input,baisboolen,epoch_input,eta_input)


#Label
FeaturesLabel=Label(top,text="Select First Feature",font=("Times New Roman",12),justify=LEFT)
FeaturesLabel.grid(column=0,row=0)

#Combobox
box=StringVar()
cbFeature1=ttk.Combobox(top,textvariable=box,values=("X1","X2","X3","X4"))
cbFeature1.set("X1")
cbFeature1.grid(column=1,row=0)

#Label
Features2label=Label(top,text="Select Second Feature",font=("Times New Roman",12),justify=LEFT)
Features2label.grid(column=0,row=1)

# Feature2listbox=Listbox(top,height=2,width=2,exportselection=0)
# Feature2listbox.grid(column=1,row=1)
# Feature2listbox.insert(END)
#
# # scrollbar2=Scrollbar(command=Feature2listbox.yview,orient="vertical")
# # scrollbar2.grid(column=5,row=0)
# # Feature2listbox.config(yscrollcommand=scrollbar2.set)
#
# for item in ["X1", "X2", "X3", "X4"]:
#     Feature2listbox.insert(END, item)
box2=StringVar()
cbFeature2=ttk.Combobox(top,textvariable=box2,values=("X1","X2","X3","X4"))
cbFeature2.set("X1")
cbFeature2.grid(column=1,row=1)
#same for classes but on the right of it
#Label
ClassLabel=Label(top,text="Select First Class",font=("Times New Roman",12),justify=LEFT)
ClassLabel.grid(column=0,row=2)

#listbox
# Class1listbox=Listbox(top,height=2,width=2,exportselection=0)
# Class1listbox.grid(column=1,row=2)
# Class1listbox.insert(END)
#
# #
# # sc1=Scrollbar(command=Class1listbox.yview,orient="vertical")
# # sc1.grid(column=2,row=1,sticky=NS)
# # Class1listbox.config(yscrollcommand=sc1.set)
#
# for item in ["C1", "C2", "C3"]:############################################################################3
#     Class1listbox.insert(END, item)
box3=StringVar()
Class1cb=ttk.Combobox(top,textvariable=box3,values=("C1","C2","C3"))
Class1cb.set("C1")
Class1cb.grid(column=1,row=2)

#Label
Class2Label=Label(top,text="Select Second Class",font=("Times New Roman",12),justify=LEFT)
Class2Label.grid(column=0,row=3)

# Class2listbox=Listbox(top,height=2,width=2,exportselection=0)
# Class2listbox.grid(column=1,row=3)
# Class2listbox.insert(END)
# #
# # sc2=Scrollbar(command=Class2listbox.yview,orient="vertical")
# # sc2.grid(column=5,row=1,sticky=NS)
# # Class2listbox.config(yscrollcommand=sc2.set)
#
# for item in ["C1", "C2", "C3"]:
#     Class2listbox.insert(END, item)
box4=StringVar()
Class2cb=ttk.Combobox(top,textvariable=box4,values=("C1","C2","C3"))
Class2cb.set("C1")
Class2cb.grid(column=1,row=3)
#

#label for learning rate
eta=Label(top,text="Enter Learning Rate",font=("Times New Roman",12),justify=LEFT)
eta.grid(column=0,row=4)
#textbox
eta_textfield=Text(top,width=15,height=1)
eta_textfield.grid(column=1,row=4)


#label for number of epochs
epoch=Label(top,text="Enter Epochs Number",font=("Times New Roman",12),justify=LEFT)
epoch.grid(column=0,row=5)
#textbox
epoch_textfield=Text(top,width=15,height=1)
epoch_textfield.grid(column=1,row=5)


#label for bais
bais=Label(top,text="Select Bias Or No Bias",font=("Times New Roman",12),justify=LEFT)
bais.grid(column=0,row=6)
#checkbox
var1 = IntVar()
Checkbutton(top, text="Bias", variable=var1).grid(column=1,row=6)
var2 = IntVar()
Checkbutton(top, text="No Bias", variable=var2).grid(column=2,row=6)

button=Button(top,text="RUN",command=get_entries)
button.grid(column=0,row=8)


top.mainloop()

