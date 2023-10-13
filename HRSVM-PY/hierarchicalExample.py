from hrsvmPy import *


parameters = "-k hierarchical HRSVM-PY/hierarchicalExample/train.hf -a 1"
trainFilePath = "HRSVM-PY/hierarchicalExample/train.dat"
trainModelOutput = "HRSVM-PY/hierarchicalExample/trainModel"
#svmTrain(parameters, trainFilePath, trainModelOutput)


predictData = "HRSVM-PY/hierarchicalExample/test.dat"
classifier = "HRSVM-PY/hierarchicalExample/trainModel"
output = "HRSVM-PY/hierarchicalExample"

svmPredict(predictData, classifier, output)