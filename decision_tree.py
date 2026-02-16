#-------------------------------------------------------------------------
# AUTHOR: Nicholas Tran
# FILENAME: decision_tree.py
# SPECIFICATION: This is a program that does a binary classification of contact_lens.csv using a decision tree
# FOR: CS 4210- Assignment #1
# TIME SPENT: Started 2/15/2026 8 PM
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
    if i > 0: #skipping the header
      db.append (row)

#encode the original categorical training features into numbers and add to the 4D array X.
#--> add your Python code here
# X =

feature_map = {}
for row in db:
  encoded_row = []
  
  for i in range(len(row) - 1): # Assuming the last column is the class label, we only encode the features
    feature = row[i]
    
    if i not in feature_map: # Map new feature index to feature_map
      feature_map[i] = {}
    if feature not in feature_map[i]: # Map new feature value to the feature index in feature_map
      feature_map[i][feature] = len(feature_map[i]) + 1
    
    encoded_row.append(feature_map[i][feature])
  
  X.append(encoded_row)

#encode the original categorical training classes into numbers and add to thevector Y.
#--> addd your Python code here
# Y =

class_map = { # In class_names, 'Yes' is represented as 0 and 'No' is represented as 1
  'Yes': 0,
  'No': 1
}
for row in db:
  Y.append(class_map[row[-1]]) # Assuming the class label is in the last column


#fitting the depth-2 decision tree to the data using entropy as your impurity measure
#--> addd your Python code here
#clf =
clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=2) # Since we are simulating ID3, we set the criterion to 'entropy' and max_depth to 2
clf = clf.fit(X, Y)


#plotting decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
