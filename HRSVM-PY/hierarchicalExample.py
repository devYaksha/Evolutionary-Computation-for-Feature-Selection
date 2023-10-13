from hrsvmPy import *
parameters = "-k hierarchical HRSVM-PY\hierarchicalExample\train.hf -a 1 -l 50 "
trainFilePath = "HRSVM-PY\hierarchicalExample\train.dat"
trainModelOutput = "HRSVM-PY\hierarchicalExample\trainModel"
svmTrain(parameters, trainFilePath, trainModelOutput)



data = "svmTest/test.dat"
classifier = "svmTest/trainModel"
predict = "svmTest/result"
svmPredict(data, classifier, predict)