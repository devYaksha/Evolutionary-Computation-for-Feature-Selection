from hrsvmPy import *
parameters = "-k hierarchical svmTest/my_hierarchy.h -a 1 -l 50 "
trainFilePath = "svmTest/train.dat"
trainModelOutput = "svmTest/trainModel"
svmTrain(parameters, trainFilePath, trainModelOutput)



data = "svmTest/test.dat"
classifier = "svmTest/trainModel"
predict = "svmTest/result"
svmPredict(data, classifier, predict)