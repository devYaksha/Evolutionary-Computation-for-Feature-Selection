import os

def delete_old_childrens(self):
    current_directory = "./datasets"
    files = os.listdir(current_directory)
    for file in files:
        if file.endswith('.arff') and (file.startswith('c') or file.startswith('o')) or file.startswith('n'):
            file_path = os.path.join(current_directory, file)
            os.remove(file_path)
            
            
def pause():
    input("Press the <ENTER> key to continue...")
