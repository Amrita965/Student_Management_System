
import os
import json

def addDataToJSONFile(dictdata, fileName, filePath):
    #Check if the file exists before trying to load data
    data = loadDataFromJSONFile(filePath, fileName)
    #Append the new data to the exitsting data
    data.append(dictdata)
    # Write the updated data back to the JSON file
    with open(os.path.join(filePath, fileName), "w") as fp:
        json.dump(data, fp, indent=2)
        
       
def loadDataFromJSONFile(filePath, fileName):
    
    fullPath = os.path.join(filePath, fileName)
    
    if os.path.exists(fullPath):
        with open(os.path.join(filePath, fileName), "r") as fp:
            try:
                return json.load(fp)
            except Exception as _:
                # Return an empty list if the file is empty or has incorrect formatting
                return []
    else:
        # Return an empty list if the file doesn't exist
        return []
        



    
       