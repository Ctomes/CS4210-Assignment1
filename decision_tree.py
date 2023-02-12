#-------------------------------------------------------------------------
# AUTHOR: Christopher Tomes
# FILENAME: decision_tree.py
# SPECIFICATION: This code implements a decision tree classifier using scikit-learn's decision tree classifier on "contact_lens.csv". The categorical data in the file is mapped to integers, fit into the model, then plotted using matplotlib.
# FOR: CS 4210- Assignment #1
# TIME SPENT: the coding portion for this assignment was around 1 hour. 
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv

#MacThings
import os
import platform
db = []
X = []
Y = []

#MacThings:
##################################################
#small change to alow me to have it work on my Mac
#also replaced name of csv with the var string_path 
if platform.system() == 'Darwin':
  string_path = os.getcwd() + '/contact_lens.csv'
else:
  string_path = 'contact_lens.csv'
###################################################

#reading the data in a csv file
with open(string_path, 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         #print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here

# Create a dictionary to store map from unique elements to integers
element_to_int = {}
int_to_element = {}

# Iterate over the columns
for column in zip(*db):
    # Get the unique elements
    unique_elements = set(column)
    
    # Iterate over the unique elements
    for element in unique_elements:
        if element not in element_to_int:
            element_to_int[element] = len(element_to_int)
            int_to_element[len(int_to_element)] = element


# Create a new 2D array to store the mapped values
mapped_arr = []

# Iterate over the rows of to convert via new vals
for row in db:
    mapped_row = []
    
    # Iterate over the elements in a row
    for element in row:
        # Replace each element with new corresponding integer value we got earlier
        mapped_element = element_to_int[element]
        mapped_row.append(mapped_element)
    
    # Add the mapped row to the mapped array
    mapped_arr.append(mapped_row)

#print(mapped_array)

# X =
#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
# Y =

#combined steps

# Iterate over the rows in the mapped array to assign into your defined data structues X/Y
for row in mapped_arr:
    # Extract the vals
    values = row[:-1]
    last_value = row[-1]
    # Add the vals to the first n-1 columns to
    X.append(values)
    # Add last column to Y
    Y.append(last_value)



#print(X)
#print(Y)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
