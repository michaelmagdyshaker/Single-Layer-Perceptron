import numpy as np
import random
import matplotlib.pyplot as plt
import math
#from sklearn.metrics import mean_squared_error
import os


def ChooseAndShuffle(C1,C2):
    firstC=C1
    secondC=C2
    train="True"
    File = open("IrisData.txt")
    Lines = File.readlines()
    i = 0
    ListOfRecords = list()
    firstThirty=0
    for EachLine in Lines:
        if i == 0:
            i = i + 1
        else:
            X1 = (EachLine.split(','))[0]
            X2 = (EachLine.split(','))[1]
            X3 = (EachLine.split(','))[2]
            X4 = (EachLine.split(','))[3]
            Label = (EachLine.split(','))[4]
            if Label == 'Iris-setosa\n':
                Cluster = "C1"
            if Label == 'Iris-versicolor\n':
                Cluster = 'C2'
            if Label == 'Iris-virginica\n':
                Cluster = 'C3'

            Record = dict(X1=X1, X2=X2, X3=X3, X4=X4, Label=Cluster, Index=i)
            ListOfRecords.append(Record)
            mod=i%50
            i = i + 1
            Line=Record["X1"]+','+ Record["X2"]+','+ Record["X3"]+','+ Record["X4"]+','+ Record["Label"]+'\n'#  to change the format of the dict
            if ((mod <31 and mod !=0 )and (Cluster==firstC or Cluster==secondC)):
                with open("TrainFile.txt", "a") as f:
                    f.writelines(Line)
            elif((mod >=31 or mod ==0  ) and (Cluster==firstC or Cluster==secondC)):
                with open("TestFile.txt", "a") as f:
                    f.writelines(Line)
    with open("TrainFile.txt") as f:
        lines = f.readlines()
    random.shuffle(lines)
    with open("TrainFile.txt", "w") as f:
        f.writelines(lines)
    # with open("TestFile.txt") as f:
    #     lines = f.readlines()
    # random.shuffle(lines)
    # with open("TestFile.txt", "w") as f:
    #     f.writelines(lines)

def ChooseFeatures (F1,F2,class1,class2,Filename):
    FirstFeatureList=list()
    SecodFeatureList=list()
    LabelList=list()
    ThisnewLabel=list()
    # File = open("TrainFile.txt")
    File=open(Filename)
    Lines = File.readlines()
    for eachline in Lines:
        X1 = (eachline.split(','))[0]
        X2 = (eachline.split(','))[1]
        X3 = (eachline.split(','))[2]
        X4 = (eachline.split(','))[3]
        ThisLabel=(eachline.split(','))[4]
        if ThisLabel==class1 + "\n":
            ThisnewLabel=1 ##############################333 -1 wnfs el klam el test ############ n2as 7war ino a7tfz bel class dah nfso
        elif ThisLabel==class2 + "\n":
            ThisnewLabel=-1

        if (F1 == "X1"):
            FirstFeatureList.append(float(X1))
        if (F1 == "X2"):
            FirstFeatureList.append(float(X2))
        if (F1 == "X3"):
            FirstFeatureList.append(float(X3))
        if (F1 == "X4"):
            FirstFeatureList.append(float(X4))
        if (F2 == "X1"):
            SecodFeatureList.append(float(X1))
        if (F2 == "X2"):
            SecodFeatureList.append(float(X2))
        if (F2 == "X3"):
            SecodFeatureList.append(float(X3))
        if (F2 == "X4"):
            SecodFeatureList.append(float(X4))
        #print (ThisLabel)
        LabelList.append(ThisnewLabel)
    return (FirstFeatureList,SecodFeatureList,LabelList)

def InputMatrixConstructor(F1,F2,BooleanBias):
    Input_Matrix=np.empty([60,3],dtype=float)
    if BooleanBias == True:
        Bias = 1
    elif BooleanBias == False:
        Bias=0
    for i in range(0,60):
        Input_Matrix[i][0] =Bias
        Input_Matrix[i][1]=F1[i]
        Input_Matrix[i][2]=F2[i]

    return Input_Matrix
