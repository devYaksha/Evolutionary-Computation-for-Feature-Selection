import os

def svmTrain(parameters, train_data_path, output_folder_path):
    """
    Trains a Support Vector Machine (SVM) model.

    Args:
        parameters (str): A string containing HRSVM training parameters.
        train_data_path (str): The path to the training data.
        output_folder_path (str): The path to the output folder where the trained model will be saved.
    """
    if os.name == "nt":
        print("Not working in windows systems yet")
        return

    if parameters != None:
        os.system(f'./HRSVM-PY/HRSVM/svm-train {parameters} "{train_data_path}" "{output_folder_path}"')
    else:
        print("Neeed HRSVM parameters.")

def svmPredict(dataPath, classifierPath, outputFolder):
    """
    Predicts using a trained Support Vector Machine (SVM) classifier.

    Args:
        data_path (str): The path to the testing data to be predicted.
        classifier_path (str): The path to the trained SVM classifier.
        output_folder (str): The path to the folder where prediction results will be saved.
    """

    if os.name == "nt":
        print("Not working in windows systems yet")
        return

    else: 
        os.system(f'./HRSVM-PY/HRSVM/svm-predict {dataPath} "{classifierPath}" "{outputFolder}"')
        os.system("echo Finished")
        os.system("exit")   



