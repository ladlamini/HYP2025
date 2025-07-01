import tkinter as tk
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import random_projection
import numpy as np
from sklearn.metrics import accuracy_score

# csv dataset 
dataframe = pd.read_csv(r'C:\Users\leedl\OneDrive\Documents\AI_based_IDS\dataset\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')

#This ensures that there are no null or infinity values 
dataframe.dropna(inplace=True)
dataframe = dataframe.apply(pd.to_numeric, errors='coerce')
dataframe.replace([' Infinity', ' INF', ' NaN', ' nan'], np.nan, inplace=True)
#print(dataframe.columns.tolist())

#convert to binary
dataframe[' Label'] = dataframe[' Label'].apply(lambda x: 0 if x == 'BENIGN' else 1)

selected_features= [
     ' Flow Duration', ' Total Fwd Packets', ' Total Backward Packets', 'Total Length of Fwd Packets', 
   ' Total Length of Bwd Packets', ' Fwd Packet Length Max', ' Fwd Packet Length Min', ' Fwd Packet Length Mean',
      ' Fwd Packet Length Std', 'Bwd Packet Length Max', ' Bwd Packet Length Min', ' Bwd Packet Length Mean', 
      ' Bwd Packet Length Std', 'Flow Bytes/s', ' Flow Packets/s', ' Flow IAT Mean', ' Flow IAT Std', ' Flow IAT Max', 
      ' Flow IAT Min', 'Fwd IAT Total', ' Fwd IAT Mean', ' Fwd IAT Std', ' Fwd IAT Max', ' Fwd IAT Min', 'Bwd IAT Total', 
      ' Bwd IAT Mean', ' Bwd IAT Std', ' Bwd IAT Max', ' Bwd IAT Min'
 ]
dataframe = dataframe.sample(n=10000, random_state=42)

#Split the dataset for training and testing purposes
X= dataframe[selected_features]


y= dataframe[' Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# print("X shape:", X.shape)  
# print("y shape:", y.shape)
#Train using random forest classifier 
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

#Test the model using dataset from initial split 
y_pred = clf.predict(X_test)
print('Training complete!')
print("Accuracy:", accuracy_score(y_test, y_pred))
