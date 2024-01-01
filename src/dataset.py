import arff

class Dataset:
    """
    
    This class is used to extract the dataset information, such as the dataset name, 
    the dataset attributes and the dataset data itself.

    Imported arff library of Connectionist Artificial Intelligence Laboratory (LIAC)    
    `Args:`
        - filename (str): the path of the dataset.
        - binary (bool): if the dataset is binary or not. default: False.

    """

    def __init__(self, file_path) -> None:

        self.dataset_dict = arff.load(open(file_path, 'r'))

        self.dataset_description = self.dataset_dict['description'] # a inlined string

        self.dataset_name = self.dataset_dict['relation'] # a inlined string

        self.dataset_attributes = self.dataset_dict['attributes'] #list of tuples [('attribute_name', 'value), ('', '')] both strings

        self.dataset_objects = self.dataset_dict['data'] #list of lists [[value, value, value], [value, value, value]] all strings



    def save_dataset(self, path):
        """
        Save the dataset in a new file.

        `Args:`
            - path (str): the path of the new file.
        """
        
        try:
            arff.dump(self.dataset_dict, open(path, 'w'))
        except:
            print("Error saving the dataset.")
  

#
#
#   Example of use  
#
#
            
if __name__ == "__main__":
    i = Dataset('datasets/cellcyle/CellCycle_test_discretized.arff')
    print(i.dataset_dict['data'][0])

