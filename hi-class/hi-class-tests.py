from hiclass import LocalClassifierPerNode
from sklearn.ensemble import RandomForestClassifier

# Define data
X_test = [[4], [3], [2], [1], [5]]
Y_train = [
    ['Animal', 'Mammal', 'Sheep'],
    ['Animal', 'Mammal', 'Cow'],
    ['Animal', 'Reptile', 'Snake'],
    ['Animal', 'Reptile', 'Lizard'],
    ['Animal', 'Mammal', 'Unknown']
]
X_train = [[i] for i in range(1, len(Y_train)+1)]

# Use random forest classifiers for every node
rf = RandomForestClassifier()
classifier = LocalClassifierPerNode(local_classifier=rf)

# Train local classifier per node
classifier.fit(X_train, Y_train)

# Predict
predictions = classifier.predict(X_test)
print(predictions)
