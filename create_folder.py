# function to create folders
def create_folder(folder_name="DEFAULT"):
    """
    If folder does not exist and it is not an empty string then create the folder and return FilePath.
    If folder does exist and it is not an empty string then return FilePath.
    Otherwise return None.
    """
    import os
    # get file_path for folder_name
    file_path = os.path.join(os.getcwd(), folder_name)
    
    # check to see if folder exists and folder name is not empty string ""
    if os.path.exists(file_path) == False and folder_name != "":
        try:
            os.makedirs(file_path) # auto create folder if it does not exist
            # return filepath
            return file_path
        except:
            print("\n(꒪Д꒪)ノ\tPATH ERROR -- cannot create folder:  ", folder_name)
            return None
    
    # if folder exists then just return filepath
    elif os.path.exists(file_path) == True and folder_name != "":
        return file_path
    
    # for all other conditions just return None
    else:
        return None