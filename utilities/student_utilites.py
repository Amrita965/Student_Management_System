
import os
import json

def addDataToJSONFile(record, fileName, filePath):
    #Check if the file exists before trying to load data
    records = loadDataFromJSONFile(filePath, fileName)
    # Append the new data to the exitsting data
    records.append(record)
    # Write the updated data back to the JSON file
    with open(os.path.join(filePath, fileName), "w") as fp:
        json.dump(records, fp, indent=2)
        
    return {"acknowledged": True}
        
       
def loadDataFromJSONFile(filePath, fileName):
    
    fullPath = os.path.join(filePath, fileName)
    
    print(fullPath)
    
    if os.path.exists(fullPath):
        with open(fullPath, "r") as fp:
            try:
                return json.load(fp)
            except Exception as _:
                # Return an empty list if the file is empty or has incorrect formatting
                return []
    else:
        # Return an empty list if the file doesn't exist
        return []
        
        
    
    
    

    
       