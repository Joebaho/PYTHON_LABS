'''
PYTHON LAB: dictionary_03.py

Print the value of key ‘history’ from the below dict
expected output: 80
sampleDict = { "class": { "student": { "name": "Mike", "marks": { "physics": 70, "history": 80 } } } }

'''
# Create the nested dictionary
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# Access the value of 'history' key
print(sampleDict["class"]["student"]["marks"]["history"])


