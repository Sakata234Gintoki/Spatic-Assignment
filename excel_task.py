# Importing Relevant Libraries
import pandas as pd
from geopy.distance import geodesic
from difflib import SequenceMatcher

# Creating function to check similarities between latitude and longitude

def is_similar(name1,name2):
    # Check if two names are similar
    if name1 == name2:
        return True

    # Check if two names are within 5 single-character edits of each other
    if SequenceMatcher(None,name1,name2).ratio() >= 0.8:
        return True

    return  False

# Importing dataset
df = pd.read_csv('assignment_data.csv')
print(df.columns)
for i in range(len(df)):
    for j in range(i+1,len(df)):
        # Calculate the distace between the two entries

        dist = geodesic((df.loc[i,'latitude'],df.loc[i,'longitude'],),(df.loc[j,'latitude'],df.loc[j,'longitude'])).m

        # Check if the distance is within 200 metres
        if dist <= 200:
            if is_similar(df.loc[i,'name'],df.loc[j,'name']):
                # Mark both entries as similar
                df.loc[i,'is_similar'] = '1'
                df.loc[j,'is_similar'] = '1'
        else:
            df.loc[i,'is_similar'] = '0'
            df.loc[j,'is_similar'] = '0'
df.to_csv("output.csv")