#def WeightMatrixConstructor(Bias):
def WeightMatrixConstructor():
    WeightMatrix=np.empty([3,1],dtype=float)
    # Weight1=np.random.rand(1,1)
    # Weight2=np.random.rand(1,1)
    weight=np.random.rand(3,1)
    for i in range (0,3):
        WeightMatrix[i]=weight[i]
        # WeightMatrix[0][i] = Bias###############################################################
        # WeightMatrix[1][i] = Weight1[0][i]
        # WeightMatrix[2][i] = Weight2[0][i]

    return WeightMatrix

def Signum(NetMatrixResult):
    if(NetMatrixResult>0):
        NetMatrixResult=1
    elif(NetMatrixResult==0):
        NetMatrixResult=1
    else:
        NetMatrixResult=-1
    return NetMatrixResult #############


def SingleLayerPers(InputMatrix,WeightMatrix,TargetList,Epochs,LR):
    # Epochs=10
    # LR=10
    for E in range(0, Epochs):
        for i in range(0, 60):
            InputRecordMat = np.empty([1, 3])
            InputRecordMat[0][0] = InputMatrix[i][0]
            InputRecordMat[0][1] = InputMatrix[i][1]
            InputRecordMat[0][2] = InputMatrix[i][2]

            NetMatrix = np.dot(InputRecordMat, WeightMatrix)
            NormaizedVal=Signum(NetMatrix)

            if (NormaizedVal != TargetList):
                Loss=TargetList[i]-NormaizedVal
                Term=np.dot(LR,Loss)
                WeightMatrix[0][0] = WeightMatrix[0][0]+(np.dot(Term,InputRecordMat[0][0]))
                WeightMatrix[1][0] = WeightMatrix[1][0]+(np.dot(Term,InputRecordMat[0][1]))
                WeightMatrix[2][0] = WeightMatrix[2][0]+(np.dot(Term,InputRecordMat[0][2]))

    return WeightMatrix

#second task algo adaline
def Adaline(InputMatrix,WeightMatrix,TargetList,Epochs,LR,mse):
    # Epochs=10
    # LR=10
    x=100000000000
    epoch=0
    loss2=0
    while (x > mse):##############################
        for i in range(0, 60):
            InputRecordMat = np.empty([1, 3])
            InputRecordMat[0][0] = InputMatrix[i][0]
            InputRecordMat[0][1] = InputMatrix[i][1]
            InputRecordMat[0][2] = InputMatrix[i][2]

            NetMatrix = np.dot(InputRecordMat, WeightMatrix)


            #if (NetMatrix != TargetList):
            Loss=TargetList[i]-NetMatrix
            Term=np.dot(LR,Loss)
            WeightMatrix[0][0] = WeightMatrix[0][0]+(np.dot(Term,InputRecordMat[0][0]))
            WeightMatrix[1][0] = WeightMatrix[1][0]+(np.dot(Term,InputRecordMat[0][1]))
            WeightMatrix[2][0] = WeightMatrix[2][0]+(np.dot(Term,InputRecordMat[0][2]))
            ###losss mean square

        #to calculae the mse
        for i in range(0, 60):
            InputRecordMat = np.empty([1, 3])
            InputRecordMat[0][0] = InputMatrix[i][0]
            InputRecordMat[0][1] = InputMatrix[i][1]
            InputRecordMat[0][2] = InputMatrix[i][2]

            NetMatrix = np.dot(InputRecordMat, WeightMatrix)


           # if (NetMatrix != TargetList):
            loss2+=np.nan_to_num(((TargetList[i]-NetMatrix)*(TargetList[i]-NetMatrix)/2))
        x=(loss2/60)
        epoch += 1
        loss2=0
    print(x)
    print("Epochs is: ",epoch)


    return WeightMatrix


def AnotherInputMatrixConstructor(F1,F2,BooleanBias):
    AnotherInputMatrix=np.empty([40,3],dtype=float)
    if BooleanBias == True:
        Bias = 1
    elif BooleanBias == False:
        Bias=0
    for i in range(0,40):
        AnotherInputMatrix[i][0] =Bias
        AnotherInputMatrix[i][1]=F1[i]
        AnotherInputMatrix[i][2]=F2[i]
    return AnotherInputMatrix

