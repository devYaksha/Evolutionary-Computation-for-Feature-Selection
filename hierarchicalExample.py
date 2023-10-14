from hrsvmPy import *
import os

parameters = "-k hierarchical hierarchicalExample/train.hf -a 1"
trainFilePath = "hierarchicalExample/train.dat"
trainModelOutput = "hierarchicalExample/svmModel"
#svmTrain(parameters, trainFilePath, trainModelOutput)


predictData = "hierarchicalExample/test.dat"
classifier = "hierarchicalExample/svmModel"
output = "hierarchicalExample/"

svmPredict(predictData, classifier, output)


