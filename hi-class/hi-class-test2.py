from sklearn.ensemble import RandomForestClassifier

from hiclass import LocalClassifierPerNode

# Define data
X_train = [[1], [2], [3], [4]]
X_test = [[4], [3], [2], [1]]
Y_train = [
    ["Animal", "Mammal", "Sheep"],
    ["Animal", "Mammal", "Cow"],
    ["Animal", "Reptile", "Snake"],
    ["Animal", "Reptile", "Lizard"],
]

# Use random forest classifiers for every node
# And exclusive siblings policy to select training examples for binary classifiers.
rf = RandomForestClassifier()
classifier = LocalClassifierPerNode(local_classifier=rf, binary_policy="inclusive")

# Train local classifier per node
classifier.fit(X_train, Y_train)

# Predict
predictions = classifier.predict(X_test)
print(predictions)