
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/leono/OneDrive/Desktop/data science/panda/files/titanic.csv")


# get the particualar column out of a condintion

adults_names = data.loc[data["Age"] > 18, "Name"]
print(adults_names)


#slicing - same as numpy 2D slicing
# the firdt indext is for rows and the second is for columns
# follows the same syntax as range functions
print(data.iloc[9:25 , 2:5])



# changing the alue in the dataset
# specify the numbers of rows and the partivualr column to change
data.iloc[2,3] = "Pilkit Chawla"
print(data["Name"])

# Save the data to local to verify changes
data.to_csv("C:/Users/leono/OneDrive/Desktop/data science/panda/files/titanicsw.csv")

#Creating a new column in the dataFrame
data["Test"] = data["fare"] + 2
data["test2"] = data["fare"] * data["Pclass"]# Any mathmatical operation could be considered

#Renaming the column names:

data_renamed = data.rename(
    columns = {
        "Pclass":"Passenger class",
        "Sibsp" : "Sibiling"
    }
)
print(data_renamed.info())