def test(AnotherInputMatrix,WeightMatrix,TargetList):
     Accuracy=0
     c1true=0
     c2true=0
     c1false=0
     c2false=0
     confMat=np.empty([2,2])
     for i in range(0, 40):
            InputRecordMat2 = np.empty([1, 3])
            InputRecordMat2[0][0] = AnotherInputMatrix[i][0]
            InputRecordMat2[0][1] = AnotherInputMatrix[i][1]
            InputRecordMat2[0][2] = AnotherInputMatrix[i][2]
            NetMatrix2 = np.dot(InputRecordMat2, WeightMatrix)
            NormaizedVal2=Signum(NetMatrix2)
            if(TargetList[i]==NormaizedVal2 and TargetList[i]==1):
                c1true+=1
                Accuracy+=1
            elif(TargetList[i]==NormaizedVal2 and TargetList[i]==-1):
                c2true+=1
                Accuracy+=1
            elif(TargetList[i]!=NormaizedVal2 and TargetList[i]==1):
                c1false+=1
            elif(TargetList[i]!=NormaizedVal2 and TargetList[i]==-1):
                c2false+=1
     confMat[0][0]=c1true
     confMat[0][1]=c2false
     confMat[1][0]=c1false
     confMat[1][1]=c2true

     return ((Accuracy/40)*100),confMat

def draw_line(F1,F2,LabelList,Updatedweight):

    FirstFeatureFirstClass=list()
    FirstFeatureSecondClass=list()
    SecondFeatureFirstClass=list()
    SecondFeatureSecondClass=list()
    for i in range(0,40):
        if(LabelList[i]==1):
            FirstFeatureFirstClass.append(F1[i])
            SecondFeatureFirstClass.append(F2[i])
        elif(LabelList[i]==-1):
            FirstFeatureSecondClass.append(F1[i])
            SecondFeatureSecondClass.append(F2[i])
    plt.figure('fig1')
    plt.scatter(FirstFeatureFirstClass,SecondFeatureFirstClass)
    plt.scatter(FirstFeatureSecondClass,SecondFeatureSecondClass)
    point1=-Updatedweight[0]/Updatedweight[2]
    point2=-Updatedweight[0]/Updatedweight[1]
    minx=min(F1)
    maxx=max(F1)
    miny=(-(Updatedweight[1]*minx)-Updatedweight[0])/Updatedweight[2]
    maxy=(-(Updatedweight[1]*maxx)-Updatedweight[0])/Updatedweight[2]

    plt.plot((minx,maxx),(miny,maxy))
    plt.xlabel('Feature1')
    plt.ylabel('Feature2')
    plt.show()



def main(Feature1,Feature2,Class1,Class2,Bias,Epochs,LearningRate,mse):


    # Epochs=10############################################################## update this!!!!!
    open("TrainFile.txt",'w').close()
    open("TestFile.txt", 'w').close()
    # DefaultBias=np.random.rand(1,1)
    ChooseAndShuffle(Class1, Class2)
    F1,F2,LabelList=ChooseFeatures(Feature1,Feature2,Class1,Class2,"TrainFile.txt")
    F1 = np.array(F1)
    F2 = np.array(F2)
    F1=F1.reshape(60,1)
    F2=F2.reshape(60,1)
    InputMatrix=InputMatrixConstructor(F1,F2,Bias)
    # WeightMatrix=WeightMatrixConstructor(DefaultBias)
    WeightMatrix=WeightMatrixConstructor()
    #UpdatedWeightMatrix=SingleLayerPers(InputMatrix,WeightMatrix,LabelList,Epochs,LearningRate)
    UpdatedWeightMatrix=Adaline(InputMatrix,WeightMatrix,LabelList,Epochs,LearningRate,mse)

    #for test
    F1T,F2T,LabelListtest=ChooseFeatures(Feature1,Feature2,Class1,Class2,"TestFile.txt")
    AnotherInputMatrix=AnotherInputMatrixConstructor(F1T,F2T,Bias)
    acuuracy,confusionMatrix=test(AnotherInputMatrix,UpdatedWeightMatrix,LabelListtest)
    print('Accuracy=', int(acuuracy),'%','\n','Confusion Matrix is:\n',confusionMatrix,'\n')

    #for drawing line
    draw_line(F1T,F2T,LabelListtest,UpdatedWeightMatrix)

main("X1","X4","C1","C2",True,10,0.005,0.05)


