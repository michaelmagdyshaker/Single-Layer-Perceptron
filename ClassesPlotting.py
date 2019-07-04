import matplotlib.pyplot as plt
import os
import numpy as np

Input_Loc = ('D:\\College\\Semester 2\\Neural Networks\\Task 1\\')

File=open(Input_Loc+"IrisData.txt")
Lines = File.readlines()
i=0
ListOfRecords=list()

for EachLine in Lines:
    if i==0:
        i = i + 1
    else:
            X1=(EachLine.split(','))[0]
            X2 =(EachLine.split(','))[1]
            X3=(EachLine.split(','))[2]
            X4=(EachLine.split(','))[3]
            Label = (EachLine.split(','))[4]
            if Label=='Iris-setosa\n':
                Cluster="C1"
            if Label=='Iris-versicolor\n':
                Cluster='C2'
            if Label=='Iris-virginica\n':
                Cluster='C3'
            Record=dict(X1=X1, X2=X2, X3=X3, X4=X4,Label=Cluster,Index=i)
            ListOfRecords.append(Record)
            i = i + 1

# ListOfRecords=np.array(ListOfRecords)
# for i in ListOfRecords:
#     if (i["Label"]=="C1"):
#         print (i)
#
mode1=mode2=mode3=mode4=mode5=mode6=0
mode3=1


X1Graph=list()#X1 for C1
X2Graph=list()#X1 for C2
X3Graph=list()
Y1Graph=list()#X2 for C1
Y2Graph=list()
Y3Graph=list()

if mode1==1:
    for I in ListOfRecords:
        if (I["Label"] == "C1"):
            X1Graph.append(I["X1"])
            Y1Graph.append(I["X2"])
        if (I["Label"] == "C2"):
            X2Graph.append(I["X1"])
            Y2Graph.append(I["X2"])
        if (I["Label"] == "C3"):
            X3Graph.append(I["X1"])
            Y3Graph.append(I["X2"])
elif mode2 ==1:
    for I in ListOfRecords:
        if (I["Label"] == "C1"):
            X1Graph.append(I["X1"])
            Y1Graph.append(I["X3"])
        if (I["Label"] == "C2"):
            X2Graph.append(I["X1"])
            Y2Graph.append(I["X3"])
        if (I["Label"] == "C3"):
            X3Graph.append(I["X1"])
            Y3Graph.append(I["X3"])
elif mode3 ==1:
    for I in ListOfRecords:
        if (I["Label"] == "C1"):
            X1Graph.append(I["X1"])
            Y1Graph.append(I["X4"])
        if (I["Label"] == "C2"):
            X2Graph.append(I["X1"])
            Y2Graph.append(I["X4"])
        if (I["Label"] == "C3"):
            X3Graph.append(I["X1"])
            Y3Graph.append(I["X4"])
elif mode4 ==1:
    for I in ListOfRecords:
        if (I["Label"] == "C1"):
            X1Graph.append(I["X2"])
            Y1Graph.append(I["X3"])
        if (I["Label"] == "C2"):
            X2Graph.append(I["X2"])
            Y2Graph.append(I["X3"])
        if (I["Label"] == "C3"):
            X3Graph.append(I["X2"])
            Y3Graph.append(I["X3"])
elif mode5 ==1:
    for I in ListOfRecords:
        if (I["Label"] == "C1"):
            X1Graph.append(I["X2"])
            Y1Graph.append(I["X4"])
        if (I["Label"] == "C2"):
            X2Graph.append(I["X2"])
            Y2Graph.append(I["X4"])
        if (I["Label"] == "C3"):
            X3Graph.append(I["X2"])
            Y3Graph.append(I["X4"])
elif mode6 ==1:
    for I in ListOfRecords:
        if (I["Label"] == "C1"):
            X1Graph.append(I["X3"])
            Y1Graph.append(I["X4"])
        if (I["Label"] == "C2"):
            X2Graph.append(I["X3"])
            Y2Graph.append(I["X4"])
        if (I["Label"] == "C3"):
            X3Graph.append(I["X3"])
            Y3Graph.append(I["X4"])




plt.figure('fig1')
plt.scatter(X1Graph,Y1Graph)
plt.scatter(X2Graph,Y2Graph)
plt.scatter(X3Graph,Y3Graph)
plt.xlabel('feature1')
plt.ylabel('feature2')
plt.show()
