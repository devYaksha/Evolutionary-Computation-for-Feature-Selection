from hrsvmPy import *

data = "svmTest/test.dat"
classifier = "svmTest/trainModel"
predict = "svmTest/result"


svmTrain(None, "svmTest/train.dat", "svmTest/trainModel")
svmPredict(data, classifier, predict)