import os

def svmTrain(classifierKernel, trainDataBase, outputFolder):
    os.system(f'./HRSVM-PY/HRSVM/svm-train -k {classifierKernel} -a 1 "{trainDataBase}" "{outputFolder}"')
    #svm-train <options> <training data> <model output folder>

def svmPredict(dataPath, classifierPath, outputFolder):
    """For predicting process, must provide testing data path to be predicted, classifier path, and prediction output path."""
    os.system(f'sudo ./HRSVM-PY/HRSVM/svm-predict {dataPath} "{classifierPath}" "{outputFolder}"')
    #svm-predict <testing data> <classifier> <prediction output>


data = "/home/yksh/Desktop/GAs-for-Hierarchical-Classification/tests/test.dat"
classifier = "/home/yksh/Desktop/GAs-for-Hierarchical-Classification/tests/output"
predict = "/home/yksh/Desktop/GAs-for-Hierarchical-Classification/tests/predict/"


svmPredict(data, classifier, predict)