from hrsvmPy import *

"""Multi-class example:

trainParameters= "-k multiclass -a 1 -t 2 -c 1 -g 0.1"
trainData = "HRSVM-PY/multiclassExample/train.dat"
predictModelPath = "HRSVM-PY/multiclassExample/predictModel"
svmTrain(trainParameters, trainData, predictModelPath)

predictDataPath = "HRSVM-PY/multiclassExample/test.dat"
svmPredict(predictDataPath, "HRSVM-PY/multiclassExample/predictModel", "HRSVM-PY/multiclassExample/predict")

"""

#Hierarchical train example:

parameters = "-k hierarchical ""HRSVM-PY/hierarchicalExample/train.hf"" -a 1 -l 50"
trainPath = "HRSVM-PY/hierarchicalExample/train.dat"
predictModelPath = "HRSVM-PY/hierarchicalExample/predictModel"
svmTrain(parameters, trainPath, predictModelPath)


PredictData = "HRSVM-PY/hierarchicalExample/test.dat"
classifierPath = "HRSVM-PY/hierarchicalExample/predictModel"
svmPredict(PredictData, classifierPath, "HRSVM-PY/hierarchicalExample/predict")