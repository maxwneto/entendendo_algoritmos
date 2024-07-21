# Importing necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Loading the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating the K-NN classifier
k = 3  # Number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)

# Fitting the model
knn.fit(X_train, y_train)

# Making predictions
y_pred = knn.predict(X_test)

# Calculating accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Explanation:
# - The load_iris() function loads the Iris dataset.
# - The train_test_split() function splits the dataset into training and testing sets.
# - The KNeighborsClassifier() creates a K-NN classifier with k neighbors.
# - The fit() method trains the classifier on the training data.
# - The predict() method predicts the classes for the test data.
# - The accuracy_score() function calculates the accuracy of the classifier.
