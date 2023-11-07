#include"classifier.h"

using namespace std;

long double nbayes(string mlnp, string usf, string trainingFile, string testFile, string resultFile){

  unsigned int numberOfAttributes;
  unsigned int numberOfTrainingExamples;
  unsigned int numberOfTestExamples;
  bool mandatoryLeafNodePrediction = false, usefulness = false;
  long double result;

	if (mlnp == "y") mandatoryLeafNodePrediction = true;
	if (usf == "y") usefulness = true;

	getDatasetsProfile(trainingFile, testFile, numberOfTrainingExamples, numberOfTestExamples,numberOfAttributes);

	ChargeTrainingSet *CTR;
	CTR = new ChargeTrainingSet(trainingFile,numberOfAttributes,numberOfTrainingExamples, mandatoryLeafNodePrediction);
	CTR->getTrainingSet();

	ChargeTestSet *CTE;
	CTE = new ChargeTestSet(testFile,numberOfTestExamples,numberOfAttributes);
	CTE->getTestSet();

	Classifier *CL;
	CL = new Classifier(numberOfTrainingExamples, numberOfTestExamples, numberOfAttributes, resultFile, usefulness);
	Classifier::auxCLCTR = CTR;
	Classifier::auxCLCTE = CTE;
	result = CL->applyClassifier();

	delete CL;
	delete CTE;
	delete CTR;
	return result;

}

